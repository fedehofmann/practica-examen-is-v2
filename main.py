# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from app.shipping_strategies import LocalShippingStrategy, NationalShippingStrategy, InternationalShippingStrategy
from app.discount_strategies import NoDiscountStrategy, PrimeUserStrategy, NewUserStrategy

# Inicializamos la aplicación FastAPI
app = FastAPI()

# Definir los modelos de entrada para las solicitudes
class Item(BaseModel):
    weight_kg: float  # Peso en kg del artículo

class ShippingRequest(BaseModel):
    items: list[Item]  # Lista de artículos
    destination: str  # 'local', 'national', 'international'
    coupon: str  # 'PRIME_USER', 'NEW_USER', 'NO_DISCOUNT'

# Endpoint para calcular el costo de envío y descuento
@app.post("/calculate-shipping")
def calculate_shipping(request: ShippingRequest):
    # Calcular el peso total de los artículos
    total_weight = sum(item.weight_kg for item in request.items)
    
    # Calcular el costo de envío según el destino
    if request.destination == 'local':
        shipping_cost = LocalShippingStrategy().calculate(total_weight)
    elif request.destination == 'national':
        shipping_cost = NationalShippingStrategy().calculate(total_weight)
    elif request.destination == 'international':
        shipping_cost = InternationalShippingStrategy().calculate(total_weight)
    else:
        return {"error": "Invalid destination"}

    # Aplicar el descuento según el cupón
    if request.coupon == 'PRIME_USER':
        discount = PrimeUserStrategy().apply_discount(shipping_cost)
    elif request.coupon == 'NEW_USER':
        discount = NewUserStrategy().apply_discount(shipping_cost)
    elif request.coupon == 'NO_DISCOUNT':
        discount = NoDiscountStrategy().apply_discount(shipping_cost)
    else:
        return {"error": "Invalid coupon"}

    # Calcular el costo final después del descuento
    final_cost = shipping_cost - discount
    
    return {
        "base_cost": shipping_cost,
        "discount_applied": discount,
        "final_cost": final_cost
    }