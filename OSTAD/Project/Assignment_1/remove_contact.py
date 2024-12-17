import save_contact

def remove_contact(contact_list):
    contact = int(input("Enter number which you want to remove"))
    for i in contact_list:
        if i ["Phone Number"] == contact:
            contact_list.remove(i)
            save_contact.save_contact(contact_list)
            print("Contact Removed")
            return contact_list
        else:
            print("Contact not found")