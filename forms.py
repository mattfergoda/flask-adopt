from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, AnyOf, URL

SPECIES = ["cat", "dog", "porcupine", "spider monkey"]
AGES_CATEGORIES = ['baby', 'young', 'adult', 'senior']

#TODO:// make two forms after all

class AddEditPetForm(FlaskForm):
    """Form for adding or editing pets."""

    name = StringField("Pet Name", validators=[InputRequired()])

    #TODO: don't need inputrequired or anyof for SelectField
    species = SelectField(
        "Species",
        choices=[(sp, sp.capitalize()) for sp in SPECIES],
        validators=[
            InputRequired(),
            AnyOf(SPECIES)
        ]
    )

    #TODO:// format better
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

