import json


def add_contact(user, age, address, phone):
    new_contact = {
        "user": user,
        "age": age,
        "address": address,
        "phone": phone
    }
    my_contacts.append(new_contact)
    return my_contacts


# Initialize an empty contacts list
my_contacts = []

# Loop to add three contacts
for i in range(2):
    # Get contact information from the user
    user = input("Enter the name of the contact: ")
    age = input("Enter the age of the contact: ")
    address = input("Enter the address of the contact: ")
    phone = input("Enter the phone of the contact: ")

    # Add a new contact
    my_contacts = add_contact(user, age, address, phone)

# Convert the list of contacts to a JSON string
contacts_json = json.dumps(my_contacts, indent=4)

# Write the JSON string to the file
with open('contacts.html', 'w') as f:
    f.write('My Contacts are:\n')
    f.write(contacts_json)