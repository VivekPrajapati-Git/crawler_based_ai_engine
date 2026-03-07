from fastapi import FastAPI

app = FastAPI()

@app.post('/crawl/{Data}')
def crawler():
    pass

@app.get('/roadmap')
def roadmap():
    pass

@app.get('/nlp_analyzer')
def nlp():
    pass

@app.get('/graph')
def graph():
    pass