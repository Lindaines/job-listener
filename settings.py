from os.path import join, dirname
import os


# Config RabbitMQ
__vhost = str(os.environ.get("RABBITMQ_VHOST"))
RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST", "localhost")
RABBITMQ_PORT = int(os.environ.get("RABBITMQ_PORT", "5672"))
RABBITMQ_USER = os.environ.get("RABBITMQ_USER", "rabbitmq")
RABBITMQ_PASSWORD = os.environ.get("RABBITMQ_PASSWORD", "rabbitmq")
RABBITMQ_VHOST = os.environ.get("RABBITMQ_VHOST", "/")
QUEUE_NAME_CONSUMER = os.environ.get("QUEUE_NAME_CONSUMER", "status-jobs")
QUEUE_NAME_PUBLISHER = os.environ.get("QUEUE_NAME_PUBLISHER", "job-listener-dead-letter")
EXCHANGE_NAME = os.environ.get("EXCHANGE_NAME", "exc-worker")
CONSUME_ROUTING_KEY = os.environ.get("CONSUME_ROUTING_KEY", "")

# Config MongoDB
MONGO_HOST = os.environ.get("MONGO_HOST", "localhost")
MONGO_DATABASE = os.environ.get("MONGO_DATABASE", "scheduler")
MONGO_COLLECTION = os.environ.get("MONGO_COLLECTION", "jobs")
MONGO_PORT = os.environ.get("MONGO_PORT", 27017)
MONGO_USER = os.environ.get("MONGO_USER", "root")
MONGO_PASSWORD = os.environ.get("RABBITMQ_PASSWORD", "KXZBE5PRfO")
MONGO_COLLECTION_JOBS = os.environ.get("MONGO_COLLECTION_JOBS", "jobs")

#Config Email Notifier
EMAIL_USER = os.environ.get("EMAIL_USER", "lindainescostav@gmail.com")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD", "doiwannaknow1700")
SEND_TO_SPLITTED_BY_COMMA = os.environ.get("SEND_TO_SPLITTED_BY_COMMA", "lindainesv49@gmail.com,linda.vieira@cedrotech.com")