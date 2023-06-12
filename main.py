from loader import client
import handlers  # noqa
from database.commands import create_tables
from loader import logger


def main():
    client.start()
    logger.info("Logging into a Telegram account has occurred")
    create_tables()
    logger.debug("A database has been created")
    client.run_until_disconnected()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.exception("Unknown error")
