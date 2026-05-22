from model.system_panel import SystemPanel


def print_message(message: str = "---Back to System Panel---"):
    print(message, "\n")


def validate_id_value(id_value: str, prefix: str = "Customer") -> bool:
    if not id_value:
        print(f"{prefix} id is required")
        return False

    if not id_value.isnumeric():
        print(f"{prefix} id must be numeric")
        return False

    return True


def cars_option(system: SystemPanel):
    prefix = "Cars->"
    while True:
        print(f"\n{prefix}")
        print("1 Add 2 List 3 Update 4 Remove 0 Exit")
        user_pick = input("Pick: ").strip().lower()
        if user_pick == "1":
            print_message(f"----{prefix}Add----")
            car_name = input("Car name: ").strip()
            car_model = input("Car model: ").strip()
            car_year = input("Car year: ").strip()
            car_price_per_day = input("Car price per day: ").strip()
            if not car_name or not car_model or not car_year or not car_price_per_day:
                print_message("All fields are required")
                continue
            system.car_service.add_car(
                name=car_name,
                model=car_model,
                year=car_year,
                price_per_day=float(car_price_per_day),
            )

        if user_pick == "2":
            print_message(f"----{prefix}List----")
            system.car_service.list_cars()

        if user_pick == "3":
            print_message(f"----{prefix}Update----")
            car_id = input("Car id: ").strip()
            if not validate_id_value(car_id, "Car"):
                continue

            print("Hint: Leave blank to skip updating a field")
            car_name = input("Car name: ").strip()
            car_model = input("Car model: ").strip()
            car_year = input("Car year: ").strip()
            car_price_per_day = input("Car price per day: ").strip()

            if system.car_service.update_car(
                car_id=int(car_id),
                name=car_name,
                model=car_model,
                year=car_year,
                price_per_day=(
                    None if not car_price_per_day else float(car_price_per_day)
                ),
            ):
                print_message("Car updated successfully")
            else:
                print_message(f"Car with id: {car_id} does not found")

        if user_pick == "4":
            print_message(f"----{prefix}Remove----")
            car_id = input("Car id to remove: ").strip()

            if not validate_id_value(car_id, "Car"):
                continue

            if system.car_service.remove_car(int(car_id)):
                print_message("Car removed successfully")
            else:
                print_message(f"Car with id: {car_id} does not found")

        if user_pick == "0":
            system.car_service.save_cars()
            print_message()
            break


def customers_option(system: SystemPanel):
    prefix = "Customers->"
    while True:
        print(f"\n{prefix}")
        print("1 Add 2 List 3 Update 4 Remove 0 Exit")
        user_pick = input("Pick: ")

        if user_pick == "1":
            print_message(f"{prefix}Add")
            customer_name = input("Customer name: ")
            customer_phone = input("Customer phone: ")
            customer_identity = input(
                "Customer identity eg (passport,national identity): "
            )

            if not customer_name or not customer_phone or not customer_identity:
                print_message("All fields are required")
                continue

            system.customer_service.add_customer(
                name=customer_name, phone=customer_phone, identity=customer_identity
            )

        if user_pick == "2":
            print_message(f"{prefix}List")
            system.customer_service.list_customers()

        if user_pick == "3":
            print_message(f"{prefix}Update")
            customer_id = input("Customer id you want to update: ").strip()
            if not validate_id_value(customer_id):
                continue

            print("Hint: Leave blank to skip updating a field")
            customer_name = input("Customer name: ")
            customer_phone = input("Customer phone: ")
            customer_identity = input(
                "Customer identity eg (passport,national identity): "
            )

            if system.customer_service.update_customer(
                customer_id=int(customer_id),
                name=customer_name,
                phone=customer_phone,
                identity=customer_identity,
            ):
                print_message("Customer updated successfully")
            else:
                print_message(f"Customer with id: {customer_id} does not found")

        if user_pick == "4":
            customer_id = input("Customer id you want to remove: ").strip()

            if not validate_id_value(customer_id):
                continue

            confirmation = (
                input(
                    f"Are you sure you want to remove customer id {customer_id} y/n: "
                )
                .strip()
                .lower()
            )

            if confirmation == "yes" or confirmation == "y":
                if system.customer_service.remove_customer(int(customer_id)):
                    print_message("Customer updated successfully")
                else:
                    print_message(f"Customer with id: {customer_id} does not found")

        if user_pick == "0":
            system.customer_service.save_customers()
            print_message()
            break


def main():
    system = SystemPanel()
    while True:
        try:
            print("1 Cars 2 Customers 3 Rents 101: Save 0 Exit")
            user_pick = input("Pick: ").strip().lower()
            if user_pick == "1":
                cars_option(system)

            if user_pick == "2":
                customers_option(system)

            if user_pick == "101":
                system.save_state()

            if user_pick == "0":
                print_message("Good bye")
                break
        except Exception as e:
            print("System exception: ", str(e))
        finally:
            # system.save_state()
            pass


if __name__ == "__main__":
    main()
