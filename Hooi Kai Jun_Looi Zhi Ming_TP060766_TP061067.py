# Hooi Kai Jun
# TP060766
# Looi Zhi Ming
# TP061067

import os 

#login function for Admin
def admin_login():
    while True:
        while True:
            username  = input("Please enter your username : ")
            if not len(username) > 0: #If the user did not enter their username, it will be in a constant loop until the conditions are met then it will break out from the loop  
                print("Username cannot be empty!")
                continue
            break
        
        while True:
            password  = input("Please enter your password : ")
            if not len(password) > 0:
                print("Password cannot be empty!")
                continue
            break    
          
        for line in open("admin.txt","r").readlines(): # Searching is done and the lines are being read
            login_info = line.split() # Split on the space, and store the results in a list of two strings
            if username == login_info[0] and password == login_info[1]: #If the username is in index 0 and password is index 1 inside the text file, then they will proceed to the next function
                print("Correct credentials!")
                admin_menu(username) #A parameter is also set to allow the Admin to access this menu only.
                return True
            else:
                print("Incorrect credentials.")
                continue

#admin_menu
def admin_menu(username):
    while True:
        print("Welcome to Admin Page!")
        print("What would you like to do?")
        print("1. Add cars to be rented out")
        print("2. Modify car details")
        print("3. Display records")
        print("4. Search specific record")
        print("5. Return rented car")
        print("6. Exit")
        input_3 = (input("Enter choice : "))

        try:
            input_3 = int(input_3)
        except:
            print("Choose a valid choice")

        if(input_3 == 1):
            cars_rented_out(username)
        elif(input_3 == 2):
            modify_car_details_menu(username)            
        elif(input_3 == 3):
            records(username)
        elif(input_3 == 4):
            search(username)
        elif(input_3 == 5):
            return_rented_car(username)
        elif(input_3 == 6):
            print("Thank you!")
            exit()
        else:
            print("Enter a valid choice")
            continue

        break 

#add cars to be rented out
def cars_rented_out(username):
    while True:
        print("What would you like to do?\n1. Add Cars\n2. Main menu")
        choice = input("Enter choice : ")

        try:
            choice = int(choice)
        except:
            print("Please choose a valid choice")

        if choice == 1:
            car_id = input("Enter Car ID : ")
            car = input("Enter car name : ")
            price = input("Enter price per hour : ")
            status = input("Enter car available or not available : ")

            print("Do you want to add car?")
            choice3 = input("Yes or No : ")
            if (choice3 == "Yes"):
                add_car = open("add_rent_cars.txt", "a")
                add_car.write("\n")
                add_car.write(car_id)
                add_car.write(" ")
                add_car.write(car)
                add_car.write(" ")
                add_car.write(price)
                add_car.write(" ")
                add_car.write(status)
                add_car.close()
                print("Car details added!")
                cars_rented_out(username)
            elif(choice3 == "No"):
                admin_menu(username)
        
        if choice == 2:
            admin_menu(username)
        else:
            print("Please choose a valid choice")

#modify car details:
def modify_car_details(username):
    while True:
        print("These are the cars available in the list")
        
        for file in open("add_rent_cars.txt","r").readlines(): # Read the lines
            print(file.rstrip()) #Spaces will be stripped
        
        i=0
        while True:
            search = input("Enter car ID : ")
            if not len(search) > 0:
                print("Field cannot be empty!")
                continue
            break

        for file in open("add_rent_cars.txt","r").readlines(): # Read the lines
            
            if search in file :
                carDetails= [] #List is created
                for cars in open("add_rent_cars.txt","r").readlines(): # Read the lines, searching will be done
                    cardetail = cars.strip("\n") #New lines will be stripped
                    carDetails.append(cardetail) #stripped data will be appended to the list that has been created
                print(carDetails[i]) #information will be printed out based on the user input
                print("1. Car ID\n2. Car Name\n3. Price\n4. Status")

                choice = input("Enter choice : ")
            
                try:
                    choice = int(choice)
                except:
                    print("Choose a valid choice")

                if choice == 1:
                    print(carDetails[i])
                    car = input("Enter old car ID : ")
                    car1 = input("Enter new car ID : ")
            
                    for line in open("add_rent_cars.txt","r").readlines(): # Read the lines
                        cars = line.split(" ") # Split on the space, and store the results in a list of two strings
                        oldcarid = cars[0].strip("\n")
                        
                        if car == oldcarid:

                            read = open("add_rent_cars.txt", "r")
                            new_file_content = ""
                            new_line_content = []
                            for line in read:
                                stripped_line = line.strip()
                                new_line = stripped_line.replace(car, car1)
                                new_file_content += new_line +"\n"

                            lnum = i
                            new_line_content = new_file_content.split("\n")

                            details = open("add_rent_cars.txt", "r")
                            list_of_lines = details.readlines()
                            list_of_lines[lnum] = new_line_content[lnum]+"\n"
                                

                            writing_file = open("add_rent_cars.txt", "w")
                            writing_file.writelines(list_of_lines) #writelines is used as list is being appended into the file
                            writing_file.close()
                            
                            for line in open("cars_rented_out.txt","r").readlines(): # Read the lines
                                cars = line.strip("\n").split(" ") # Split on the space, and store the results in a list of two strings
                                if car == cars[1]:
                                                            
                                    read = open("cars_rented_out.txt", "r")
                                    new_file_content = ""
                                    for line in read:
                                        stripped_line = line.strip()
                                        new_line = stripped_line.replace(car, car1)
                                        new_file_content += new_line +"\n"
                                

                                    writing_file = open("cars_rented_out.txt", "w")
                                    writing_file.write(new_file_content)
                                    writing_file.close()
                    
                            
   
                    modify_car_details_menu(username)
                
                elif choice == 2:
                    print(carDetails[i])
                    car = input("Enter old car name : ")
                    car1 = input("Enter new car name : ")
            
                    for line in open("add_rent_cars.txt","r").readlines(): # Read the lines
                        cars = line.split(" ") # Split on the space, and store the results in a list of two strings
                        oldcarid = cars[1].strip("\n")
                        
                        if car == oldcarid:

                            read = open("add_rent_cars.txt", "r")
                            new_file_content = ""
                            new_line_content = []
                            for line in read:
                                stripped_line = line.strip()
                                new_line = stripped_line.replace(car, car1)
                                new_file_content += new_line +"\n"

                            lnum = i
                            new_line_content = new_file_content.split("\n")

                            details = open("add_rent_cars.txt", "r")
                            list_of_lines = details.readlines()
                            list_of_lines[lnum] = new_line_content[lnum]+"\n"
                                

                            writing_file = open("add_rent_cars.txt", "w")
                            writing_file.writelines(list_of_lines)
                            writing_file.close()
                            
                            for line in open("cars_rented_out.txt","r").readlines(): # Read the lines
                                cars = line.strip("\n").split(" ") # Split on the space, and store the results in a list of two strings
                                if car == cars[2]:
                                                            
                                    read = open("cars_rented_out.txt", "r")
                                    new_file_content = ""
                                    for line in read:
                                        stripped_line = line.strip()
                                        new_line = stripped_line.replace(car, car1)
                                        new_file_content += new_line +"\n"
                                

                                    writing_file = open("cars_rented_out.txt", "w")
                                    writing_file.write(new_file_content)
                                    writing_file.close()
                    
                    modify_car_details_menu(username)
                
                elif choice == 3:
                    print(carDetails[i])
                    car = input("Enter old price : ")
                    car1 = input("Enter new price : ")
            
                    for line in open("add_rent_cars.txt","r").readlines(): # Read the lines
                        cars = line.split(" ") # Split on the space, and store the results in a list of two strings
                        oldcarid = cars[2].strip("\n")
                        
                        if car == oldcarid:

                            read = open("add_rent_cars.txt", "r")
                            new_file_content = ""
                            new_line_content = []
                            for line in read:
                                stripped_line = line.strip()
                                new_line = stripped_line.replace(car, car1)
                                new_file_content += new_line +"\n"

                            lnum = i
                            new_line_content = new_file_content.split("\n")

                            details = open("add_rent_cars.txt", "r")
                            list_of_lines = details.readlines()
                            list_of_lines[lnum] = new_line_content[lnum]+"\n"
                                

                            writing_file = open("add_rent_cars.txt", "w")
                            writing_file.writelines(list_of_lines)
                            writing_file.close()                          
                    
                    modify_car_details_menu(username)
                
                elif choice == 4:
                    print(carDetails[i])
                    car = input("Enter old availability: ")
                    car1 = input("Enter new availability : ")
            
                    for line in open("add_rent_cars.txt","r").readlines(): # Read the lines
                        cars = line.split(" ") # Split on the space, and store the results in a list of two strings
                        oldcarid = cars[3].strip("\n")
                        
                        if car == oldcarid:

                            read = open("add_rent_cars.txt", "r")
                            new_file_content = ""
                            new_line_content = []
                            for line in read:
                                stripped_line = line.strip()
                                new_line = stripped_line.replace(car, car1)
                                new_file_content += new_line +"\n"

                            lnum = i
                            new_line_content = new_file_content.split("\n")

                            details = open("add_rent_cars.txt", "r")
                            list_of_lines = details.readlines()
                            list_of_lines[lnum] = new_line_content[lnum]+"\n"


                            writing_file = open("add_rent_cars.txt", "w")
                            writing_file.writelines(list_of_lines)
                            writing_file.close()
                            break

                    
                    modify_car_details_menu(username)
                
                
                else:
                    print("Enter a valid choice")
                    continue
            i+=1
        
        else:
            print("Car ID not found!")
            
#modify car details menu
def modify_car_details_menu(username):
    while True:
        print("What would you like to do?\n1. Modify Car Details\n2. Main menu")
        choice = input("Enter choice : ")

        try:
            choice = int(choice)
        except:
            print("Enter a valid choice")
            continue

        if choice == 1:
            modify_car_details(username)
        elif choice == 2:
            admin_menu(username)
        else:
            print("Choose a valid choice")

#display records
def records(username):
    while True:
        print("What would you like to do?")
        print("1. Display Cars Rented Out")
        print("2. Display Cars Available For Rent")
        print("3. Display Customer Bookings")
        print("4. Display Customer Payment For a Specific Time Duration")
        print("5. Main Menu")
        choice4 = input("Enter choice : ")

        try:
            choice4 = int(choice4)
        except:
            print("Choose a valid choice")

        if(choice4 == 1):
            file = open("cars_rented_out.txt", "r") #A variable is assigned to open the file
            print(file.read()) #All the contents of the file will be printed out 
            file.close() #File will be closed
            records(username) #User will be returned back to the records function
        elif(choice4 == 2):
            file = open("add_rent_cars.txt", "r")
            print(file.read())
            file.close()
            records(username)           
        elif(choice4 == 3):
            file = open("cars_rented_out.txt", "r")
            print(file.read())
            file.close()
            records(username)
        elif(choice4 == 4):
            file = open("cars_rented_out.txt", "r")
            print(file.read())
            file.close()
            records(username)
        elif(choice4 == 5):
            admin_menu(username)
        else:
            print("Enter a valid choice")
            continue

        break 

#search record
def search(username):
    while True:
        print("What would you like to do?")
        print("1. Search Customer Booking")
        print("2. Search Customer Payment")
        print("3. Main Menu")
        choice5 = input("Enter choice : ")

        try:
            choice5 = int(choice5)
        except:
            print("Choose a valid choice")

        if(choice5 == 1):
            while True:
                data = input("Enter Customer Name : ")
                i = 0
            
                for file in open("cars_rented_out.txt","r").readlines(): # Read the lines
                    
                    if data in file :
                        carDetails= []
                        for cars in open("cars_rented_out.txt","r").readlines(): # Read the lines
                            cardetail = cars.strip("\n")
                            carDetails.append(cardetail)
                        print(carDetails[i])
                        search(username)
                    i+=1
                else:
                    print("Username not found! Please try again!")
                
    
        elif(choice5 == 2):
            while True:
                data = input("Enter Customer Name : ")
                i = 0
            
                for file in open("cars_rented_out.txt","r").readlines(): # Read the lines
                    
                    if data in file :
                        carDetails= []
                        for cars in open("cars_rented_out.txt","r").readlines(): # Read the lines
                            cardetail = cars.strip("\n")
                            carDetails.append(cardetail)
                        print(carDetails[i])
                        search(username)
                    i+=1
                else:
                    print("Username not found! Please try again!")   
        
        elif(choice5 == 3):
            admin_menu(username)
        else:
            print("Enter a valid choice")
            continue

        break 

#return rented car
def return_rented_car(username):
    while True:
        print("Please enter CarID to return car")
        CarID = input("Enter CarID : ")

        i=0

        for file in open("add_rent_cars.txt" , "r").readlines():
            details = file.strip("\n").split(" ")
            a = details[0]
            b = details[3]
            if a == CarID:
                if b == "NotAvailable":
                    lnum = i
                    
            i+=1
        
        read = open("add_rent_cars.txt", "r")
        new_file_content = ""
        new_line_content = []
        
        for line in read:
            stripped_line = line.strip()
            new_line = stripped_line.replace("NotAvailable", "Available")
            new_file_content += new_line +"\n"

            
        new_line_content = new_file_content.split("\n")

        details = open("add_rent_cars.txt", "r")
        list_of_lines = details.readlines()
        list_of_lines[lnum] = new_line_content[lnum]+"\n"
                

        writing_file = open("add_rent_cars.txt", "w")
        writing_file.writelines(list_of_lines)
        writing_file.close()

        print("Car Returned!")

        admin_menu(username)
                
#login function for registered customers
def registered_customer_login():
    while True:
        print("--Login--")
        username1 = input("Please enter your username : ")
        while len(username1) == 0:
            username1 = input(" Please enter your username : ")

        password = input("Please enter your password : ")
        while len(password) == 0:
            password = input(" Please enter your password : ")
            
        
        userslist = []
        with open ("usernames and password.txt") as textfile:
            for row in textfile:
                row = row.strip ("\n")
                userslist.append(row.split())

        for everything in userslist:       
            UserName = everything[0]
            PassWord = everything[1]

            if username1 == UserName and password == PassWord:
                print("Logged on!")
                registered_customer_menu(username1)
               
#customer registeration as a member
def customer_registration():
    while True:
        while True:
            username  = input("Enter a username : ")
            if not len(username) > 0:
                print("Username cannot be empty!")
                continue
            break
        
        while True:
            password  = input("Enter a password : ")
            if not len(password) > 0:
                print("Password cannot be empty!")
                continue
            break

        while True:
            password1 = input("Confirm password : ")
            if not len(password1) > 0:
                print("Password cannot be empty!")
                continue
            break

        while True:
            phone_num = input("Enter phone number : ")
            if not len(phone_num) > 0:
                print("Phone number cannot be empty")
                continue
            break

        if password == password1:
            username_password = open("usernames and password.txt", "a")
            username_password.write("\n")
            username_password.write(username)
            username_password.write(" ")
            username_password.write(password)
            username_password.write(" ")
            username_password.write(phone_num)
            username_password.close()
            print("Your username is", username, "your password is", password, "and your phone number is", phone_num)
            registered_customer_function()         
        else:
            print("Passwords do NOT match!")
            continue
        break

#unregistered_customer_menu
def unregistered_customer_menu():
    while True:
        print("Welcome!")
        print("What would you like to do?")
        print("1. View cars available for rent")
        print("2. Go back to main menu")
        print("3. Exit")
        input_1 = (input("Enter choice : "))

        try:
            input_1 = int(input_1)
        except:
            print("Choose a valid choice")

        if(input_1 == 1):
            cars_available_unregistered()
            unregistered_customer_menu()
        elif(input_1 == 2):
            main_menu()
        elif input_1 == 3:
            exit()
        else:
            print("Enter a valid choice")
            continue

        break 

# registered customer function 
def registered_customer_function():
    while True:
        print("Do you want to proceed to customer login page?\n1. Registered Customer Login\n2. Unregistered Customer Menu\n3. Exit")
        choice = input("Enter choice : ")

        try:
            choice = int(choice)
        except:
            print("Please choose a valid choice")

        if choice == 1:
            registered_customer_login()
        elif choice == 2:
            unregistered_customer_menu()
        elif choice == 3:
            exit()
        else:
            print("Enter a valid choice")
            continue
        break

#registered_customer_menu:
def registered_customer_menu(username1):
    while True:
        print("Welcome!")
        print("What would you like to do?")
        print("1. View cars available for rent")
        print("2. Modify personal details")
        print("3. Personal rental history")
        print("4. View details of car to be rented out")
        print("5. Select and book car for a specific duration")
        print("6. Exit")
        input_2 = (input("Enter choice : "))

        try:
            input_2 = int(input_2)
        except:
            print("Choose a valid choice")

        if(input_2 == 1):
            cars_available(username1)
        elif(input_2 == 2):
            modify_personal_details_menu(username1)            
        elif(input_2 == 3):
            rental_history_menu(username1)
        elif(input_2 == 4):
            details_cars_to_be_rented(username1)
        elif(input_2 == 5):
            book_car(username1)
        elif(input_2 == 6):
            print("Thank you for using our booking system!")
            exit()
        else:
            print("Enter a valid choice")
            continue

        break     

# view cars available for rent (unregistred customer)
def cars_available_unregistered():
    cars_available = open("add_rent_cars.txt", "r")
    print(cars_available.read())
    cars_available.close()

    unregistered_customer_menu()

# view cars available for rent (registred customer)
def cars_available(username1):
    cars_available = open("add_rent_cars.txt", "r")
    print(cars_available.read())
    cars_available.close()
    
    registered_customer_menu(username1)

# #modify personal details
def modify_personal_details(username1):
    while True:
        search = input("Enter username : ")
        
        i=0
        
        for file in open("usernames and password.txt","r").readlines(): # Read the lines
            
            if search in file :
                carDetails= []
                for cars in open("usernames and password.txt","r").readlines(): # Read the lines
                    cardetail = cars.strip("\n")
                    carDetails.append(cardetail)
                print(carDetails[i])
                print("1. Username\n2. Password\n3. Phone number")

                choice = input("Enter choice : ")
            
                try:
                    choice = int(choice)
                except:
                    print("Choose a valid choice")

                if choice == 1:
                    print(carDetails[i])
                    car = input("Enter old username : ")
                    car1 = input("Enter new username : ")
            
                    for line in open("usernames and password.txt","r").readlines(): # Read the lines
                        cars = line.split(" ") # Split on the space, and store the results in a list of two strings
                        oldcarid = cars[0]
                        
                        if car == oldcarid:

                            read = open("usernames and password.txt", "r")
                            new_file_content = ""
                            new_line_content = []
                            for line in read:
                                stripped_line = line.strip()
                                new_line = stripped_line.replace(car, car1)
                                new_file_content += new_line +"\n"

                            lnum = i
                            new_line_content = new_file_content.split("\n")

                            details = open("usernames and password.txt", "r")
                            list_of_lines = details.readlines()
                            list_of_lines[lnum] = new_line_content[lnum]+"\n"
                                

                            writing_file = open("usernames and password.txt", "w")
                            writing_file.writelines(list_of_lines)
                            writing_file.close()
                            
                            for line in open("cars_rented_out.txt","r").readlines(): # Read the lines
                                cars = line.strip("\n").split(" ") # Split on the space, and store the results in a list of two strings
                                if car == cars[0]:
                                                            
                                    read = open("cars_rented_out.txt", "r")
                                    new_file_content = ""
                                    for line in read:
                                        stripped_line = line.strip()
                                        new_line = stripped_line.replace(car, car1)
                                        new_file_content += new_line +"\n"
                                

                                    writing_file = open("cars_rented_out.txt", "w")
                                    writing_file.write(new_file_content)
                                    writing_file.close()
                    
                    modify_personal_details_menu(username1)
                
                elif choice == 2:
                    print(carDetails[i])
                    car = input("Enter old password : ")
                    car1 = input("Enter new password : ")
            
                    for line in open("usernames and password.txt","r").readlines(): # Read the lines
                        cars = line.split(" ") # Split on the space, and store the results in a list of two strings
                        oldcarid = cars[1]
                        
                        if car == oldcarid:

                            read = open("usernames and password.txt", "r")
                            new_file_content = ""
                            new_line_content = []
                            for line in read:
                                stripped_line = line.strip()
                                new_line = stripped_line.replace(car, car1)
                                new_file_content += new_line +"\n"

                            lnum = i
                            new_line_content = new_file_content.split("\n")

                            details = open("usernames and password.txt", "r")
                            list_of_lines = details.readlines()
                            list_of_lines[lnum] = new_line_content[lnum]+"\n"
                                

                            writing_file = open("usernames and password.txt", "w")
                            writing_file.writelines(list_of_lines)
                            writing_file.close()
                            
                            
                    
                    modify_personal_details_menu(username1)
                
                elif choice == 3:
                    print(carDetails[i])
                    car = input("Enter old phone number : ")
                    car1 = input("Enter new phone number : ")
            
                    for line in open("usernames and password.txt","r").readlines(): # Read the lines
                        cars = line.strip("\n").split(" ") # Split on the space, and store the results in a list of two strings
                        oldcarid = cars[2]
                        
                        if car == oldcarid:

                            read = open("usernames and password.txt", "r")
                            new_file_content = ""
                            new_line_content = []
                            for line in read:
                                stripped_line = line.strip()
                                new_line = stripped_line.replace(car, car1)
                                new_file_content += new_line +"\n"

                            lnum = i
                            new_line_content = new_file_content.split("\n")

                            details = open("usernames and password.txt", "r")
                            list_of_lines = details.readlines()
                            list_of_lines[lnum] = new_line_content[lnum]+"\n"
                                

                            writing_file = open("usernames and password.txt", "w")
                            writing_file.writelines(list_of_lines)
                            writing_file.close()                           
                            
                    modify_personal_details_menu(username1)
                
                else:
                    print("Enter a valid choice")
                    continue
            i+=1
        
        else:
            print("Username not found!")

#modify personal details menu
def modify_personal_details_menu(username1):
    while True:
        print("What would you like to do?\n1. Modify Personal Details\n2. Main menu")
        choice = input("Enter choice : ")

        try:
            choice = int(choice)
        except:
            print("Enter a valid choice")
            continue

        if choice == 1:
            modify_personal_details(username1)
        elif choice == 2:
            registered_customer_menu(username1)
        else:
            print("Choose a valid choice")

#personal rental history
def rental_history(username1):
    while True:
        choice = input("Enter username : ")

        i = 0
        
        for file in open("cars_rented_out.txt","r").readlines(): # Read the lines
                
                if choice in file :
                    carDetails= []
                    for cars in open("cars_rented_out.txt","r").readlines(): # Read the lines
                        cardetail = cars.strip("\n")
                        carDetails.append(cardetail)
                    print(carDetails[i])
                    rental_history_menu(username1)
                i+=1
        else:
            print("Username not found! Please Try again!")
                
#rental history menu
def rental_history_menu(username1):
    while True:
        print("What would you like to do?\n1. View Personal Rental History\n2. Main menu")
        choice = input("Enter choice : ")

        try:
            choice = int(choice)
        except:
            print("Enter a valid choice")
            continue

        if choice == 1:
            rental_history(username1)
        elif choice == 2:
            registered_customer_menu(username1)
        else:
            print("Choose a valid choice")

#details of cars to be rented out
def details_cars_to_be_rented(username1):
    print("These are the cars that have been rented out")
    file = open("cars_rented_out.txt", "r")
    print(file.read())
    file.close()

    registered_customer_menu(username1)

#payment
def payment(username1):
    while True:
        while True:
            name  = input("Enter a card name : ")
            if not len(name) > 0:
                print("Card name cannot be empty!")
                continue
            break
        
        while True:
            pin  = input("Enter pin : ")
            if not len(pin) > 0:
                print("Pin cannot be empty!")
                continue
            break

        while True:
            pin1  = input("Enter pin again for conformation : ")
            if not len(pin1) > 0:
                print("Pin cannot be empty!")
                continue
            break

        if pin == pin1:
            print("Payment success! You have booked your car!")
            registered_customer_menu(username1)

#select and book car for specific duration
def book_car(username1):
    while True:
        print("These are the cars that the shop currently has")
        
        for file in open("add_rent_cars.txt","r").readlines(): # Read the lines
            print(file.rstrip())

        choice = input("Enter car name to book : ")

        i = 0
        for file in open("add_rent_cars.txt","r").readlines(): # Read the lines
                
                if choice in file :
                    carDetails= []
                    for cars in open("add_rent_cars.txt","r").readlines(): # Read the lines
                        cardetail = cars.strip("\n")
                        carDetails.append(cardetail)
                    print(carDetails[i])

                    hour = input("Enter how many hours you would like to book : ")
                    
                    print("1. Proceed to payment?\n2. Cancel existing booking")
                    choice1 = input("Enter choice : ")
                    
                    try:
                        choice1 = int(choice1)
                    except:
                        print("Enter a valid choice")

                    if choice1 == 1:
                            
                        file = open("cars_rented_out.txt","a")
                        file.write("\n")
                        file.write(username1)
                        file.write(" ")
                        file.write(carDetails[i])
                        file.write(" ")
                        file.write(hour)
                        file.close()
                        
                        payment(username1)

                        

                    elif choice1 == 2:
                        registered_customer_menu(username1)

                    else:
                        print("Enter a valid choice")
                        continue
                i+=1        
        else:
            print("Invalid Car Name")

#Main menu for the interface
def main_menu():
    print("Welcome to Online Car Rental Service!")
    print("Are you a registered customer?")
    choice2 = input("Yes or No : " )

    if (choice2 == "No"):
        print("Do you want to create an account?")
        option = input("Yes or No : ")

        if (option == "Yes"):
            customer_registration()
        elif (option == "No"):
            unregistered_customer_menu()
        else:
            main_menu()
            
    if (choice2 == "Yes"):
        registered_customer_login()

#master menu
def main():
    num_list = [1, 2, 3]
    while True: #While loop is used as a infinite loop, it will break out from the loop if the conditions are met
        print("Welcome to Super Car Rental Services!\nSelect a choice to continue")
        print("1. Admin")
        print("2. Customer")
        print("3. Exit")
        choice = input("Enter here : ")

        try: #try and except is used because of data validation
            choice = int(choice) #Choice variable converted from string to integer
        except:
            print("Choose a valid choice") #If user were to enter alphabets, it will print out this sentence

        if choice == num_list [0]: #If the user were to enter 1, the index 0 in the list which is 1, it will break out from the loop and bring the user to the next function
            admin_login()
        elif choice == num_list [1]:
            main_menu()
        elif choice == num_list [2]:
            print("Thank you!")
            exit()  
        else:
            print("Enter a valid choice") #If the user entered a number that is not in the list, it will print out this sentence
            continue
    
        break  

main()