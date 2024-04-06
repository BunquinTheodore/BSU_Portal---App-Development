#Batangas State University Portal 
#Good day sir, this is my simplified BSU portal I made using python

#I placed an empty dictionary to store the student's SR Code, name and password
student_account = {}

#This is my data base for membership payments and basis for the student's liability
memberships = {
    "SSC Membership" : {"cost" : 45},
    "Department Membership" : {"cost" : 60},
    "Organization Membership" : {"cost" : 80}
}

#I also placed for 4 different curriculum for each department
#I generalized the subjects for all courses within the departments due to the complexity of code if I asked the student's program

#This is the data base for the Department of College of Engineering 
engineering_urriculum = { 
    "First Year": [
        "Introduction to Engineering",
        "Mathematics for Engineers",
        "Physics for Engineers",
        "Engineering Drawing",
        "Introduction to Computer Programming",
        "English Composition",
        "General Chemistry",
        "Engineering Mechanics",
        "Engineering Materials"
    ],
    "Second Year": [
        "Engineering Mathematics",
        "Electrical Circuits",
        "Thermodynamics",
        "Engineering Economics",
        "Engineering Graphics",
        "Computer-Aided Design",
        "Statics and Dynamics",
        "Engineering Communication",
        "Fluid Mechanics"
    ],
    "Third Year": [
        "Mechanics of Materials",
        "Electrical Machines",
        "Control Systems",
        "Environmental Engineering",
        "Heat Transfer",
        "Engineering Electives",
        "Engineering Ethics and Professionalism",
        "Engineering Design and Analysis",
        "Engineering Internship"
    ],
    "Fourth Year": [
        "Engineering Management",
        "Renewable Energy Systems",
        "Industrial Engineering",
        "Engineering Project Management",
        "Engineering Seminar",
        "Capstone Design Project",
        "Engineering Electives",
        "Engineering Law and Regulations"
    ]
}

#This one is for the Department of College  of Informatics and Computing Sciences
informatics_computing_sciences_curriculum = {
    "First Year": [
        "Introduction to Computer Science",
        "Programming Fundamentals",
        "IT Fundamentals",
        "Discrete Mathematics",
        "Computer Networks Basics",
        "Introduction to Information Systems",
        "Data Structures and Algorithms",
        "Database Management Systems",
        "Web Development Basics",
        "Computing Mathematics",
        "Operating Systems Fundamentals",
        "Software Engineering Principles"
    ],
    "Second Year": [
        "Advanced Programming Concepts",
        "Computer Architecture",
        "Systems Analysis and Design",
        "Cybersecurity Fundamentals",
        "Object-Oriented Programming",
        "IT Project Management",
        "Algorithms and Complexity",
        "Network Security",
        "Database Design and Implementation",
        "Web Development Intermediate",
        "Human-Computer Interaction",
        "IT Infrastructure Management"
    ],
    "Third Year": [
        "Artificial Intelligence Fundamentals",
        "Cloud Computing",
        "Software Development Lifecycle",
        "Mobile Application Development",
        "Data Mining and Analytics",
        "IT Governance and Compliance",
        "Machine Learning",
        "Distributed Systems",
        "Advanced Database Management",
        "Web Development Advanced",
        "Information Security Management",
        "Emerging Technologies in IT"
    ],
    "Fourth Year": [
        "Capstone Project/Thesis Part I",
        "Professional Ethics in Computing",
        "Enterprise Systems Integration",
        "IT Innovation and Entrepreneurship",
        "Network Administration and Maintenance",
        "Software Testing and Quality Assurance",
        "Capstone Project/Thesis Part II",
        "IT Law and Regulations",
        "Big Data Technologies",
        "IT Strategic Planning",
        "Internship/Practical Training",
        "Career Development and Industry Trends"
    ]
}

#This is the database for the department of College of Architecture, Fine Arts and Design
architecture_fine_arts_design_curriculum = {
    "First Year": [
        "Introduction to Architecture",
        "Architectural Design Basics",
        "Architectural History",
        "Drawing Fundamentals",
        "Design Principles",
        "Introduction to Fine Arts",
        "Art History",
        "Architectural Technology",
        "Basic Photography"
    ],
    "Second Year": [
        "Architectural Design Studio I",
        "Building Construction",
        "Environmental Design",
        "Digital Design Tools",
        "Structural Systems",
        "Fine Arts Workshop",
        "Urban Design",
        "Building Materials",
        "Architectural Drawing"
    ],
    "Third Year": [
        "Architectural Design Studio II",
        "Interior Design",
        "Landscape Architecture",
        "Advanced Digital Design",
        "Sustainable Architecture",
        "Fine Arts Studio",
        "Architectural Theory",
        "Professional Practice",
        "Cultural Heritage Preservation"
    ],
    "Fourth Year": [
        "Architectural Design Studio III",
        "Advanced Architectural Technology",
        "Urban Planning",
        "Design Management",
        "Portfolio Development",
        "Fine Arts Exhibition",
        "Architectural Research",
        "Internship",
        "Thesis Project"
    ]
}

#This one is for the Department of Industrial Technology
industrial_technology_curriculum = {
    "First Year": [
        "Introduction to Industrial Technology",
        "Basic Electronics",
        "Engineering Drawing",
        "Technical Mathematics",
        "Workshop Practices",
        "Computer-Aided Design (CAD)",
        "Introduction to Manufacturing Processes",
        "Technical Communication",
        "Safety and Health in Industry"
    ],
    "Second Year": [
        "Industrial Automation",
        "Materials Science",
        "Machine Design",
        "Electrical Machines",
        "Fluid Mechanics",
        "Quality Control",
        "Technical Writing",
        "Industrial Management",
        "Internship Preparation"
    ],
    "Third Year": [
        "Advanced Manufacturing Technologies",
        "Robotics and Automation",
        "Industrial Instrumentation",
        "Supply Chain Management",
        "Product Design and Development",
        "Energy Management",
        "Industrial Safety Engineering",
        "Technical Presentations",
        "Industrial Training"
    ],
    "Fourth Year": [
        "Industrial Project Management",
        "Environmental Management",
        "Lean Manufacturing",
        "Human Factors in Industry",
        "Professional Ethics in Technology",
        "Industrial Internship",
        "Capstone Project",
        "Industry Seminar",
        "Career Development Workshop"
    ]}

#This one is my main function containing register, log-in and exit options
def main():
    while True: 
        print ("\nWelcome to Batangas State University Portal!")
        print ("1. Register Student Account")
        print ("2. Log-In Student Account")
        print ("3. Exit Portal")
        try:
            choice = int(input("Enter choice of action(1-3): "))
            if choice == 1:
                sr_code = (input("Enter SR Code: "))
                name = (input("Enter Name: "))
                password = input("Enter password: ")
                register_account(name, sr_code, password)
            elif choice == 2:
                sr_code = (input("Enter SR Code: "))
                name =(input("Enter Name: "))
                password = input ("Enter password: ")
                log_in_account(name, sr_code, password)
            elif choice == 3:
                print ("Exiting Portal...\n")
                break
            else:
                print ("Invalid Input!")
        except ValueError as e:
            print (f"Error occured: {e}")
            main()

#This is my function for registering their student account
#It checks if SR Code is in the student account dictionary, if not, assigns the input into the dictionary
def register_account(name, sr_code, password):
    if sr_code in student_account:
        print ("\nSR Code already in use!")
    else:
        student_account[sr_code] = {"password": password, "name" : name, "balance": 0}
        print ('\nAccount Registered Successfully!')

#This is my log-in function
#It checks if the SR Code is in the student account dictionary where:
#It requires the correct name and password to access the student account
#After successfully logging in, it goes to the school department function
def log_in_account(name, sr_code, password):
    if sr_code in student_account:
        if name == student_account[sr_code]["name"]:
            if password == student_account[sr_code]["password"]:
                school_department(name, sr_code, password)
            else: 
                print("\nWrong Password! Try Again")
        elif name != student_account [sr_code]["name"]:
            print (f"\nIncorrect name: {name}!")
            return
    else:
        print (f"\n'{sr_code}' Account not Found!")
        return

#This is my school department function
#It lets the student pick their designated College Department
#It also assigns their curriculum based on the department they input and then goes to the year level function
def school_department(name, sr_code, password):
    while True:
        print (f"\nWelcome {name}, Choose your Designated Department!")
        print ("1. College of Informatics and Computing Sciences")
        print ("2. College of Engineering")
        print ("3. College of Industrial Technology")
        print ("4. College of Architecture, Fine Arts and Design")
        while True:
            try:
                choice = int(input("Enter choice(1-4): "))
                if choice == 1:
                    department_curriculum = informatics_computing_sciences_curriculum
                    department = "College of Informatics and Computing Sciences"
                    year_level(name, sr_code, department_curriculum, department, password)
                elif choice == 2:
                    department_curriculum = engineering_urriculum
                    department = "College of Engineering"
                    year_level(name, sr_code, department_curriculum, department, password)
                elif choice == 3:
                    department_curriculum = industrial_technology_curriculum
                    department = "College of Industrial Technology"
                    year_level(name, sr_code, department_curriculum, department, password)
                elif choice == 4:
                    department_curriculum = architecture_fine_arts_design_curriculum
                    department = "College of Architecture, Fine Arts and Design"
                    year_level(name, sr_code, department_curriculum, department, password)
                else:
                    print ("\nInvalid Input!")
            except ValueError as e:
                print (f"Error Occured: {e}")
                school_department(name, sr_code, password)

#This is my year level function
#It ask for the year level of students and assigns it to their corresponding department
#It then goes to the the Sub Portal after
def year_level(name, sr_code, department_curriculum, department, password):
    while True:
        print (f"\nWelcome {name}, Choose your Year Level")
        print ('1. 1st year')
        print ('2. 2nd Year')
        print ('3. 3rd Year')
        print ('4. 4th Year')
        try: 
            choice = int(input('Enter Year Level(1-4): '))
            if choice == 1:
                student_year_level = "First Year Student"
                curriculum_of_student_year_level = department_curriculum['First Year']
                sub_portal(name, sr_code, curriculum_of_student_year_level, student_year_level, department_curriculum, department, password)
            elif choice == 2:
                student_year_level = "Second Year Student"
                curriculum_of_student_year_level = department_curriculum['Second Year']
                sub_portal(name, sr_code, curriculum_of_student_year_level, student_year_level, department_curriculum, department, password)
            elif choice == 3:
                student_year_level = "Third Year Student"
                curriculum_of_student_year_level = department_curriculum['Third Year']
                sub_portal(name, sr_code, curriculum_of_student_year_level, student_year_level,department_curriculum, department, password)
            elif choice == 4:
                student_year_level = "Fourth Year Student"
                curriculum_of_student_year_level = department_curriculum['Fourth Year']
                sub_portal(name, sr_code, curriculum_of_student_year_level, student_year_level,department_curriculum, department,password)
            else: 
                print ("\nInvalid Input!")
                year_level(name, sr_code, department_curriculum, department, password)
        except ValueError as e: 
            print (f"Error Occured: {e}")
            year_level(name, sr_code, department_curriculum, department, password)

#This is my Sub Portal function containing different actions similar to the BSU portal
def sub_portal(name, sr_code, curriculum_of_student_year_level, student_year_level, department_curriculum, department, password):
    while True:
        print ("________________________________________________________________________________________")
        print (f'Welcome {name} to the Portal!')
        print ("1. View ID")
        print ("2. View Subjects")
        print ("3. View Grades")
        print ("4. Schedules")
        print ("5. Curriculum")
        print ("6. Liabilities")
        print ("7. Scholarships")
        print ("8. Certificate of Registration")
        print ("9. Membership Payments")
        print ("10. Add Balance")
        print ("11. Online Registration")
        print ("12. Change Password")
        print ("13. Exit")
        try:
            choice = int(input("Enter choice(1-13): "))
            if choice == 1:
                view_ID(name, sr_code, department, student_year_level)
            elif choice == 2:
                view_subjects(curriculum_of_student_year_level)
            elif choice == 3:
                view_grades(curriculum_of_student_year_level)
            elif choice == 4:
                schedules()
            elif choice == 5:
                curriculum(department_curriculum)
            elif choice == 6:
                liabilities()
            elif choice == 7:
                scholarships()
            elif choice == 8:
                certificate_of_registration(name, sr_code, department, curriculum_of_student_year_level, student_year_level)
            elif choice == 9:
                membership_payments(name, sr_code, curriculum_of_student_year_level, student_year_level, department_curriculum, department, password)
            elif choice == 10:
                add_balance(sr_code)
            elif choice == 11:
                online_registration(curriculum_of_student_year_level)
            elif choice == 12:
                sr_code = input("Enter SR Code: ")
                password = input("Enter original password: ")
                new_password = input("Enter new password: ")
                change_password(sr_code, password, new_password)
            elif choice == 13:
                main()
            else:
                print ("\nInvalid Input!")
        except ValueError as e:
            print (f"Error occured: {e}")
            sub_portal(name, sr_code, curriculum_of_student_year_level, student_year_level, department_curriculum, department, password)

#This is my View Subject function where it let the student view their subjects for their current school year level
def view_subjects(curriculum_of_student_year_level):
    print ("________________________________________________________________________________________")
    print ("\nYour Subjects: ")
    for subjects in curriculum_of_student_year_level:
        print (f"- {subjects}")

#Meanwhile, this is my curriculum function where it let the students view all thier subjects for the entire program
def curriculum(department_curriculum):
    print ("________________________________________________________________________________________")
    print ("\nYour Entire Curriculum: ")
    for year_level, subjects in department_curriculum.items():
        print (f"\n{year_level}:")
        for subject in subjects: 
            print (f"- {subject}")

#This is my Add Balance function, utilized for paying their membership payments
def add_balance(sr_code):
    print ("________________________________________________________________________________________")
    print ("Cash In to Add Balance")
    cash_in = int(input("Enter amount you want to cash in: "))
    student_account[sr_code]["balance"] += cash_in
    print ("Succesfully Added Balance!")
    return

#This is my Membership Payment function, it let the student choose which membership to pay
#This uses the membership dictionary as database for the payments
def membership_payments(name, sr_code, curriculum_of_student_year_level, student_year_level, department_curriculum, department, password):
    while True:
        print ("________________________________________________________________________________________")
        print ("Choose which Membership to Pay")
        print ("1. SSC Membership: Php 45")
        print ("2. Department Membership: Php 60")
        print ("3. Organization Membership: Php 80")
        print ("4. Exit")
        try:
            choice = int(input("Enter choice(1-3): "))
            if choice == 1: 
                membership = "SSC Membership"
                processing_payments(sr_code, membership)
            elif choice == 2:
                membership = "Department Membership"
                processing_payments(sr_code, membership)
            elif choice == 3:
                membership = "Organization Membership"
                processing_payments(sr_code, membership)
            elif choice == 4:
                sub_portal(name, sr_code, curriculum_of_student_year_level, student_year_level, department_curriculum, department, password)
                break
            else:
                print ("\nInvalid Input!")
                membership_payments(name, sr_code, curriculum_of_student_year_level, student_year_level, department_curriculum, department, password)
        except ValueError as e:
            print (f"Error Occured: {e}")
            membership_payments(name, sr_code, curriculum_of_student_year_level, student_year_level, department_curriculum, department, password)

#This is my Processing Payment Function that gets what membership the student is paying for to make it more scalable and flexible
#It checks if the membership is already paid, if not; if process the payment of student. If the balance is insufficient, it prints that the balance is insufficient            
def processing_payments(sr_code, membership):
    membership_type = memberships[membership]
    if membership_type["cost"] == 0:
        print (f"You have already paid {membership}!")
    elif student_account[sr_code]["balance"] >= membership_type["cost"]:
        student_account[sr_code]["balance"] -= membership_type["cost"]
        membership_type['cost'] = 0
        print (f"\nSuccessfully paid {membership}!")
    else:
        print (f"Insufficient Cash Balance\n Balance: {student_account[sr_code]['balance']} ")
       
            
#This is my Liability function which is based on the membership_payments function and processing payment functions
def liabilities():
    print ("________________________________________________________________________________________")
    print ("LIABILITIES")
    while True: 
        no_liabilities = 3
        liabilities = []
        if memberships["SSC Membership"]["cost"] == 0:
            no_liabilities -= 1
        elif memberships["SSC Membership"] != 0:
            liabilities.append("SSC Memberships")
        if memberships["Department Membership"]["cost"] == 0:
            no_liabilities -= 1
        elif memberships["Department Membership"] != 0:
            liabilities.append("Department Memberships")
        if memberships ["Organization Membership"]["cost"] == 0:
            no_liabilities -= 1
        elif memberships["Organization Membership"] != 0:
            liabilities.append("Organization Memberships")
        print (f"You have {no_liabilities} liability(s)")
        print ("You liabiltiy(s):")
        if no_liabilities != 0:
            for liability in liabilities:
                print (f"- {liability}")
        elif no_liabilities == 0:
            print ("- None")
        return

#This is my Schedule function where I simplified it due to the complexity of the code, it simply prints an unavailble schedule
def schedules():
    print ("________________________________________________________________________________________")
    print ("Schedules: ")
    print ("Schedules not available yet...")


#This is my View ID function, letting the students view their name, SR code, department and student year level
def view_ID(name, sr_code, department, student_year_level):
    print ("________________________________________________________________________________________")
    print ('''
           ___________________
           |                 |
           |                 |
           |     Photo       |
           |   Unavailable   |
           |                 |
           |_________________|''')
    print (f"{name}\n{sr_code}\n{department}\n{student_year_level}")

#This is my Certificate of Registration Function that shows the student's detail and curriculum and also states that they are enroll
def certificate_of_registration(name, sr_code, department, curriculum_of_student_year_level, student_year_level):
    print ("______________________________")
    print ("\nCERTIFICATE OF REGISTRATION")
    print (f"SR Code: {sr_code}")
    print (f"Name: {name}")
    print (f"Year Level: {student_year_level}")
    print (f"Department: {department}")
    view_subjects(curriculum_of_student_year_level)
    scholarships()
    print ("ENROLLED")

#This is my Scholarship function which is similar to the portal, it simply prints the 100% Scholarship
def scholarships():
    print ("________________________________________________________________________________________")
    print ("\nScholarships: ")
    print ("Higher Education Support Program: \nTuition Fee Discount: 100% \nMisc Fee Discount: 100%")

#Meanwhile, this is the Online Registration function, it let the students enroll on their subjects if and only if their liability is zero
def online_registration(curriculum_of_student_year_level):
    print ("________________________________________________________________________________________")
    print ("ONLINE REGISTRATION")
    if memberships["Department Membership"] != 0 and memberships["Organization Membership"] != 0 and memberships["SSC Membership"] != 0:
        print ("Liabilities found, unable for online registration!")
    else: 
        view_subjects(curriculum_of_student_year_level)
        print ("\n1. Enroll to All Subjects")
        print ("2. Back to Menu")
        while True:
            try: 
                choice = int(input("Enter choice(1-2): "))
                if choice == 1:
                    ("______________________________")
                    print ("Successfully Enrolled!")
                    for subjects in curriculum_of_student_year_level:
                        print (f"Enrolled: {subjects}")
                elif choice == 2:
                    sub_portal()
            except ValueError as e:
                print (f"Error occured: {e}")
            break

#This is my View Grades function where I simply print that the grades are unavailable
def view_grades(curriculum_of_student_year_level):
    print ("________________________________________________________________________________________")
    print ("GRADES: ")
    for subjects in curriculum_of_student_year_level:
        print (f"{subjects}: Grades Unavailable")

#This is my Change Password function in case the student wants to change their password 
def change_password(sr_code, password, new_password): 
    print ("________________________________________________________________________________________")
    if sr_code in student_account and password == student_account[sr_code]["password"]:
        student_account[sr_code]["password"] = new_password
        print ("Successfully Changed Password!")
        main()
    elif sr_code in student_account and password != student_account[sr_code]["password"]:
        print ("Wrong Password")
    else:
        print ("Student Account not Found...")

#This simply calls the main function which is the backbone of this program           
if __name__ == "__main__":
    main()