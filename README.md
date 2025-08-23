# AI-BASED-STUDY-PLANNER
<!DOCTYPE html>
<html lang="en">
<body>
    <div class="container">
        <header>
            <h1>AI Study Planner 📚</h1>
            <p class="tagline">A smart Flask-based web application that generates personalized study plans using Google's Gemini AI</p>
            <div class="badges">
                <span class="badge badge-ai">AI-Powered</span>
                <span class="badge badge-flask">Flask 2.3.3</span>
                <span class="badge badge-mysql">MySQL 8.0</span>
            </div>
        </header>
                <section>
            <h2>✨ Features</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">🤖</div>
                    <h3>AI-Powered Planning</h3>
                    <p>Utilizes Google's Gemini AI to generate personalized study plans based on your preferences and goals.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">👤</div>
                    <h3>User Authentication</h3>
                    <p>Secure login and registration system with password hashing to protect your data.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">💾</div>
                    <h3>Data Persistence</h3>
                    <p>MySQL database integration to save user data and study plans for future reference.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🎯</div>
                    <h3>Personalized Inputs</h3>
                    <p>Customizable parameters including subjects, study hours, learning style, and goals.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">📊</div>
                    <h3>Visual Representations</h3>
                    <p>Multiple views of study plans including text, charts, and calendar views.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">📱</div>
                    <h3>Responsive Design</h3>
                    <p>Works seamlessly on desktop and mobile devices with an intuitive interface.</p>
                </div>
            </div>
        </section>
                <section>
            <h2>🚀 Quick Start</h2>
                    <h3>Prerequisites</h3>
            <ul>
                <li>Python 3.8+</li>
                <li>WAMP Server (for MySQL database)</li>
                <li>Google Gemini API key</li>
            </ul>
                <h3>Installation</h3>        
            <div class="step">
                <div class="step-number">1</div>
                <div>
                    <h4>Clone the repository</h4>
                    <div class="code-block">
                        <span class="command">git clone</span> https://github.com/scriptseekers/ai-study-planner.git<br>
                        <span class="command">cd</span> ai-study-planner
                    </div>
                </div>
            </div>
            <div class="step">
                <div class="step-number">2</div>
                <div>
                    <h4>Set up a virtual environment</h4>
                    <div class="code-block">
                        <span class="command">python -m venv venv</span><br>
                        <span class="command">source venv/bin/activate</span>  # On Windows: venv\Scripts\activate
                    </div>
                </div>
            </div>
            <div class="step">
                <div class="step-number">3</div>
                <div>
                    <h4>Install dependencies</h4>
                    <div class="code-block">
                        <span class="command">pip install -r requirements.txt</span>
                    </div>
                </div>
            </div>
            <div class="step">
                <div class="step-number">4</div>
                <div>
                    <h4>Set up the database</h4>
                    <ul>
                        <li>Start WAMP Server</li>
                        <li>Open phpMyAdmin (http://localhost/phpmyadmin)</li>
                        <li>Create a new database named <code>study_planner_db</code></li>
                        <li>Import the SQL schema from <code>database/schema.sql</code></li>
                    </ul>
                </div>
            </div>
            <div class="step">
                <div class="step-number">5</div>
                <div>
                    <h4>Configure environment variables</h4>
                    <div class="code-block">
                        <span class="command">cp</span> .env.example .env
                    </div>
                    <p>Edit <code>.env</code> with your settings:</p>
                    <div class="code-block">
                        FLASK_SECRET_KEY=your_secret_key_here<br>
                        GEMINI_API_KEY=your_gemini_api_key_here<br>
                        DB_PASSWORD=your_mysql_password
                    </div>
                </div>
            </div>
            <div class="step">
                <div class="step-number">6</div>
                <div>
                    <h4>Run the application</h4>
                    <div class="code-block">
                        <span class="command">python app.py</span>
                    </div>
                    <p>Open your browser and navigate to <code>http://localhost:5000</code></p>
                </div>
            </div>
        </section>
        <section>
            <h2>🗂️ Project Structure</h2>
            <div class="structure">
                <div class="folder">ai-study-planner/</div>
                <div class="file">app.py</div>
                <div class="file">requirements.txt</div>
                <div class="file">config.py</div>
                <div class="file">.env</div>
                <div class="folder">database/</div>
                <div class="file" style="margin-left: 40px;">schema.sql</div>
                <div class="folder">templates/</div>
                <div class="file" style="margin-left: 40px;">login.html</div>
                <div class="file" style="margin-left: 40px;">register.html</div>
                <div class="file" style="margin-left: 40px;">dashboard.html</div>
                <div class="file" style="margin-left: 40px;">result.html</div>
                <div class="file" style="margin-left: 40px;">history.html</div>
                <div class="folder">static/</div>
                <div class="file" style="margin-left: 40px;">style.css</div>
                <div class="file" style="margin-left: 40px;">script.js</div>
                <div class="folder" style="margin-left: 40px;">images/</div>
            </div>
        </section>
        <section>
            <h2>🛠️ Technology Stack</h2>
            <div class="tech-stack">
                <div class="tech-item">🔷 Backend: Flask (Python web framework)</div>
                <div class="tech-item">🗃️ Database: MySQL with WAMP Server</div>
                <div class="tech-item">🤖 AI Integration: Google Gemini API</div>
                <div class="tech-item">🎨 Frontend: HTML5, CSS3, JavaScript</div>
                <div class="tech-item">🔒 Security: Werkzeug password hashing</div>
            </div>
        </section>
        <section>
            <h2>📋 API Usage</h2>
            <p>The application integrates with Google's Gemini AI API to generate study plans:</p>
            <div class="code-block">
                prompt = f"""<br>
                Generate a weekly personalized study plan for a student with:<br>
                Name: {name},<br>
                Age: {age},<br>
                Subjects: {subjects},<br>
                Study Hours per Day: {hours},<br>
                Study Style: {style},<br>
                Time Slots: {time_slots},<br>
                Short Term Goal: {short_goal},<br>
                Long Term Goal: {long_goal}.<br>
                """<br>
            </div>
        </section>
        <section>
            <h2>🎨 Screenshots</h2>
            <h3>Login Page</h3>
            <div class="placeholder">Login Page Screenshot</div>    
            <h3>Dashboard</h3>
            <div class="placeholder">Dashboard Screenshot</div>
            <h3>Study Plan Results</h3>
            <div class="placeholder">Study Plan Results Screenshot</div>
        </section>
        <section>
            <h2>🔧 Configuration</h2>
            <h3>Gemini API Setup</h3>
            <ol>
                <li>Get your API key from <a href="https://makersuite.google.com/app/apikey">Google AI Studio</a></li>
                <li>Add it to your <code>.env</code> file:</li>
            </ol>
            <div class="code-block">
                GEMINI_API_KEY=your_actual_api_key_here
            </div>
        </section>
        <section>
            <h2>🤝 Contributing</h2>
            <div class="contributing">
                <p>We welcome contributions! Please feel free to submit pull requests or open issues for bugs and feature requests.</p>
                <ol>
                    <li>Fork the project</li>
                    <li>Create your feature branch (<code>git checkout -b feature/AmazingFeature</code>)</li>
                    <li>Commit your changes (<code>git commit -m 'Add some AmazingFeature'</code>)</li>
                    <li>Push to the branch (<code>git push origin feature/AmazingFeature</code>)</li>
                    <li>Open a pull request</li>
                </ol>
            </div>
        </section>
        <section>
            <h2>🙏 Acknowledgments</h2>
            <ul>
                <li>Google Gemini AI for powering the study plan generation</li>
                <li>Flask community for the excellent web framework</li>
                <li>Chart.js for beautiful data visualizations</li>
            </ul>
        </section>
        <footer>
            <p>Made with ❤️ using Flask and Gemini AI</p>
        </footer>
    </div>
</body>
</html>
