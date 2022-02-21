import unittest
import cap

# Define the class and inherit unittest.TestCase
class TestCap(unittest.TestCase):

	# Define methods
	# This is a general structure of a test
	def test_one_word(self):
		text = 'python'
		result = cap.cap_text(text)
		self.assertEqual(result,"Python")

	#Let's define another test class
	def test_multiple_words(self):
		text = 'monty python'
		result = cap.cap_text(text)
		self.assertEqual(result,"Monty Python")

if __name__=="__main__":
	unittest.main()