__author__ = 'Raghavendra'
'''
Code to check for the database connection
'''
#code to connect mysql database
import MySQLdb
# a global to hold the DB handle
the_database_connection = False

'''
This function saves the database connection, so if you
invoke this again, it gives you the same one, rather
than making a second connection.  This is the so-called
Singleton pattern.
'''
if not the_database_connection:
    try:
        the_database_connection = MySQLdb.connect("localhost","root","test123","Masterproject")
        # so modifications take effect automatically
        the_database_connection.autocommit(True)
        print("Connected to project database succesfully")
    except MySQLdb.Error, e:
            print ("Couldn't connect to database. MySQL error",e)



















