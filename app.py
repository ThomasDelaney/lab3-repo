
from flask import Flask
from flask_mysqldb import MySQL
from flask import Flask, render_template, redirect, url_for
mysql = MySQL()
app = Flask(__name__)
# My SQL Instance configurations 
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'thomas'
app.config['MYSQL_DB'] = 'studentbook'
app.config['MYSQL_HOST'] = '35.197.205.126'
mysql.init_app(app)

# The first route to access the webservice from http://external-ip:5000 
#@pp.route("/add") this will create a new endpoints that can be accessed using http://external-ip:5000/add
@app.route("/")
def view(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT * FROM students''') # execute an SQL statment
    rv = cur.fetchall() #Retreive all rows returend by the SQL statment
    return render_template("index.html", rv=rv)

@app.route("/add")
def add(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''INSERT INTO students (studentName, email) VALUES ("Thomas", "c15300756@mydit.ie")''') # execute an SQL statment
    mysql.connection.commit()
    return redirect(url_for("view"))

@app.route("/update")
def update(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''UPDATE students SET studentName="Thomas2" WHERE studentName="Thomas"''') # execute an SQL statment
    mysql.connection.commit()
    return redirect(url_for("view"))

@app.route("/delete")
def delete(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''DELETE FROM students WHERE studentName="Thomas"''') # execute an SQL statment
    mysql.connection.commit()
    return redirect(url_for("view"))

if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000') #Run the flask app at port 5000

