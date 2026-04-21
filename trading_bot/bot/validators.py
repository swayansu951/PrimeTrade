from enum import Enum
from .logging_config import logger

class OrderSide(str, Enum):
    BUY = "BUY"
    SELL = "SELL"

class OrderType(str, Enum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"

def validate_order_inputs(order_type: OrderType, quantity: float, price: float = None) -> None:
    """Validates properties of the order."""
    if quantity <= 0:
        error_msg = f"Invalid quantity: {quantity}. Quantity must be greater than 0."
        logger.error(error_msg)
        raise ValueError(error_msg)
        
    if order_type == OrderType.LIMIT:
        if price is None or price <= 0:
            error_msg = f"Invalid price: {price}. Price must be greater than 0 for LIMIT orders."
            logger.error(error_msg)
            raise ValueError(error_msg)
