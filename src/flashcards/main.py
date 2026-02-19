import logging

from .example import add
from .logging_config import configure_logging

logger = logging.getLogger(__name__)


def main() -> None:
    """Entry point for the flashcards' application."""
    configure_logging()
    logger.info(msg="Application started")


if __name__ == "__main__":
    main()
    add(1, 2)
