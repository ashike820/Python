#Menu List
import restore_from_file
import view_contact
import add_contact
import remove_contact
contact_list = []
while True:
    print("Welcome to Contact Book Management System \n Enter any number for operate")
    print(" 1. View All Contact.")
    print(" 2. Add Contact. ")
    print(" 3. Remove Contact. ")
    print(" 4. Exit ")

    contact_list = restore_from_file.restore_from_file(contact_list)
    value = input("Enter Any Number : ")
    if value == "1":
        view_contact.view_contact(contact_list)
    elif value == "2":
        contact_list = add_contact.add_contact(contact_list)
    elif value == "3":
        remove_contact.remove_contact(contact_list)
    elif value == "4":
        print("Thanks For Using....")
        break
