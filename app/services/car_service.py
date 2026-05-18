from model.car import Car
from core.config import CARS_FILE_PATH
from utils.utils import is_header_line


class CarService:
    def __init__(self) -> None:
        self.cars_file_header = f"id,name,model,year,price_per_day,is_rented"
        self.encoding = "utf-8"

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
            return cars
        except FileNotFoundError as e:
            print(e)
            return []

    def save_cars(self, cars: list[Car]) -> bool:
        try:
            with open(CARS_FILE_PATH, "w", encoding=self.encoding) as file:
                file.write(self.cars_file_header)
                for car in cars:
                    file.write(
                        f"\n{car.id},{car.name},{car.model},{car.year},{car.price_per_day},{car.is_rented}"
                    )
            return True
        except Exception as e:
            print(str(e))
            return False
