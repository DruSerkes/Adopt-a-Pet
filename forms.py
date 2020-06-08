from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.fields.html5 import URLField
from wtforms.validators import InputRequired, Optional, AnyOf, NumberRange


class PetForm(FlaskForm):
    name = StringField("Pet Name", validators=[
                       InputRequired(message="Enter a name for your pet")])
    species = StringField("Species", validators=[
                          InputRequired(message="Enter a species for your pet"), AnyOf(['Dog', 'Cat', 'Porcupine'], message="Species must be either 'Dog' 'Cat' or 'Porcupine'")])
    photo_url = URLField('Image URL', validators=[Optional()])
    age = IntegerField("Pet Age", validators=[Optional(), NumberRange(
        min=0, max=30, message="Age must be between 0 and 30")])
    notes = StringField("Anything else we should know?",
                        validators=[Optional()])
