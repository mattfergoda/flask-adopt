from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, AnyOf


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])

    species = StringField("Species", validators=[InputRequired()])

    photo_url = StringField("Pet Photo URL", validators=[Optional()])

    age = SelectField('Pet Age Category',
        choices=[
            ('baby', 'Baby'),
            ('young', 'Young'),
            ('adult', 'Adult'),
            ('senior', 'Senior'),
                 ],
        validators=[
            InputRequired(),
            AnyOf(values=['baby', 'young', 'adult', 'senior'])
            ]
        )

    notes = TextAreaField("Anything you want us to know?", validators=[Optional()])

