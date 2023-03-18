from salesman.basket.models import BaseBasket, BaseBasketItem
from salesman.orders.models import (
    BaseOrder,
    BaseOrderItem,
    BaseOrderNote,
    BaseOrderPayment,
)


class Order(BaseOrder):
    pass


class OrderItem(BaseOrderItem):
    pass


class OrderPayment(BaseOrderPayment):
    pass


class OrderNote(BaseOrderNote):
    pass


class Basket(BaseBasket):
    pass


class BasketItem(BaseBasketItem):
    pass
