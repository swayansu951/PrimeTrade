import typer
from rich.console import Console
from rich.table import Table
from typing import Optional
from dotenv import load_dotenv

# Load environment variables once at startup (this loads .env if present)
load_dotenv()

from bot.orders import place_order
from bot.validators import OrderSide, OrderType

app = typer.Typer(help="Binance Futures Testnet Trading CLI")
console = Console()

@app.command()
def trade(
    symbol: str = typer.Option(..., "--symbol", "-s", help="Trading pair symbol (e.g., BTCUSDT)", prompt="Please enter the trading symbol (e.g., BTCUSDT)"),
    side: OrderSide = typer.Option(..., "--side", help="Order side (BUY/SELL)", prompt="Are you placing a BUY or SELL order?"),
    order_type: OrderType = typer.Option(..., "--type", "-t", help="Order type (MARKET/LIMIT)", prompt="Enter the order type (MARKET/LIMIT)"),
    quantity: float = typer.Option(..., "--quantity", "-q", help="Order quantity", prompt="How much quantity would you like to trade?"),
    price: Optional[float] = typer.Option(None, "--price", "-p", help="Price for LIMIT orders")
):
    """
    Submits a trading order to Binance Futures Testnet.
    """
    console.print(f"[bold cyan]Submitting Order Request:[/bold cyan]")
    console.print(f"  Symbol: [yellow]{symbol.upper()}[/yellow]")
    console.print(f"  Side: [yellow]{side.value}[/yellow]")
    console.print(f"  Type: [yellow]{order_type.value}[/yellow]")
    console.print(f"  Quantity: [yellow]{quantity}[/yellow]")
    
    if order_type == OrderType.LIMIT:
        console.print(f"  Price: [yellow]{price}[/yellow]")
        
    try:
        response = place_order(
            symbol=symbol.upper(),
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )
        
        console.print("\n[bold green][+] Order Successfully Placed![/bold green]")
        
        # Display response details nicely in a table
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Detail")
        table.add_column("Value")
        
        keys_to_show = ["orderId", "symbol", "status", "type", "side", "origQty", "executedQty", "avgPrice", "price"]
        for k in keys_to_show:
            if k in response:
                table.add_row(k, str(response[k]))
                
        console.print(table)
        
    except Exception as e:
        console.print(f"\n[bold red]❌ Order Failed![/bold red]")
        console.print(f"[red]Reason: {e}[/red]")

if __name__ == "__main__":
    app()
