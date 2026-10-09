"""
This program performs an initial verification of a vehicle purchase application.
When a customer wants to purchase a vehicle,
the program records the customer's information,
vehicle information, payment information, and document status.
The program use this information to determine whether 
the application should be **approved or rejected**.
"""


# Customer details
first_name = input("Please enter your Full name: ").strip().title()
surname = input("Please enter your Surname: ").strip()
id_number = int(input("Please enter your valid ID number: "))
amount_payed = int(input("How much are you paying for this vehicle: R"))

# Vehicle details
vehicle_make = "VW Tiguan"
vehicle_model = "R-Line 2026"
vehicle_registration = "PHG123FH GP"
vehicle_price = 420.0000