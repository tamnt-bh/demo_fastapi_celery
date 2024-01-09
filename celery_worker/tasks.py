from app.models.user import UserModel
from celery_worker.controller.send_email import send_for_using_non_buying
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
def send_email_remind_buying():
    connect()
    try:
        users = UserModel.objects()
        disconnect()
        return list(send_for_using_non_buying(users))
    except Exception as e:
        print("💥💥 Query Error >> ", e)
    disconnect()
