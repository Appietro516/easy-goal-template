from fastapi import Body, APIRouter, BackgroundTasks
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBasicCredentials
from passlib.context import CryptContext

from send_email import send_email_async, send_email_background

router = APIRouter()

hash_helper = CryptContext(schemes=["bcrypt"])

@router.get('/send-email/asynchronous')
async def send_email_asynchronous(to_email: str = '', title: str = '', name: str=''):
    await send_email_async(title, to_email, {'title': title, 'name': name})
    return 'Success'
@router.get('/send-email/backgroundtasks')
def send_email_backgroundtasks(background_tasks: BackgroundTasks):
    send_email_background(background_tasks, 'Hello World',   
    'someemail@gmail.com', {'title': 'Hello World', 'name':       'John Doe'})
    return 'Success'