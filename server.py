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

@app.route('/show/<int:friend_id>')
def show_friend(friend_id):
    friend = Friend.get_one(friend_id)
    return render_template('show.html', friend = friend)


@app.route('/update/<int:friend_id>')
def update_form(friend_id):
    friend = Friend.get_one(friend_id)
    return render_template('update.html', friend = friend)

@app.route('/update',methods=['POST'])
def update():
    Friend.update(request.form)
    return redirect('/')

@app.route('/delete/<int:friend_id>')
def delete(friend_id):
    Friend.delete(friend_id)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)