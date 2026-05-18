from model.car import Car
from services.car_service import CarService

car = Car(name="Honda",model="H242",year="2026",is_rented=False,id=1,price_per_day=19)
car_service = CarService()
car_service.save_cars([car,car])
cars = car_service.load_cars()
print(cars)