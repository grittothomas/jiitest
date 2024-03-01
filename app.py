from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return """Welcome to My Text-Based Web Application!

This is a simple example of a text-based web application built with Python Flask.

Features:
- Displays a welcome message on the home page.
- Provides basic information about the application.

Feel free to explore and modify this application to suit your needs!

"""


@app.route('/about')
def about():
    return """About This Application:

This text-based web application is built using Python Flask, a lightweight web framework.
It serves as a starting point for building more complex web applications.
You can add more routes, templates, and functionality as needed.
Flask allows for easy expansion and customization, making it a great choice for web development projects.

"""


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
