from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/list')
def list():
    # Fill data for List page
    data = []
    current_dict = {}

    with open('data.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                if 'name' not in current_dict:
                    current_dict['name'] = line
                else:
                    current_dict['email'] = line
                    data.append(current_dict)
                    current_dict = {}
    return render_template('list.html', data=data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form['email']
        message = request.form['message']
        # Process the form data (e.g., send an email)
        # Print data to log (for now)
        print('Email:', email)
        print('Message:', message)
        return redirect('/')
    return render_template('contact.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        # Process the form data (e.g., register for website)
        # Save it to data file
        with open('data.txt', 'a') as file:
            file.write(name + '\n')
            file.write(email + '\n')
        return redirect('/')
    return render_template('registration.html')

if __name__ == '__main__':
    app.run(debug=True)
