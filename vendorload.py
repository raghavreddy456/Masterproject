__author__ = 'Raghavendra'
import csv
import MySQLdb

mydb = MySQLdb.connect("localhost","root","test123","Masterproject")
cursor = mydb.cursor()
csv_data = csv.reader(file('C:\Users\Raghavendra\Desktop\Master project\itemvendors.csv'))
counter=0
for row in csv_data:

    query="INSERT INTO vendors(vendor_id,vendorname,emailid,gender,phoneno,address,country,state,city,zipcode) \
                   VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,row)
    counter= counter+1

#close the connection to the database.
mydb.commit()
cursor.close()
print("Total Number of rows inserted into the vendor table"+ " "+ str(counter))
print "Successfully imported customer csv data into the project database"
