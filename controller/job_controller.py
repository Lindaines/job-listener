from bson import ObjectId

from persistences.mongodb_persistence import MongoDB
from notification.email_sender import EmailSender
import settings


class JobController:
    def __init__(self):
        self.mongo = MongoDB()
        self.notificator = EmailSender()

    def update_db(self, id_job: str, status_job: str):
        return self.mongo.update_one(
            settings.MONGO_COLLECTION_JOBS,
            {"_id": ObjectId(id_job)},
            {"$set": {"status_job": status_job}}, upsert=True
        )

    def notify(self, id_job, status_job):
        self.notificator.send(id_job, status_job)

    def handle_package(self, package: dict):
        error_message = {}
        id_job = package.get('id_job')
        status_job = package.get('status_job')
        if not all([id_job, status_job]):
            raise Exception("Invalid package")
        try:
            self.update_db(id_job, status_job)
        except Exception as e:
            error_message['id_job'] = id_job
            error_message['type'] = 'db_update'
            error_message['message'] = str(e)
        try:
            self.notify(id_job, status_job)
        except Exception as e:
            error_message['id_job'] = id_job
            error_message['type'] = 'email_sender'
            error_message['message'] = str(e)
        return error_message
