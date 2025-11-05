from fastapi import FastAPI

app = FastAPI(tags="hola")

@app.get("/Hola/")
async def hola():
    '''
    hace un hola mundo
    '''
    return "hola mundo"
