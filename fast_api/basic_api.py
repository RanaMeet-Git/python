from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return {"message":"hello world"}
@app.get("/anime")
def anime():
    return ["goku","itachi",'gojo']
@app.get("/contact")
def contact():
    return {"ph.no":9455672}
@app.get("/about")
def about():
    return {"about":"hello rana here"}

