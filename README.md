# Python-GUI-project
This project was my assignment for Database and file structures class. This assignment was completed in 12 hours by 2 members (me and my teammate Saurav Kumar Sah).  We used SQL command line and python program to create this GUI which helps in data management and data search using specific criteria. 
Installing the system:
1.	Install sqlite3 in your system from https://www.sqlite.org/download.html
2.	Install python programming language from https://www.python.org/downloads/
3.	Project2.db file that I have provided already has imported data from the provided .csv files. To show what the database are, I have also attached Project2.sql, however to create a GUI, Project2.sql is used but CarRental2019part2.sql not used at all in the creation of this GUI(python), but rather used early on in the project. All additional data is removed, so project.db file only contains data that was from the .csv files. 
4.	.csv file is an excel file that contains all the tabular data for the databases and I have attached all that too. CarRental2019part2.sql contains code for the creation of databases.
I imported data with the given code:
import --skip 1 CUSTOMER.csv customer
.import --skip 1 RENTAL.csv rental
.import --skip 1 RATE.csv rate
.import --skip 1 VEHICLE.csv vehicle

5.	There is no more import required to run the file. In the python code itself titled main.py, we have maintained the connection with code as follows:
Car_rental_connect= sqlite3.connect('project2.db')

6.	I do not use CarRental2019part2.sql  document anywhere in the code. But I have a copy of CarRenta2019part2l.sql that I used for MySQL workbench when I did project part 2. This part of the project was totally done in the console like professor explained in class, so only project2.db file is used, that I have provided.

Submitted by: Resha Adhikari
