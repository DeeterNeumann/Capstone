from sqlalchemy.orm import sessionmaker
from database.database_connection import engine
from model.car_t_therapies_model import CART

Session = sessionmaker(bind=engine)
session = Session()

def therapies():
    
    if session.query(CART).first() is not None:
        return
    
    therapies = [
        CART(car_t_cell = "tisagenlecleucel"),
        CART(car_t_cell = "axicabtagene ciloleucel"),
        CART(car_t_cell = "lisocabtagene maraleucel"),
        CART(car_t_cell = "brexucabtagene autoleucel"),
        CART(car_t_cell = "idecabtagene vicleucel"),
        CART(car_t_cell = "ciltacabtagene autoleucel")
    ]

    session.add_all(therapies)
    session.commit()