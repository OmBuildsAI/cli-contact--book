class Contact:
    
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def display(self):
        print("\n" + "-" * 30)
        print(f"Name: {self.name}")
        print(f"Phone Number: {self.phone}")
        print(f"Email ID: {self.email}")

   
class ContactBook:
    
    def __init__(self):
        self.contacts = []

    def add_contact(self, new_contact):
        self.contacts.append(new_contact)
    
    def show_all_contacts(self):
        print(f"\nTotal Contacts: {len(self.contacts)}")
        for contact in self.contacts:
            contact.display()


def main():
    book = ContactBook()

    while True:
        print("\n==== CLI CONTACT BOOK ====")
        print("1. Add Contact")
        print("2. Show all Contacts")
        print("3. Exit")

        choice = int(input("\nEnter choice (1-3): "))

        if choice == 1:
            name = input("\nName: ")
            phone = input("Phone Number: ")
            email = input("Email ID: ")

            new_contact = Contact(name, phone, email)
            
            book.add_contact(new_contact)
            print(f"\nContact {new_contact.name} Added!")

        elif choice == 2:
            book.show_all_contacts()

        elif choice == 3:
            print("\nBye!")
            break

        else:
            print("\nInvalid choice!")

    
if __name__ == "__main__":
    main()

