from app.models.user import UserModel
from celery_worker.worker import celery_app
from common.database import connect, disconnect
from utils.email.email import Email


@celery_app.task
def send_email_register_success(to_email: str, fullname: str):
    try:
        email = Email(to_email=to_email, fullname=fullname)
        email.send_register_success()
        return {"message": "Send success"}

    except Exception as e:
        print("💥💥 Error send email >> ", e)
        return {"message": "Send fail"}


@celery_app.task
def mul(x, y):
    return x * y


@celery_app.task
def xsum(numbers):
    return sum(numbers)


@celery_app.task
def send_email_remind_buying():
    connect()
    try:
        users = UserModel.objects()

        for user in users:
            try:
                email = Email(to_email=user.email, fullname=user.fullname)
                email.send_reminder_buying()
            except Exception as e:
                print("💥💥 Send Error >> ", e)
    except Exception as e:
        print("💥💥 Query Error >> ", e)

    disconnect()
