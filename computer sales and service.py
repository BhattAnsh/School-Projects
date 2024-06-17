#importing mysql connector
import mysql.connector as mysql

#connecting mysql to the python
con = mysql.connect(host="localhost", user = "root", password="9013836121")
if con.is_connected():
    print("Connection is successfull.")
cursor = con.cursor()

#creating and using database
cursor.execute('create database if not exists computer_sales_and_service;')
cursor.execute('use computer_sales_and_service;')
print(" ")
print("--------------------------------------------------------------------------------------------------------------")
print(" ")

# welcome note
print("WELCOME TO COMPUTER SALES AND SERVICE")
print('1.to buy computer parts')
print('2.to ask for computer service')
print('3.problem with our sales or service')
print('4.to see various comments and ratings on our products')
print('5.exit')
print(" ")
choice=int(input('enter your choice:'))
while True:
# checking user choice and performing the task according to the user choice
    if choice == 1:
        print("Welcome sir/Mam please choose the computer parts you want to buy-")
        print("RAM\nHDD\nSSD\nMother board\nGraphic card\nProcessor\nCooling system")
        print(" ")
        print("----------------------------------------------------------------------------------------------------------")
        print(" ")
        print("Please fill the following details so we can deliver your product as soon as possible")
        name = input("Enter your name here: ")
        phn_number = int(input("Enter your phone number here: "))
        gender = input("Enter your gender here: ")
        address = input("Enter your address here: ")
        part = input("Enter the part you want to buy: ")
        print("Thankyou sir/Mam! For placing order from CSS, We will try to deliver your product as soon as possible.")
        print(" ")
        print(" ")
        print("Can you please give the rating and comment to our service ")
        print('1. 1 Star')
        print('2. 2 Star')
        print('3. 3 Star')
        print('4. 4 Star')
        print('5. 5 Star')
        print(" ")
        print(" ")
        rating = int(input("Please enter rating here: "))
        comment = input("Enter the Comment here: ")

        # creating table and inserting values in it
        create_customer_table = "create table if not exists customer_detail(Name varchar(20), Phone_number bigint, Gender varchar(20), address varchar(100),Part_purchased varchar(20));"
        cursor.execute(create_customer_table)
        create_rateing_table = "create table if not exists ratings(Name varchar(20),Phone_number bigint, Product varchar(20),Rating int, Comment varchar(200));"
        cursor.execute(create_rateing_table)
        insert1 = "insert into customer_detail values(%s, %s, %s, %s, %s)"
        insert1_val = (name, phn_number, gender, address, part)
        insert2 = "insert into ratings values(%s, %s, %s, %s, %s)"
        insert2_val = (name, phn_number, part, rating, comment)
        cursor.execute(insert1, insert1_val)
        con.commit()
        cursor.execute(insert2, insert2_val)
        con.commit()
        print("")
        print("----------------------------------------------------------------------------------------------------------------")
        print("")
        print("WELCOME TO COMPUTER SALES AND SERVICE")
        print('1.to buy computer parts')
        print('2.to ask for computer service')
        print('3.problem with our sales or service')
        print('4.to see various comments and ratings on our products')
        print('5.exit')
        print(" ")
        choice=int(input('enter your choice:'))

    # if user entered 2 in the choice
    elif choice == 2:
        print(" ")
        print("COMPUTER SERVICES")
        print(" ")
        name = input("Enter your name here: ")
        phn_no = int(input("Enter your phone number here: "))
        email = input("Enter your email here: ")
        address = input("Enter your address here: ")
        service = input("Enter which service you want: ")
        print("")
        print("Sir/Mam service you want is registered and will be done in few days thanks for visiting :) ")
        print("")

    # creating table for customer services
        create_customer_service_table = "create table if not exists customer_services(Name varchar(20), Phone_number bigint, Email varchar(50), address varchar(100),Service varchar(100));"
        cursor.execute(create_customer_service_table)
        con.commit()
        insert = "insert into customer_services values(%s, %s, %s, %s, %s)"
        insert_val = (name, phn_no, email, address, service)
        cursor.execute(insert, insert_val)
        con.commit()
        print("")
        print("----------------------------------------------------------------------------------------------------------------")
        print("")
        print("WELCOME TO COMPUTER SALES AND SERVICE")
        print('1.to buy computer parts')
        print('2.to ask for computer service')
        print('3.problem with our sales or service')
        print('4.to see various comments and ratings on our products')
        print('5.exit')
        print(" ")
        choice=int(input('enter your choice:'))

    #if user entered 3 in the choice
    elif choice == 3:
        print("")
        print("PROBLEMS WITH OUR SERVICE")
        print("")
        print("Sir/Mam Please fill the following form to register your complain.")

        #taking information of user and problem
        print("------------------------------------------------------------------------------------------------------------")
        name = input("Enter your name here: ")
        phn_no = int(input("Enter your phone numbere here: "))
        email_id = input("Enter your email address here: ")
        address = input("Enter your address here: ")
        problem = input("Enter your Problem here: ")

        #creating problems table
        create_customer_problem_table = "create table if not exists customer_problem(Name varchar(20), Phone_Number bigint, Email_Address varchar(50), Address varchar(100),Problem varchar(999));"
        cursor.execute(create_customer_problem_table)
        con.commit()
        insert1 = "insert into customer_problem values(%s, %s, %s, %s, %s)"
        insert1_val = (name, phn_no, email_id, address, problem)
        cursor.execute(insert1, insert1_val)
        con.commit()
        print("")
        print("----------------------------------------------------------------------------------------------------------------")
        print("")
        print("WELCOME TO COMPUTER SALES AND SERVICE")
        print('1.to buy computer parts')
        print('2.to ask for computer service')
        print('3.problem with our sales or service')
        print('4.to see various comments and ratings on our products')
        print('5.exit')
        print(" ")
        choice=int(input('enter your choice:'))
    elif choice == 4:
        print("RATINGS AND COMMENTS")
        part = input("Enter the part of which you want to know about: ")
        task = "select Name, Rating, Comment from ratings where Product = %s"
        part = (part,)
        cursor.execute(task,part)
        result = cursor.fetchall()
        for x in result:
            print('name=',x[0])
            print('rating= ',x[-2])
            print('comment = ', x[-1])
            print('--------------------------')
        print("")
        print("----------------------------------------------------------------------------------------------------------------")
        print("")
        print("WELCOME TO COMPUTER SALES AND SERVICE")
        print('1.to buy computer parts')
        print('2.to ask for computer service')
        print('3.problem with our sales or service')
        print('4.to see various comments and ratings on our products')
        print('5.exit')
        print(" ")
        choice = int(input("Enter your choice here: "))
    elif choice == 5:
        break
    else:
        print("Choose service from the given opions")
        print()
        print('1.to buy computer parts')
        print('2.to ask for computer service')
        print('3.problem with our sales or service')
        print('4.to see various comments and ratings on our products')
        print('5.exit')
        print(" ")
        choice = int(input("Enter your choice here: "))
        
