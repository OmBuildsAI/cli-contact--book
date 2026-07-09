class Contact:
    """Ek single contact ko represent karta hai"""
    
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        print("-" * 30)
    

class ContactBook:
    """Saare contacts ko manage karta hai"""
    
    def __init__(self):
        self.contacts = []  # abhi ke liye list mein store karenge (memory mein)
    
    def add_contact(self, name, phone, email):
        if name.strip() == "":
            print("\n❌ Naam khaali nahi ho sakta!\n")
            return
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        print(f"\n✅ Contact '{name}' add ho gaya!\n")
    
    def show_all_contacts(self):
        if len(self.contacts) == 0:
            print("\nAbhi koi contact nahi hai.\n")
            return
        print(f"\n--- Total Contacts: {len(self.contacts)} ---")
        for index, contact in enumerate(self.contacts, start=1):
            print(f"\n[{index}]")
            contact.display()
    
    def search_contact(self, keyword):
        keyword = keyword.strip().lower()
        results = []
        
        for contact in self.contacts:
            if keyword in contact.name.lower():
                results.append(contact)
        
        if len(results) == 0:
            print(f"\n❌ '{keyword}' se koi contact nahi mila.\n")
        else:
            print(f"\n--- {len(results)} contact(s) mile ---")
            for contact in results:
                contact.display()


def main():
    book = ContactBook()
    
    while True:
        print("\n===== CLI CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. Show All Contacts")
        print("3. Search Contact")
        print("4. Exit")
        
        choice = input("Apna choice enter karo (1-3): ")
        
        if choice == "1":
            name = input("Naam: ")
            phone = input("Phone number: ")
            email = input("Email: ")
            book.add_contact(name, phone, email)
        
        elif choice == "2":
            book.show_all_contacts()

        elif choice == "3":
            keyword = input("Naam se search karo: ")
            book.search_contact(keyword)
        
        elif choice == "4":
            print("Bye! 👋")
            break
        
        else:
            print("Galat choice, dobara try karo.")


if __name__ == "__main__":
    main()


