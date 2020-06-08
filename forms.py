from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.fields.html5 import URLField
from wtforms.validators import InputRequired, Optional


class PetForm(FlaskForm):
    name = StringField("Pet Name", validators=[
                       InputRequired(message="Enter a name for your pet")])
    species = StringField("Species", validators=[
                          InputRequired(message="Enter a species for your pet")])
    photo_url = URLField('Image URL', validators=[Optional()])
    age = IntegerField("Pet Age", validators=[Optional()])
    notes = StringField("Anything else we should know?",
                        validators=[Optional()])
