# Import libraries.
from flask import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)

class Weather(db.Model):
   __tablename__ = 'combined'
   field1 = db.Column(db.Integer, primary_key=True)
   Date = db.Column(db.Text)

@app.route('/')
def testdb():
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return '<h1>Go Travel!</h1>'
    except Exception as er:
        # er describes the error
        error_text = "<p>The error:<br>" + str(er) + "</p>"
        state = '<h1>Connection unsuccessful.</h1>'
        return state + error_text


if __name__ == '__main__':
    app.run(debug=True)

# Replace with your file path.
db_name = r'C:\Users\nesis\combine.csv...L.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True