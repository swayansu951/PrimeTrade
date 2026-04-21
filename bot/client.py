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
        
    client = Client(api_key, api_secret, testnet=use_testnet)
    
    if use_testnet:
        # python-binance's testnet=True only redirects Spot endpoints by default.
        # We must explicitly redirect Futures endpoints to the Futures Testnet URL.
        client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        
    return client
