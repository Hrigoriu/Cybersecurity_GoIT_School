import time
import pika
from config import Config
from logger import RetroLogger

class RabbitMQService:
    """
    Сервіс для управління підключенням до RabbitMQ та публікації повідомлень.
    """
    def __init__(self):
        parameters = pika.URLParameters(Config.RABBITMQ_URI)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

        # Оголошуємо черги для збереження цілісності. durable=True захищає від втрати даних при рестарті брокера.
        self.channel.queue_declare(queue=Config.QUEUE_EMAIL, durable=True)
        self.channel.queue_declare(queue=Config.QUEUE_SMS, durable=True)
        RetroLogger.info("SYSTEM: RabbitMQ Channels Initialized.")

    def publish_message(self, queue_name: str, message: str):
        """Відправляє повідомлення у вказану чергу."""
        self.channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=message.encode('utf-8'),
            properties=pika.BasicProperties(
                delivery_mode=2,  # Зробити повідомлення персистентним
            )
        )
        RetroLogger.info(f"RABBITMQ TX -> [Queue: {queue_name}] Payload: {message}")

    def close(self):
        """Закриває з'єднання з брокером."""
        self.connection.close()

class NotificationStub:
    """
    Клас-заглушка для імітації відправки реальних повідомлень.
    """
    @staticmethod
    def send_email(email_address: str, payload: str):
        """Імітація відправки Email."""
        RetroLogger.info(f"STUB: Connecting to SMTP server... Sending payload to {email_address}...")
        time.sleep(1.5)  # Імітація мережевої затримки
        RetroLogger.success(f"STUB: Email successfully sent to {email_address}.")

    @staticmethod
    def send_sms(phone_number: str, payload: str):
        """Імітація відправки SMS."""
        RetroLogger.info(f"STUB: Connecting to SMS Gateway... Sending payload to {phone_number}...")
        time.sleep(1.0)
        RetroLogger.success(f"STUB: SMS successfully delivered to {phone_number}.")
