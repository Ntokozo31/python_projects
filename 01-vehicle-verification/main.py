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
surname = input("Please enter your Surname: ").strip().title()
id_number = input("Please enter your valid ID number: ").strip()
amount_payed = int(input("How much are you paying for this vehicle: R"))

# Vehicle details
vehicle_make = "VW Tiguan"
vehicle_model = "R-Line 2026"
vehicle_registration = "PHG123FH GP"
vehicle_price = 4200000

# Document status
document_status = "Valid"

# Document verification
if len(id_number) < 13 and document_status == "Valid":
    document_status = "Invalid"
    reason = "Custormer Documents"
    application_status = "Application Rejected"

# Payment verificarion
elif document_status == "Valid" and amount_payed >= vehicle_price:
    application_status = "Application Approved"
    reason = "Documents are valid and amount paid is sufficient"
else:
    application_status = "Rejected"
    reason = "Insufficient payment"


#Print Final report
print("=================Final Report=============")
print(f"Full name: {first_name} {surname}")
print(f"ID Number: {id_number}")
print(f"Vehicle make: {vehicle_make}")
print(f"Vehicle Model: {vehicle_model}")
print(f"Vehicle registration: {vehicle_registration}")
print(f"Vehicle price: {vehicle_price}")
print(f"Amount payed: {amount_payed}")
print(f"Document Status: {document_status}")
print(f"Application Status: {application_status}")
print(f"Reason: {reason}")
print("=========================================\n")

print("*******************************************")

# Message from dealership
if reason == "Insufficient payment" or reason == "Custormer Documents":
    print(f"We're sorry {first_name} {surname} please try again after 3 months")
else:
    print(f"***Congratulation*** {first_name} {surname} on your new ride {vehicle_make} {vehicle_model}")

print("*******************************************")

