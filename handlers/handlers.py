import logging

from telethon import events
from loader import client


async def initial_sender(username_list: list, message: str):
    """
    Функция для рассылки сообщения группе юзеров
    :param username_list: список юзернэймов
    :param message: текст сообщения
    :return: None
    """
    for username in username_list:
        await client.send_message(
            entity=username,
            message=message,
            schedule=10
        )
        logging.info(f"Message sent to {username}")
