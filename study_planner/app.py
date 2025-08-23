from flask import Flask, render_template, request, redirect, url_for, session, flash
import google.generativeai as genai
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Your WAMP MySQL password
    'database': 'study_planner_db'
}

# Initialize Gemini AI
genai.configure(api_key="AIzaSyD2FUOv9FKMip-OiJJtBYr1USpjD3Hk0A4")  
model = genai.GenerativeModel("gemini-2.0-flash")

def get_db_connection():
    return mysql.connector.connect(**db_config)

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create study_plans table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS study_plans (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL,
            subjects TEXT NOT NULL,
            hours_per_day INT NOT NULL,
            study_style VARCHAR(20) NOT NULL,
            time_slots TEXT NOT NULL,
            short_term_goal TEXT NOT NULL,
            long_term_goal TEXT NOT NULL,
            study_plan TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    ''')
    
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        confirm_password = request.form['confirm_password']
        
        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return render_template('register.html')
        
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            # Check if username or email already exists
            cursor.execute("SELECT id FROM users WHERE username = %s OR email = %s", (username, email))
            if cursor.fetchone():
                flash('Username or email already exists!', 'error')
                return render_template('register.html')
            
            # Insert new user
            password_hash = generate_password_hash(password)
            cursor.execute(
                "INSERT INTO users (username, password_hash, email) VALUES (%s, %s, %s)",
                (username, password_hash, email)
            )
            conn.commit()
            
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
            
        except mysql.connector.Error as err:
            flash(f'Database error: {err}', 'error')
            return render_template('register.html')
        finally:
            cursor.close()
            conn.close()
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()
            
            if user and check_password_hash(user['password_hash'], password):
                session['user_id'] = user['id']
                session['username'] = user['username']
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid username or password!', 'error')
                
        except mysql.connector.Error as err:
            flash(f'Database error: {err}', 'error')
        finally:
            cursor.close()
            conn.close()
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        user_input = request.form.to_dict(flat=True)
        
        # Validate study hours
        try:
            hours = int(user_input['hours_per_day'])
            if hours < 1 or hours > 24:
                flash('Please enter valid study hours (1-24)', 'error')
                return render_template('dashboard.html')
        except ValueError:
            flash('Please enter a valid number for study hours', 'error')
            return render_template('dashboard.html')
        
        prompt = f"""
        Generate a weekly personalized study plan for a student with:
        Name: {user_input['name']},
        Age: {user_input['age']},
        Subjects: {user_input['subjects']},
        Study Hours per Day: {user_input['hours_per_day']},
        Study Style: {user_input['study_style']},
        Time Slots: {user_input['time_slots']},
        Short Term Goal: {user_input['short_term_goal']},
        Long Term Goal: {user_input['long_term_goal']}.
        Make the schedule visually structured and motivating. Note* Don't make any table format, just a simple text output. Provide a detailed plan for each day of the week, including specific tasks and study techniques.
        """

        try:
            response = model.generate_content(prompt)
            plan = response.text
            
            # Save to database
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO study_plans 
                (user_id, name, age, subjects, hours_per_day, study_style, time_slots, short_term_goal, long_term_goal, study_plan)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (
                session['user_id'], 
                user_input['name'], 
                user_input['age'], 
                user_input['subjects'], 
                user_input['hours_per_day'], 
                user_input['study_style'], 
                user_input['time_slots'], 
                user_input['short_term_goal'], 
                user_input['long_term_goal'], 
                plan
            ))
            
            conn.commit()
            cursor.close()
            conn.close()
            
            return render_template('result.html', plan=plan)
            
        except Exception as e:
            flash(f'Error generating study plan: {str(e)}', 'error')
            return render_template('dashboard.html')

    return render_template('dashboard.html')

@app.route('/history')
def history():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute('''
            SELECT id, name, subjects, created_at 
            FROM study_plans 
            WHERE user_id = %s 
            ORDER BY created_at DESC
        ''', (session['user_id'],))
        
        plans = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return render_template('history.html', plans=plans)
    except mysql.connector.Error as err:
        flash(f'Database error: {err}', 'error')
        return redirect(url_for('dashboard'))

@app.route('/plan/<int:plan_id>')
def view_plan(plan_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute('''
            SELECT * FROM study_plans 
            WHERE id = %s AND user_id = %s
        ''', (plan_id, session['user_id']))
        
        plan = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if plan:
            return render_template('result.html', plan=plan['study_plan'])
        else:
            flash('Study plan not found!', 'error')
            return redirect(url_for('history'))
            
    except mysql.connector.Error as err:
        flash(f'Database error: {err}', 'error')
        return redirect(url_for('history'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)