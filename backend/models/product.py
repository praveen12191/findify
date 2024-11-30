from pydantic import BaseModel

class Product(BaseModel):
    priceMin : int 
    priceMax : int 
    productName : str 