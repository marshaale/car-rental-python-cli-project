from model.system_panel import SystemPanel


def print_message(message: str = "---Back to System Panel---"):
    print(message, "\n")


def cars_option(system: SystemPanel):
    while True:
        prefix = "Cars->"
        print("1 Add 2 List 3 Update 4 Remove 0 Exit")
        user_pick = input("Pick: ").strip().lower()
        if user_pick == "2":
            print_message(f"----{prefix}List----")
            system.car_service.list_cars()
        if user_pick == "4":
            print_message(f"----{prefix}Remove----")
            car_id = int(input("Car id to remove: ").strip())
            if system.car_service.remove_car(car_id):
                print_message("Car removed successfully")
            else:
                print_message(f"Car with id: {car_id} does not not found")

        if user_pick == "0":
            system.car_service.save_cars()
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
