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

# Print the updated contacts list
print("Your contacts:")
for contact in my_contacts:
    contacts_json = json.dumps(contact, indent=4)
    print(contacts_json)
with open('contacts.html', 'w') as f:
    for contact in my_contacts:
        contacts_json = json.dumps(contact, indent=4)
        print('My Contacts are:', contact, file=f)