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

# print(system.customer_service.customers)

# print(system.customer_service.find_customer(1))

# print(system.customer_service.remove_customer(1))

# print(system.customer_service.update_customer(customer_id=2,identity="Document"))

# print(system.customer_service.save_customers())

# print(system.customer_service.customers)

system.car_rent_service.add_car_rent(car_id=1,customer_id=2,num_of_days=15,base_price=21,payment_type="Pre Payment")
system.car_service.update_car(car_id=1,is_rented=True)
system.car_rent_service.save_rent_cars()
print(system.car_rent_service.customer_car_rents)
print(system.car_rent_service.find_rent_car(1))
system.car_service.update_car(car_id=1,is_rented=False)
system.car_rent_service.update_rent_car(customer_car_rent_id=1,status="return_due_to_issue")
print(system.car_rent_service.customer_car_rents)
print(system.car_rent_service.remove_rent_car(2))
system.car_rent_service.save_rent_cars()