from model.car import Car
from model.system_panel import SystemPanel
from model.customer import Customer

system = SystemPanel()
# car = Car(name="Honda",model="H242",year="2026",is_rented=False,id=1,price_per_day=19)
# print(system.car_service.cars)
# print(system.car_service.find_car(1))
# print(system.car_service.update_car(car_id=1,name="Honda",model="H245",year="2026",is_rented=False,price_per_day=22))
# print(system.car_service.cars)
# print(system.car_service.save_cars())
# print(system.car_service.remove_car(2))
# print(system.car_service.cars)
# print(system.car_service.save_cars())


customer = Customer(id=1,name="Osman",phone="2368102",identity="National Identity")

# system.customer_service.add_customer(name="Osman",phone="2368102",identity="National Identity")
# system.customer_service.add_customer(name="Ahmed",phone="760284",identity="Passport")

print(system.customer_service.customers)

print(system.customer_service.find_customer(1))

print(system.customer_service.remove_customer(1))

print(system.customer_service.update_customer(customer_id=2,identity="Document"))

print(system.customer_service.save_customers())

print(system.customer_service.customers)
