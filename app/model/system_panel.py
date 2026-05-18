from services.car_service import CarService

class SystemPanel:
    def __init__(self) -> None:
        self.car_service = CarService()
        self.car_service.load_cars()
