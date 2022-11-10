from typing import Optional,Union
from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def healtcheck():
    #capture the name of the container
    container_name = os.environ.get('HOSTNAME')
    #return the name of the container
    return {"message": "Service is up and running - {}".format(container_name)}

@app.get("/enviroment")
def get_enviroment(str_enviroment: str):
    #capture the name of the container
    env_value = os.environ.get(str_enviroment)
    #return the name of the container
    return {"message": "{}:{}".format(str_enviroment,env_value)}