# import subprocess

from fastapi import FastAPI

from core.settings import Settings
from core.urls import router as core_router

app = FastAPI()

# Inclui os roteadores principais
app.include_router(core_router)

settings = Settings()

# is_debug = settings.DEBUG
# app_port = "8000" if settings.APP_PORT is None else str(settings.APP_PORT)


# async def run_server():
#     """
#     Asynchronously runs the server.

#     This function starts the server by executing the `uvicorn`
#     command in a subprocess. The `uvicorn` command is set to run the `server`
#     module as the main application (`server:app`) on
#     the host `0.0.0.0` and port `8000`.
#     """
#     uvicorn_command = tuple(
#         [
#             "uvicorn",
#             "server:app",
#             "--host",
#             "0.0.0.0",
#             "--port",
#             app_port,
#         ]
#     )

#     subprocess.Popen(uvicorn_command, shell=True)


# if __name__ == "__main__":
#     import asyncio

#     asyncio.run(run_server(), debug=True)
