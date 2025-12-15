from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return"<h1>Welcome to Phase 4</h1>"

@app.route('/about')
def about():
    return "<h3>This is about us page</h3>"





if __name__ == "__main__":
    app.run(port=4000, debug=True)
