"""
Autovermietung
Menü:
- Anlegen eines Fahrzeugs
- Anzeigen von allen Autos im Bestand
- Vermieten eines Fahrzeugs
- Anlegen eines Kunden
- Fahrzeugrückgabe
"""

# imports
import time
import os
import vehicle
import customer
import exp

def get_vehicle_by_number_plate(number_plate: str) -> vehicle.Vehicle:
    """
    Returns the vehicle object which matches with the given number plate.
    """

    for vehicle in vehicle_list:
        if vehicle.get_number_plate() == number_plate:
            return vehicle

    return None

def get_customer_by_id(id: str) -> customer.Customer:
    """
    Returns the customer object which matches the given id.
    """

    for c in customer_list:
        if id == c.get_ID():
            return c

    return None


def display_error_message(error_key: str):
    """
    Function displays an error message for the given error key.
    """

    error_messages = {
        'wrong_user_input': 'Ungültige Eingabe, bitte versuchen Sie es erneut.',
        'user_already_exist': 'Dieser Nutzer existiert bereits.',
        'vehicle_already_exists': 'Dieses Fahrzeug existiert bereits',
        'vehicle_already_rented': 'Dieses Fahrzeug ist bereits vermietet.'
    }

    print(error_messages[error_key])


# functions
def show_menu():
    """
    Function to display the menu on the screen and get user input.
    """

    # print menu
    print("""1 - neues Fahrzeug anlegen
    2 - Bestand anzeigen
    3 - Fahrzeug vermieten
    4 - Kunden anlegen
    5 - Fahrzeugrückgabe
    6 - Beenden""")
    print("Auswahl:")

    # get user decision
    user_input = input()

    # clear screen before start working outside main menu
    os.system('cls')

    try:
        user_input = int(user_input)
    except ValueError as e:
        display_error_message('wrong_user_input')

    return user_input

def create_vehicle() -> vehicle.Vehicle:
    """
    Function to create a new vehicle object and add it to the
    list of available vehicles.
    """

    print("Farbe: ")
    color = input()
    print("Anzahl der Sitze: ")
    seats = input()
    print("Mietpreis: ")
    price = input()
    print("Fahrzeugkategorie: ")
    category = input()
    print("Kraftstoff: ")
    fuel = input()
    print("Marke: ")
    brand = input()
    print("Modell: ")
    model = input()
    print("Kennzeichen: ")
    number_plate = input()

    if get_vehicle_by_number_plate(number_plate) is not None:
        raise exp.SameIDException()

    return vehicle.Vehicle(color, seats, price,category, fuel, brand, model, \
                           number_plate)

def show_available_vehicles():
    """
    Function to show which vehicles are available at the moment.
    """

    for vehicle in vehicle_list:
        print(vehicle.show_available_vehicle())

def show_rented_vehicles():
    """
    Function to show which vehicles are rented at the moment.
    """

    for vehicle in vehicle_list:
        print(vehicle.show_rented_vehicle())

def rent_vehicle():
    """
    Function to rent a vehicle and to remove it from the lsit of
    available vehicles. Add it to list of rented vehicles.
    """

    try:
        print("ID des Kunden: ")
        id = input()

        if get_customer_by_id(id) is None:
            raise exp.CustomerNotFoundException()

        print("Kennzeichen des Fahrzeugs: ")
        number_plate = input()

        vehicle = get_vehicle_by_number_plate(number_plate)
        if vehicle is None:
            raise exp.VehicleNotAvailable()
        vehicle.rent(id)

    except exp.AlreadyRentedException:
        display_error_message('vehicle_already_rented')

    except (exp.VehicleNotAvailable, exp.CustomerNotFoundException):
        display_error_message('wrong_user_input')

def create_customer():
    """
    Create a customer object and add it to the list of customers.
    """

    print("Name: ")
    name = input()
    print("Vorname: ")
    surname = input()
    print("Gebutsdatum: ")
    birthday = input()
    print("ID: ")
    id = input()

    if get_customer_by_id(id) is not None:
        raise exp.SameIDException()

    return customer.Customer(name, surname, birthday, id)

def return_vehicle():
    """
    Remove the vehicle from the list of rented vehicles and add it to
    list of available vehicles.
    """

    print('Kennzeichen')
    number_plate = input()

    try:
        vehicle = get_vehicle_by_number_plate(number_plate)
        if vehicle is None:
            raise exp.VehicleNotAvailable()

        vehicle.return_vehicle()

    except exp.VehicleNotAvailable:
        display_error_message('wrong_user_input')

if __name__ == "__main__":

    vehicle_list = list()
    customer_list = list()


    # menu / navigation
    while True:

        user_input = show_menu()

        # create new vehicle
        if user_input == 1:
            print("--- Fahrzeug anlegen ---")
            try:
                vehicle_list.append(create_vehicle())

            except exp.SameIDException:
                display_error_message('vehicle_already_exists')

        # show all available vehicles
        elif user_input == 2:
            print("--- Bestand anzeigen ---")
            print('verfügbar:')
            show_available_vehicles()
            print('vermietet')
            show_rented_vehicles()

        # rent a vehicle
        elif user_input == 3:
            print("--- Fahrzeug vermieten ---")
            rent_vehicle()

        # create new customer
        elif user_input == 4:
            print("--- Kunden anlegen ---")
            try:
                customer_list.append(create_customer())

            except exp.SameIDException:
                display_error_message('user_already_exist')

        # return a vehicle
        elif user_input == 5:
            print("--- Fahrzeug zurückgeben ---")
            return_vehicle()

        # exit program
        elif user_input == 6:
            print("--- Beenden ---")
            time.sleep(2)
            break
