"""Flask app for adopt app."""

import os

from flask import Flask, flash, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, db, Pet
from forms import AddPetForm


app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get('/')
def show_homepage():
    ''' show the homepage with list of pets '''

    pets = Pet.query.all()

    return render_template('pets.html', pets=pets)



@app.route("/add", methods=["GET", "POST"])
def add_pet_form():
    """ shows and handles add pet form """

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data or ''
        age = form.age.data
        notes = form.notes.data or ''


        # do stuff with data/insert to db
        new_pet = Pet(
            name=name,
            species=species,
            photo_url=photo_url,
            age=age,
            notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added {name} to adoptable pets")
        return redirect("/")

    else:
        return render_template(
            "add_pet.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def handle_edit_pet_form(pet_id):
    """ shows and handles the edit pet form """

    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data or ''
        age = form.age.data
        notes = form.notes.data or ''


        # do stuff with data/insert to db
        new_pet = Pet(
            name=name,
            species=species,
            photo_url=photo_url,
            age=age,
            notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added {name} to adoptable pets")
        return redirect("/")

    else:
        return render_template(
            "pet_details.html", form=form, pet=pet)

