from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
app = Flask(__name__)

cnx = mysql.connector.connect(user='root', password='MySQL22!',
                              host='localhost',
                              database='employees')


@app.route('/')
@app.route('/employees')
def GetEmployees():
	lastname = request.args.get('lastname')
	employees = '<table><tr><th>First Name</th></tr>'
	cursor = cnx.cursor(buffered=True)
	querystr = 'SELECT * FROM employees'

	if lastname != '':
		querystr = querystr + ' WHERE last_name like "%' + lastname + '%"'

	query = (querystr)
	cursor.execute(query)
	myresult = cursor.fetchmany(10) 
	cursor.close() 
 
	employees = myresult
	
	return render_template('employees.html', employees = employees)
 
if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000) 