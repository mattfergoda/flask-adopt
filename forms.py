from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, AnyOf, URL

SPECIES = ["cat", "dog", "porcupine", "spider monkey"]
AGES_CATEGORIES = ['baby', 'young', 'adult', 'senior']

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])

    species = SelectField("Species",
                          choices=[(sp, sp.capitalize()) for sp in SPECIES],
                          validators=[
                              InputRequired(),
                              AnyOf(SPECIES)
                              ]
                          )

    photo_url = StringField("Pet Photo URL",
                            validators=[
                                Optional(),
                                URL()
                                ])

    age = SelectField('Pet Age Category',
        choices=[(age, age.capitalize()) for age in AGES_CATEGORIES],
        validators=[
            InputRequired(),
            AnyOf(AGES_CATEGORIES)
            ]
        )

    notes = TextAreaField("Anything you want us to know?", validators=[Optional()])

