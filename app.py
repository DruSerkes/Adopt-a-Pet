from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secretkey1239123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


# This should be at the URL path /add. Add a link to this from the homepage.

@app.route('/')
def show_home_page():
    """ Home page - displays all pets """
    pets = Pet.query.all()
    return render_template('base.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """ Add pet form """
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data if form.photo_url.data else ""
        age = form.age.data if form.age.data else ""
        notes = form.notes.data if form.notes.data else ""

        pet = Pet(name=name, species=species,
                  photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet.html', form=form)


@app.route('/<int:id>', methods=['GET', 'POST'])
def view_edit_pet(id):
    """ Show/Edit details about a pet """
    pet = Pet.query.get(id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        photo_url = form.photo.data
        notes = form.notes.data
        available = form.available.data

        pet.photo_url = photo_url
        pet.notes = notes
        pet.available = available
        db.session.commit()
        return redirect(f'/{id}')
    else:
        return render_template('edit_pet.html', form=form, pet=pet)
