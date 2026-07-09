class Contact: 

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def display(self):
        print("\n" + "-" * 30)
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        print("-" * 30)

class ContactBook:

    def __init__(self):
        self.contacts = []

    def add_contact(self, new_contact):
        self.contacts.append(new_contact)
        print(f"\nContact {new_contact.name} Added.")

    def show_all_contacts(self): 

        if len(self.contacts) == 0:
            print("\nNo contact is there.")

        else:        
            for contact in self.contacts:
                contact.display()
        

def main():

    book = ContactBook()

    while True:

        print("\n==== CLI CONTACT BOOK ====")
        print("1. Add Contact")
        print("2. Show All Contacts")
        print("3. Exit")
        
        choice = int(input("\nEnter your choice (1-3): "))

        if choice == 1:
            name = input("\nName: ")
            phone = input("Phone: ")
            email = input("Email: ")

            new_contact = Contact(name, phone, email)

            book.add_contact(new_contact)
        
        elif choice == 2:
            book.show_all_contacts()

        elif choice == 3:
            print("\nBye!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
