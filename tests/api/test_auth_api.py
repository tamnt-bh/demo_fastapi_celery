import unittest
from unittest.mock import patch

import mongomock
from app.controller.security import get_password_hash, verify_password
from app.main import app
from app.models.user import UserModel
from fastapi.testclient import TestClient
from mongoengine import connect, disconnect


class TestUserApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        disconnect()
        connect("mongoenginetest", host="mongodb://localhost:1234", mongo_client_class=mongomock.MongoClient)
        cls.client = TestClient(app)
        cls.user = UserModel(
            email="test@test.com",
            fullname="John Doe",
            password=get_password_hash("12345678")
        ).save()

    @classmethod
    def tearDownClass(cls):
        disconnect()

    def test_login(self):
        r = self.client.post(
            "/auth/login",
            json={"email": "test@test.com", "password": "12345678"},
        )
        assert r.status_code == 200

        resp = r.json()
        user = UserModel.objects(id=resp["user"].get("id")).get()
        assert user.email == "test@test.com"
        assert user.fullname
        assert user.password

    def test_register(self):
        with patch('app.controller.auth.send_email_register_success') as mock_task_celery:
            r = self.client.post(
                "/auth/register",
                json={"email": "test1@test.com", "password": "12345678", "fullname": "Test Joe"},
            )

            # mock_task_celery.assert_called_once_with(to_email="test1@test.com", fullname="Test Joe")

            assert r.status_code == 200

            resp = r.json()
            user = UserModel.objects(id=resp["user"].get("id")).get()
            assert user.email == "test1@test.com"
            assert user.fullname
            assert verify_password("12345678", user.password)
