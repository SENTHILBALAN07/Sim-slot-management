class Sim:
    def __init__(self, operator, band_width, price):
        self.operator = operator
        self.band_width = band_width
        self.price = price

    def get_operator(self):
        return self.operator

    def get_band_width(self):
        return self.band_width

    def get_price(self):
        return self.price

    def details_of_sim(self):
        print("Operator:", self.get_operator())
        print("Band Width:", self.get_band_width())
        print("Price:", self.get_price())
        print("--------------------------")


class Mobile:
    def __init__(self, name, ram, price):
        self.name = name
        self.ram = ram
        self.price = price
        self.slot = None

    def insert_sim(self, sim):
        if self.is_slot_empty():
            self.slot = sim
            print("\t\t\t" + self.slot.get_operator() + " Added")
        else:
            print("\t\t\t" + self.slot.get_operator() + " Already sim exists")

    def remove_sim(self):
        if self.is_slot_empty():
            print("\t\t\tAlready Sim Removed")
        else:
            print("\t\t\t" + self.slot.get_operator() + " Removed")
            self.slot = None

    def is_slot_empty(self):
        return self.slot is None

    def details_of_mobile(self):
        print("Name:", self.get_name())
        print("Price:", self.get_price())
        print("RAM:", self.get_ram())

    def get_name(self):
        return self.name

    def get_ram(self):
        return self.ram

    def get_price(self):
        return self.price


def main():
    my_sim = Sim("Jio", "5g", 600)
    my_mobile = Mobile("Nokia", "8GB", 40000)

    while True:
        print("\n\t\t\tSim Tracker")
        print("\t\t\t-------------")
        print("1. Add Sim")
        print("2. Remove Sim")
        print("3. Is Slot Empty")
        print("4. Details Of Mobile")
        print("5. Details Of Sim")
        print("6. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("\t\t\tInvalid Input")
            continue

        if choice == 1:
            my_mobile.insert_sim(my_sim)
        elif choice == 2:
            my_mobile.remove_sim()
        elif choice == 3:
            print("\t\t\tYes" if my_mobile.is_slot_empty() else "\t\t\tNo")
        elif choice == 4:
            my_mobile.details_of_mobile()
        elif choice == 5:
            my_sim.details_of_sim()
        elif choice == 6:
            print("\t\t\t---Thank You---")
            break
        else:
            print("\t\t\tInvalid Choice")


if __name__ == "__main__":
    main()
