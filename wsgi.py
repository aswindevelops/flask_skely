import os
import sys
import site
import inspect
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')  # Path to .env file
load_dotenv(dotenv_path)

root_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

activate_this = f'{root_dir}/env/Scripts/activate_this.py'

with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir(f'{root_dir}/env/Lib/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append(f'{root_dir}')

from averich import create_app

application = create_app()
