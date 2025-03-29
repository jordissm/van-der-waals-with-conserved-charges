from pathlib import Path
from rich.console import Console
from rich.traceback import install
from core.config import Config
from core.runner import CPPRunner

# Install rich traceback for better error handling
install(show_locals=True)

def main():
    console = Console()

    config_path = Path("./input/config.yml")
    output_file = Path("./output/results.h5")

    config = Config(config_path)

    runner = CPPRunner(config, output_file)

    console.print("[bold green]Starting simulations for all input files...[/bold green]")
    runner.run()
    console.print(f"[bold blue]All results saved to {output_file}[/bold blue]")

if __name__ == "__main__":
    main()
