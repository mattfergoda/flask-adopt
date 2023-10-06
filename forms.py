from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("Pet Photo URL")
    age = SelectField('Pet Age Category',
        choices=[
            ('baby', 'Baby'),
            ('young', 'Young'),
            ('adult', 'Adult'),
            ('senior', 'Senior'),
                 ])
    notes = TextAreaField("Anything you want us to know?")
    
