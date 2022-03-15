from django.test import TestCase
from .forms import ItemForm


class TesItemForm(TestCase):
    """ form testing class"""

    def test_item_name_is_required(self):
        """ test forms """
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        """ test that done field is not required,
        form is valid without done field """
        form = ItemForm({'name': 'Test Todo Items'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """ test the exact fileds displayed on the form """
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
