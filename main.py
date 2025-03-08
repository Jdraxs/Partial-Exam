from fastapi import FastAPI
app = FastAPI()

@app.get("/test")
def read_root():
    return {"first_member":"The Sosa", "second_member":"The Jd", "first_city":"armenia", "second_city":"leticia", "first_age": 31}