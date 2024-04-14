import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont


def download():
    filetypes = [('Image files', '*.png;*jpg;*.jpeg')]
    path = tk.filedialog.askopenfilename(filetypes=filetypes)

    if not len(path):
        messagebox.showinfo(title='Oops', message="No image selected!!!")
        return

    if not len(entry_watermark.get()):
        messagebox.showinfo(title='Oops', message="Don't leave any fields empty!!")
        return

    img = Image.open(path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(r'arial.ttf', size=50)

    draw.text((0, 0), entry_watermark.get(), (255, 255, 255), font=font)

    messagebox.showinfo(title='Success', message="The image has been saved!!")
    img.save(f'watermark.{img.format}', format=img.format)


window = tk.Tk()
window.title("Custom Watermark")
window.config(padx=100, pady=50)

label_watermark = tk.Label(text='Enter watermark: ')
label_watermark.grid(row=1, column=0)

entry_watermark = tk.Entry()
entry_watermark.grid(row=1, column=1, columnspan=2, pady=10)

button_download = tk.Button(text='Save Image', padx=20, pady=5, command=download)
button_download.grid(row=2, column=1)


window.mainloop()
