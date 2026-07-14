from fastapi import FastAPI
from mockdata import products

app=FastAPI()

@app.get("/home")
def home():
    return "welcome to fission labs"
@app.get("/contact")
def contact():
    return "you can contact uss"


@app.get("/product")
def get_product():
    return products


##path parameters
@app.get("/product/{product_id}")
def get_product(product_id:int):

    for i in products:
        if i.get("id")==product_id:
            return i
    return {
        "error":'product_id not found'
    }