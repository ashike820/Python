from docutils.io import Input

from save_contact import save_contact

def add_contact(contact_list):
    while True:
        try:
            name = str(input("Enter Person Name :"))
            break
        except ValueError:
            print("Name Must be a string.")
    while True:
        try:
            email = str(input("Enter Person email :"))
            break
        except ValueError:
            print("Name Must be a string.")
    while True:
        try:
            phone_number = int(input("Enter Person Number :"))
            break
        except ValueError:
            print("Number Must be integer.")
    while True:
        try:
            address = str(input("Enter Person Address :"))
            break
        except ValueError:
            print("Address Must be a string.")


    contact = {
        "Name": name,
        "email" : email,
        "Phone Number" : phone_number,
        "Address" : address
    }
    if contact_list == []:
        contact_list.append(contact)
        save_contact(contact_list)
        print("Contact added Successfully")
    else:
        for i in contact_list:
            if int(i ["Phone Number"]) != int(phone_number) :
                contact_list.append(contact)
                save_contact(contact_list)
                print("Contact added Successfully")
                return contact_list

            else:
                print("Already Exist")
                break
