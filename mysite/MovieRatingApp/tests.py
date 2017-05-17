from django.test import TestCase
# Run tests without affecting the data. It creates a temporary db.
from . import views

# Create your tests here.

class UserInputTests(TestCase):
				
	def testUserSearchInputModifier(self):
		testInput = "  The Lord of the Rings "
		compressedInput = "#TheLordoftheRings"

		self.assertEqual(views.userInputModifier(testInput), compressedInput)

			
