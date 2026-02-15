from PIL import Image, ImageFile
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

class Utils:

    def __init__(self):
        pass

    def load_image(self, rel_path: str):
        img_path = BASE_DIR / rel_path  
        return Image.open(img_path)