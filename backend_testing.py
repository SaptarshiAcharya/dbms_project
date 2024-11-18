import tkinter
from tkinter import PhotoImage
from tkinter import StringVar
from tkinter import OptionMenu
from tkinter import Text
from tkinter import Entry
import mysql.connector
import random
database=mysql.connector.connect(host="localhost",user="root",password="1234",database="railway_resrvation_database")

def main():
  main_menu=tkinter.Tk()
  main_menu.geometry("900x900")
  main_menu.title("RAILWAY RESERVATION SYSTEM")
  global img
  img=PhotoImage(file='railway_image.png')
  background=tkinter.Label(main_menu,font=("times new roman",50),image=img)
  background.place(x=0,y=0)
  l_1=tkinter.Label(main_menu,text="Welcome To Indian Railway Online Booking",font=("times new roman",35),fg="black",bg="yellow").pack()#l_1 is the label displaying text 
  book_ticket=tkinter.Button(main_menu,text="BOOK TICKET",font=("times new roman",35),fg="black",bg="red",command=lambda:book_ticket_window()).pack()
  cancel_ticket=tkinter.Button(main_menu,text="CANCEL TICKET",font=("times new roman",35),fg="black",bg="#00BFFF",command=lambda:cancel_ticket_window()).pack()
  check_status=tkinter.Button(main_menu,text="CHECK STATUS",font=("times new roman",35),fg="black",bg="purple",command=lambda:check_status_window()).pack()
  exit_key_1=tkinter.Button(main_menu,text="EXIT",command=main_menu.destroy,font=("times new roman",35),fg="black",bg="violet").pack()
def book_ticket_window():
  book_ticket=tkinter.Toplevel()
  book_ticket.geometry("300x300")
  book_ticket.title("BOOK TICKET")
  book_ticket.configure(bg="pink")
  
  def callback():
     def confirmation_1():
       confirmation_window=tkinter.Toplevel()
       confirmation_window.geometry("300x300")
       confirmation_window.title("CONFIRM TICKET")
       confirmation_window.configure(bg="pink")
       l_2=tkinter.Label(confirmation_window,text="TRAIN AVAILABLE",font=("times new roman",15),fg="green",bg="pink").grid(row=0,column=0) #l_2 is a lable
       train_data_label_2=tkinter.Label(confirmation_window,text="TRAIN NO: "+str(x[0]),font=("times new roman",10),fg="black",bg="pink").place(x=0,y=40)
       train_data_label_3=tkinter.Label(confirmation_window,text="TRAIN NAME: "+str(x[1]),font=("times new roman",10),fg="black",bg="pink").place(x=0,y=60)
       train_data_label_4=tkinter.Label(confirmation_window,text="DATE OF DEPARTURE: "+str(x[2]),font=("times new roman",10),fg="black",bg="pink").place(x=0,y=80)
       train_data_label_5=tkinter.Label(confirmation_window,text="DATE OF ARRIVAL: "+str(x[3]),font=("times new roman",10),fg="black",bg="pink").place(x=0,y=100)
       train_data_label_6=tkinter.Label(confirmation_window,text="DEPARTURE: "+str(x[4]),font=("times new roman",10),fg="black",bg="pink").place(x=0,y=120)
       train_data_label_7=tkinter.Label(confirmation_window,text="ARRIVAL: "+str(x[5]),font=("times new roman",10),fg="black",bg="pink").place(x=0,y=140)
       if x[6]>0:
        train_data_label_8=tkinter.Label(confirmation_window,text="STATUS: "+"AVAILABLE",font=("times new roman",10),fg="green",bg="pink").place(x=0,y=160)
       else:
         train_data_label_8=tkinter.Label(confirmation_window,text="STATUS: "+"WAITING",font=("times new roman",10),fg="red",bg="pink").place(x=0,y=160)
       proceed_button=tkinter.Button(confirmation_window,text="PROCEED",command=payment,font=("times new roman",10),fg="black",bg="light blue").place(x=0,y=200)
       
     def confirmation_2():
       confirmation_window=tkinter.Toplevel()
       confirmation_window.geometry("300x300")
       confirmation_window.title("CONFIRM TICKET")
       confirmation_window.configure(bg="pink")
       l_2=tkinter.Label(confirmation_window,text="SORRY! NO SCHEDULE TRAIN FOUND",font=("times new roman",10),fg="red",bg="pink").pack()
       exit_key_2=tkinter.Button(confirmation_window,text="GO BACK",command=confirmation_window.destroy,font=("times new roman",10),fg="black",bg="light blue").pack()
       
     def payment():
       payment_window=tkinter.Toplevel()
       payment_window.geometry("300x300")
       payment_window.title("PAYMENT WINDOW")
       payment_window.configure(bg="pink")
       card_var=StringVar()
       card_var.set("       ")
       card_menu=OptionMenu(payment_window,card_var,"CREDIT CARD","DEBIT CARD","UPI").grid(row=0,column=1)
       card_label=tkinter.Label(payment_window,text="PAYMENT METHOD",font=("times new roman",10),fg="black",bg="pink").grid(row=0,column=0)
       card_no_label=tkinter.Label(payment_window,text="CARD NO.",font=("times new roman",10),fg="black",bg="pink").grid(row=1,column=0)
       card_no=Entry(payment_window,width=14,show="*").grid(row=1,column=1)                                                                           
       cvv_label=tkinter.Label(payment_window,text="CVV",font=("times new roman",10),fg="black",bg="pink").grid(row=2,column=0)
       cvv=Entry(payment_window,show="*",width=3).grid(row=2,column=1)
       exp_mon_label=tkinter.Label(payment_window,text="EXPIRY MONTH",font=("times new roman",10),fg="black",bg="pink").grid(row=3,column=0)
       exp_mon=Text(payment_window,width=2,height=0.25).grid(row=3,column=1)
       exp_year_label=tkinter.Label(payment_window,text="EXPIRY YEAR",font=("times new roman",10),fg="black",bg="pink").grid(row=4,column=0)
       exp_year=Text(payment_window,width=4,height=0.25).grid(row=4,column=1)
       payment_button=tkinter.Button(payment_window,text="MAKE PAYMENT",font=("times new roman",10),fg="black",bg="light blue",command=final_confirmation).grid(row=5,column=0)
     def final_confirmation():
       final_window=tkinter.Tk()
       final_window.geometry("300x300")
       final_window.title("PNR NUMBER")
       final_window.configure(bg="pink")
      
       query_2="select * from Reservation_Table"
       cursor_object.execute(query_2)
       l=cursor_object.fetchall()#gets everything from the table in form of tuple in a series
       for i in l:
         pnr_no=i[0]
           
       if pnr_no==None:
         pnr_no=100001 
       else:
         pnr_no=pnr_no+1
       password=random.randint(10000,99999)
       if x[6]>0:
         st="CONFIRMED"
         m=x[6]
         cursor_object.execute("update ticket_booking_table set SEAT_AVAILABLE=%s where t_no=%s",(m-1,x[0]))
         database.commit()
       else:
         st="WAITING"
       cursor_object.execute("insert into Reservation_Table values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(pnr_no,password,x[0],x[1],x[2],x[3],x[4],x[5],st))
       database.commit()
       
       l_3=tkinter.Label(final_window,text="PAYMENT SUCCESSFULL \n YOUR TICKET HAS BEEN BOOKED",font=("times new roman",10),fg="green",bg="pink").grid(row=0,column=0)
       pnr_no_label=tkinter.Label(final_window,text="PNR NO. :"+ str(pnr_no),font=("times new roman",10),fg="black",bg="pink").place(x=0,y=50)
       password_label=tkinter.Label(final_window,text="PASSWORD :"+str(password),font=("times new roman",10),fg="black",bg="pink").place(x=0,y=70)       
       l_4=tkinter.Label(final_window,text="(PLEASE SAVE FOR FUTURE REFERENCE)",font=("times new roman",10),fg="black",bg="pink").place(x=0,y=90)
       exit_key_3=tkinter.Button(final_window,text="EXIT",command=final_window.destroy,font=("times new roman",10),fg="black",bg="light blue").place(x=0,y=130)       
      
     a=from_var.get() 
     b=to_var.get()
     c=date_input.get("1.0","end-1c")
     cursor_object=database.cursor()
     query_1 ="select * from ticket_booking_table"
     cursor_object.execute(query_1)
     m=cursor_object.fetchall()#gets everything from the table in form of tuple in a series
     for x in m:
        if x[4]==a and x[5]== b and x[2]==c:
           
           h=1
           break
        else:
           
           h=0
     if h==1:
       confirmation_1()
     elif h==0:
       confirmation_2()
           
  from_var=StringVar()
  from_var.set("       ")
  from_menu=OptionMenu(book_ticket,from_var,"MUMBAI","KOLKATA","CHENNAI","DELHI","BHOPAL","JAIPUR","SEALDAH","JAMMU","DURG","PUNE","KANPUR CENTRAL","AGARTALA,DHANBAD JN","GANDHINAGAR").grid(row=0,column=1)
  from_label=tkinter.Label(book_ticket,text="DEPARTURE",font=("times new roman",10),fg="black",bg="pink").grid(row=0,column=0)
  to_var=StringVar()
  to_var.set("       ")
  to_menu=OptionMenu(book_ticket,to_var,"MUMBAI","KOLKATA","CHENNAI","DELHI","BHOPAL","JAIPUR","SEALDAH","JAMMU","DURG","PUNE","KANPUR CENTRAL","AGARTALA,DHANBAD JN","GANDHINAGAR").grid(row=2,column=1)
  to_label=tkinter.Label(book_ticket,text="ARRIVAL",font=("times new roman",10),fg="black",bg="pink").grid(row=2,column=0)
  class_var=StringVar()
  class_var.set("       ")
  class_menu=OptionMenu(book_ticket,class_var,"EC","1AC","2AC","3AC","FC","CC","SL").grid(row=3,column=1)
  class_label=tkinter.Label(book_ticket,text="CLASS",font=("times new roman",10),fg="black",bg="pink").grid(row=3,column=0)
  date_var=StringVar()
  date_label=tkinter.Label(book_ticket,text="DATE",font=("times new roman",10),fg="black",bg="pink").grid(row=4,column=0)
  date_input=Text(book_ticket,width=10,height=0.25)
  date_input.grid(row=4,column=1)
  date_label_2=tkinter.Label(book_ticket,text="(YYYY-MM-DD)",font=("times new roman",10),fg="black",bg="pink").grid(row=5,column=0)
  check_avail_button=tkinter.Button(book_ticket,text="CHECK AVAILABILITY",font=("times new roman",10),fg="black",bg="light blue",command=callback).place(x=0,y=140)
  
def check_status_window():
  def information():
    def ticket_details_1():
         ticket_details_window=tkinter.Toplevel()
         ticket_details_window.geometry("300x300")
         ticket_details_window.title("TICKET DETAILS")
         ticket_details_window.configure(bg="pink")
         l_2=tkinter.Label(ticket_details_window,text="TICKET DETAILS",font=("times new roman",15),fg="blue",bg="pink").grid(row=0,column=0) #l_2 is a lable
         train_data_label_2=tkinter.Label(ticket_details_window,text="TRAIN NO: "+str(i[2]),font=("times new roman",10),fg="black",bg="pink").place(x=0,y=40)
         train_data_label_3=tkinter.Label(ticket_details_window,text="TRAIN NAME: "+str(i[3]),font=("times new roman",10),fg="black",bg="pink").place(x=0,y=60)
         train_data_label_4=tkinter.Label(ticket_details_window,text="DATE OF DEPARTURE: "+str(i[4]),font=("times new roman",10),fg="black",bg="pink").place(x=0,y=80)
         train_data_label_5=tkinter.Label(ticket_details_window,text="DATE OF ARRIVAL: "+str(i[5]),font=("times new roman",10),fg="black",bg="pink").place(x=0,y=100)
         train_data_label_6=tkinter.Label(ticket_details_window,text="DEPARTURE: "+str(i[6]),font=("times new roman",10),fg="black",bg="pink").place(x=0,y=120)
         train_data_label_7=tkinter.Label(ticket_details_window,text="ARRIVAL: "+str(i[7]),font=("times new roman",10),fg="black",bg="pink").place(x=0,y=140)
         print(i[8])
         if i[8]=="CONFIRMED":
           train_data_label_8=tkinter.Label(ticket_details_window,text="STATUS: "+"AVAILABLE",font=("times new roman",10),fg="green",bg="pink").place(x=0,y=160)
         else:
           train_data_label_8=tkinter.Label(ticket_details_window,text="STATUS: "+"WAITING",font=("times new roman",10),fg="red",bg="pink").place(x=0,y=160)
         exit_button=tkinter.Button(ticket_details_window,text="EXIT",command=ticket_details_window.destroy,font=("times new roman",10),fg="black",bg="light blue").place(x=10,y=190)
    def ticket_details_2():
         ticket_details_window=tkinter.Toplevel()
         ticket_details_window.geometry("300x300")
         ticket_details_window.title("TICKET DETAILS")
         ticket_details_window.configure(bg="pink")
         l_4=tkinter.Label(ticket_details_window,text="INVALID PNR.NO. OR PASSWORD",font=("times new roman",10),fg="red",bg="pink").pack() #l_4 is a lable
         l_5=tkinter.Label(ticket_details_window,text="PLEASE TRY AGAIN",font=("times new roman",10),fg="red",bg="pink").pack() #l_5 is a lable
         go_back_button=tkinter.Button(ticket_details_window,text="GO BACK",command=ticket_details_window.destroy,font=("times new roman",10),fg="black",bg="light blue").pack()
          
    cursor_object=database.cursor()
    d=password_input.get("1.0","end-1c")
    e=pnr_no_input.get("1.0","end-1c")
    query_3="select * from Reservation_Table"
    cursor_object.execute(query_3)
    l=cursor_object.fetchall()#gets everything from the table in form of tuple in a series
    for i in l:
        
        if e==str(i[0]) and d==str(i[1]):
          ticket_details_1()
          break
    else:
      ticket_details_2()
            
  check_status=tkinter.Toplevel()
  check_status.geometry("300x300")
  check_status.title("CHECK STATUS")
  check_status.configure(bg="pink")
  l_2=tkinter.Label(check_status,text="PLEASE ENTER YOUR PNR. NO. AND PASSWORD",font=("times new roman",10),fg="black",bg="pink").grid(row=0,column=0) 
  pnr_no_label=tkinter.Label(check_status,text="PNR. NO.",font=("times new roman",10),fg="black",bg="pink").place(x=0,y=40)
  pnr_no_input=Text(check_status,width=10,height=0.25)
  pnr_no_input.place(x=120,y=40)
  password_label=tkinter.Label(check_status,text="PASSWORD",font=("times new roman",10),fg="black",bg="pink").place(x=0,y=70)
  password_input=Text(check_status,width=10,height=0.25)
  password_input.place(x=120,y=70)
  submit_button=tkinter.Button(check_status,text="SUBMIT",command=information,font=("times new roman",10),fg="black",bg="light blue").place(x=10,y=120)
   
def cancel_ticket_window():
  def information():
    def cancellation():
        cancel_ticket=tkinter.Toplevel()
        cancel_ticket.geometry("300x300")
        cancel_ticket.title("CANCEL TICKET")
        cancel_ticket.configure(bg="pink")
        cancel_ticket_label=tkinter.Label(cancel_ticket,text="YOUR TICKET HAS BEEN CANCELLED",font=("times new roman",10),fg="red",bg="pink").place(x=30,y=0)
        return_payment_label=tkinter.Label(cancel_ticket,text="YOUR PAYMENT WILL BE RETURNED \n WITHIN 1 TO 2 WORKING DAYS",font=("times new roman",10),fg="red",bg="pink").place(x=30,y=20)
        exit_key_1=tkinter.Button(cancel_ticket,text="EXIT",command=cancel_ticket.destroy,font=("times new roman",12),fg="black",bg="lightblue").place(x=120,y=60)       
        cursor_object.execute("delete from reservation_table where PNR_NO=%s",(i[0],))
        database.commit()
        t=[]
        if i[8]=="CONFIRMED":
         for x in l:
           if x[2]==i[2] and x[8]=="WAITING":
             t.append(x[0])
         if t==[]:
           cursor_object.execute("update ticket_booking_table set SEAT_AVAILABLE=SEAT_AVAILABLE+1 where t_no=%s",(i[2],))
           database.commit()
         else:
           cursor_object.execute("update reservation_table set STATUS='CONFIRMED' where PNR_NO=%s",(min(t),))
           database.commit()                      
    def ticket_details():
         ticket_details_window=tkinter.Toplevel()
         ticket_details_window.geometry("300x300")
         ticket_details_window.title("TICKET DETAILS")
         ticket_details_window.configure(bg="pink")
         l_2=tkinter.Label(ticket_details_window,text="TICKET DETAILS",font=("times new roman",15),fg="blue",bg="pink").grid(row=0,column=0) #l_2 is a lable
         train_data_label_2=tkinter.Label(ticket_details_window,text="TRAIN NO: "+str(i[2]),font=("times new roman",10),fg="black",bg="pink").place(x=0,y=40)
         train_data_label_3=tkinter.Label(ticket_details_window,text="TRAIN NAME: "+str(i[3]),font=("times new roman",10),fg="black",bg="pink").place(x=0,y=60)
         train_data_label_4=tkinter.Label(ticket_details_window,text="DATE OF DEPARTURE: "+str(i[4]),font=("times new roman",10),fg="black",bg="pink").place(x=0,y=80)
         train_data_label_5=tkinter.Label(ticket_details_window,text="DATE OF ARRIVAL: "+str(i[5]),font=("times new roman",10),fg="black",bg="pink").place(x=0,y=100)
         train_data_label_6=tkinter.Label(ticket_details_window,text="DEPARTURE: "+str(i[6]),font=("times new roman",10),fg="black",bg="pink").place(x=0,y=120)
         train_data_label_7=tkinter.Label(ticket_details_window,text="ARRIVAL: "+str(i[7]),font=("times new roman",10),fg="black",bg="pink").place(x=0,y=140)
         if i[8]=="CONFIRMED":
           train_data_label_8=tkinter.Label(ticket_details_window,text="STATUS: "+"AVAILABLE",font=("times new roman",10),fg="green",bg="pink").place(x=0,y=160)
         else:
           train_data_label_8=tkinter.Label(ticket_details_window,text="STATUS: "+"WAITING",font=("times new roman",10),fg="red",bg="pink").place(x=0,y=160)
         cancel_button=tkinter.Button(ticket_details_window,text="CANCEL TICKET",font=("times new roman",10),command=cancellation,fg="black",bg="light blue").place(x=10,y=190)
    def ticket_details_2():
         ticket_details_window=tkinter.Toplevel()
         ticket_details_window.geometry("300x300")
         ticket_details_window.title("TICKET DETAILS")
         ticket_details_window.configure(bg="pink")
         l_4=tkinter.Label(ticket_details_window,text="INVALID PNR.NO. OR PASSWORD",font=("times new roman",10),fg="red",bg="pink").pack() #l_4 is a lable
         l_5=tkinter.Label(ticket_details_window,text="PLEASE TRY AGAIN",font=("times new roman",10),fg="red",bg="pink").pack() #l_5 is a lable
         go_back_button=tkinter.Button(ticket_details_window,text="GO BACK",command=ticket_details_window.destroy,font=("times new roman",10),fg="black",bg="light blue").pack()     
    cursor_object=database.cursor()
    d=password_input.get("1.0","end-1c")
    e=pnr_no_input.get("1.0","end-1c")
    query_3="select * from Reservation_Table"
    cursor_object.execute(query_3)
    l=cursor_object.fetchall()#gets everything from the table in form of tuple in a series
    for i in l:
        
        if e==str(i[0]) and d==str(i[1]):
          ticket_details()
          break
    else:
      ticket_details_2()       
  cancel_ticket=tkinter.Toplevel()
  cancel_ticket.geometry("300x300")
  cancel_ticket.title("CANCEL TICKET")
  cancel_ticket.configure(bg="pink")
  l_2=tkinter.Label(cancel_ticket,text="PLEASE ENTER YOUR PNR. NO. AND PASSWORD",font=("times new roman",10),fg="black",bg="pink").grid(row=0,column=0)
  pnr_no_label=tkinter.Label(cancel_ticket,text="PNR. NO.",font=("times new roman",10),fg="black",bg="pink").place(x=0,y=40)
  pnr_no_input=Text(cancel_ticket,width=10,height=0.25)
  pnr_no_input.place(x=120,y=40)
  password_label=tkinter.Label(cancel_ticket,text="PASSWORD",font=("times new roman",10),fg="black",bg="pink").place(x=0,y=70)
  password_input=Text(cancel_ticket,width=10,height=0.25)
  password_input.place(x=120,y=70)
  submit_button=tkinter.Button(cancel_ticket,text="SUBMIT",command=information,font=("times new roman",10),fg="black",bg="light blue").place(x=10,y=120)
   
  
  
 

  
#__MAIN__

main()











