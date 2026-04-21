import os
from dotenv import load_dotenv

# Try to load from the current directory
load_dotenv()

api_key = os.getenv('BINANCE_API_KEY')
api_secret = os.getenv('BINANCE_API_SECRET')
use_testnet = os.getenv('USE_TESTNET')

print(f"--- Debugging Env Variables ---")
print(f"USE_TESTNET: {use_testnet}")

if not api_key or api_key == "your_testnet_api_key_here":
    print("❌ BINANCE_API_KEY is either missing or still a placeholder.")
else:
    print(f"✅ BINANCE_API_KEY starts with: {api_key[:5]}...")

if not api_secret or api_secret == "your_testnet_api_secret_here":
    print("❌ BINANCE_API_SECRET is either missing or still a placeholder.")
else:
    print(f"✅ BINANCE_API_SECRET is set (length: {len(api_secret)})")
