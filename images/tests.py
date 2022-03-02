from django.test import TestCase

# Create your tests here.
from images.models import Location, Category, Image


class CategoryTestCase(TestCase):

    def setUp(self):
        """
        Create a category for testing
        """
        Category.objects.create(name="Category")

    def test_category_name(self):
        """
        Test that the category name is correct
        """
        category = Category.objects.get(name="Category")
        self.assertEqual(category.name, "Category")

    def test_category_str(self):
        """
        Test that the category string representation is correct
        """
        category = Category.objects.get(name="Category")
        self.assertEqual(str(category), "Category")


class LocationTestCase(TestCase):

    def setUp(self):
        """
        Create a location for testing
        """
        Location.objects.create(name="Location")

    def test_location_name(self):
        """
        Test that the location name is correct
        """
        location = Location.objects.get(name="Location")
        self.assertEqual(location.name, "Location")

    def test_location_str(self):
        """
        Test that the location string representation is correct
        """
        location = Location.objects.get(name="Location")
        self.assertEqual(str(location), "Location")




class ImageTestCase(TestCase):

    def setUp(self):
        """
        Create a image for testing
        """
        Image.objects.create(
            name="Image",
            image="http://t@test.ts/test.jpg",
            description="Description",
            location=Location.objects.create(name="Location"),
            category=Category.objects.create(name="Category"),
            
            time_posted=None
        )

    def test_image_name(self):
        """
        Test that the image name is correct
        """
        image = Image.objects.get(name="Image")
        self.assertEqual(image.name, "Image")

    def test_image_description(self):
        """
        Test that the image description is correct
        """
        image = Image.objects.get(name="Image")
        self.assertEqual(image.description, "Description")

    def test_image_location(self):
        """
        Test that the image location is correct
        """
        image = Image.objects.get(name="Image")
        self.assertEqual(image.location.name, "Location")

    def test_image_category(self):
        """
        Test that the image category is correct
        """
        image = Image.objects.get(name="Image")
        self.assertEqual(image.category.name, "Category")

    def test_image_image(self):
        """
        Test that the image image is correct
        """
        image = Image.objects.get(name="Image")
        self.assertEqual(image.image, "http://t@test.ts/test.jpg")


    def test_image_str(self):
        """
        Test that the image string representation is correct
        """
        image = Image.objects.get(name="Image")
        self