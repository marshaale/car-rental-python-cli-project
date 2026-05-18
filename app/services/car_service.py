from model.car import Car
from core.config import CARS_FILE_PATH
from utils.utils import is_header_line


class CarService:
    def __init__(self) -> None:
        self.cars_file_header = f"id,name,model,year,price_per_day,is_rented"
        self.encoding = "utf-8"
        self.cars = []

    def load_cars(self) -> list[Car]:
        try:
            cars = []
            with open(CARS_FILE_PATH, "r", encoding=self.encoding) as file:
                for line in file.readlines():
                    raw = line.strip("\n").strip()
                    if raw is None:
                        continue

                    print(raw)
                    print(
                        f"Is header file",
                        is_header_line(line=raw, lookup=self.cars_file_header),
                    )
                    if is_header_line(line=raw, lookup=self.cars_file_header):
                        continue

                    [id, name, model, year, price_per_day, is_rented] = raw.split(",")
                    cars.append(
                        Car(
                            id=int(id),
                            name=name,
                            model=model,
                            year=year,
                            price_per_day=float(price_per_day),
                            is_rented=bool(is_rented),
                        )
                    )
            self.cars = cars
            return cars
        except FileNotFoundError as e:
            print(e)
            return []

    def save_cars(self) -> bool:
        try:
            with open(CARS_FILE_PATH, "w", encoding=self.encoding) as file:
                file.write(self.cars_file_header)
                for car in self.cars:
                    file.write(
                        f"\n{car.id},{car.name},{car.model},{car.year},{car.price_per_day},{car.is_rented}"
                    )
            return True
        except Exception as e:
            print(str(e))
            return False

    def find_car(self, car_id: int) -> Car | None:
        try:
            for car in self.cars:
                if car.id == car_id:
                    return car
            return None
        except Exception as e:
            print(str(e))
            return None

    def add_car(
        self, *, name: str, model: str, year: str, price_per_day: float
    ) -> bool:
        try:
            car = Car(
                id=len(self.cars) + 1,
                name=name,
                model=model,
                year=year,
                price_per_day=price_per_day,
                is_rented=False,
            )
            self.cars.append(car)
            return True
        except Exception as e:
            print(str(e))
            return False

    def update_car(
        self,
        *,
        car_id: int,
        name: str,
        model: str,
        year: str,
        price_per_day: float,
        is_rented: bool,
    ) -> bool:
        try:
            car = self.find_car(car_id)
            if not car:
                return False
            car.name = name
            car.model = model
            car.year = year
            car.price_per_day = price_per_day
            car.is_rented = is_rented
            return True
        except Exception as e:
            print(str(e))
            return False

    def remove_car(self, car_id: int) -> bool:
        try:

            for index, value in enumerate(self.cars):
                if value.id == car_id:
                    del self.cars[index]
                    return True

            return False
        except Exception as e:
            print(str(e))
            return False
