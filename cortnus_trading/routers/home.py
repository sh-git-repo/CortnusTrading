'''
    Name: server.py

    Description: Simple home page module.
'''
from fastapi import APIRouter

router = APIRouter()

@router.get('/v1')
async def home():
    '''
    Home page to test application is working.
    '''
    return {"message": "Welcome to the Cortnus Trading API."}
