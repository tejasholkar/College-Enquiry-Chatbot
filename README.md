# 🎓 College Enquiry Chatbot

A smart AI-powered **College Enquiry Chatbot** designed to answer students' questions regarding admissions, courses, fees, faculty, placements, campus facilities, and other college-related information. The chatbot provides quick, accurate, and user-friendly responses through a web interface.

---

# 📌 Project Overview

The College Enquiry Chatbot is a web-based application that automates responses to frequently asked questions by students and parents. Instead of manually answering repetitive queries, the chatbot retrieves information from a database and generates responses instantly.

The project consists of:

* **Frontend** for user interaction
* **Backend (Python)** for processing requests
* **MySQL Database** for storing college information
* REST APIs to communicate between frontend and backend

---

# 🚀 Features

* Student-friendly chatbot interface
* Admission enquiry support
* Course information
* Department details
* Faculty information
* Fee structure details
* Placement information
* Scholarship details
* College timings
* Contact information
* Campus facilities
* Frequently Asked Questions (FAQ)
* Responsive design
* Fast response time
* Database integration
* Easy to customize

---

# 🛠 Technologies Used

## Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap (Optional)

### Responsibilities

* User Interface
* Chat Window
* Send/Receive Messages
* API Requests
* Responsive Design

---

## Backend

**Language:** Python

### Framework (Choose One)

* Flask
* FastAPI
* Django (Optional)

### Responsibilities

* Handle chatbot requests
* Connect with database
* Process user messages
* Generate responses
* API development
* Business logic

---

## Database

**MySQL**

### Stores

* Student FAQs
* Courses
* Departments
* Faculty
* Fee Details
* Placements
* Scholarships
* Contact Details
* Admission Information

---

# 📂 Project Structure

```text
College-Enquiry-Chatbot/
│
├── static/
│   ├── css/
│   │      style.css
│   ├── js/
│   │      script.js
│   └── images/
│
├── templates/
│   └── index.html
│
├── database/
│   ├── college.sql
│   └── database.py
│
├── chatbot/
│   ├── chatbot.py
│   ├── intents.json
│   ├── model.py
│   └── utils.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙ Installation

## Step 1

Clone the repository

```bash
git clone https://github.com/yourusername/college-enquiry-chatbot.git
```

---

## Step 2

Move into the project directory

```bash
cd college-enquiry-chatbot
```

---

## Step 3

Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 4

Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 5

Setup MySQL Database

Create database

```sql
CREATE DATABASE college_chatbot;
```

Import SQL file

```bash
mysql -u root -p college_chatbot < college.sql
```

---

## Step 6

Update Database Credentials

Example

```python
host="localhost"
user="root"
password="your_password"
database="college_chatbot"
```

---

## Step 7

Run the Project

```bash
python app.py
```

Server starts at

```text
http://127.0.0.1:5000
```

---

# 💾 Database Design

Example Tables

### students

| Field | Type    |
| ----- | ------- |
| id    | INT     |
| name  | VARCHAR |
| email | VARCHAR |

---

### courses

| Field       | Type    |
| ----------- | ------- |
| id          | INT     |
| course_name | VARCHAR |
| duration    | VARCHAR |
| fees        | DECIMAL |

---

### departments

| Field           | Type    |
| --------------- | ------- |
| id              | INT     |
| department_name | VARCHAR |
| hod             | VARCHAR |

---

### faculty

| Field        | Type    |
| ------------ | ------- |
| id           | INT     |
| faculty_name | VARCHAR |
| department   | VARCHAR |

---

### faq

| Field    | Type |
| -------- | ---- |
| id       | INT  |
| question | TEXT |
| answer   | TEXT |

---

# 🔄 Application Workflow

```text
User
   │
   ▼
Frontend (HTML/CSS/JS)
   │
   ▼
Python Backend (Flask/FastAPI)
   │
   ▼
MySQL Database
   │
   ▼
Response Generated
   │
   ▼
Displayed to User
```

---

# 📡 API Endpoints

## Home Page

```http
GET /
```

---

## Chat API

```http
POST /chat
```

Request

```json
{
  "message": "What are the admission fees?"
}
```

Response

```json
{
  "reply": "The admission fee for B.Tech is ₹50,000."
}
```

---

# 📦 Python Packages

Example requirements

```text
Flask
mysql-connector-python
pymysql
SQLAlchemy
nltk
numpy
pandas
scikit-learn
tensorflow (optional)
gunicorn
requests
```

---

# 🎨 Frontend Screens

* Home Page
* Chat Window
* About College
* Contact Page
* FAQ Section

---

# 🤖 Chatbot Capabilities

The chatbot can answer questions like:

* What courses are available?
* What is the admission process?
* What are the fees?
* What are the placement statistics?
* Who is the Head of Computer Department?
* What is the college timing?
* How can I contact the college?
* Is hostel available?
* What scholarships are offered?
* Where is the college located?

---

# 🔐 Security Features

* Input validation
* SQL Injection prevention using parameterized queries
* Error handling
* Secure database connection
* API request validation

---

# 📈 Future Enhancements

* AI-powered NLP responses
* Voice Assistant
* Speech-to-Text
* Text-to-Speech
* Multi-language support
* WhatsApp Integration
* Telegram Bot
* Admin Dashboard
* Student Login
* Authentication System
* Live Chat Support
* PDF Admission Brochure
* Email Notifications
* Analytics Dashboard
* Chat History

---

# 🧪 Testing

Test the chatbot with sample queries:

```text
Hi

Tell me about admission.

What courses are available?

What is the fee structure?

Who is the HOD of Computer Department?

Tell me about placements.

Where is the college located?

Thank you
```

---

# 📷 Sample Output

```text
User:
What courses are available?

Bot:
We offer B.Tech, BCA, MCA, MBA, Diploma, and B.Sc programs.
```

---

# 👨‍💻 Advantages

* Reduces manual enquiry workload
* 24×7 availability
* Instant responses
* User-friendly interface
* Centralized database
* Easy maintenance
* Scalable architecture
* Improves student experience

---

# ⚠ Limitations

* Depends on database accuracy
* Limited to available information
* Requires internet access (for web deployment)
* Cannot answer unsupported queries without additional logic or AI integration

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Push the branch.
6. Open a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👥 Authors

Developed as a College Mini/Major Project.

---

# 🙏 Acknowledgements

Special thanks to:

* Python Community
* Flask Framework
* MySQL
* Bootstrap
* Open-source contributors

---

# 📞 Contact

For suggestions or issues, please open an issue in the project repository or contact the project maintainer.

---

⭐ If you find this project useful, consider giving it a star on GitHub!

