import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "mlProject"


list_of_files = [
    ".github/workflows/.gitkeep",
    "src/{}/__init__.py".format(project_name),
    "src/{}/components/__init__.py".format(project_name),
    "src/{}/utils/__init__.py".format(project_name),
    "src/{}/utils/common.py".format(project_name),
    "src/{}/config/__init__.py".format(project_name),
    "src/{}/config/configuration.py".format(project_name),
    "src/{}/pipeline/__init__.py".format(project_name),
    "src/{}/entity/__init__.py".format(project_name),
    "src/{}/entity/config_entity.py".format(project_name),
    "src/{}/constants/__init__.py".format(project_name),
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info("Creating directory: {} for the file: {}".format(filedir, filename))

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info("Creating empty file: {}".format(filepath))


    else:
        logging.info("{} already exists".format(filename))