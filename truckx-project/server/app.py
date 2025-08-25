from flask import Flask, render_template, send_from_directory, request, redirect, url_for
import os

app = Flask(__name__, static_folder='../client/assets', template_folder='../client')
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/policy')
def policy():
    return render_template('policy.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        phone = request.form['phone']
        print(f"Login attempt with Email: {email}, Phone: {phone}")
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        role = request.form['role']
        email = request.form['email']
        phone = request.form['phone']
        id_file = request.files['id_proof']
        if id_file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], id_file.filename)
            id_file.save(filepath)
            print(f"Registered {role}: {name}, Email: {email}, ID saved at: {filepath}")
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/customer', methods=['GET', 'POST'])
def customer():
    if request.method == 'POST':
        pickup = request.form['pickup']
        drop = request.form['drop']
        weight = request.form['weight']
        date = request.form['date']
        notes = request.form['notes']
        print(f"Customer load request: {pickup} to {drop}, {weight}kg, Date: {date}, Notes: {notes}")
        return redirect(url_for('home'))
    return render_template('customer.html')

@app.route('/driver', methods=['GET', 'POST'])
def driver():
    if request.method == 'POST':
        name = request.form['name']
        truck_type = request.form['truck_type']
        capacity = request.form['capacity']
        availability = request.form['availability']
        police_cert = request.files['police_cert']
        if police_cert:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], police_cert.filename)
            police_cert.save(filepath)
            print(f"Driver {name} registered with truck {truck_type} - Capacity: {capacity}, Availability: {availability}, Cert saved at: {filepath}")
        return redirect(url_for('home'))
    return render_template('driver.html')

@app.route('/assets/<path:filename>')
def send_asset(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(debug=True)
