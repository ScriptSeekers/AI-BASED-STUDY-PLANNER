from flask import Flask, render_template, request, redirect, url_for, session, send_file
import google.generativeai as genai

app = Flask(__name__)
app.secret_key = '1234'

# Dummy login credentials
users = {'arpit': '1234','sanju': '1234'}

# Gemini API setup
genai.configure(api_key="AIzaSyD2FUOv9FKMip-OiJJtBYr1USpjD3Hk0A4")  
model = genai.GenerativeModel("gemini-2.0-flash")


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials"
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        user_input = request.form.to_dict(flat=True)
        session['form_data'] = user_input

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
        Make the schedule visually structured and motivating.

        Note* Don't make any table format, just a simple text output.
        Provide a detailed plan for each day of the week, including specific tasks and study techniques.
        """

        response = model.generate_content(prompt)
        plan = response.text
        session['study_plan'] = plan

        return render_template('result.html', plan=plan)

    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
