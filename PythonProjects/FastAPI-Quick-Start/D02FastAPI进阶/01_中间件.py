from fastapi import FastAPI

app = FastAPI()


@app.middleware("http")
async def middleware_two(request, call_next):
    print("middleware two start")
    response = await call_next(request)
    print("middleware two end")
    return response


@app.middleware("http")
async def middleware_one(request, call_next):
    print("middleware one start")
    response = await call_next(request)
    print("middleware one end")
    return response


@app.get("/")
async def root():
    return {"message": "Hello World"}
