
from tkinter import *

import sqlite3        

TK_SILENCE_DEPRECATION=1

#create tkinter window

root= Tk()

root.title('Car Rental')
root.geometry("1000x1000") 

Car_rental_connect= sqlite3.connect('project2.db')
Car_rental_cursor= Car_rental_connect.cursor()

#alr have code so no execute functions

#insert data in Customer db
def submit1():
    submit_conn= sqlite3.connect('project2.db')
    submit_cursor= submit_conn.cursor()
    
    submit_cursor.execute("select * from customer")
    noOfRows = submit_cursor.fetchall()
    sizeRow = len(noOfRows)
    row = noOfRows[sizeRow-1]
    CustId = row[0]
    CustId = CustId + 1 


    
    submit_cursor.execute("INSERT INTO CUSTOMER  SELECT :CustId, :Name, :Phone",
                        {
                              'Name': Name.get(),
                              'CustId': CustId,
                              'Phone': Phone.get()                          
                        })

    #commit changes   
    submit_conn.commit()
    
    #close connection
    submit_conn.close()


#building gui components
    #build text boxes for Customer db
    
Name= Entry(root, width= 30)
Name.grid(row=1, column=1,  padx=20)

Phone= Entry(root, width= 30)
Phone.grid(row=2, column=1)



#create label

Name_label= Label(root, text= 'Name: ')
Name_label.grid(row=1, column=0)

    
Phone_label= Label(root, text= 'Phone: ')
Phone_label.grid(row=2, column=0)  
    
#submit button to submit data to the Customer db

submit_btn1= Button(root, text= '1. Add records to Customer DB', command= submit1)
submit_btn1.grid(row=4, column=0, columnspan=2, pady=10, padx=100)

    
#insert data in Vehicle DB
def submit2():
    submit_conn= sqlite3.connect('project2.db')
    submit_cursor= submit_conn.cursor()
    
    submit_cursor.execute("INSERT INTO VEHICLE  VALUES(:VehicleId, :Description, :Year, :Type, :Category)",
                        {
                              'VehicleId': VehicleId.get(),
                              'Description': Description.get(),
                              'Year': Year.get(),
                              'Type': Type.get(),
                              'Category': Category.get(),
                                                   
                        })

    #commit changes   
    submit_conn.commit()
    
    #close connection
    submit_conn.close()
   
#build text boxes for vehicle db
    
VehicleId= Entry(root, width= 30)
VehicleId.grid(row=5, column=1,  padx=20)

Description= Entry(root, width= 30)
Description.grid(row=6, column=1)

Year= Entry(root, width= 30)
Year.grid(row=7, column=1)

Type= Entry(root, width= 30)
Type.grid(row=8, column=1)

Category= Entry(root, width= 30)
Category.grid(row=9, column=1)



#create label for vehicle db

VehicleId_label= Label(root, text= 'VehicleId: ')
VehicleId_label.grid(row=5, column=0)

Description_label= Label(root, text= 'Description: ')
Description_label.grid(row=6, column=0)
    
Year_label= Label(root, text= 'Year: ')
Year_label.grid(row=7, column=0)   

Type_label= Label(root, text= 'Type: ')
Type_label.grid(row=8, column=0)
    
Category_label= Label(root, text= 'Category: ')
Category_label.grid(row=9, column=0)       

submit_btn2= Button(root, text= '2. Add records to Vehicle DB', command= submit2)
submit_btn2.grid(row=10, column=0, columnspan=2, pady=10, padx=100)


#qn no 3

#build text boxes for RENTAL db


CustId = Entry (root, width=30)
CustId.grid(row= 19, column=1 )

RentalType= Entry(root, width= 30)
RentalType.grid(row=21, column=1)


VehicleId = Entry (root, width=30)
VehicleId.grid(row = 20 , column=1)

StartDate= Entry(root, width= 30)
StartDate.grid(row=11, column=1)

Category= Entry(root, width= 30)
Category.grid(row=12, column=1)


VehicleType= Entry(root, width= 30)
VehicleType.grid(row=13, column=1)

OrderDate = Entry(root, width=30)
OrderDate.grid(row=17 , column=1)

Qty = Entry(root, width=30)
Qty.grid(row=18, column=1)


ReturnDate= Entry(root, width= 30)
ReturnDate.grid(row=14, column=1)

TotalAmount= Entry(root, width= 30)
TotalAmount.grid(row=15, column=1)

PaymentDate= Entry(root, width= 30)
PaymentDate.grid(row=16, column=1)



#create label for Rental DB

StartDate_label= Label(root, text= 'StartDate: ')
StartDate_label.grid(row=11, column=0)
     
Category_label= Label(root, text= 'Category: ')
Category_label.grid(row=12, column=0)

Orderdate_label = Label(root, text = 'OrderDate: ')
Orderdate_label.grid(row = 17,column=0)

Qty_label = Label(root, text = 'Qty')
Qty_label.grid(row=18, column=0)

VehicleType_label= Label(root, text= 'VehicleType: ')
VehicleType_label.grid(row=13, column=0)
     

ReturnDate_label= Label(root, text= 'ReturnDate: ')
ReturnDate_label.grid(row=14, column=0)

TotalAmount_label= Label(root, text= 'TotalAmount ')
TotalAmount_label.grid(row=15, column=0)

Payment_label= Label(root, text= 'PaymentDate: ')
Payment_label.grid(row=16, column=0)

CustId_label = Label(root, text = "Customer Id")
CustId_label.grid(row = 19, column=0)

VehicleId_label = Label(root, text= "Vehicle Id : ")
VehicleId_label.grid(row = 20, column=0)

RentalType_label= Label(root, text= 'RentalType: ')
RentalType_label.grid(row=21, column=0)
     


def see_available_rental():


    newRentalWindow = Toplevel(root)
    newRentalWindow.geometry('500x500')
    newRentalWindow.title('See available rental')
    
    see_available_rental_conn= sqlite3.connect('project2.db')
    see_available_rental_cursor= see_available_rental_conn.cursor()
   
    records= None
    see_available_rental_cursor.execute("SELECT Vehicle.VehicleId, Vehicle.Type, Vehicle.Category,Vehicle.Type, Vehicle.Description from Vehicle left join Rental on Vehicle.VehicleId = Rental.VehicleId where Rental.VehicleId is NULL and Type = ? AND Category = ?",
                                    (VehicleType.get(),Category.get(),))
                                    
   
                                    
    records= see_available_rental_cursor.fetchall()
    if (records is not None):
   
        print_records= ' '
        for record in records:
            print_records+= (str(record[0])+" "+str(record[1])+ " "+ str(record[2])+ str(record[3])+" "+str(record[4])+"\n")
        print(print_records)
   
    else:
        print("No such records found")
    
    #commit changes   
    see_available_rental_conn.commit()
    
    #close connection
    see_available_rental_conn.close()
    
    view_balance_label= Label(newRentalWindow, text= print_records)
    view_balance_label.grid(row= 25, column=5, columnspan=2)
    
    
    
    
available_rental_btn= Button(root, text= '3. See Available Rental using SD, RD, category, type', command= see_available_rental)
available_rental_btn.grid(row=22, column=0, columnspan=5, pady=10, padx=100)


# Add rental 

def add_new_rental():
    add_new_rental_conn= sqlite3.connect('project2.db')
    add_new_rental_cursor= add_new_rental_conn.cursor()
    
    add_new_rental_cursor.execute("INSERT INTO Rental  VALUES(:CustId, :VehicleId, :StartDate, :OrderDate, :RentalType, :Qty, :ReturnDate, :TotalAmount, :PaymentDate,0)",
                        {
                              'CustId': CustId.get(),
                              'VehicleId': VehicleId.get(),
                              'StartDate': StartDate.get(),
                              'OrderDate': OrderDate.get(),
                              'RentalType': RentalType.get(),
                              'Qty': Qty.get(),
                              'ReturnDate': ReturnDate.get(),
                              'TotalAmount': TotalAmount.get(),
                              'PaymentDate':PaymentDate.get(),
                                                   
                        })

    #commit changes   
    add_new_rental_conn.commit()
    
    #close connection
    add_new_rental_conn.close()
    


add_new_rental_button = Button(root, text = " 3. Add new rental(CustId, VehicleId, all dates, RentalType, Qty, TotalAmount),", command = add_new_rental)
add_new_rental_button.grid(row = 25, column=1, columnspan=2, pady=10 , padx=10)

# Handle the return of a rented car
#Question 4    


rented_ReturnDate_label = Label(root, text=' Returned Date: ')
rented_ReturnDate_label.grid(row= 1, column=5)

rented_customerName_label = Label(root, text = 'Customer Name: ')
rented_customerName_label.grid(row=2,column=5)

rented_customerId_label = Label(root, text = 'Customer ID: ')
rented_customerId_label.grid(row=3,column =5)

rented_VehicleId_label = Label(root, text = 'Vehicle ID: ')
rented_VehicleId_label.grid(row=4,column=5)

rented_Vehicle_Description_label = Label(root, text = 'Description: ')
rented_Vehicle_Description_label.grid(row=5,column=5)

rented_Vehicle_Year_label= Label(root, text = 'Year: ')
rented_Vehicle_Year_label.grid(row=6,column=5)

rented_Vehicle_Category_label = Label(root, text = 'Category: ')
rented_Vehicle_Category_label.grid(row=7,column=5)

rented_Vehicle_Type_label = Label(root, text = 'Type')
rented_Vehicle_Type_label.grid(row=8,column=5)


rented_ReturnDate = Entry (root, width=30)
rented_ReturnDate.grid(row= 1, column=6)

rented_customerName = Entry(root, width=30)
rented_customerName.grid(row=2,column=6)

rented_customerId = Entry(root, width=30)
rented_customerId.grid(row=3,column =6)

rented_VehicleId = Entry(root, width=30)
rented_VehicleId.grid(row=4,column=6)

rented_Vehicle_Description = Entry(root, width=30)
rented_Vehicle_Description.grid(row=5,column=6)

rented_Vehicle_Year = Entry(root, width=30)
rented_Vehicle_Year.grid(row=6,column=6)

rented_Vehicle_Category = Entry(root, width=30)
rented_Vehicle_Category.grid(row=7,column=6)

rented_Vehicle_Type = Entry(root, width=30)
rented_Vehicle_Type.grid(row=8,column=6)



def return_rental():
   return_rental_conn= sqlite3.connect('project2.db')
   return_rental_cursor= return_rental_conn.cursor()
   
   return_rental_cursor.execute(" UPDATE Rental SET Returned = 1, ReturnDate= ? WHERE VehicleId= ? AND ReturnDate=?",
                                 (rented_ReturnDate.get(), rented_VehicleId.get(), rented_ReturnDate.get(),))
  
                                    
   #commit changes   
   return_rental_conn.commit()
    
    #close connection
   return_rental_conn.close()
    
return_rental_btn= Button(root, text= '4. Return rental using VehicleId and ReturnDate', command= return_rental)
return_rental_btn.grid(row=10, column=5, columnspan=2, pady=10, padx=100)

# new Window 
def viewBalance4():


    newVehicleWindow = Toplevel(root)
    newVehicleWindow.geometry('500x500')
    newVehicleWindow.title('View Balance')
    

    view_balance_conn= sqlite3.connect('project2.db')
    view_balance_cursor= view_balance_conn.cursor()
    
    view_balance_cursor.execute(" SELECT Rental.CustId, Rental.VehicleId, Rental.TotalAmount as Balance, Vehicle.Description, Vehicle.Year, Vehicle.Type, Vehicle.Category FROM Vehicle, Rental WHERE CustId= ? GROUP BY Rental.VehicleId",
                                 (rented_customerId.get(),))
    
    output_records= view_balance_cursor.fetchall()
    print_records= ' '
    for record in output_records:
        print_records+= (str(record[0])+" "+str(record[1])+ " "+ str(record[2])+" "+str(record[3])+" "+str(record[4])+" "+str(record[5])+ str(record[6])+ "\n")
    print(print_records)
     #commit changes   
    view_balance_conn.commit()
    
    #close connection
    view_balance_conn.close()

    view_balance_label= Label(newVehicleWindow, text= print_records)
    view_balance_label.grid(row= 25, column=5, columnspan=2)


   
view_balance_btn= Button(root, text= '4. View balance using custId', command= viewBalance4)
view_balance_btn.grid(row=9, column=5, columnspan=2, pady=10, padx=100)


#Question 5 a. View Results

# row 11 col 5

#use text boxes and label from qn 4 rented_customerName.grid(row=2,column=6)  rented_customerId


def viewTotalBalance5a():

    newVehicleWindow = Toplevel(root)
    newVehicleWindow.geometry('500x500')
    newVehicleWindow.title('View Total Balance')
    
    
    viewRemaingBalance_conn = sqlite3.connect('project2.db')
    viewRemaingBalance_cursor = viewRemaingBalance_conn.cursor()
    
    print_records= ' '
    
    if (len(rented_customerName.get())!=0):
        viewRemaingBalance_cursor.execute("SELECT Customer.Name, Sum(Rental.TotalAmount) FROM RENTAL,Customer WHERE Customer.CustId= Rental.CustId AND Rental.Returned=0 AND  Customer.Name=? Group BY Customer.Name",
                                       (rented_customerName.get(),))
                                       
        output_records = viewRemaingBalance_cursor.fetchall()
        for record in output_records:
            print_records+= (str(record[0])+"  $"+str(record[1])+ "\n")
        print(print_records)
                               
                               
    elif (len(rented_customerId.get())!=0):
        viewRemaingBalance_cursor.execute("SELECT Customer.Name, Sum(Rental.TotalAmount) AS TOTALBALANCE FROM RENTAL, Customer WHERE Customer.CustId= Rental.CustId AND Rental.Returned=0 AND Rental.CustId=? Group BY Rental.CustId",
                                       (rented_customerId.get(),))
        output_records = viewRemaingBalance_cursor.fetchall()
        for record in output_records:
            print_records+= (str(record[0])+" "+str(record[1])+ "\n")
        print(print_records)
        

    #Commit changes 
    viewRemaingBalance_conn.commit()
    # close connection
    viewRemaingBalance_conn.close()
    
    
    # print to gui
    view_RemainingBalance_label = Label(newVehicleWindow, text = print_records)
    view_RemainingBalance_label.grid(row= 25, columnspan=2, pady=10, padx=100)

view_RemaingBalance_btn = Button(root, text = " 5a.View the Total Balance using only the Customer name or id", command = viewTotalBalance5a)
view_RemaingBalance_btn.grid(row = 11, column=5, columnspan=2, pady=10 , padx=100 )


def vehicleDescription5b():
    newVehicleWindow = Toplevel(root)
    newVehicleWindow.geometry('500x500')
    newVehicleWindow.title('View Vehicle Description')
    
    vehicleDescription5b_conn = sqlite3.connect('project2.db')
    vehicleDescription5b_cursor = vehicleDescription5b_conn.cursor()
    
    print_records= ' '
    
    if (len(rented_Vehicle_Description.get())!=0):
        vehicleDescription5b_cursor.execute("SELECT Vehicle.VehicleId, Vehicle.Description, AVG(TotalAmount) from vehicle left join rental on Vehicle.VehicleId= Rental.VehicleId WHERE Vehicle.Description=? AND Vehicle.Description  '%rented_Vehicle_Description.get()%' ",
                                       (rented_Vehicle_Description.get(),))
        output_records = vehicleDescription5b_cursor.fetchall()
        for record in output_records:
            print_records+= (str(record[0])+" "+str(record[1])+ " "+str(record[2]) +"\n")
        print(print_records)

                               
                               
    elif (len(rented_VehicleId.get())!=0):
        vehicleDescription5b_cursor.execute("SELECT Vehicle.VehicleId, Vehicle.Description, AVG(Rental.TotalAmount) from vehicle left join rental on Vehicle.VehicleId= Rental.VehicleId Where Vehicle.VehicleId=?",
                                       (rented_VehicleId.get(),))
                                       
        output_records = vehicleDescription5b_cursor.fetchall()
        for record in output_records:
            print_records+= (str(record[0])+" "+str(record[1])+ " "+str(record[2])+"\n")
        print(print_records)
    
    
    vehicleDescription5b_conn.commit()
    # close connection
    vehicleDescription5b_conn.close()
    
    # print to gui
    vehicleDescription_label = Label(newVehicleWindow, text = print_records)
    vehicleDescription_label.grid(row= 25, columnspan=2, pady=10, padx=100)
    
      

view_RemaingBalance_btn = Button(root, text = " 5b.View the Vehicle Description(by Vid or description", command = vehicleDescription5b)
view_RemaingBalance_btn.grid(row = 12, column=5, columnspan=2, pady=10 , padx=100 )

root.mainloop()

