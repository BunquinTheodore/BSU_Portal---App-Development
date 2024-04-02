#BSU Portal 

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
                sign_in()
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

def sign_in():
    pass


main()