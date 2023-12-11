# app.py

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from weather_data import get_weather

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
app.config['SECRET_KEY'] = 'your_secret_key'  # Add a secret key for CSRF protection
db = SQLAlchemy(app)

# Define the Weather model in weather_data.py (similar to previous example)

class LocationForm(FlaskForm):
    city = StringField('City', render_kw={"placeholder": "Enter city name"})
    submit = SubmitField('Get Weather')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LocationForm()

    if form.validate_on_submit():
        # Get city name from the form
        city = form.city.data

        # Example: Get weather for the entered city
        weather_data = get_weather(city)
        return render_template('chatbot.html', weather_data=weather_data, form=form)

    return render_template('chatbot.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
