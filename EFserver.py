from flask import Flask, render_template, request, session, redirect, url_for
import utils, MySQLdb

app = Flask(__name__)

#set secret key for sessions
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
#set current user to 'guest'
currentUser = 'guest'

@app.route('/')
def mainIndex():
    return render_template('index.html', name = currentUser)
  
@app.route('/houses', methods=['GET', 'POST'])
def report3():
  
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)

    cur.execute('SELECT b.address, b.county, b.state, b.price, SUM(hd.cost) FROM basicHouse b INNER JOIN house_damages hd ON b.house_id = hd.house_id GROUP BY b.address')
    rows = cur.fetchall()
    print(rows)
    return render_template('houses.html', houses=rows, name = currentUser)
  
@app.route('/add', methods=['GET', 'POST'])
def estateadd():
    return render_template('add.html', name = currentUser)
  
@app.route('/add2', methods=['GET', 'POST'])
def estateadd2():
    db = utils.db_connect()
    cur = db.cursor()    
    #if user typed in the form and submitted
    if request.method == 'POST':
      damageType=MySQLdb.escape_string(request.form['damageType'])
      address=request.form['address']
      query = "INSERT INTO basicHouse (address,county,state,price) VALUES ('" + address +"', '"+MySQLdb.escape_string(request.form['county'])+"', '"+MySQLdb.escape_string(request.form['state'])+"', "+MySQLdb.escape_string(request.form['price'])+")"
      print(query)
      cur.execute(query)
      db.commit()
      query = "INSERT INTO house_damages (damage_id,type,cost) VALUES ('"
      query+=damageType+"'), (SELECT house_id FROM basicHouse WHERE address= '"+ address+"') , '"+ MySQLdb.escape_string(request.form['damageCost']) + "');" 
      print(query)
      cur.execute(query)
      #rows = cur.fetchall()
      db.commit()
    return render_template('index.html', name = currentUser)

@app.route('/locateForm', methods=['GET', 'POST'])
def estatelocate():
    return render_template('estatelocate.html', name = currentUser)
  
@app.route('/locateForm2', methods=['GET', 'POST'])
def estatelocate2():
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)    
    #if user typed in the form and submitted
    if request.method == 'POST':
		
        if 'state' in request.form:
  	    #if request.form['state']:
            query = "SELECT b.address, b.county, b.state, b.price, SUM(hd.cost) FROM basicHouse b INNER JOIN house_damages hd ON b.house_id = hd.house_id AND b.state = '" + MySQLdb.escape_string(request.form['state']) + "' GROUP BY b.address;"
        if 'address' in request.form: 
        #if request.form['address']:
            query = "SELECT b.address, b.county, b.state, b.price, SUM(hd.cost) FROM basicHouse b INNER JOIN house_damages hd ON b.house_id = hd.house_id AND b.address LIKE '%" + MySQLdb.escape_string(request.form['address']) + "%';" 
        if 'max' in request.form:
        #if request.form['min']:
            query = "SELECT b.address, b.county, b.state, b.price, SUM(hd.cost) FROM basicHouse b INNER JOIN house_damages hd ON b.house_id = hd.house_id AND hd.cost <= " + MySQLdb.escape_string(request.form['max']) + " GROUP BY b.address;" 
            print(query)		
			
    cur.execute(query)
    rows = cur.fetchall()
    print(rows)
    return render_template('locateReturn.html', houses = rows, name = currentUser)
	

@app.route('/locateReturn', methods=['GET', 'POST'])
def report4():

    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)

    cur.execute(query)
    rows = cur.fetchall()

    return render_template('locateReturn.html', selectedMenu='List', name = currentUser)
@app.route('/contact')
def contact():
  return render_template('contact.html', name = currentUser)

@app.route('/login', methods=['GET', 'POST'])
def login():
  
    global currentUser
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    # if user typed in a post ...
    if request.method == 'POST':
      print "HI"

      username = MySQLdb.escape_string(request.form['username'])
      session['username'] = username
      #currentUser = username
      print(session['username'])                                  
      currentUser = username

      pw = MySQLdb.escape_string(request.form['pw'])
      query = "SELECT * FROM users WHERE password = SHA2('%s', 0)" % pw
      print query
      cur.execute(query)
      if cur.fetchone():
         return redirect(url_for('mainIndex'))
    
    return render_template('login.html', selectedMenu='Login', name = currentUser)
@app.route('/register', methods=['GET', 'POST'])
def register():
  #If they registered for an account
  if request.method == 'POST':
    
    #set up database connections
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    
    #get form results.
    username = MySQLdb.escape_string(request.form['username'])
    password = MySQLdb.escape_string(request.form['pw'])
    zipcode = MySQLdb.escape_string(request.form['zipcode'])
    
    #testing in terminal
    print "Hi " + username + " " + password + " " + zipcode
    
    #Insert into 'users' table
    #query = "INSERT INTO users (username, password, zipcode) VALUES ('";
    #query += request.form['username'] + "','" + request.form['pw'] + "','" + request.form['zipcode'] + "')"
    #Hash it
    ###ADD ZIPCODE TO USERS TABLE  
    query = "INSERT INTO users (username, password, zipcode) VALUES ('%s', SHA2('%s', 0), '%d')" % (username, password, int(zipcode))
    print query          #testing in terminal
      
    cur.execute(query)
    db.commit()
    
    return render_template('login.html', selectedMenu='Login')
  
  return render_template('register.html', selectedMenu='Register', name = currentUser)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there

    currentUser = 'guest'
    #return redirect(url_for('mainIndex'), currentUser)
    #else: 
    return render_template('index.html', selectedMenu='Home', name = currentUser)
  
if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port = 3000)