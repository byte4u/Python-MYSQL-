
# Install the Python drive connector
pip install mysql-connector-python

# Import the drive connector
import mysql.connector

# Connect to the database using the MYSQLConnection class
mysql.connector.MYSQLConnection(host='localhost',user='root',password='your pass')

# Successful connection
mysql.connector.connection.MySQLConnection object at 0x0271EB50

# Connect to the database using the connect() function
mysql.connector.connect(host='localhost',user='root',password='your pass')

# Successful connection
mysql.connector.connection.MySQLConnection object at 0x0271EE20
