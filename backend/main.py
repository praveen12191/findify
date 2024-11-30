from fastapi import FastAPI
from models.product import Product
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from help import findProduct
app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/")
async def root(data : Product):
    priceMin = data.priceMin
    priceMax = data.priceMax
    productName = data.productName
    result = findProduct(productName,priceMin,priceMax)
    return JSONResponse(content={'value':result['value'],'url':result['product']},status_code=200)
    