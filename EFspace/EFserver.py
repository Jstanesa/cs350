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

    cur.execute('select * from basicHouse')
    rows = cur.fetchall()

    return render_template('houses.html', houses=rows)
@app.route('/locateForm', methods=['GET', 'POST'])
def estatelocate():

    return render_template('estatelocate.html')
  
@app.route('/locateForm2', methods=['GET', 'POST'])
def estatelocate2():
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)    
    #if user typed in the form and submitted
    if request.method == 'POST':
      query = "SELECT * from basicHouse WHERE state = '" + request.form['state'] + "';"
      cur.execute(query)
      rows = cur.fetchall()
    
    return render_template('locateReturn.html', houses = rows)

@app.route('/locateReturn', methods=['GET', 'POST'])
def report4():

    
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)


    cur.execute(query)
    rows = cur.fetchall()

    return render_template('locateReturn.html', selectedMenu='List')

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port = 3000)