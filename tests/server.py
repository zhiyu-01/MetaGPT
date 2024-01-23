from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/v1')
async def q():
    return True

@app.post('/v1')
async def ask():
    return 'hello'

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8080)
