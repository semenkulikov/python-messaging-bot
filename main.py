import logging

from loader import client
import handlers  # noqa
from database.commands import create_tables


def main():
    client.start()
    logging.info("Logging into a Telegram account has occurred")
    create_tables()
    logging.debug("A database has been created")
    client.run_until_disconnected()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.exception("Unknown error")
