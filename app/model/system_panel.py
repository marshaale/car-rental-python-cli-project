from services.car_service import CarService
from services.customer_service import CustomerService

class SystemPanel:
    def __init__(self) -> None:
        self.car_service = CarService()
        self.car_service.load_cars()
        self.customer_service = CustomerService()
        self.customer_service.load_customers()
