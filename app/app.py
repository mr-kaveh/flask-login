from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# SQLite database configuration
DATABASE = 'users.db'

def create_table():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT NOT NULL,
                 password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def insert_user(username, password):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

def check_user(username, password):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()
    return user

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = check_user(username, password)
        
        if user:
            return "Login successful!"
        else:
            return "Invalid username or password. Please try again."
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        insert_user(username, password)
        
        return redirect(url_for('login'))
    return render_template('register.html')

if __name__ == '__main__':
    create_table()
    app.run(debug=True, port=9000)
