
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "roofing_secret"  # Required for session (admin login)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Booking Model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    problem = db.Column(db.Text)

# Create database tables if not exist
with app.app_context():
    db.create_all()

# -------------------------------
# Admin Login Route
# -------------------------------
@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Simple hardcoded credentials
        if username == 'admin' and password == '1234':
            session['admin_logged_in'] = True
            return redirect(url_for('admin'))
        else:
            return render_template('admin-login.html', error="Invalid Credentials")
    return render_template('admin-login.html')

# -------------------------------
# Admin Dashboard
# -------------------------------
@app.route('/admin')
def admin():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    all_bookings = Booking.query.all()
    return render_template("admin.html", bookings=all_bookings)

# -------------------------------
# Delete Booking
# -------------------------------
@app.route('/delete-booking/<int:booking_id>', methods=['POST'])
def delete_booking(booking_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    booking = Booking.query.get_or_404(booking_id)
    db.session.delete(booking)
    db.session.commit()
    return redirect(url_for('admin'))

# -------------------------------
# Booking Route (for users)
# -------------------------------
@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        new_booking = Booking(
            name=request.form['name'],
            phone=request.form['phone'],
            address=request.form['address'],
            problem=request.form['problem']
        )
        db.session.add(new_booking)
        db.session.commit()
        return render_template("success.html")  # success page after booking
    return render_template("booking.html")

# -------------------------------
# Home Page (optional)
# -------------------------------
@app.route('/')
def home():
    return render_template("index.html")

# -------------------------------
if __name__ == '__main__':
    app.run(debug=True)