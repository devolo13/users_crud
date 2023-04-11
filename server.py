from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)

# WORKS
@app.route("/users")
def show_users():
    users = User.get_all()
    print(users)
    return render_template("read.html", users=users)

# NEEDS TWEAKED
@app.route('/add_user', methods=['POST'])
def create_user():
    # create database entry
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
    }
    User.save(data)
    return redirect('/users/') # NEEDS USER ID IN URL

# PROBABLY WORKS
@app.route('/users/new')
def create_page():
    return render_template('create.html')


# NONE OF THESE FUNCTIONS HAVE BEEN WRITTEN
@app.route('/users/<int: id>')
def show_single_user(id):
    # show a single user profile
    return render_template('single_user.html')

@app.route('/users/<int: id>/edit')
def edit_a_user(id):
    # edit a user
    return render_template('edit.html')

@app.route('/users/<int: id>/delete')
def remove_a_user(id):
    # delete the entry from the database and return to index page
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)


# CHANGED EVERY FILE EXCEPT USER.PY AND MYSQLCONNECTION.PY
# ASSUME ALL OF THEM ARE BROKEN. NOTHING HAS BEEN TESTED