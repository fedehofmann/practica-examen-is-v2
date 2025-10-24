# app/shipping_strategies.py
from abc import ABC, abstractmethod

class ShippingStrategy(ABC):
    @abstractmethod
    def calculate(self, weight: float) -> float:
        pass

class LocalShippingStrategy(ShippingStrategy):
    def calculate(self, weight: float) -> float:
        return 5 + (1 * weight)

class NationalShippingStrategy(ShippingStrategy):
    def calculate(self, weight: float) -> float:
        return 10 + (2 * weight)

class InternationalShippingStrategy(ShippingStrategy):
    def calculate(self, weight: float) -> float:
        return 25 + (5 * weight)