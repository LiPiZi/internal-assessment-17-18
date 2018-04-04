import mysql.connector

cnx = mysql.connector.connect(user='root', password='C00lc4t!',
                              host='127.0.0.1',
                              database='orufood')
cursor = cnx.cursor()

testquery = 'INSERT INTO patron (name, email) VALUES (%s, %s);'
testdata = ['jane', 'orufoodbot@gmail.com']
cursor.execute(testquery, testdata)

cursor.close()
cnx.close()