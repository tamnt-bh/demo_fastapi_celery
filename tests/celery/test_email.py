from unittest.mock import patch

import pytest

from celery_worker.tasks import send_email_register_success, send_email_remind_buying, send_remind_buying_to_user


def test_send_email_register_success_success():
    with patch('celery_worker.tasks.Email') as mock_email_class:
        mock_email_instance = mock_email_class.return_value
        mock_email_instance.send_register_success.return_value = None

        result = send_email_register_success("test@example.com", "John Doe")

        mock_email_class.assert_called_once_with(to_email="test@example.com", fullname="John Doe")
        mock_email_instance.send_register_success.assert_called_once()

        assert result == {"message": "Send success"}


def test_send_remind_buying_to_user():
    with patch('celery_worker.tasks.Email') as mock_email_class:
        mock_user = {"email": "test@example.com", "fullname": "John Doe"}

        mock_email_instance = mock_email_class.return_value

        result = send_remind_buying_to_user(mock_user)

        mock_email_class.assert_called_once_with(to_email=mock_user["email"], fullname=mock_user["fullname"])
        mock_email_instance.send_reminder_buying.assert_called_once()

        assert result == {"message": "Send remind {} success".format(mock_user["email"])}


@pytest.fixture
def mocked_send_email_remind_buying(mocker):
    return mocker.patch("celery_worker.tasks.send_email_remind_buying.delay", return_value=None)


def test_send_email_remind_buying(mocked_send_email_remind_buying):
    result = send_email_remind_buying.delay()
    mocked_send_email_remind_buying.assert_called_once()
    assert result is None
