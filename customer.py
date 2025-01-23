class Customer:
    """
    Customer class with all parameters and methods to create a customer.
    """

    def __init__(self, name, surname, birthday, ID):
        """
        Constructor to create a customer with all necessary parameters.
        """

        self.__name = name
        self.__surname = surname
        self.__birthday = birthday
        self.__ID = ID

    def get_ID(self):
        """
        """

        return self.__ID
