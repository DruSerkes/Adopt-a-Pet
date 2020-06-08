from models import db, Pet
from app import app


# Create all tables
db.drop_all()
db.create_all()

# Create pets

p1 = Pet(name='Woofer', species='Dog',
         photo_url="https://images.radio.com/aiu-media/GettyImages1061822700-eb517cd2-387f-4448-ab1b-759627ede846.jpg?width=800", age='2', notes="He loves to play")
p2 = Pet(name='Meowth', species='Cat', photo_url="https://i.pinimg.com/originals/98/2a/b6/982ab66f09a7cc30332ebd73cb4ab4fc.png",
         age='4', notes="He's a literal pokemon")
p3 = Pet(name='Spike', species='Porcupine',
         photo_url="https://i.ytimg.com/vi/ZphlCdI2yqA/maxresdefault.jpg")

db.session.add_all([p1, p2, p3])
db.session.commit()
