from fastapi import FastAPI

app = FastAPI(ta)

@app.get("/Hola/")
async def hola():
    '''
    hace un hola mundo
    '''
    return "hola mundo"
