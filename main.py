# https://stackoverflow.com/a/65917164/16237146
import os
from uvicorn import run

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from variables import URL_BETA_IOS, URL_BETA_ANDROID

app = FastAPI()

@app.get("/ios")
async def main():
    # automatically redirect to TestFlight link.
    return RedirectResponse(url=URL_BETA_IOS, status_code=303)

@app.get("/android")
async def main():
    return "Sorry, Cashpile's Beta is not available yet on Android."
    # return RedirectResponse(url=URL_BETA_ANDROID, status_code=303)

app.mount("/", StaticFiles(directory="static", html=True), name="home")

if __name__ == "__main__":
    run("main:app", host="0.0.0.0", reload=True)
