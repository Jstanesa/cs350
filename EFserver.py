from flask import Flask, render_template, request
import utils, MySQLdb

app = Flask(__name__)


@app.route('/')
def mainIndex():
    return render_template('index.html')
  
@app.route('/houses', methods=['GET', 'POST'])
def report3():
  
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)

    cur.execute('SELECT b.address, b.county, b.state, b.price, SUM(hd.cost) FROM basicHouse b INNER JOIN house_damages hd ON b.house_id = hd.house_id GROUP BY b.address')
    rows = cur.fetchall()
    print(rows)
    return render_template('houses.html', houses=rows)
  
@app.route('/add', methods=['GET', 'POST'])
def estateadd():

    return render_template('add.html')
  
@app.route('/add2', methods=['GET', 'POST'])
def estateadd2():
    db = utils.db_connect()
    cur = db.cursor()    
    #if user typed in the form and submitted
    if request.method == 'POST':
      damageType=request.form['damageType']
      address=request.form['address']
      query = "INSERT INTO basicHouse (address,county,state,price) VALUES ('" + address +"', '"+request.form['county']+"', '"+request.form['state']+"', "+request.form['price']+")"
      print(query)
      cur.execute(query)
      db.commit()
      query = "INSERT INTO house_damages (damage_id,house_id,cost) VALUES ((SELECT damage_id from damages where type='"
      query+=damageType+"'), (SELECT house_id FROM basicHouse WHERE address= '"+ address+"') , '"+ request.form['damageCost'] + "');" 
      print(query)
      cur.execute(query)
      #rows = cur.fetchall()
      db.commit()
    return render_template('index.html')

@app.route('/locateForm', methods=['GET', 'POST'])
def estatelocate():

    return render_template('estatelocate.html')
  
@app.route('/locateForm2', methods=['GET', 'POST'])
def estatelocate2():
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)    
    #if user typed in the form and submitted
    if request.method == 'POST':
		
        if 'state' in request.form:
  	    #if request.form['state']:
            query = "SELECT b.address, b.county, b.state, b.price, SUM(hd.cost) FROM basicHouse b INNER JOIN house_damages hd ON b.house_id = hd.house_id AND b.state = '" + request.form['state'] + "' GROUP BY b.address;"
        if 'address' in request.form: 
        #if request.form['address']:
            query = "SELECT b.address, b.county, b.state, b.price, SUM(hd.cost) FROM basicHouse b INNER JOIN house_damages hd ON b.house_id = hd.house_id AND b.address LIKE '%" + request.form['address'] + "%';" 
        if 'max' in request.form:
        #if request.form['min']:
            query = "SELECT b.address, b.county, b.state, b.price, SUM(hd.cost) FROM basicHouse b INNER JOIN house_damages hd ON b.house_id = hd.house_id AND hd.cost <= " + request.form['max'] + " GROUP BY b.address;" 
            print(query)		
			
		
			
    cur.execute(query)
    rows = cur.fetchall()
    print(rows)
    return render_template('locateReturn.html', houses = rows)
	

@app.route('/locateReturn', methods=['GET', 'POST'])
def report4():

    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)

    cur.execute(query)
    rows = cur.fetchall()

    return render_template('locateReturn.html', selectedMenu='List')
@app.route('/contact')
def contact():
  return render_template('contact.html')

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port = 3000)
