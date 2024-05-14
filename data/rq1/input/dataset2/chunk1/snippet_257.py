#Source: https://stackoverflow.com/questions/46052925/python3-multiple-inheritance-typeerror-object-init-takes-no-parameters
class ContactList(list):
    def search(self, name):
        """Return all contacts that contain the search value
        in their name."""
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contacts = ContactList()

    def __init__(self, name="", email="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
        print("Cotact")


class AddressHolder:
    def __init__(self, street="", city="", state="", code="", **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code
        print("AddressHolder")


class Friend(Contact, AddressHolder):
    # case# 1
    # def __init__(self, phone="", **kwargs):
    #     self.phone = phone
    #     super().__init__(**kwargs)
    #     print("Friend")

    # case# 2
    def __init__(self, **kwargs):
        self.phone = kwargs["phone"]
        super().__init__(**kwargs)
        print("Friend")


if __name__ == "__main__":
    friend = Friend(
        phone="01234567",
        name="My Friend",
        email="myfriend@example.net",
        street="Street",
        city="City",
        state="State",
        code="0123")