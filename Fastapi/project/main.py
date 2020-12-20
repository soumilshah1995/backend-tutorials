try:
    from fastapi import FastAPI, Request,Body,Depends,Header
    from fastapi import Depends, FastAPI, HTTPException, status
    import secrets
    import uvicorn
    import json
    from pydantic import BaseModel
    from fastapi.security import HTTPBasic, HTTPBasicCredentials
    print("All  Module loaded ")
except Exception as e:
    print("Error Some Modules are Missing  : {} ".format(e))

app = FastAPI()
security  = HTTPBasic()


class Item(BaseModel):
    name: str
    age: str


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):


    correct_username = secrets.compare_digest(credentials.username, "admin")
    correct_password = secrets.compare_digest(credentials.password, "admin")

    if not (correct_password and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"}

        )
    return credentials.username


@app.get("/")
def read_root(item:Item, credentials: HTTPBasicCredentials = Depends(get_current_username)):
    return item



