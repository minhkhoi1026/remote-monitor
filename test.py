import pyautogui
import tkinter as tk
from PIL import Image, ImageTk  # Place this at the end (to avoid any conflicts/errors)
import time
import threading
import streaming

window = tk.Tk()
# window.geometry("500x500") # (optional)    
img = ImageTk.PhotoImage(pyautogui.screenshot())
lbl = tk.Label(window, image = img)
lbl.pack()

client = streaming.StreamingClient('127.0.0.1', 9999, lbl)
client.start_stream()

window.mainloop()

qimage = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
pixmap = QPixmap(qimage)
pixmap = pixmap.scaled(700,500, Qt.KeepAspectRatio)
self.__window.setPixmap(pixmap)