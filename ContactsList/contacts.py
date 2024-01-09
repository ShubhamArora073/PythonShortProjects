import json


def add_contact(user, age, address, phone, country):
    new_contact = {
        "user": user,
        "age": age,
        "address": address,
        "phone": phone
    }
    new_contact.update({"country": country})
    my_contacts.append(new_contact)
    return my_contacts

# Initialize an empty contacts list
my_contacts = []

# Loop to add three contacts
for i in range(2):
    # Get contact information from the user
    user = input("Enter the name of the contact: ")
    age = int(input("Enter the age of the contact: "))
    address = input("Enter the address of the contact: ")
    phone = int(input("Enter the phone of the contact: "))
    country = input("Enter the country: ")

    # Add a new contact
    my_contacts = add_contact(user, age, address, phone, country)
#
# for contact in my_contacts:
#     if contact["age"] > 30:
#         contacts_json = json.dumps(contact, indent=2)
#         print("Here are your contacts:")
#         print(contacts_json)

# Write the JSON string to the file
with open('contacts.html', 'w') as f:
    f.write('My Contacts are:\n')
    for contact in my_contacts:
        if contact["age"] > 30:
            contacts_json = json.dumps(contact, indent=2)
            f.write(contacts_json)





