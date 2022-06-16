from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import *
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///to_do_website.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)


class ToDos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    task = db.Column(db.String(250), nullable=False)


# db.create_all()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/tasks/<int:user_id>', methods=['POST', 'GET'])
def show_tasks(user_id):
    new_task_form = NewTaskForm()
    check_form = OldTaskForm()
    all_tasks = db.session.query(ToDos).all()

    if new_task_form.validate_on_submit():
        new_task = ToDos(user_id=user_id, task=new_task_form.task.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('show_tasks', user_id=user_id))

    return render_template('personal_tasks.html', tasks=all_tasks, new_task_form=new_task_form, check_form=check_form)


@app.route('/tasks/<user_id>/<int:task_id>', methods=['POST', 'GET'])
def mark_done(task_id, user_id):
    done_task = ToDos.query.get(task_id)
    db.session.delete(done_task)
    db.session.commit()
    return redirect(url_for('show_tasks', user_id=1))


if __name__ == '__main__':
    app.run(debug=True)