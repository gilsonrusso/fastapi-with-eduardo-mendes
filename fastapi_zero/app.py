from http import HTTPStatus

from fastapi import FastAPI

from fastapi_zero.routers import auth, users
from fastapi_zero.schemas import Message

app = FastAPI(title='FastAPI Zero', description='FastAPI Zero')

app.include_router(auth.router)
app.include_router(users.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return Message(message='API is Running...')
