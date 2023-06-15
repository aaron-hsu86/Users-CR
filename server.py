from flask import Flask, render_template, redirect, request
from friend import Friend
app = Flask(__name__)

@app.route('/')
def main_page():
    friends = Friend.get_all()

    return render_template('users.html', friends = friends)

@app.route('/create_user')
def create_user():
    return render_template('create.html')

@app.route('/add_user', methods=['post'])
def add_user():
    Friend.save(request.form)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)