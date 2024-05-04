import subprocess
import os
from pathlib import Path
import os
import logging

print(f"Running Python File Script: {os.path.basename(__file__)}")


# Get the script name without the extension
script_name = os.path.splitext(os.path.basename(__file__))[0]

# Configure logging
logging.basicConfig(filename=f"log_{script_name}.log", filemode='w', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



# Change the current working directory to the script's directory
try:
    script_dir = Path(__file__).parent.resolve()
    os.chdir(script_dir)
except Exception as e:
    logging.error(f"Error changing working directory: {e}")
    raise

# Run the first script
try:
    command = ["python3.10", "01_change_python_version_on_colab.py"]
    subprocess.run(command)
    logging.info('Successful running of 01_change_python_version_on_colab.py')
except Exception as e:
    logging.error(f"Error running command: {command}")
    logging.error(f"Error running script: {e}")
    raise

# Run the second script
try:
    command = ["python3.10", "02_install_llama_factory_in_google_colab.py"]
    subprocess.run(command)
    logging.info('Successful running of 02_install_llama_factory_in_google_colab.py')
except Exception as e:
    logging.error(f"Error running command: {command}")
    logging.error(f"Error running script: {e}")
    raise

# Activate the virtual environment
try:
    venv_path = os.path.join(script_dir, "env_llama_factory", "bin", "activate")
    subprocess.run(["source", venv_path], shell=True)
    logging.info(f"Virtual environment activated: {venv_path}")
    print(f"Virtual environment activated: {venv_path}")
    # pip install GitPython
    subprocess.run(["pip", "install", "GitPython"])
    print("GitPython installed")
    logging.info("GitPython installed")
    
    # change the directory to the LLaMA-Factory repository
    os.chdir("LLaMA-Factory")
    print("Changed directory to LLaMA-Factory")
    logging.info("Changed directory to LLaMA-Factory")
    subprocess.run(['pip', 'install', '-e', '.[metrics]'])
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
    subprocess.run(['pip', 'install', 'gradio'])
    subprocess.run(['pip', 'install', 'bitsandbytes'])


except Exception as e:
    logging.error(f"Error activating virtual environment: {e}")
    raise

# Run the third script within the activated virtual environment
try:
    # change directory go back
    os.chdir("..")
    command = ["python", "03_local_llama_factory.py"]
    subprocess.run(command, env=os.environ.copy())
    logging.info('Successful running of 03_local_llama_factory.py')
except Exception as e:
    logging.error(f"Error running command: {command}")
    logging.error(f"Error running script: {e}")
    raise