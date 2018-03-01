CONTACTS ={}

class Contacts(object):
    def __init__(self):
        self.name = ""
        self.phone = ""

    def Add_contact(self, name, phone):
        self.name = name
        self.phone = phone
        if self.name in CONTACTS:
            return " Contact already exists"
        CONTACTS[name]= {
            "name": self.name, 
            "phone": self.phone
        }
        return CONTACTS[name]

    def View_contact(self, name):
        """Uses name to get contact"""
        if name in CONTACTS :
            return CONTACTS[name]
        return "Contact does not exist"

    def Delete_contact(self, name):
        """deletes a contact from contacts"""
        if name in CONTACTS:
            CONTACTS.pop(name)
            return "Removed Successfully"
        return "Contact does not exist"


    def Update_contact(self, name, phone):
        """Updates contact details"""
        if name in CONTACTS:
            CONTACTS["phone"]= self.phone
            return "Contact Updated successfully"
        return "Contact does not exist"
        
            
