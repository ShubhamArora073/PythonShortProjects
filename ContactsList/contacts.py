import json
import pathlib
import boto3
import os

def create_contact():
    try:
        minimum_age = 30
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
    except Exception as e:
        print(e)
def display_contacts(contacts):
    try:
        contacts_json = json.dumps(contacts, indent=4)
        with open('templates/contacts.json', 'w') as f:
            f.write(contacts_json)
    except Exception as e:
        print(e)

def upload_file_s3():
    try:
        s3 = boto3.client("s3")
        bucket_name = "contacts-demo-shubham"
        object_name = "contacts.json"
        file_name = os.path.join(pathlib.Path(__file__).parent.resolve(), "templates/contacts.json")
        response = s3.upload_file(file_name, bucket_name, object_name)
        print(response)
    except Exception as e:
        print(e)
def main():
    my_contacts = create_contact()
    display_contacts(my_contacts)
    upload_file_s3()


if __name__ == "__main__":
    main()
