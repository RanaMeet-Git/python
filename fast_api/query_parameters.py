from fastapi import FastAPI
app = FastAPI()

#https://google.com/search?q=python
#q=python is query parameter

@app.get("/search")
def search(name:str): #/search?name=Ravi
    return {"search":name}

@app.get("/products")
def products(category:str, price:int):
    return {
        "category":category,
        "price":price
    }

