import json
from rest_framework import status
from rest_framework.test import APITestCase
from levelupapi.models import Event, Gamer, Game

class EventTests(APITestCase):
    def setUp(self):
        """
        Create a new account and create sample category
        """
        url = "/register"
        data = {
            "username": "steve",
            "password": "Admin8*",
            "email": "steve@stevebrownlee.com",
            "address": "100 Infinity Way",
            "phone_number": "555-1212",
            "first_name": "Steve",
            "last_name": "Brownlee",
            "bio": "Love those eventz!!"
        }
        # Initiate request and capture response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Store the auth token
        self.token = json_response["token"]

        # Assert that a user was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # SEED DATABASE WITH ONE gamer
        # This is needed because the API does not expose a /gamer
        # endpoint for creating gamer
        gamer = Gamer()
        gamer.user_id = 1
        gamer.save()

        # SEED DATABASE WITH ONE gamer
        # This is needed because the API does not expose a /gamer
        # endpoint for creating gamer
        gamer = Game()
        gamer.user_id = "Dungeons & Dragons"
        gamer.save()

    def test_create_event(self):
        """
        Ensure we can create a new event.
        """
        # DEFINE event PROPERTIES
        url = "/events"
        data = {
            "time": "19:30:00",
            "date": "2021-08-14",
            "game": 3,
            "description": "We all live in a yellow submarine",
            "organizer": 1,
        }

        # Make sure request is authenticated
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the event was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties on the created resource are correct
        self.assertEqual(json_response["time"], "19:30:00")
        self.assertEqual(json_response["date"], "2021-08-14")
        self.assertEqual(json_response["description"], "We all live in a yellow submarine")
