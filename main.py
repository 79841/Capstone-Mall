import os, sys

# p = os.path.abspath('.')
# sys.path.insert(1, p)


from fastapi import FastAPI
import uvicorn
import models
from database import engine
from routers import product, user, authentication, preference, review, exception
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi import status, Request


from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


models.Base.metadata.create_all(engine)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.exception_handler(exception.AuthException)
async def authentication_exception_handler(request: Request, exc: exception.AuthException):
    # return RedirectResponse(
    #     '/login',
    #     status_code=status.HTTP_303_SEE_OTHER
    # )
    return {"msg":"Authentication Error"}

app.include_router(authentication.router)
app.include_router(product.router)
app.include_router(user.router)
app.include_router(review.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, access_log=False)
