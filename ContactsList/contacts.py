import json
#test

minimum_age = 30


def create_contact():
    my_contacts = []
    country = "usa"
    for i in range(2):
        user = input("Enter the name of the contact: ")
        age = int(input("Enter the age of the contact: "))
        address = input("Enter the address of the contact: ")
        phone = input("Enter the phone of the contact: ")

        new_contact = {
            "user": user,
            "age": age,
            "address": address,
            "phone": phone
        }
        new_contact.update({"country": country})
        if new_contact['age'] >= minimum_age:
            my_contacts.append(new_contact)
        else:
            print("The age", new_contact['age'], "is less than", minimum_age, ",Please change the age !")
    return my_contacts


def display_contacts(contacts):
    contacts_json = json.dumps(contacts, indent=4)
    with open('templates/contacts.html', 'w') as f:
        f.write('My Contacts are:\n')
        f.write(contacts_json)


def main():
    my_contacts = create_contact()
    display_contacts(my_contacts)


if __name__ == "__main__":
    main()
