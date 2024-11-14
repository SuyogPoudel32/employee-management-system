import datetime

def database_value():
    lst = []
    file = open("file.txt")
    for i in file:
        split_val = i.split()
        lst.append(split_val)
    file.close()
    return lst

def show_val():
    value = database_value()
    print(value)
    for i in value:
        print(f"ID: {i[1]} NAME: {i[3]} {i[4]} EMAIL: {i[6]} PHONE: {i[8]}, AGE: {i[10]}")
        print("\n")

def finding():
    value = database_value()
    try:
        id_no = int(input("ENTER YOUR ID NUMBER TO FIND: "))
        for i in value:
            id_val = i[1]
            if int(id_val) == id_no:
                print(f"ID: {i[1]} NAME: {i[3]} {i[4]} EMAIL: {i[6]} PHONE: {i[8]}, AGE: {i[10]}")
    except ValueError:
        print("VALUE ERROR!!")
        finding()

## Adding Data Function
def adding_data():
    try:
        iterate = int(input("ENTER HOW MANY DATA YOU WANT TO ADD? "))
    except ValueError:
        print("VALUE ERROR!!")
        adding_data()

    def adding_id():
        value = database_value()
        for i in range(iterate):
            try:
                id_value = int(input("ENTER ID VALUE: "))
                id_exists = False
                for j in value:
                    if len(j) > 1:
                        check_id = int(j[1])
                        if check_id == id_value:
                            print(f"THIS {id_value} ID ALREADY EXISTS!!")
                            adding_id()
                            id_exists = True

                if not id_exists:
                    # file1= open("file.txt", "a")
                    # file1.write("\n")
                    file = open("file.txt", "a")
                    file.write(f"ID: {id_value} ")
                    file.close()
                    print(f"ID {id_value} ADDED SUCCESSFULLY.")


                    def adding_name():
                        try:
                            name_val = str(input(f"ENTER NAME OF {id_value} ID: "))
                            file = open("file.txt", "a")
                            file.write(f"Name: {name_val} ")
                            file.close()
                            print(f"NAME {name_val} ADDED SUCCESSFULLY.")
                        except ValueError:
                            print("VALUE ERROR!!")
                            adding_name()

                    def adding_email():
                        try:
                            email_val = str(input(f"ENTER EMAIL OF {id_value} ID: "))
                            if "@" in email_val and "gmail.com" in email_val:
                                file = open("file.txt", "a")
                                file.write(f"Email: {email_val} ")
                                file.close()
                                print(f"EMAIL {email_val} ADDED SUCCESSFULLY.")
                            else:
                                print("YOUR EMAIL IS INVALID!!")
                                adding_email()
                        except ValueError:
                            print(f"VALUE ERROR {email_val}")
                            adding_email()

                    def adding_phone():
                        try:
                            phone_val = int(input(f"ENTER PHONE NUMBER OF {id_value} ID: "))
                            int_phone_val = str(phone_val)
                            if len(int_phone_val) != 10:
                                print(f"YOUR PHONE NUMBER IS INCORRECT. LENGTH IS {len(int_phone_val)}")
                                adding_phone()
                            else:
                                file = open("file.txt", "a")
                                file.write(f"Phone: {phone_val} ")
                                file.close()
                                print(f"PHONE {phone_val} ADDED SUCCESSFULLY.")
                        except ValueError:
                            print("VALUE ERROR!!")
                            adding_phone()
                    def adding_age():
                        try:
                            age_val = int(input(f"AGE OF ID {id_value} "))
                            file = open("file.txt", "a")
                            file.write(f"Age: {age_val}\n")
                            file.close()
                        except ValueError:
                            print("VALUE ERROR!!")
                            adding_age()



                    
                    adding_name()
                    adding_email() 
                    adding_phone()
                    adding_age()  

            except ValueError:
                print("VALUE ERROR!!")
                adding_id()

    adding_id()

def delete():
    value = database_value()
    for i in value:
        try:
            if i[2] == "" or i[6] =="" or i[7] == "" or i[9]==" ":
                print(" ")
        except IndexError:
            values = i[1]
            file = open("file.txt", "r")
            reading = file.readlines()
            file.close()
            file = open("file.txt", "w")
            for j in reading:
                if not j.startswith(f"ID: {values}"):    ##IDK HOWS THIS CODE WORKS 😂
                    file.write(j)
            file.close()
            print(f"Deleted all rows with ID: {i} BECAUSE IT IS INCOMPLETE" )  

delete()

def delete_data1(): ###DELETE DATA WHICH USER WANTS!!!!
    show_val()
    delete_val = int(input("WHICH ID DATA YOU WANT TO DELETE?"))
    file = open("file.txt", "r")
    reading = file.readlines()
    file.close()
    file = open("file.txt","w")
    list_new =[]
    for i in reading:
        i_val = i[4:6]
        if str(delete_val)== i_val:
            continue
        else:
            list_new.append(i)
            file.write(i)
    file.close()
while True:
    try:
        op = int(input("ENTER VALUE (1 for show, 2 for find, 3 for add): "))
        if op == 1:
            show_val()
        elif op == 2:
            finding()
        elif op == 3:
            adding_data()
        elif op ==4:
            delete_data1()
    except ValueError:
        print("VALUE ERROR tkgjgg!")
        continue

