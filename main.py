import streamlit as st
from contact_manager import ContactManager

def main():
    st.title("Contact Management System")

    manager = ContactManager()

    menu = ["Add Contact", "View Contacts", "Edit Contact", "Delete Contact"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Contact":
        st.subheader("Add a New Contact")
        name = st.text_input("Name")
        phone = st.text_input("Phone Number")
        email = st.text_input("Email Address")
        if st.button("Add Contact"):
            if name and phone and email:
                manager.add_contact(name, phone, email)
                st.success(f"Contact {name} added successfully!")
            else:
                st.error("Please enter all details.")

    elif choice == "View Contacts":
        st.subheader("View All Contacts")
        contacts = manager.view_contacts()
        if contacts:
            for i, contact in enumerate(contacts):
                st.write(f"{i}. {contact}")
        else:
            st.write("No contacts available.")

    elif choice == "Edit Contact":
        st.subheader("Edit a Contact")
        index = st.number_input("Enter contact index to edit", min_value=0, step=1)
        name = st.text_input("New Name")
        phone = st.text_input("New Phone Number")
        email = st.text_input("New Email Address")
        if st.button("Edit Contact"):
            if name and phone and email:
                manager.edit_contact(index, name, phone, email)
                st.success(f"Contact at index {index} updated successfully!")
            else:
                st.error("Please enter all details.")

    elif choice == "Delete Contact":
        st.subheader("Delete a Contact")
        index = st.number_input("Enter contact index to delete", min_value=0, step=1)
        if st.button("Delete Contact"):
            manager.delete_contact(index)
            st.success(f"Contact at index {index} deleted successfully!")

if __name__ == '__main__':
    main()
