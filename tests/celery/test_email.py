from unittest.mock import patch, Mock

from celery_worker.tasks import send_email_register_success, send_email_remind_buying


def test_send_email_register_success_success():
    with patch('celery_worker.tasks.Email') as mock_email_class:
        mock_email_instance = mock_email_class.return_value
        mock_email_instance.send_register_success.return_value = None

        result = send_email_register_success("test@example.com", "John Doe")

        mock_email_class.assert_called_once_with(to_email="test@example.com", fullname="John Doe")
        mock_email_instance.send_register_success.assert_called_once()

        assert result == {"message": "Send success"}


def test_send_email_remind_buying():
    with (patch('celery_worker.tasks.UserModel.objects') as mock_objects,
          patch('celery_worker.controller.send_email.Email') as mock_email_class,
          patch('celery_worker.tasks.connect') as mock_connect_db,
          patch('celery_worker.tasks.disconnect') as mock_disconnect_db):
        mock_user = Mock(email="test@example.com", fullname="John Doe")
        mock_objects.return_value = [mock_user]

        mock_email_instance = mock_email_class.return_value

        result = send_email_remind_buying()

        mock_objects.assert_called_once()
        mock_connect_db.assert_called_once()
        mock_disconnect_db.assert_called_once()

        mock_email_class.assert_called_once_with(to_email=mock_user.email, fullname=mock_user.fullname)
        mock_email_instance.send_reminder_buying.assert_called_once()

        assert isinstance(result, list)
