class Contact: 

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def display(self):
        print(f"Name: {self.name}")
        print(f"\nPhone: {self.phone}")
        print(f"\nEmail: {self.email}")

class ContactBook:

    def __init__(self):
        self.contacts = []

    def add_contact(self, new_contact):
        self.contacts.append(new_contact)
        print(f"Contact {new_contact.name} Added.\n")

    def show_all_contacts(self): 

        if len(self.contacts) == 0:
            print("No contact is there.")

        else:        
            for contact in self.contacts:
                contact.display()
        

def main():

    book = ContactBook(new_contact)

    new_contact = Contact(name, phone, email)

    while True:

        print("==== CLI CONTACT BOOK ====\n")
        print("1. Add Contact")
        print("\n2. Show All Contacts")
        print("\n3. Exit")
        
        choice = int(input("\nEnter your choice (1-3): "))

        if choice == 1:
            name = input("Name: ")
            phone = input("\nPhone: ")
            email = input("\nEmail: ")

            book.add_contact(new_contact)
        
        elif choice == 2:
            book.show_all_contacts()

        elif choice == 3:
            print("Bye!\n")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
