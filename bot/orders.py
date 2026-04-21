from binance.exceptions import BinanceAPIException
from .client import get_binance_client
from .validators import OrderSide, OrderType, validate_order_inputs
from .logging_config import logger

def place_order(symbol: str, side: OrderSide, order_type: OrderType, quantity: float, price: float = None):
    """
    Places an order on the Binance Futures Testnet.
    Returns the response JSON from Binance or raises an Exception.
    """
    validate_order_inputs(order_type, quantity, price)
    
    client = get_binance_client()
    
    params = {
        'symbol': symbol,
        'side': side.value,
        'type': order_type.value,
        'quantity': quantity
    }
    
    if order_type == OrderType.LIMIT:
        params['price'] = price
        params['timeInForce'] = 'GTC' # Good Till Cancelled is typically required for LIMIT orders
        
    logger.info(f"Submitting {order_type.value} {side.value} order for {quantity} of {symbol}. Params: {params}")
    
    try:
        response = client.futures_create_order(**params)
        logger.info(f"Order successful. Response: {response}")
        return response
    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e.status_code} - {e.message}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error when placing order: {e}")
        raise e
