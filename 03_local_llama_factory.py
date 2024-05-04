import os

import subprocess
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
os.environ['GRADIO_SERVER_PORT'] = '7860'
os.environ['GRADIO_SHARE'] = 'True'

subprocess.run(["llamafactory-cli", "webui"])