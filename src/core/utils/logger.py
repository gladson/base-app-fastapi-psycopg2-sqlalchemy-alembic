import logging


class Logger:
    """
    Initialize the logger with the given name and logging level.

    Parameters:
        name (str): The name of the logger. Defaults to "root".
        level (int): The logging level. Defaults to logging.DEBUG.

    Returns:
        None
    """

    def __init__(self, name="root", level=logging.DEBUG):
        self.logger = logging.getLogger(name.upper())
        self.logger.setLevel(level)

        formatter = logging.Formatter(
            "%(levelname)s:     [%(name)s] - %(asctime)s " "- '%(message)s'"
        )

        # Configura a saída do log para o console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def debug(self, message):
        """
        Method to log a debug message.

        :param message: The message to be logged.
        :type message: str
        """
        self.logger.debug(message)

    def info(self, message):
        """
        Method to log a info message.

        :param message: The message to be logged.
        :type message: str
        """
        self.logger.info(message)

    def warning(self, message):
        """
        Method to log a warning message.

        :param message: The message to be logged.
        :type message: str
        """
        self.logger.warning(message)

    def error(self, message):
        """
        Method to log a error message.

        :param message: The message to be logged.
        :type message: str
        """
        self.logger.error(message)

    def critical(self, message):
        """
        Method to log a critical message.

        :param message: The message to be logged.
        :type message: str
        """
        self.logger.critical(message)


# Exemplo de uso
# if __name__ == "__main__":
#     logger = Logger()

#     logger.debug("Debug message")
#     logger.info("Info message")
#     logger.warning("Warning message")
#     logger.error("Error message")
#     logger.critical("Critical message")
