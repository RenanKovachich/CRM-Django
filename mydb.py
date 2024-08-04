# Install Mysql on your computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'teste123' ,
    auth_plugin= 'mysql_native_password'
    )

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("All done!")
