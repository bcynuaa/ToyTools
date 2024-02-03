'''
 # @ author: bcynuaa
 # @ date: 2024-02-03 22:52:36
 # @ description: pdf generator for image files
 '''

import os
import img2pdf

class PDFGenerator:
    
    def __init__(self) -> None:
        self.image_filenames_: list = []
        self.output_path_: str = os.path.abspath("./")
        self.output_filename_: str = "output.pdf"
        pass
    
    def addNewImage(self, image_filename: str) -> None:
        image_filename = os.path.abspath(image_filename)
        self.image_filenames_.append(image_filename)
        pass
    
    def deleteImageByIndex(self, index: int) -> None:
        self.image_filenames_.pop(index)
        pass
    
    def setOutputPath(self, output_path: str) -> None:
        self.output_path_ = output_path
        pass
    
    def setOutputFilename(self, output_filename: str) -> None:
        self.output_filename_ = output_filename
        pass
    
    def getOutputPath(self) -> str:
        return os.path.join(self.output_path_, self.output_filename_)
        pass
    
    def exportPDF(self) -> None:
        with open(self.getOutputPath(), "wb") as pdf_file:
            pdf_file.write(img2pdf.convert(self.image_filenames_))
        pass
    
    pass