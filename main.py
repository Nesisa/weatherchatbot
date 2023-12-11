from flask import *

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
        return render_template('chat_form.html')  # Render the chat form template
    except Exception as er:
        # Handle the database connection error
        error_text = "<p>The error:<br>" + str(er) + "</p>"
        state = '<h1>Connection unsuccessful.</h1>'
        return state + error_text

@app.route('/submit_chat', methods=['POST'])
def submit_chat():
    if request.method == 'POST':
        message = request.form.get('message')
        # Handle the submitted message (e.g., store it in the database)
        # For now, let's print it to the console
        print("Received Message:", message)
        return "Message submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
