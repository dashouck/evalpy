import time

from rich.console import Console
from rich.syntax import Syntax
from rich.table import Table
from rich.progress import Progress

console = Console()

def info(str):
    console.print(f"[yellow]{str}[/yellow]")

def error(str):
    console.print(f"[red]{str}[/red]")

def test():
    "test out different capabilities of rich"
    console.print("[bold magenta]Hello[/bold magenta] [underline green]World[/underline green]!")
    
    # code
    code = '''
    def greet(name):
        print(f"Hello, {name}!")
    greet("Rich")
    '''
    syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
    console.print(syntax)

    # tables
    table = Table(title="Sample Table")

    table.add_column("Name", style="cyan", justify="right")
    table.add_column("Age", style="magenta")
    table.add_column("City", style="green")

    table.add_row("John Doe", "30", "New York")
    table.add_row("Jane Smith", "25", "San Francisco")
    table.add_row("Sam Brown", "22", "Austin")

    console.print(table)

    # progress bar
    with Progress() as progress:
        task = progress.add_task("[cyan]Processing...", total=100)
        while not progress.finished:
            progress.update(task, advance=5)
            time.sleep(0.1)


if __name__=="__main__":
    test()

    