from flask import Flask
from flask_migrate import Migrate
from models import db

app = Flask(__name__)

#database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'


migrate = Migrate(app, db)

#initialize flask app to use our db
db.init_app(app)

@app.route('/')
def index():
    return"<h1>INTO TO FLASK APP</h1>"

@app.route('/about')
def about():
    return "<h3>This is about us page</h3>"

@app.route('/profile/<string:username>')
def profile(username):
    return f"<h2>This profile belongs to {username}</h2>"





if __name__ == "__main__":
    app.run(port=4000, debug=True)
