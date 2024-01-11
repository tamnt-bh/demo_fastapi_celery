from celery import group

from app.models.user import UserModel
from celery_worker.controller.utils import chunk_list, convert_type_user
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
    page_size = 1000
    page_index = 0
    try:
        data = UserModel.objects.skip(page_index * page_size).limit(page_size)
        while len(data) > 0:
            data = convert_type_user(data)
            chunk_users = chunk_list(data, 100)
            job = group(
                [send_remind_buying_to_chunk.s(users) for users in chunk_users]
            )
            job.apply_async()

            page_index += 1
            data = UserModel.objects.skip(page_index * page_size).limit(page_size)
    except Exception as e:
        print("💥💥 Error >> ", e)
    disconnect()


@celery_app.task
def send_remind_buying_to_chunk(users: list[dict[str, str]]):
    try:
        job = group(
            [send_remind_buying_to_user.s(user) for user in users]
        )
        job.apply_async()
    except Exception as e:
        print("💥💥 Error >> ", e)


@celery_app.task
def send_remind_buying_to_user(user: dict[str, str]):
    try:
        email = Email(to_email=user["email"], fullname=user["fullname"])
        email.send_reminder_buying()
        return {"message": "Send remind {} success".format(user["email"])}
    except Exception as e:
        print("💥💥 Send Error >> ", e)
        return {"message": "Send remind {} fail".format(user["email"])}
