from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient

from .models import Feed
# Create your tests here.
User = get_user_model()

class FeedTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='abc', password='somepassword')
        self.userb = User.objects.create_user(username='xyz', password='somepassword2')
        Feed.objects.create(content="my first feed", 
            user=self.user)
        Feed.objects.create(content="my second feed", 
            user=self.user)
        Feed.objects.create(content="my third feed", 
            user=self.userb)
        self.currentCount = Feed.objects.all().count()

    def test_feed_created(self):
        feed_obj = Feed.objects.create(content="my second feed", 
            user=self.user)
        self.assertEqual(feed_obj.id, 4)
        self.assertEqual(feed_obj.user, self.user)
    
    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='somepassword')
        return client
    
    def test_feed_list(self):
        client = self.get_client()
        response = client.get("/api/feeds/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_feed_list(self):
        client = self.get_client()
        response = client.get("/api/feeds/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)
    
    def test_action_like(self):
        client = self.get_client()
        response = client.post("/api/feeds/action/", 
            {"id": 1, "action": "like"})
        self.assertEqual(response.status_code, 200)
        like_count = response.json().get("likes")
        self.assertEqual(like_count, 1)
    
    def test_action_unlike(self):
        client = self.get_client()
        response = client.post("/api/feeds/action/", 
            {"id": 2, "action": "like"})
        self.assertEqual(response.status_code, 200)
        response = client.post("/api/feeds/action/", 
            {"id": 2, "action": "unlike"})
        self.assertEqual(response.status_code, 200)
        like_count = response.json().get("likes")
        self.assertEqual(like_count, 0)
    
    def test_action_share(self):
        client = self.get_client()
        response = client.post("/api/feeds/action/", 
            {"id": 2, "action": "share"})
        self.assertEqual(response.status_code, 201)
        data = response.json()
        new_feed_id = data.get("id")
        self.assertNotEqual(2, new_feed_id)
        self.assertEqual(self.currentCount + 1, new_feed_id)

    def test_feed_create_api_view(self):
        request_data = {"content": "This is my test feed"}
        client = self.get_client()
        response = client.post("/api/feeds/create/", request_data)
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        new_feed_id = response_data.get("id")
        self.assertEqual(self.currentCount + 1, new_feed_id)
    
    def test_feed_detail_api_view(self):
        client = self.get_client()
        response = client.get("/api/feeds/1/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        _id = data.get("id")
        self.assertEqual(_id, 1)

    def test_feed_delete_api_view(self):
        client = self.get_client()
        response = client.delete("/api/feeds/1/delete/")
        self.assertEqual(response.status_code, 200)
        client = self.get_client()
        response = client.delete("/api/feeds/1/delete/")
        self.assertEqual(response.status_code, 404)
        response_incorrect_owner = client.delete("/api/feeds/3/delete/")
        self.assertEqual(response_incorrect_owner.status_code, 401)