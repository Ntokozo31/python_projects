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
amount_paid = float(input("How much are you paying for this vehicle: R"))

# Vehicle details
vehicle_make = "VW Tiguan"
vehicle_model = "R-Line 2026"
vehicle_registration = "PHG123FH GP"
vehicle_price = 4200000

# Document status
document_status = input("Please enter document status: (Valid/Invalid): ").lower().strip()

# Application status
rejected = "Rejected"
approved = "Approved"


# Application reasons
insufficient_payment = "Insufficient payment"
unrecognized_status = "Unrecognized status"
fields = "All fields must be filled."
invalid_doc = "Invalid documents"
app_approved = "Application has been Approved"
invalid_id = "Please enter a valid 13-digit ID number."


# Document verification
if not first_name or not surname or not id_number:
    document_status = "invalid"
    application_status = rejected
    reason = fields
elif len(id_number) != 13 or not id_number.isdigit():
    document_status = "invalid"
    application_status = rejected
    reason = invalid_id
elif document_status not in ["valid", "invalid"]:
    application_status = rejected
    reason = unrecognized_status
elif document_status == "invalid":
    application_status = rejected
    reason = invalid_doc

# Payment verificarion
elif document_status == "valid" and amount_paid > vehicle_price:
    application_status = approved
    reason = app_approved
elif document_status == "valid" and amount_paid < vehicle_price:
    application_status = rejected
    reason = insufficient_payment
elif document_status == "valid" and amount_paid == vehicle_price:
    application_status = approved
    reason = app_approved


#Print Final report
print("=================Final Report=============")
print(f"Full name: {first_name} {surname}")
print(f"ID Number: {id_number}")
print(f"Vehicle make: {vehicle_make}")
print(f"Vehicle Model: {vehicle_model}")
print(f"Vehicle registration: {vehicle_registration}")
print(f"Vehicle price: {vehicle_price}")
print(f"Amount paid: {amount_paid}")
print(f"Document Status: {document_status}")
print(f"Application Status: {application_status}")
print(f"Reason: {reason}")
print("=========================================\n")

print("*******************************************")

# Message from dealership
if reason == insufficient_payment or reason == unrecognized_status or reason == fields or reason == invalid_doc or reason == invalid_id:
    print(f"We're sorry {first_name} {surname}")
elif reason == app_approved:
    print(f"***Congratulation*** {first_name} {surname} on your new ride {vehicle_make} {vehicle_model}")

print("*******************************************")

