import os
import subprocess
from datetime import datetime
import sys
import logging


print(f"Running Python File Script: {os.path.basename(__file__)}")


# Get the script name without the extension
script_name = os.path.splitext(os.path.basename(__file__))[0]

# Configure logging
logging.basicConfig(filename=f"log_{script_name}.log", filemode='w', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_command(command: list[str]) -> None:
    """
    Runs a command using subprocess and handles any exceptions.
    """
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        handle_command_error(e, command)

def handle_command_error(error: Exception, command: list[str]) -> None:
    """
    Handles errors that occur while running a command.
    """
    logging.error(f"Error running command: {error}")
    if isinstance(error, FileNotFoundError):
        logging.error(f"Error: '{command[0]}' not found. Please ensure it is installed and available in your system's PATH.")
    raise error

def main() -> None:
    """
    Main function that installs the LLaMA-Factory repository dependencies.
    """
    try:
        start_install = datetime.now()
        # Check Python version 3.10
        if sys.version_info < (3, 10):
            print("Python 3.10 or higher is required.")
            sys.exit(1)
        else:
            print(f"Python version: {sys.version}")
        


        print("Launch the Gradio Web UI using: llamafactory-cli webui")

        finish_install = datetime.now()
        duration = finish_install - start_install

        print(f"Total installation time: {duration.seconds // 60} minutes.")

    except KeyboardInterrupt:
        print("Installation interrupted by the user.")
    except Exception as e:
        print(f"Error during installation: {e}")
        logging.error(f"Error during installation: {e}")

if __name__ == "__main__":
    main()
