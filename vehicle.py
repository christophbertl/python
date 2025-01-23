import exp

class Vehicle:
    """
    Vehicle class with all parameters and methods to create a vehicle.
    """

    def __init__(self, color, seats, price, category, fuel, brand, model, number_plate):
        """
        Constructor to create a Vehicle with all necessary parameters.
        """

        self.__color = color
        self.__seats = seats
        self.__price = price
        self.__category = category
        self.__fuel = fuel
        self.__brand = brand
        self.__model = model
        self.__number_plate = number_plate
        self.__rented_by = None

    def show(self):
        """
        Returns string which describes this vehicle.
        """

        return self.__brand + " " + self.__model

    def get_number_plate(self):
        """
        """
        return self.__number_plate

    def rent(self, customer_id):
        """
        Rent vehicle by given customer ID.
        """

        if self.__rented_by is not None:
            raise exp.AlreadyRentedException()

        self.__rented_by = customer_id

    def show_available_vehicle(self):
        """
        Returns brand and model if not rentend.
        """

        if self.__rented_by is None:
            return self.show()

    def show_rented_vehicle(self):
        """
        Returns brand and model if rentend.
        """

        if self.__rented_by is not None:
            return self.show()

    def return_vehicle(self):
        """
        Remove customer ID from instance variables.
        """

        self.__rented_by = None


