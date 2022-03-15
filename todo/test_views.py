""" test views """
from django.test import TestCase
from .models import Item


# Create your tests here.


class TestViews(TestCase):
    """ test views """
    def test_get_todo_list(self):
        """ test that home page responds """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        """ add item check """
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        """ edit item view"""
        item = Item.objects.create(name='Test Todo Item', done='False')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        """ Create a new item, check it redirects to the home page """
        response = self.client.post('/add', {'name': 'Test Added Item'})
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        """
        Create a new item object instance
        delete this item
        assert that it redirects to the home page
        Try to return the item from the database using filter and the item_id
        Check the length of existing_items = 0
        """
        item = Item.objects.create(name='Test Todo Item', done='False')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        """
        Create a new item object instance with done=True
        toggle this item so done=False
        assert that it redirects to the home page
        Get the item again and save as updated_item
        Check the done status is False
        """
        item = Item.objects.create(name='Test Todo Item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)

    def test_can_edit_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated Name')
