# AI-BASED-STUDY-PLANNER
A smart Flask-based web application that generates personalized study plans using Google's Gemini AI. This tool helps students create optimized study schedules based on their preferences, goals, and learning styles.

https://img.shields.io/badge/AI-Powered-blue?style=for-the-badge&logo=google
https://img.shields.io/badge/Flask-2.3.3-green?style=for-the-badge&logo=flask
https://img.shields.io/badge/MySQL-8.0-blue?style=for-the-badge&logo=mysql

✨ Features
🤖 AI-Powered Planning: Utilizes Google's Gemini AI to generate personalized study plans

👤 User Authentication: Secure login and registration system with password hashing

💾 Data Persistence: MySQL database integration to save user data and study plans

🎯 Personalized Inputs: Customizable parameters including:

Study subjects and hours per day

Preferred time slots

Learning style (Visual, Auditory, Kinesthetic)

Short-term and long-term goals

📊 Visual Representations: Multiple views of study plans including:

Text-based detailed plans

Visual charts showing study distribution

Calendar view for weekly planning

📱 Responsive Design: Works seamlessly on desktop and mobile devices

🚀 Quick Start
Prerequisites
Python 3.8+

WAMP Server (for MySQL database)

Google Gemini API key

Installation
Clone the repository

bash
git clone https://github.com/your-username/ai-study-planner.git
cd ai-study-planner
Set up a virtual environment

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
pip install -r requirements.txt
Set up the database

Start WAMP Server

Open phpMyAdmin (http://localhost/phpmyadmin)

Create a new database named study_planner_db

Import the SQL schema from database/schema.sql

Configure environment variables

text
FLASK_SECRET_KEY=your_secret_key_here
GEMINI_API_KEY=your_gemini_api_key_here
DB_PASSWORD=your_mysql_password
Run the application

bash
python app.py
Open your browser and navigate to http://localhost:5000

🗂️ Project Structure

ai-study-planner/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── config.py             # Configuration settings
├── .env                  # Environment variables
├── database/
│   └── schema.sql        # Database schema
├── templates/
│   ├── login.html        # Login page
│   ├── register.html     # Registration page
│   ├── dashboard.html    # Main dashboard
│   ├── result.html       # Study plan results
│   └── history.html      # Study plan history
└── static/
    ├── style.css         # Main stylesheet
    ├── script.js         # Client-side JavaScript
    └── images/           # Static images
🛠️ Technology Stack
Backend: Flask (Python web framework)

📋 API Usage
The application integrates with Google's Gemini AI API to generate study plans:

python
prompt = f"""
Generate a weekly personalized study plan for a student with:
Name: {name},
Age: {age},
Subjects: {subjects},
Study Hours per Day: {hours},
Study Style: {style},
Time Slots: {time_slots},
Short Term Goal: {short_goal},
Long Term Goal: {long_goal}.
"""

Open a pull request

🙏 Acknowledgments
Google Gemini AI for powering the study plan generation


<div align="center"> Made with ❤️ using Flask and Gemini AI </div>
New chat
