# Binance Futures Testnet Trading Bot

A Python-based CLI application to place Market and Limit orders on the Binance Futures Testnet (USDT-M), created for a developer assignment.

## Setup Instructions

1. **Clone or Download the Repository**
   Make sure you are in the project folder `trading_bot`.

2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   - Copy the `.env.example` file to create a `.env` file (if not already done).
   - Enter your Binance Futures Testnet API Key and Secret into the `.env` file like so:
     ```
     BINANCE_API_KEY=your_testnet_api_key_here
     BINANCE_API_SECRET=your_testnet_api_secret_here
     ```

## How to Run Examples

This bot uses a CLI interface. You can execute orders using the `cli.py` script.

**To view all options:**
```bash
python cli.py --help
```

**Example 1: Running a MARKET order**
Buy 0.01 BTCUSDT at Market Price:
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

**Example 2: Running a LIMIT order**
Sell 0.01 BTCUSDT at a Limit price of 100000:
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 100000
```

## Logs
All API requests, responses, and errors are logged to `trading_bot.log` located in the root of the project.

## Assumptions
- The user has a working Binance Futures Testnet account and valid API keys with permissions to place orders.
- The default `timeInForce` applied for `LIMIT` orders is `GTC` (Good Till Cancelled).
- `python-binance` library has been used under the hood to manage signatures and request routing safely.
