'''
    Name: server.py

    Description: The server module which creates the app instance and serves
                    using uvicorn.
'''
from dataclasses import asdict

import uvicorn

from cortnus_trading.main import create_app
from configuration import DevelopmentConfiguration


app = create_app(asdict(DevelopmentConfiguration()))


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")
