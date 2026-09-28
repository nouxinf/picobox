import os
import glob
import shutil

SOURCE_DIR = os.path.dirname(os.path.abspath(__file__))
APP_PATH = "F:/"
INSTALL_PATH = ""
FILES_TO_TRANSFER = ["code.py", "font5x8.bin", "hardware.py"]
DIRS_TO_TRANSFER = ["lib", "games"]
full_install_path = os.path.join(APP_PATH, INSTALL_PATH)

if os.path.isdir(APP_PATH):
    os.makedirs(full_install_path, exist_ok=True)

    for filename in FILES_TO_TRANSFER:
        src = os.path.join(SOURCE_DIR, filename)
        dst = os.path.join(full_install_path, filename)
        shutil.copy(src, dst)

    for dirname in DIRS_TO_TRANSFER:
        src = os.path.join(SOURCE_DIR, dirname)
        dst = os.path.join(full_install_path, dirname)
        shutil.copytree(src, dst, dirs_exist_ok=True, copy_function=shutil.copy)
else:
    print(
        f"Warning: {APP_PATH} does not exist, skipping installation. You probably need to change the directory in APP_PATH"
    )
