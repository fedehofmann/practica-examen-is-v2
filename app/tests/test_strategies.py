from app.shipping_strategies import LocalShippingStrategy, NationalShippingStrategy, InternationalShippingStrategy
from app.discount_strategies import NoDiscountStrategy, PrimeUserStrategy, NewUserStrategy

def test_local_shipping_strategy():
    strategy = LocalShippingStrategy()
    cost = strategy.calculate(2.0)  # Peso de 2 kg
    assert cost == 7.0  # Debería devolver $7.0

def test_national_shipping_strategy():
    strategy = NationalShippingStrategy()
    cost = strategy.calculate(3.0)  # Peso de 3 kg
    assert cost == 16.0  # Debería devolver $16.0

def test_international_shipping_strategy():
    strategy = InternationalShippingStrategy()
    cost = strategy.calculate(1.0)  # Peso de 1 kg
    assert cost == 30.0  # Debería devolver $30.0

def test_no_discount():
    strategy = NoDiscountStrategy()
    final_cost = strategy.apply_discount(10.0)  # Sin descuento
    assert final_cost == 10.0  # Debería devolver 10.0

def test_prime_user_discount():
    strategy = PrimeUserStrategy()
    final_cost = strategy.apply_discount(10.0)  # 15% de descuento
    assert final_cost == 8.5  # Debería devolver 8.5

def test_new_user_discount():
    strategy = NewUserStrategy()
    final_cost = strategy.apply_discount(10.0)  # Descuento de $5
    assert final_cost == 5.0  # Debería devolver 5.0