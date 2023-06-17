# FastAPI goes down the code and uses the first unique function. Unique by HTTP Method and URL, so order matters if there are duplicate functions

# All our imports

from typing import List, Optional
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user, auth


models.Base.metadata.create_all(bind=engine)

# Starting Fast API app
app = FastAPI()


# Connecting to the fastapi postgres database that we created using pgadmin4
while True:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="fastapi",
            user="postgres",
            password="jkvbl151296",
            cursor_factory=RealDictCursor,
        )
        cursor = conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Connecting to Database failed")
        print("Error: ", error)
        time.sleep(5)

# List of initial posts
my_posts = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "favotite foods", "content": "I like pizzas", "id": 2},
]


# Function to find a post by id in the my_posts dictionary
def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


# Find the index of the post in the my_posts dictionary given the id
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

# Basic GET @localhost:8000 to print Hello World
@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"message": "Hello World"}
