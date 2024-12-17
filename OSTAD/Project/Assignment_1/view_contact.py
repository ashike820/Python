import json

def view_contact (contact_list):
    with open("Contact_list.json", "r") as fp:
        contact_list = json.load(fp)

        if contact_list != []:
            for i in contact_list:
                print(f"Name:{i['Name']} | Email: {i['email']} | Phone Number: {i['Phone Number']} | Address : {i['Address']}")
        else:
            print("No Contact Found")