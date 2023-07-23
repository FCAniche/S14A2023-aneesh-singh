from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from datetime import datetime
import os
from dotenv import load_dotenv

# Load database URI from .env file
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone_number = db.Column(db.String(255))
    updated_at = db.Column(db.DateTime)
    status = db.Column(db.Integer)
    is_admin = db.Column(db.Boolean)

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(255))
    item_count = db.Column(db.Integer)
    total = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # Add foreign key relationship to 'users' table
    user = db.relationship('User', backref=db.backref('orders', lazy=True))

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/adduser', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        email = request.form['email']
        phone_number = request.form['phone_number']
        # Add other form fields as needed
        new_user = User(
            email=email, 
            phone_number=phone_number, 
            updated_at=datetime.utcnow())
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_user.html')

@app.route('/updateuser/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.email = request.form['email']
        user.phone_number = request.form['phone_number']
        user.updated_at = datetime.utcnow()
        # Update other columns as needed
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update_user.html', user=user)

@app.route('/deleteuser/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/orders', methods=['GET'])
def orders():
    user_id = request.args.get('user_id')  # Get the user ID from the query string
    if user_id:
        orders = Order.query.filter_by(user_id=user_id).all()
        return render_template('orders.html', orders=orders)
    return "No orders found for this user."

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)