from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    created_at = db.Column(db.String(100))
    updated_at = db.Column(db.String(100))

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    image = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.String(100))
    updated_at = db.Column(db.String(100))

@app.route('/')
def index():
    title = 'Todo App | Index'
    todos = Contacts.query.all()
    print(todos)
    return render_template(
        'index.html',
        title=title,
        todos=todos
    )

@app.route('/create', methods=['POST'])
def create():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    new_todo = Contacts(name=name, email=email, phone=phone)
    db.session.add(new_todo)
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    todo = Contacts.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    contact = Contacts.query.filter_by(id=id).first()
    contact.name = name
    contact.email = email
    contact.phone = phone
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0')