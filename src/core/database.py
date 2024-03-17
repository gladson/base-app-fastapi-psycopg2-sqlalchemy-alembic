from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.settings import Settings
from core.utils.logger import Logger


class Database:
    def __init__(self):
        self.engine = None
        self.settings = Settings()
        self.database_url = str(self.settings.DATABASE_URL)
        Logger("Database").info(message="Conectando ao banco de dados...")
        if self.database_url is not None:
            Logger("Database").info(
                message="Crie uma instância do objeto Database "
                "com a URL do banco de dados",
            )
            self.engine = create_engine(self.database_url)
        else:
            raise ValueError(
                "A variável de ambiente DATABASE_URL não está definida.",
            )

        self.Session = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine,
        )
