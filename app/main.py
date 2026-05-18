from model.car import Car
from model.system_panel import SystemPanel

car = Car(name="Honda",model="H242",year="2026",is_rented=False,id=1,price_per_day=19)
system = SystemPanel()
print(system.car_service.cars)
print(system.car_service.find_car(1))
print(system.car_service.update_car(car_id=1,name="Honda",model="H245",year="2026",is_rented=False,price_per_day=22))
print(system.car_service.cars)
print(system.car_service.save_cars())
print(system.car_service.remove_car(2))
print(system.car_service.cars)
print(system.car_service.save_cars())
