import pika
from config import Config
from repository import ContactRepository
from services import NotificationStub
from logger import RetroLogger

def email_callback(ch, method, properties, body):
    """Callback-функція для обробки повідомлень з черги Email."""
    contact_id = body.decode('utf-8')
    RetroLogger.info(f"CONSUMER [EMAIL]: Received Contact ID: {contact_id}")

    contact = ContactRepository.get_contact_by_id(contact_id)
    if contact and not contact.is_sent:
        # Викликаємо функцію-заглушку
        payload = f"Шановний(а) {contact.full_name}, ваші результати обстеження готові."
        NotificationStub.send_email(str(contact.email), payload)
        
        # Оновлюємо статус в БД
        ContactRepository.mark_as_sent(contact_id)
        RetroLogger.success(f"DB: Contact ID {contact_id} marked as SENT.")

    # Підтверджуємо успішну обробку повідомлення брокеру (ACK)
    ch.basic_ack(delivery_tag=method.delivery_tag)

def start_email_consumer():
    """Запускає процес прослуховування Email черги."""
    ContactRepository.connect_db()
    parameters = pika.URLParameters(Config.RABBITMQ_URI)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    # Забезпечуємо наявність черги
    channel.queue_declare(queue=Config.QUEUE_EMAIL, durable=True)
    # QoS налаштування: отримувати не більше 1 повідомлення за раз (розподіл навантаження)
    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(queue=Config.QUEUE_EMAIL, on_message_callback=email_callback)

    RetroLogger.info("SYSTEM: [*] Email Consumer is running. To exit press CTRL+C")
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        RetroLogger.warning("SYSTEM: Consumer stopped by user.")
        connection.close()

if __name__ == "__main__":
    start_email_consumer()
