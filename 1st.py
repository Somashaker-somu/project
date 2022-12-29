from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)


@app.route('/')
def demo():
    return render_template('first.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


conn = sqlite3.connect('Database.db')
# print ("Opened database successfully")


@app.route('/signup', methods=['POST', 'GET'])
def signup1():
    new_email = request.form['email']
    new_pwd = request.form['password']
    new_cpwd = request.form['new_password']
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute('INSERT INTO student (email,password,new_password) values(?,?,?)',
                (new_email, new_pwd, new_cpwd))
    conn.commit()
    return render_template('login.html', info="successfully added student details")


if __name__ == '__main__':
    app.run(port=5000, debug=True)
