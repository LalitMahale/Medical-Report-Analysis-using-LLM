import os
from pathlib import Path

list_file = [
    "src/__init__.py",
    "src/pipeline.py",
    "src/settings.py",
    "src/prompts.py",
    "logs/medical_report_analysis.log",
    "test_docs/.gitkeep",
    "app.py",
    "experiments/experiments.ipynb",
    ".env",
    "Dockerfile",
    "requirements.txt",
    ".gitignore",
    "README.md",


]


for file in list_file:
    file = Path(file)
    folder, filename = os.path.split(file)

    if not os.path.exists(folder) and folder != "":
        os.makedirs(folder,exist_ok=True)

    if not os.path.exists(file) or (os.path.getsize(file)==0):
        with open(file=file,mode="w") as f:
            pass

