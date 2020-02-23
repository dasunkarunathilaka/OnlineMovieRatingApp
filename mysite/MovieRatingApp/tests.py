from django.test import TestCase, RequestFactory, Client
# Run tests without affecting the data. It creates a temporary db.
from . import views, youtubeConnector
from models import Tweet
from django.utils import timezone
from django.core.urlresolvers import reverse


class UserInputTests(TestCase):
				
	def testUserSearchInputModifier(self):
		testInput = "  The Lord of the Rings "
		compressedInput = "#TheLordoftheRings"

		self.assertEqual(views.userInputModifier(testInput), compressedInput)

	def testYoutubeSearchString(self):
		testInput = "titanic"
		youtubeEmbedURL = "https://www.youtube.com/embed/2e-eXJ6HgkQ"
		self.assertEqual(youtubeConnector.youtubeSearch(testInput), youtubeEmbedURL)


class ModelTest(TestCase):

	def createTweet(self, username="TestUser", text="Model Test for Tweet.", date=timezone.now(), sentiment="pos"):
		return Tweet.objects.create(username=username, text=text, date=date, sentiment=sentiment)

	def testModelTweetCreation(self):
		w = self.createTweet()
		self.assertTrue(isinstance(w, Tweet))
		self.assertEqual(w.__unicode__(), w.username)		

	# def test_whatever_list_view(self):
	# 	w = self.createTweet()
	# 	url = reverse('views.index')
	# 	resp = self.client.get(url)

	# 	self.assertEqual(resp.status_code, 200)
	# 	self.assertIn(w.username, resp.content)


# class PostViewTestCase(TestCase):
# 	def test_post_creation(self):
# 		c = Client()  # instantiate the Django test client
# 		response = c.post('movieratingapp/accounts/login', {'username': 'Callum', 'password': 'australia'})
# 		self.assertEqual(response.status_code, 302)
# 		self.assertContains(response, 'Post created.')
# 		self.assertContains(response, 'Some title')