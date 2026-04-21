import os
from binance.client import Client
from .logging_config import logger

def get_binance_client() -> Client:
    """Initialize and return the python-binance client targeting futures testnet."""
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')
    
    if not api_key or not api_secret:
        error_msg = "BINANCE_API_KEY and BINANCE_API_SECRET must be set in the environment or .env file."
        logger.error(error_msg)
        raise ValueError(error_msg)
        
    logger.debug("Initializing Binance Client.")
    # Read testnet flag from environment, default to True (paper trading)
    use_testnet = os.getenv('USE_TESTNET', 'True').lower() in ('true', '1', 't')
    
    if use_testnet:
        logger.info("Using Binance Futures TESTNET (Paper Trading).")
    else:
        logger.warning("Using Binance Futures MAINNET (Live Trading).")
        
    # Initialize without testnet=True in constructor to avoid auto-pinging the Spot API
    client = Client(api_key, api_secret)
    
    if use_testnet:
        logger.info("Configuring client for Binance Futures TESTNET.")
        # Override endpoints for Futures
        client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        # Important: python-binance may use specialized URLs for some calls
        client.API_URL = 'https://testnet.binance.vision/api'
    else:
        logger.warning("Using Binance Futures MAINNET (Live Trading).")
        
    return client
