from Flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_view():
    return render_template('home.html')
