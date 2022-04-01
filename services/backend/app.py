from flask import Flask, json, request
import mysql.connector 

app = Flask(__name__)  

@app.route("/person", methods=["GET", "POST"])
def insertPerson():
    mydb = mysql.connector.connect(
        user='root',
        password='hej123',
        host='db',
        port='3306',
        database='person'
    )
    mycursor = mydb.cursor() 
    
    if request.method == 'POST':
        fname = request.form['firstname']
        lname = request.form['lastname']
        sql = "INSERT INTO persons (Firstname, Lastname) VALUES (%s, %s)"
        val = (fname, lname)
        mycursor.execute(sql, val)
    
    mydb.commit()

    mycursor.close()

    mydb.close()

    return "Person " + fname+ " " + lname + " is posted"

@app.route("/persons", methods=["GET"])
def getPersons():
    mydb = mysql.connector.connect(
        user='root',
        password='hej123',
        host='db',
        port='3306',
        database='person'
    )
    mycursor = mydb.cursor()

    if request.method == 'GET':
        mycursor.execute("SELECT * FROM persons")

    list = mycursor.fetchall()

    mycursor.close()

    mydb.close() 

    keys = ['PersonID', 'Firstname', 'Lastname']

    personsList = [dict(zip(keys, sublst)) for sublst in list]

    return json.dumps(personsList)

if __name__ == "__main__": 
    app.run(host= "0.0.0.0")





