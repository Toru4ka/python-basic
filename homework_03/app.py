from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/ping")
def pong():
    return {"message": "pong"}


@app.get("/hello")
def hello():
    return {"message": "hello"}


@app.get("/hello/{name}")
def hello_user(name: str):
    return {"message": f"hello {name}!"}


@app.get("/github")
def github():
    return {"message": "my github: https://github.com/Toru4ka"}