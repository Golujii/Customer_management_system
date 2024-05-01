import json
import requests
import streamlit as st
import mysql.connector
import pandas as pd
import datetime
st.set_page_config(page_title="Customer Management System")
st.title("CUSTOMER MANAGEMENT SYSTEM")
st.header("WELCOME")
choice=st.sidebar.selectbox("My Menu",("Home","Employee Login","Add Customers","Order Online"))
st.sidebar.image("https://th.bing.com/th/id/OIP.73wb-l_G0LOLEP7iWwYJlwHaHq?rs=1&pid=ImgDetMain")
prompt = st.chat_input("How may I help you today?")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
st.sidebar.title("Contact Us 1800-965-897")
with st.sidebar:
    add_radio = st.radio("Choose a shipping method",("Standard (5-15 days)", "Express (2-5 days)"))
if(choice=="Home"):
    st.image("https://www.clipartkey.com/mpngs/m/273-2734478_customer-relationship-manager-vector.png")
    st.write("Hello this is an application developed by Divyansh Verma as a part of Training Project")
    with st.form("my_form"):
        st.write("Customer Satisfaction Form")
        my_number = st.slider('Pick a number', 1,5)
        my_color = st.selectbox('Pick a color', ['Red','Green'])
        st.form_submit_button('Submit My Picks')
        st.write(my_number)
        st.write(my_color)
elif(choice=="Employee Login"):
    if 'login' not in st.session_state:
        st.session_state['login']=False
    uid=st.text_input("Enter Admin ID")
    ups=st.text_input("Enter Password")
    btn=st.button("Login")
    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="customers")
        c=mydb.cursor()
        c.execute("Select * from Admin")
        for row in c:
            if(uid==row[0] and ups==row[1]):
                st.session_state['login']=True
                break
    if(st.session_state['login']==False):
        st.subheader("Incorrect ID or Password")
    if(st.session_state['login']==True):
        st.subheader("Login Successful")
    choice2=st.selectbox("Features",("None","Customer Details","Contacts"))
    if(choice2=="Customer Details"):
        mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="customers")
        c=mydb.cursor()
        c.execute("Select * from customer")
        l=[]
        for r in c:
            l.append(r)
        df=pd.DataFrame(data=l,columns=['customer_id','first_name','last_name','email','phone','address'])
        st.dataframe(df)
    elif(choice2=="Contacts"):
        mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="customers")
        c=mydb.cursor()
        c.execute("Select * from contacts")
        l=[]
        for r in c:
            l.append(r)
        df=pd.DataFrame(data=l,columns=['contact_id','customer_id','contact_date','message'])
        st.dataframe(df)
elif(choice=="Add Customers"):
    if 'login2' not in st.session_state:
        st.session_state['login2']=False
    uid=st.text_input("Enter Admin ID")
    ups=st.text_input("Enter Password")
    btn2=st.button("Login")
    if btn2:
        mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="customers")
        c=mydb.cursor()
        c.execute("Select * from Admin")
        for row in c:
            if(uid==row[0] and ups==row[1]):
                st.session_state['login']=True
                break
    if(st.session_state['login']==False):
        st.subheader("Incorrect ID or Password")
    if(st.session_state['login']==True):
        st.subheader("Login Successful")
    choice3=st.selectbox("Manage Customer",("Add Customer","Order Items","Payments","View Orders"))
    if(choice3=="Add Customer"):
        cid=input("Enter CustomerID")
        fn=input("Enter First Name")
        ln=input("Enter Last Name")
        em=input("Enter E-Mail")
        ph=input("Enter Phone Number")
        add=input("Enter Address")
        btn3=st.button("Add Attendance")
        if(btn3):
            mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="customers")
            c=mydb.cursor()
            c.execute("insert into customer values(%s,%s,%s,%s,%s,%s)",(cid,fn,ln,em,ph,add))
            mydb.commit()
            st.header("Customer Data Recorded")
    if(choice3=="Order Items"):
        Oid=st.text_input("Enter Order Item ID")
        Pd=st.text_input("Enter Product ID")
        qt=st.text_input("Enter Enter Quantity")
        sut=st.text_input("Enter Subtotal")
        btn4=st.button("Add Order Items")
        if(btn4):
            mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="customers")
            c=mydb.cursor()
            c.execute("insert into order_items values(%s,%s,%s,%s)",(Oid,Pd,qt,sut))
            mydb.commit()
            st.header("Order Items Recorded")
    if(choice3=="Payments"):
        Pid=st.text_input("Enter Payment ID")
        Od=st.text_input("Enter Order ID")
        Pyd=st.text_input("Enter Payment Date")
        Am=st.text_input("Enter Amount")
        btn5=st.button("Enter Transaction")
        if(btn5):        
            mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="customers")
            c=mydb.cursor()
            c.execute("insert into payments values(%s,%s,STR_TO_DATE('%d-%m-%Y'),%s)",(Pid,Od,Pyd,Am))
            mydb.commit()
            st.header("Transaction Recorded")
    if(choice3=="View Orders"):
        mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="customers")
        c=mydb.cursor()
        c.execute("Select * from orders")
        l=[]
        for r in c:
            l.append(r)
        df=pd.DataFrame(data=l,columns=['order_id','customer_id','order_date','total_amount'])
        st.dataframe(df)
elif(choice=="Order Online"):
    if 'login' not in st.session_state:
        st.session_state['login']=False
    fid=st.text_input("Enter Customer ID")
    cps=st.text_input("Enter Password")
    btn6=st.button("Login")
    if btn6:
        mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="customers")
        c=mydb.cursor()
        c.execute("Select * from Customer_Login")
        for row in c:
            if(fid==row[0] and cps==row[1]):
                st.session_state['login']=True
                break
    if(st.session_state['login']==False):
        st.subheader("Incorrect ID or Password")
    if(st.session_state['login']==True):
        st.subheader("Login Successful")
    choice4=st.selectbox("Place Your Order Here",("Check Availability","Place Order"))
    if (choice4=="Check Availability"):
        Product_Check= ['Wheat', 'Biscuits', 'Cold Drink', 'Coffee','Alcohol','Books']
        Product = st.text_input('Type a Product')
        btn7=st.button("Check Availability")
        if btn7:
            have_it = Product.lower() in Product_Check 
            st.text_input("This Product is Available")
        else: 
            ("We don't have that Product")
    