import os

from dotenv import load_dotenv

from core.utils.logger import Logger


class Settings:
    def __init__(self):
        Logger("Settings").info(
            message="Carregando as variáveis " "de ambiente...",
        )
        if (
            os.getenv("DEBUG", "").lower()
            == "true"
            # or os.getenv("ENVIRONMENT", "").lower() == "development"
        ):
            Logger("Settings").info(
                message="Carrega as variáveis de ambiente do "
                "arquivo .env.development",
            )
            load_dotenv(".env.development")
        # else:
        #     Logger("Settings").info(
        #         message="Carrega as variáveis de ambiente do "
        #         "arquivo .env.production",
        #     )
        #     load_dotenv(".env.production")
        Logger("Settings").info(
            message="Carregado as variáveis " "de ambiente...",
        )

    def __getattr__(self, name):
        Logger("Settings").info(
            message=f"Retorna o valor da variável de "
            f"ambiente: {name} = {os.getenv(name)}",
        )
        return os.getenv(name)


# # Crie uma instância da classe Settings
# settings = Settings()

# # Acesse a variável DATABASE_URL
# database_url = settings.DATABASE_URL
# print("DATABASE_URL:", database_url)
