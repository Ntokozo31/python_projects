"""
This program performs an initial verification of a vehicle purchase application.
When a customer wants to purchase a vehicle,
the program records the customer's information,
vehicle information, payment information, and document status.
The program use this information to determine whether 
the application should be **approved or rejected**.
"""


# Customer details
first_name = input("Please enter your First name: ").strip().title()
surname = input("Please enter your Surname: ").strip().title()
id_number = input("Please enter your valid ID number: ").strip()
amount_payed = float(input("How much are you paying for this vehicle: R"))

# Vehicle details
vehicle_make = "VW Tiguan"
vehicle_model = "R-Line 2026"
vehicle_registration = "PHG123FH GP"
vehicle_price = 4200000

# Document status
document_status = input("Please enter document status: (Valid/Invalid): ").lower()

# Document verification
if not first_name or not surname or not id_number:
    document_status = "invalid"
    application_status = "Application Rejected"
    reason = "Please make sure all fields are filled."

elif len(id_number) != 13 or not id_number.isdigit():
    document_status = "invalid"
    application_status = "Application Rejected"
    reason = "Invalid customer ID number Please enter your 13 Valid ID number"

# Payment verificarion
elif document_status == "valid" and amount_payed >= vehicle_price:
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
if reason == "Insufficient payment" or reason == "Please make sure all fields are filled." or reason == "Invalid customer ID number Please enter your 13 Valid ID number":
    print(f"We're sorry {first_name} {surname}")
else:
    print(f"***Congratulation*** {first_name} {surname} on your new ride {vehicle_make} {vehicle_model}")

print("*******************************************")

