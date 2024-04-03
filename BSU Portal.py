#Batangas State University Portal 

student_account = {}
coe_subjects = []
cics_subjects = []
cafad_subjects = []
cit_subjects = []

def main():
    while True: 
        print ("Welcome to Batangas State University Portal!\n")
        print ("1. Sign-Up  Student Account")
        print ("2. Sign-In Student Account")
        print ("3. Exit Portal")
        choice = int(input("Enter choice of action: "))
        try:
            if choice == 1:
                sr_code = input("Enter SR Code: ")
                password = input ("Enter password: ")
                sign_up(sr_code,password)
            elif choice == 2:
                sr_code = input ("Enter SR Code: ")
                password = input ("Enter password: ")
                sign_in(sr_code, password)
            elif choice == 3:
                print ("Exiting Portal...")
                break
            else:
                print ("Invalid Input!")
        except ValueError as e:
            print (f"Error occured: {e}")

def sign_up(sr_code, password):
    if sr_code in student_account:
        print("SR Code already in use!")
    else:
        student_account[sr_code] = {"password": password}
        print ('Account Registered Successfully!')

def sign_in(sr_code, password):
    if sr_code in student_account:
        if password == student_account[sr_code]["password"]:
            year_level()
        else: 
            print ("wrong password!")
    else:
        print ("Student Account not Found!")
        return
            
def year_level():
    while True:
        print ('1. 1st year')
        print ('2. 2nd Year')
        print ('3. 3rd Year')
        print ('4. 4th Year')
        choice = int(input('Enter Year Level: '))
        if choice == 1:
            school_department()
            break
        elif choice == 2:
            school_department()
            break
        elif choice == 3:
            school_department()
            break
        elif choice == 4:
            school_department()
            break
        else: 
            print ("Invalid Input!")
            break
        

def school_department():
    while True:
        print ("1. College of Informatics and Computing Sciences")
        print ("2. College of Engineering")
        print ("3. College of Information Technology")
        print ("4. College of Architecture, Fine Arts and Design")
        choice = int(input("Enter College Department: "))
        if choice == 1:
            sub_portal(choice)
            break
        elif choice == 2:
            sub_portal(choice)
            break
        elif choice == 3:
            sub_portal(choice)
            break
        elif choice == 4:
            sub_portal(choice)
            break
        else:
            print ("Invalid Input!")
            break
            
def sub_portal(choice):
    while True:
        print ("1. View Subjects")
        print ("2. View ID")
        print ("3. Schedules")
        print ("4. Liabilities")
        print ("5. Membership Payments")
        print ("6. Curriculum")
        print ("7. Scholarships")
        print ("8. Online Registration")
        print ("9. Certificate of Registration")
        choice = int(input("Enter choice: "))
        try:
            if choice == 1:
                view_subjects(choice)
            elif choice == 2:
                view_ID()
            elif choice == 3:
                schedules()
            elif choice == 4:
                liabilities()
            elif choice == 5:
                membership_payments()
            elif choice == 6:
                curriculum()
            elif choice == 7:
                scholarships()
            elif choice == 8:
                online_registration()
            elif choice == 9:
                certificate_of_registration()
            else:
                print ("Invalid Input")
        except ValueError as e:
            print (f"Error occured: {e}")

def view_subjects(choice):
    if choice == 1:
        for subjects in cics_subjects:
            print (subjects)
    elif choice == 2:
        for subjects in coe_subjects:
            print (subjects)
    elif choice == 3:
        for subjects in cit_subjects:
            print (subjects)
    elif choice == 4:
        for subjects in cafad_subjects:
            print (subjects)
    else: 
        print ("Invalid Input!")

def curriculum():
    pass

def liabilities():
    pass

def schedules():
    pass

def membership_payments():
    pass

def view_ID():
    pass

def certificate_of_registration():
    pass

def scholarships():
    pass

def online_registration():
    pass

main()