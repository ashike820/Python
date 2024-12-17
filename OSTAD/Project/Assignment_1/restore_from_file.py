import json
def restore_from_file(contact_list):
    with open("Contact_list.json", "r") as fp:
        contact_list = json.load(fp)
    return contact_list