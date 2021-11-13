'''
    Name: server.py

    Description: The main module for creating the app instance with the
                    required configurations
'''
from fastapi import FastAPI

from cortnus_trading.routers import home


def create_app(configuration: dict) -> FastAPI:
    '''
    '''
    app = FastAPI()
    app.include_router(home.router)
    return app
