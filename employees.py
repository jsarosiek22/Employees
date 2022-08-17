from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
app = Flask(__name__)

cnx = mysql.connector.connect(user='root', password='MySQL22!',
                              host='localhost',
                              database='employees')


@app.route('/')
@app.route('/employees')
def GetEmployees():
	employees = ''
	cursor = cnx.cursor(buffered=True)

	query = ("SELECT * FROM employees")
	cursor.execute(query)
	myresult = cursor.fetchmany(10)

	print(myresult)
	employees = 'test'

	cursor.close()
	cnx.close()
	return render_template('employees.html', employees = employees)

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)