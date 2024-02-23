#!/usr/bin/python3
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

if __name__ == "__main__":
    bm = BaseModel()
    bm.save()

    user = User()
    user.save()

    state = State()
    state.save()

    city = City()
    city.save()

    place = Place()
    place.save()

    amenity = Amenity()
    amenity.save()

    review = Review()
    review.save()

    storage.save()
