from flask import Flask
app = Flask(__name__)

@app.get('/welcome')
def say_welcome():
    """Return simple string 'welcome'"""
    return """
        <html>
            <body>
                <h1>welcome</h1>
            </body>
        </html>
    """

@app.get('/welcome/home')
def say_welcome_home():
    """Return simple string 'welcome home'"""
    return """
        <html>
            <body>
                <h1>welcome home</h1>
            </body>
        </html>
    """

@app.get('/welcome/back')
def say_welcome_back():
    """Return simple string 'welcome back'"""
    return """
        <html>
            <body>
                <h1>welcome back</h1>
            </body>
        </html>
    """