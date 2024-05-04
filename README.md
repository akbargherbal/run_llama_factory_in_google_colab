# LLaMA-Factory Google Colab Setup

This repository provides scripts and instructions to set up and run LLaMA-Factory within a Google Colab environment.

## Files

- **01_change_python_version_on_colab.py**: This script checks and updates the Python version to 3.11, sets up virtual environments for both Python 3.10 and 3.11, and installs the necessary venv module.
- **02_install_llama_factory_in_google_colab.py**: This script installs the required dependencies for LLaMA-Factory and provides instructions for launching the Gradio web UI.
- **03_local_llama_factory.py**: This script sets environment variables and launches the LLaMA-Factory web UI locally within Colab.
- **main_script.py**: This is the main script that orchestrates the entire setup process by running the other scripts in sequence. It also activates the virtual environment and installs additional required libraries.
- **README.md**: This file provides a brief overview of the repository and instructions on running the scripts.

## Instructions

1. Open the `main_script.py` file in Google Colab.
2. Run the entire script. This will execute the following steps:
   - Update Python version and set up virtual environments.
   - Install LLaMA-Factory dependencies.
   - Activate the virtual environment and install additional libraries.
   - Launch the LLaMA-Factory web UI locally within Colab.
3. Once the script finishes, you will receive a Gradio URL. Access this URL to interact with the LLaMA-Factory web UI and utilize its features.

## Notes

- The installation process may take some time depending on your internet connection and the availability of resources.
- If you do not have a GPU available, you can disable the installation of the `bitsandbytes` library by commenting out the corresponding line in the `main_script.py` file.
- Ensure you have sufficient disk space available in your Google Colab environment.

## Disclaimer

This repository is provided for educational and experimental purposes only. Please refer to the official LLaMA-Factory documentation for detailed information and support.
