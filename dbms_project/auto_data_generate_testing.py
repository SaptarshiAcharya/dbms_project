import mysql.connector
mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="RAILWAY_RESRVATION_DATABASE",
    #charset='utf8'
    
    )
mycursor = mydb.cursor()

sql= "INSERT INTO Ticket_Booking_Table VALUES(%s,%s,%s,%s,%s,%s,%s)"
val=[
    (1001, 'RAJDHANI EXPRESS', '2022-02-02', '2022-02-04', 'NEW DELHI', 'KOLKATA', 2),
    (1002, 'DURONTO EXPRESS', '2022-03-29', '2022-03-01', 'KOLKATA', 'MUMBAI', 3),
    (1003, 'SHALIMAR EXPRESS', '2022-02-04', '2022-02-05', 'DELHI', 'JAMMU', 4),
    (1004, 'AMARKANTAK EXPRESS', '2022-03-01', '2022-03-03', 'BHOPAL', 'DURG', 1),
    (1005, 'DURONTO EXPRESS', '2022-02-05', '2022-02-07', 'JAIPUR', 'PUNE', 5),
    (1006, 'RAJDHANI EXPRESS', '2022-02-13', '2022-02-14', 'DELHI', 'KANPUR CENTRAL', 5),
    (1007, 'DURONTO EXPRESS', '2022-03-15', '2022-03-18', 'DELHI', 'CHENNAI', 2),
    (1008, 'SEALDAH EXPRESS', '2022-02-22', '2022-02-25', 'SEALDAH', 'AGARTALA', 7),
    (1009, 'RAJHDHANI EXPRESS', '2022-03-10', '2022-03-11', 'DELHI', 'DHANBAD JN', 4),
    (1010, 'SHATAPDI EXPRESS', '2022-02-25', '2022-02-28', 'MUMBAI', 'GANDHINAGAR', 5)
]
mycursor.executemany(sql,val)
mydb.commit()

'''IMPORTANT NOTES:
FIRST CREATE THE DATABASE USING SQL- RAILWAY_RESRVATION_DATABASE
USE THIS CODE IN SQL TO FIRST CREATE THE TABLE 1: CREATE TABLE Ticket_Booking_Table(T_NO int,T_NAME VARCHAR(100),DATE_OF_DEPARTURE VARCHAR(100), DATE_OF_ARRIVAL VARCHAR(100),DEPARTURE VARCHAR(50),ARRIVAL VARCHAR(50), SEAT_AVAILABLE int,primary key(T_NO));
AFTER THAT RUN THE ABOVE CODE TO INSERT THE DATA.
NOW USE THIS CODE TO CREATE THE SECOND TABLE:  create table Reservation_Table(PNR_NO int NOT NULL PRIMARY KEY, PASSWORD int,T_NO int, T_NAME varchar(100), DATE_OF_DEPARTURE varchar(100), DATE_OF_ARRIVAL varchar(100), DEPARTURE varchar(100), ARRIVAL varchar(100), STATUS varchar(50));
 NOW U CAN START CODDING THE GUI AS BOTH TABLES ARE CREATED'''
