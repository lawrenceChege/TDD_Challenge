"""
This test contains tests for adding contacts, updating, delete and view contacts"""
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
inspect.getfile(inspect.currentframe())))
parentdir =os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from unittest import TestCase
from app.phonebook import Contacts, CONTACTS 


CONTACT = Contacts()

class ContactsTestCase(TestCase):
    """ consists of tests for contact"""
    def setUp(self):
        """tests for set up"""
        #clear the dictionary
        CONTACTS.clear()
        self.name = "Lawrence"
        self.phone = "0708686842"
    
    def test_Add_contact(self):
        """tests that a new contact can be added successfully"""
        #test that the dictionary is empty
        self.assertIsInstance(CONTACT,Contacts)
        self.assertTrue(len(CONTACTS) == 0)
        #add a contact
        response = CONTACT.Add_contact('james','0709686842')
        #test for the lenth of the dict to see if something has been inserted
        self.assertTrue(len(CONTACTS) > 0)
        #test to see if inserted name matches what we put in
        self.assertEqual(response ['name'],"james")
        duplicate = CONTACT.Add_contact('james','0708978765')
        #test to see if it rejects duplicates
        self.assertEqual(duplicate, " Contact already exists")

    def test_View_contact(self):
        """test if a contact can be retrieved"""
        #add contact
        CONTACT.Add_contact('mary', '0705678543')
        #test if view works
        seek = CONTACT.View_contact('mary')
        self.assertEqual(seek['name'],'mary')
        #test view for absent contact
        seek = CONTACT.View_contact('wahu')
        self.assertEqual(seek, 'Contact does not exist')

    def test_Update_contact(self):
        """test if contact can be updated"""
        #test for update absent contact
        update = CONTACT.Update_contact('kezzy','0723456765')
        self.assertEqual(update, "Contact does not exist" )
        #add to dict for test
        add = CONTACT.Add_contact('kezzy','0798765432')
        #test for update contact
        self.assertTrue(add['name'] in CONTACTS)
        update = CONTACT.Update_contact('kezzy','0723456765')
        self.assertEqual(update,"Contact Updated successfully")

    def test_Delete_contact(self):
        """Test for deleting a contact"""
        CONTACT.Add_contact('justin', '0708765432')
        assert 'justin' in CONTACTS
        #test for delete
        deletion = CONTACT.Delete_contact('justin')
        self.assertEqual(deletion,"Removed Successfully")
        deletion = CONTACT.Delete_contact('justin')
        self.assertEqual(deletion,"Contact does not exist")



