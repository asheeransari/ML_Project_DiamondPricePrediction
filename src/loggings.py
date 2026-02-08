import logging
import os
from datetime import datetime

Folder_path = os.path.join(os.getcwd(),"logs")
os.makedirs(Folder_path,exist_ok = True)
File = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"

log_file = os.path.join(Folder_path,File)

logging.basicConfig(
    filename = log_file,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s %(message)s",
    level = logging.INFO
)