from app.models.user import UserModel
from utils.email.email import Email


def send_for_using_non_buying(users: list[UserModel]):
    for user in users:
        try:
            email = Email(to_email=user.email, fullname=user.fullname)
            email.send_reminder_buying()
            yield {"message": "Send remind {} success".format(user.email)}
        except Exception as e:
            yield {"message": "Send remind {} fail".format(user.email)}
            print("💥💥 Send Error >> ", e)
