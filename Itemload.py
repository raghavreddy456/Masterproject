__author__ = 'Raghavendra'
import csv
import MySQLdb
import datetime


#a = datetime.datetime.strptime('09/15/2015', "%b %d %Y %H:%M")
mydb = MySQLdb.connect("localhost","root","test123","Masterproject")
cursor = mydb.cursor()
csv_data = csv.reader(file('C:\Users\Raghavendra\Desktop\Master project\Itemslist.csv'))
counter=0
for row in csv_data:


    query="INSERT INTO Items(item_id,itemname,ItemDescription,ItemMeasurement,ShortItemNo,unitprice,Itemstatus,itemtype,imageurl,vendor_id) \
                   VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,row)
    counter= counter+1

#close the connection to the database.
mydb.commit()
cursor.close()
print("Total Number of rows inserted into the Item table"+ " "+ str(counter))
print "Successfully imported Item csv data into the project database"
