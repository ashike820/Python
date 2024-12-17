import json

def save_contact(contact_list):
    with open("Contact_list.json","w") as fp:
        json.dump(contact_list,fp)
