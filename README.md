# Batangas State University Portal 🎓

Welcome to the Batangas State University (BSU) Portal, a simplified student portal developed using Python. This portal allows students to register, log in, and access various functionalities, including viewing their ID, subjects, curriculum, grades, and handling membership payments.

## Features ✨

- **Student Account Management**: Register and log in to your student account using your SR Code, name, and password. 🆔🔑
- **Department and Curriculum Selection**: Choose your designated college department and view the corresponding curriculum based on your year level. 📚🏛️
- **Sub Portal Functionalities**: Access a variety of options, including:
  - Viewing ID, subjects, grades, and schedules 📄📅
  - Checking liabilities and processing membership payments 💸
  - Adding balance to your account 💰
  - Online registration 🌐
  - Changing your account password 🔒

## Departmental Curriculums 🎓

The portal supports four college departments, each with a unique curriculum:

- **College of Engineering** 🏗️
- **College of Informatics and Computing Sciences** 💻
- **College of Architecture, Fine Arts, and Design** 🎨
- **College of Industrial Technology** ⚙️

The curriculums are generalized for all courses within each department to keep the code manageable. The curriculum is divided into four year levels, with each level offering a distinct set of subjects.

## Membership Payments 💳

The portal includes a membership payments system, where students can pay for:

- **SSC Membership**: Php 45
- **Department Membership**: Php 60
- **Organization Membership**: Php 80

Students can add balance to their account and choose which memberships to pay for. The system checks for sufficient balance before processing payments and keeps track of liabilities.

## Error Handling 🚨

The portal includes basic error handling, such as catching invalid inputs and guiding users back to the correct options.

## How to Use 🛠️

1. **Register**: Create a student account by entering your SR Code, name, and password. 📝
2. **Log In**: Access your account by entering your SR Code, name, and password. 🔑
3. **Navigate the Portal**: Choose your department, select your year level, and explore the various functionalities available in the sub-portal. 🌐

## Installation and Setup ⚙️

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/bsu-portal.git
    ```
2. Navigate to the project directory:
    ```bash
    cd bsu-portal
    ```
3. Run the Python script:
    ```bash
    python bsu_portal.py
    ```

## Requirements 📋

- Python 3.x

## Conclusion 🏆

This BSU Portal project is a simplified representation of a student portal, focusing on key functionalities and user experience. It serves as a foundational project, which can be expanded with more features and refined for real-world application.
