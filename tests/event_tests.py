import json
from rest_framework import status
from rest_framework.test import APITestCase
from levelupapi.models import Game, Event, GameType

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

        # SEED DATABASE WITH ONE GAME TYPE
        # This is needed because the API does not expose a /gametypes
        # endpoint for creating game types
        gametype = GameType()
        gametype.label = "Board game"
        gametype.save()

        # SEED DATABASE WITH ONE game
        # This is needed because the API does not expose a /game
        # endpoint for creating game
        game = Game()
        game.gamer_id = 1
        game.gametype_id = gametype.id
        game.skill_level = 5
        game.number_of_players = 3
        game.maker = "Wizards of the Coast"
        game.title = "Dungeons & Dragons"
        game.save()

    def test_create_event(self):
        """
        Ensure we can create a new event.
        """
        # DEFINE event PROPERTIES
        url = "/events"
        data = {
            "time": "19:30:00",
            "date": "2021-08-14",
            "description": "We all live in a yellow submarine",
            "gameId": 1,
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

    def test_get_event(self):
        """
        Ensure we can get an existing event.
        """

        # Seed the database with a event
        event = Event()
        event.time = "19:30:00"
        event.date = "2021-08-14"
        event.game_id = 1
        event.description = "We all live in a yellow submarine"
        event.organizer_id = 1

        event.save()

        # Make sure request is authenticated
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        # Initiate request and store response
        response = self.client.get(f"/events/{event.id}")

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was retrieved
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the values are correct
        self.assertEqual(json_response["time"], "19:30:00")
        self.assertEqual(json_response["date"], "2021-08-14")
        self.assertEqual(json_response["description"], "We all live in a yellow submarine")