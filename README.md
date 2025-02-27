*Student Management System using Django ModelForm*

**Overview**
    The Student Management System is a simple web application built using Django's ModelForm feature. It provides CRUD (Create, Read, Update, Delete) functionality, allowing users to manage student records efficiently.
**Features**
    ✅ Add Students – Users can add new students with Name, Email, and Password fields.
    ✅ View Students – Displays student details dynamically on the webpage.
    ✅ Edit Students – Allows users to update student information.
    ✅ Delete Students – Users can remove student records with a confirmation prompt.
    ✅ User-Friendly UI – Styled with Bootstrap for a clean and responsive design.
**Technologies Used**
    Python (Django Framework)
    Django ModelForm (for form handling)
    HTML, CSS, Bootstrap (for frontend design)
    SQLite3 (default Django database)

**Project Structure**

StudentManagementSystem/
│── students/               # Django app for student management
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates
│   ├── static/             # CSS, JS, Bootstrap files
│   ├── views.py            # Handles user requests
│   ├── models.py           # Database models
│   ├── forms.py            # Django ModelForm for Student
│   ├── urls.py             # URL routing
│── StudentManagementSystem/ # Main Django project settings
│── db.sqlite3              # SQLite Database
│── manage.py               # Django command-line utility
│── requirements.txt        # Python dependencies
│── README.md               # Project documentation
