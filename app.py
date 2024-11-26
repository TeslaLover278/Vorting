from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Simple home page

@app.route('/about')
def about():
    return render_template('about.html')  # Simple about page

@app.route('/contact')
def contact():
    return render_template('contact.html')  # Simple contact page

@app.route('/redirect-example')
def redirect_example():
    # Example redirect
    return redirect(url_for('home'))  # Redirect to home page

if __name__ == '__main__':
    app.run(debug=True)
