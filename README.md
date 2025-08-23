# AI-BASED-STUDY-PLANNER
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Study Planner</title>
    <style>
        :root {
            --primary: #3498db;
            --secondary: #2ecc71;
            --accent: #9b59b6;
            --dark: #2c3e50;
            --light: #ecf0f1;
            --warning: #e74c3c;
            --text: #34495e;
        }
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--text);
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 20px;
        }
                .container {
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }
                header {
            background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%);
            color: white;
            padding: 40px 20px;
            text-align: center;
        }
        h1 {
            font-size: 2.8rem;
            margin-bottom: 15px;
        }
        .tagline {
            font-size: 1.2rem;
            opacity: 0.9;
        }
        .badges {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin: 20px 0;
        }
        .badge {
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: bold;
        }
                .badge-ai {
            background: var(--accent);
            color: white;
        }
                .badge-flask {
            background: var(--secondary);
            color: white;
        }
                .badge-mysql {
            background: var(--primary);
            color: white;
        }
                section {
            padding: 30px;
            border-bottom: 1px solid #eee;
        }
                h2 {
            color: var(--primary);
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid var(--light);
        }
                h3 {
            color: var(--dark);
            margin: 15px 0 10px;
        }
                .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }
                .feature-card {
            background: var(--light);
            padding: 20px;
            border-radius: 10px;
            transition: transform 0.3s ease;
        }
                .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
                .feature-icon {
            font-size: 2rem;
            margin-bottom: 15px;
            color: var(--primary);
        }
                .tech-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin: 20px 0;
        }
                .tech-item {
            background: var(--light);
            padding: 10px 15px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
                .code-block {
            background: #2d3436;
            color: #dfe6e9;
            padding: 15px;
            border-radius: 8px;
            overflow-x: auto;
            margin: 15px 0;
        }
                .command {
            color: #fd9644;
        }
                .structure {
            background: var(--light);
            padding: 15px;
            border-radius: 8px;
            font-family: monospace;
            line-height: 1.8;
        }
                .folder {
            color: var(--primary);
            font-weight: bold;
        }
                .file {
            color: var(--dark);
            margin-left: 20px;
        }
                .screenshot {
            width: 100%;
            border-radius: 8px;
            margin: 15px 0;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
                .placeholder {
            background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
            height: 200px;
            border-radius: 8px;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
            font-weight: bold;
        }
                .step {
            display: flex;
            margin-bottom: 20px;
            align-items: flex-start;
        }
                .step-number {
            background: var(--primary);
            color: white;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            margin-right: 15px;
            flex-shrink: 0;
        }
                .contributing {
            background: var(--light);
            padding: 20px;
            border-radius: 10px;
        }
                footer {
            text-align: center;
            padding: 30px;
            background: var(--dark);
            color: white;
        }
                @media (max-width: 768px) {
            .features-grid {
                grid-template-columns: 1fr;
            }
                    h1 {
                font-size: 2.2rem;
            }
        }
    </style>
</head>
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
