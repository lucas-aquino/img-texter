from PIL import Image
import pytesseract as tct

class Texter:
    __imagePath : Image

    def __init__(self, imgPath: str):
        self.setNewImage(imgPath = imgPath)

    def getText(self) -> str:
        return tct.image_to_string(self.__imagePath)

    def getImagePath(self) -> str:
        return self.__imagePath

    def setNewImage(self, imgPath : str):
        self.__imagePath = Image.open(imgPath)

    def __str__(self) -> str:
        return self.getText()