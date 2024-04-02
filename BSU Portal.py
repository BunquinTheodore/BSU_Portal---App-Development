#Batangas State University Portal 

student_account = {}

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
            sub_portal()
        else: 
            print ("wrong password!")
    else:
        print ("Student Account not Found!")
        return
            
            
def sub_portal():
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

def subjects():
    pass

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

def course_registration():
    pass

main()