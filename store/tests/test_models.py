from django.test import TestCase

# Create your tests here.
from store.models import Category, Product
from django.contrib.auth.models import User

class TestCategoriesModel(TestCase):

  def setUp(self):
    self.data1 = Category.objects.create(name='django',slug='django')

  def test_category_model_entry(self):
    data = self.data1
    self.assertTrue(isinstance(data,Category))

  def test_category_model_entry(self):
    """
    test model insertion/types/fields
    """
    data:Category
    data = self.data1
    self.assertEqual(str(data),'django')

  def TestProductModel(Testcase):
    def setUp(self):
      Category.objects.create(name='django',slug='django')
      User.objects.create(username='admin')
      self.data1 = Product.objects.create(category_id=1,title='django beginners', created_by_id=1,slug='django-beginners',price='20.00',image='django')


  def test_products_model_entry(self):
    """
    Test product model data insertion/types/field attributes
    """
    data = self.data1
    self.assertTrue(isinstance(data,Product))
    self.assertEqual(str(data),'django beginners')
