import threading
from rabbitmq.rabbitmq import RabbitMQClient


if __name__ == "__main__":
    """ This is executed when run from the command line """
    RabbitMQClient().run()
