import pika
from config import Config
from repository import ContactRepository
from services import NotificationStub
from logger import RetroLogger

def sms_callback(ch, method, properties, body):
    """Callback-функція для обробки повідомлень з черги SMS."""
    contact_id = body.decode('utf-8')
    RetroLogger.info(f"CONSUMER [SMS]: Received Contact ID: {contact_id}")

    contact = ContactRepository.get_contact_by_id(contact_id)
    if contact and not contact.is_sent:
        # Викликаємо функцію-заглушку
        payload = f"{contact.full_name}, нагадуємо про візит завтра о 10:00."
        NotificationStub.send_sms(str(contact.phone), payload)

        # Оновлюємо статус в БД
        ContactRepository.mark_as_sent(contact_id)
        RetroLogger.success(f"DB: Contact ID {contact_id} marked as SENT.")

    # Підтверджуємо успішну обробку повідомлення брокеру (ACK)
    ch.basic_ack(delivery_tag=method.delivery_tag)

def start_sms_consumer():
    """Запускає процес прослуховування SMS черги."""
    ContactRepository.connect_db()
    parameters = pika.URLParameters(Config.RABBITMQ_URI)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue=Config.QUEUE_SMS, durable=True)
    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(queue=Config.QUEUE_SMS, on_message_callback=sms_callback)

    RetroLogger.info("SYSTEM: [*] SMS Consumer is running. To exit press CTRL+C")
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        RetroLogger.warning("SYSTEM: Consumer stopped by user.")
        connection.close()

if __name__ == "__main__":
    start_sms_consumer()
