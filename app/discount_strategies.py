# app/discount_strategies.py
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, base_cost: float) -> float:
        pass

class NoDiscountStrategy(DiscountStrategy):
    def apply_discount(self, base_cost: float) -> float:
        return base_cost

class PrimeUserStrategy(DiscountStrategy):
    def apply_discount(self, base_cost: float) -> float:
        return base_cost * 0.85  # 15% off

class NewUserStrategy(DiscountStrategy):
    def apply_discount(self, base_cost: float) -> float:
        return base_cost - 5  # $5 off