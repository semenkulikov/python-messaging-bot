from telethon.sync import TelegramClient
from config_data import config
import logging


logging.basicConfig(
    level=logging.INFO,
    filename='my_logging.log',
    format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]',
    datefmt='%d/%m/%Y %I:%M:%S',
    encoding='utf-8',
)


client = TelegramClient(
    session='my_session',
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    device_model="iPhone 13 Pro Max",
    system_version="14.8.1",
    app_version="8.4",
    lang_code="en",
    system_lang_code="en-US"
)

# Пути решения вылета всех сессий:

# Текущий — авторизация через айфон


# 1. Прокси
# proxy = (socks.SOCKS5 , proxy_ip, proxy_port)
# client = TelegramClient(name, api_id, api_hash,proxy=proxy)

# 2. Version
# client = TelegramClient(
# 'my_session',
# api_id,
# api_hash,
# system_version="4.16.30-vxCUSTOM")
