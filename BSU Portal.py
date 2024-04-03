#Batangas State University Portal 

student_account = {}
coe_curriculum = { 
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
cics_curriculum = {
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
cafad_curriculum = {
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
cit_curriculum = {
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

def main():
    while True: 
        print ("\nWelcome to Batangas State University Portal!")
        print ("1. Sign-Up  Student Account")
        print ("2. Sign-In Student Account")
        print ("3. Exit Portal")
        try:
            choice = int(input("Enter choice of action: "))
            if choice == 1:
                name = str(input("Enter Name: "))
                sr_code = int(input("Enter SR Code: "))
                password = input("Enter password: ")
                sign_up(name, sr_code, password)
            elif choice == 2:
                sr_code = int(input("Enter SR Code: "))
                password = input ("Enter password: ")
                sign_in(name, sr_code, password)
            elif choice == 3:
                print ("Exiting Portal...\n")
                break
            else:
                print ("Invalid Input!")
        except ValueError as e:
            print (f"Error occured: {e}")

def sign_up(name, sr_code, password):
    if sr_code in student_account:
        print("SR Code already in use!")
    else:
        student_account[sr_code] = {"password": password, "name" : name}
        print ('\nAccount Registered Successfully!')

def sign_in(name,sr_code, password):
    if sr_code in student_account:
        if password == student_account[sr_code]["password"]:
            school_department(name, sr_code)
        else: 
            print ("wrong password!\n")
    else:
        print ("Student Account not Found!")
        return
            
def year_level(name, sr_code, department_curriculum, department):
    while True:
        print (f"\nWelcome {name}, Choose your Year Level")
        print ('1. 1st year')
        print ('2. 2nd Year')
        print ('3. 3rd Year')
        print ('4. 4th Year')
        try: 
            choice = int(input('Enter Year Level: '))
            if choice == 1:
                student_year_level = "First Year Student"
                curriculum_of_student_year_level = department_curriculum['First Year']
                sub_portal(name, sr_code, curriculum_of_student_year_level, student_year_level, department_curriculum, department)
            elif choice == 2:
                student_year_level = "Second Year Student"
                curriculum_of_student_year_level = department_curriculum['Second Year']
                sub_portal(name, sr_code, curriculum_of_student_year_level, student_year_level, department_curriculum, department)
            elif choice == 3:
                student_year_level = "Third Year Student"
                curriculum_of_student_year_level = department_curriculum['Third Year']
                sub_portal(name, sr_code, curriculum_of_student_year_level, student_year_level,department_curriculum, department)
            elif choice == 4:
                student_year_level = "Fourth Year Student"
                curriculum_of_student_year_level = department_curriculum['Fourth Year']
                sub_portal(name, sr_code, curriculum_of_student_year_level, student_year_level,department_curriculum, department)
            else: 
                print ("Invalid Input!")
                break
        except ValueError as e: 
            print (f"Error Occured: {e}")
        

def school_department(name, sr_code):
    while True:
        print (f"\nWelcome {name}, Choose your Designated Department!")
        print ("1. College of Informatics and Computing Sciences")
        print ("2. College of Engineering")
        print ("3. College of Industrial Technology")
        print ("4. College of Architecture, Fine Arts and Design")
        while True:
            try:
                choice = int(input("Enter choice: "))
                if choice == 1:
                    department_curriculum = cics_curriculum
                    department = "College of Informatics and Computing Sciences"
                    year_level(name, sr_code, department_curriculum, department)
                elif choice == 2:
                    department_curriculum = coe_curriculum
                    department = "College of Engineering"
                    year_level(name, sr_code, department_curriculum, department)
                elif choice == 3:
                    department_curriculum = cit_curriculum
                    department = "College of Industrial Technology"
                    year_level(name, sr_code, department_curriculum, department)
                elif choice == 4:
                    department_curriculum = cafad_curriculum
                    department = "College of Architecture, Fine Arts and Design"
                    year_level(name, sr_code, department_curriculum, department)
                else:
                    print ("Invalid Input!")
                return
            except ValueError as e:
                print (f"Error Occured: {e}")
            
def sub_portal(name, sr_code, curriculum_of_student_year_level, student_year_level, department_curriculum, department):
    while True:
        print (f'\nWelcome {name} to the Portal!')
        print ("1. View Subjects")
        print ("2. View ID")
        print ("3. Schedules")
        print ("4. Liabilities")
        print ("5. Membership Payments")
        print ("6. Curriculum")
        print ("7. Scholarships")
        print ("8. Online Registration")
        print ("9. Certificate of Registration")
        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                view_subjects(curriculum_of_student_year_level)
            elif choice == 2:
                view_ID(name, sr_code, department, student_year_level)
            elif choice == 3:
                schedules()
            elif choice == 4:
                liabilities()
            elif choice == 5:
                membership_payments()
            elif choice == 6:
                curriculum(department_curriculum)
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

def view_subjects(curriculum_of_student_year_level):
    print ("\nYour Subjects: ")
    for subjects in curriculum_of_student_year_level:
        print (f"- {subjects}")

def curriculum(department_curriculum):
    print ("\nYour Entire Curriculum: ")
    for year_level, subjects in department_curriculum.items():
        print (f"\n{year_level}:")
        for subject in subjects: 
            print (f"- {subject}")

def liabilities():
    pass

def schedules():
    pass

def membership_payments():
    pass

def view_ID(name, sr_code, department, student_year_level):
    print (f'''
           ___________________
           |                 |
           |                 |
           |     Photo       |
           |   Unavailable   |
           |     {name}      |
           |     {sr_code}   |
           |    {department} |
           | {student_year_level}|
           |                 |
           |_________________|''')
    

def certificate_of_registration(name, sr_code, department, student_year_level):
    print ("\nCertificate of Registration")
    print ("\nRepublic of the Philippines\nBatangas State University\nThe National Engineering University\n")
    print 

def scholarships():
    print ("\nScholarships: ")
    print ("Higher Education Support Program: \nTuition Fee Discount: 100% \nMisc Fee Discount: 100%")

def online_registration():
    pass

main()