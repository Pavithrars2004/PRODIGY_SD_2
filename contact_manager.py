import csv
from contact import Contact

class ContactManager:
    def __init__(self, filename='contacts.csv'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        contacts = []
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    contacts.append(Contact(*row))
        except FileNotFoundError:
            pass
        return contacts

    def save_contacts(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for contact in self.contacts:
                writer.writerow([contact.name, contact.phone, contact.email])

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        self.save_contacts()

    def view_contacts(self):
        return self.contacts

    def edit_contact(self, index, name, phone, email):
        if 0 <= index < len(self.contacts):
            self.contacts[index].name = name
            self.contacts[index].phone = phone
            self.contacts[index].email = email
            self.save_contacts()
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            self.save_contacts()
        else:
            print("Invalid contact index.")
