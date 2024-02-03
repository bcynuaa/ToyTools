'''
 # @ author: bcynuaa
 # @ date: 2024-02-03 23:21:24
 # @ description: tkinter gui for pdf transfer
 '''

import os
import tkinter
import tkinter.filedialog
from PDFGenerator import PDFGenerator

'''
a main window with:

- a listbox to show the image files
- a button to add new image files with file dialog
- a button to delete selected image files
- a button to set the output path and filename with file dialog
'''

class PDFTransferGUI(PDFGenerator):
    
    def __init__(self) -> None:
        super().__init__()
        self.root_window_ = tkinter.Tk()
        self.root_window_.title("图像 - PDF 转换器")
        self.root_window_.geometry("600x400")
        self.root_window_.resizable(False, False)
        self.root_window_.configure(bg="white")
        # image list box, with size 400x200
        self.image_list_box_ = tkinter.Listbox(self.root_window_, selectmode=tkinter.MULTIPLE)
        self.image_list_box_.configure(width=80, height=12)
        self.image_list_box_.pack()
        self.image_list_box_.configure(bg="white")
        self.image_list_box_.configure(selectbackground="lightblue")
        # buttons with 2*2 grid
        self.button_frame_ = tkinter.Frame(self.root_window_)
        self.button_frame_.configure(bg="white")
        self.button_frame_.pack()
        self.add_image_button_ = tkinter.Button(self.button_frame_, text="添加图像", command=self.addImage)
        self.add_image_button_.configure(width=10, height=2)
        self.add_image_button_.grid(row=1, column=0)
        self.delete_image_button_ = tkinter.Button(self.button_frame_, text="删除图像", command=self.deleteImage)
        self.delete_image_button_.configure(width=10, height=2)
        self.delete_image_button_.grid(row=1, column=1)
        self.set_output_filename_button_ = tkinter.Button(self.button_frame_, text="设置文件名", command=self.setOutputFilenameGUI)
        self.set_output_filename_button_.configure(width=10, height=2)
        self.set_output_filename_button_.grid(row=2, column=0)
        self.transfer_button_ = tkinter.Button(self.button_frame_, text="转换PDF", command=self.transferPDF)
        self.transfer_button_.configure(width=10, height=2)
        self.transfer_button_.grid(row=2, column=1)
        # output label
        self.output_label_ = tkinter.Label(self.root_window_, text="输出路径: ")
        self.output_label_.configure(bg="white")
        self.output_label_.pack()
        # output path label
        self.output_path_label_ = tkinter.Label(self.root_window_, text=self.getOutputPath())
        self.output_path_label_.configure(bg="white")
        self.output_path_label_.pack()
        pass
    
    def addImage(self) -> None:
        # require the image files to end with ".jpg", ".jpeg", ".png", ".bmp"
        image_filenames = tkinter.filedialog.askopenfilenames(filetypes=[("图片文件", "*.jpg;*.jpeg;*.png;*.bmp")])
        for image_filename in image_filenames:
            if os.path.isfile(image_filename) and image_filename.endswith((".jpg", ".jpeg", ".png", ".bmp")):
                self.addNewImage(image_filename)
                self.image_list_box_.insert(tkinter.END, self.image_filenames_[-1])
                pass
            else:
                pass
            pass
        pass
    
    def deleteImage(self) -> None:
        selected_indices = self.image_list_box_.curselection()
        for index in selected_indices:
            self.deleteImageByIndex(index)
            self.image_list_box_.delete(index)
            pass
        pass
    
    def setOutputFilenameGUI(self) -> None:
        # require the output filename to end with ".pdf"
        output_filename = tkinter.filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF 文件", "*.pdf")])
        if output_filename.endswith(".pdf"):
            pure_pdf_filename = os.path.basename(output_filename)
            pure_pdf_path = os.path.dirname(output_filename)
            self.setOutputPath(pure_pdf_path)
            self.setOutputFilename(pure_pdf_filename)
            self.output_path_label_.configure(text=self.getOutputPath())
            pass
        else:
            pass
        pass
    
    def transferPDF(self) -> None:
        self.exportPDF()
        pass
    
    pass