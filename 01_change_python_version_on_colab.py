import subprocess
from datetime import datetime
import sys
import os
import logging

print(f"Running Python File Script: {os.path.basename(__file__)}")


# Get the script name without the extension
script_name = os.path.splitext(os.path.basename(__file__))[0]

# Configure logging
logging.basicConfig(filename=f"log_{script_name}.log", filemode='w', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clone_llama_factory_repo():
    repo_page = 'https://github.com/hiyouga/LLaMA-Factory.git'
    # make sure the repo doesn't already exist; Ask the user if they want to delete it.
    try:
        subprocess.run(f"git clone {repo_page}".split(), check=True)
        logging.info("Repo cloned successfully")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error cloning repo: {e}")
        # Ask the user if they want to delete the repo
        delete_repo = input("Do you want to delete the repo? (y/n)")
        if delete_repo.lower()[0] == 'y':
            # Delete the repo
            subprocess.run(["rm", "-rf", "LLaMA-Factory"], check=True)
            logging.info("Repo deleted successfully")
            # Clone the repo again
            subprocess.run(f"git clone {repo_page}".split(), check=True)
        else:
            logging.info("Repo not cloned")


def check_python_version():
    # using sys module; print current pyton version.
    print(f"Python Version: {sys.version}")

def check_available_python_versions():
    try:
        subprocess.run(["sudo", "update-alternatives", "--config", "python3"], check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error checking available Python versions: {e}")

def update_package_lists():
    try:
        subprocess.run(["sudo", "apt-get", "update", "-y"], check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error updating package lists: {e}")

def install_python_3_11():
    try:
        subprocess.run(["sudo", "apt-get", "install", "python3.11", "python3.11-dev", "python3.11-distutils", "libpython3.11-dev"], check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error installing Python 3.11 and related packages: {e}")


def update_python_alternatives():
    try:
        subprocess.run(["sudo", "update-alternatives", "--install", "/usr/bin/python3", "python3", "/usr/bin/python3.10", "1"], check=True)
        subprocess.run(["sudo", "update-alternatives", "--install", "/usr/bin/python3", "python3", "/usr/bin/python3.11", "2"], check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error updating Python alternatives: {e}")


def verify_python_version():
    try:
        # using python sys module:
        print(f"Python Version: {sys.version}")    
    except subprocess.CalledProcessError as e:
        logging.error(f"Error verifying Python version: {e}")

def install_venv_module():
    try:
        subprocess.run(["sudo", "apt-get", "install", "python3.10-venv"], check=True)
        subprocess.run(["sudo", "apt-get", "install", "python3.11-venv"], check=True)
        print(f'venv module was installed for both Python 3.10 and Python 3.11')
    except subprocess.CalledProcessError as e:
        logging.error(f"Error installing venv module: {e}")

def create_virtual_environment():
    try:
        subprocess.run(["python3.10", "-m", "venv", "env_llama_factory"], check=True)
        subprocess.run(["python3.11", "-m", "venv", "env_python311"], check=True)
        print(f'Two virtual environments were created; env_python311 and env_llama_factory (Python 3.10)')

        # install dotenv for both Python3.10 and python3.11
        subprocess.run(["env_python311/bin/python3", "-m", "pip", "install", "python-dotenv"], check=True)
        subprocess.run(["env_llama_factory/bin/python3", "-m", "pip", "install", "python-dotenv"], check=True)
        print(f'python-dotenv was installed on both environments')
        
    except subprocess.CalledProcessError as e:
        print(f"Error creating virtual environment: {e}")
        logging.error(f"Error creating virtual environment: {e}")

def main():
    print(datetime.now())
    start_install = datetime.now()
    clone_llama_factory_repo()

    check_python_version()
    check_available_python_versions()
    update_package_lists()
    install_python_3_11()
    update_python_alternatives()
    verify_python_version()

    finish_install = datetime.now()
    duration = finish_install - start_install
    print(f"Installation duration: {duration}")

    install_venv_module()
    create_virtual_environment()

if __name__ == "__main__":
    main()
