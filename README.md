# Running LLaMA-Factory in Google Colab

This repository provides scripts to set up and run LLaMA-Factory in Google Colab environment.

## Installation and Setup

1. **Clone the Repository**: 
    - Run the following command to clone the repository:
    ```bash
    !git clone https://github.com/hiyouga/run_llama_factory_in_google_colab.git
    ```

2. **Change Python Version on Colab**:
    - Run the script `01_change_python_version_on_colab.py` to change the Python version to 3.11.

3. **Install LLaMA-Factory Dependencies**:
    - Run the script `02_install_llama_factory_in_google_colab.py` to install LLaMA-Factory dependencies.

4. **Run LLaMA-Factory Locally**:
    - Execute the script `03_local_llama_factory.py` to run LLaMA-Factory locally.

5. **Accessing LLaMA-Factory**:
    - After running the script, a GRADIO URL will be generated. Use this URL to access LLaMA-Factory remotely.

## Notes
- Ensure you have a GPU for optimal performance. If not, consider disabling the installation of the `bitsandbytes` library.
- The installation process may take some time, depending on your system's resources.

## Running the Script
In Google Colab, run the following command in a notebook cell:
```python
!python main_script.py
