import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk, ImageEnhance
import pytesseract
import cv2
import numpy as np

# Set the tesseract_cmd to the path where tesseract is installed (adjust as needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")])
    if file_path:
        load_image(file_path)
        # Show OCR buttons after an image is selected
        ocr_printed_btn.pack(side=tk.LEFT, padx=5)
        ocr_handwritten_btn.pack(side=tk.LEFT, padx=5)
        discard_btn.pack(side=tk.LEFT, padx=5)
        export_btn.pack(side=tk.LEFT, padx=5)

def load_image(file_path):
    global img, img_for_ocr
    image = Image.open(file_path)
    img_for_ocr = image  # Store the original PIL image for OCR
    thumbnail_image = image.copy()  # Make a copy of the original image for the thumbnail
    thumbnail_image.thumbnail((400, 400))  # Resize only the copy for display purposes
    img = ImageTk.PhotoImage(thumbnail_image)
    img_label.config(image=img)
    img_label.image = img

def discard_image():
    global img, img_for_ocr
    img = None
    img_for_ocr = None
    img_label.config(image='')
    result_text.delete(1.0, tk.END)
    messagebox.showinfo("Image Discarded", "The selected image has been discarded.")
    # Hide OCR buttons and result text box
    ocr_printed_btn.pack_forget()
    ocr_handwritten_btn.pack_forget()
    discard_btn.pack_forget()
    export_btn.pack_forget()
    result_text.pack_forget()

def preprocess_image(image):
    # Convert to grayscale
    gray = image.convert('L')

    # Increase contrast
    enhancer = ImageEnhance.Contrast(gray)
    gray = enhancer.enhance(2)

    # Convert to OpenCV format
    open_cv_image = np.array(gray)

    # Apply thresholding
    _, binary = cv2.threshold(open_cv_image, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Remove noise
    denoised = cv2.fastNlMeansDenoising(binary, None, 30, 7, 21)

    # Resize image
    resized = cv2.resize(denoised, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)

    # Convert back to PIL format
    processed_image = Image.fromarray(resized)
    return processed_image

def perform_ocr(ocr_mode):
    if img_for_ocr is None:
        messagebox.showerror("Error", "No image selected")
        return
    
    if ocr_mode == 'handwritten':
        config = '--psm 6'  # Adjust as needed for better results with handwritten text
        processed_image = preprocess_image(img_for_ocr)
    else:
        config = ''
        processed_image = img_for_ocr

    text = pytesseract.image_to_string(processed_image, config=config)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, text)
    # Show result text box
    result_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=10)

def export_text():
    if result_text.get(1.0, tk.END).strip():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(result_text.get(1.0, tk.END).strip())
            messagebox.showinfo("Export Successful", f"Text exported to {file_path}")
    else:
        messagebox.showerror("Error", "No text to export")

# Create main window
root = tk.Tk()
root.title("ImageToText")
root.geometry("1080x720")
root.configure(bg='#2e3f4f')

# Define styles
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), padding=10)
style.configure('TLabel', background='#2e3f4f', foreground='white', font=('Helvetica', 12))
style.configure('TFrame', background='#2e3f4f')

# Create frames
frame_top = ttk.Frame(root, padding=(20, 10))
frame_top.pack(side=tk.TOP, fill=tk.X)
frame_bottom = ttk.Frame(root, padding=(20, 10))
frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Create widgets
title_label = ttk.Label(frame_top, text="OCR Image to Text", font=('Helvetica', 16, 'bold'))
title_label.pack(side=tk.TOP, pady=10)

img_label = ttk.Label(frame_top)
img_label.pack(side=tk.TOP, pady=10)

button_frame = ttk.Frame(frame_top)
button_frame.pack(side=tk.TOP, pady=10)

select_img_btn = ttk.Button(button_frame, text="Select Image", command=select_image)
select_img_btn.pack(side=tk.LEFT, padx=5)

discard_btn = ttk.Button(button_frame, text="Discard Image", command=discard_image)

ocr_printed_btn = ttk.Button(button_frame, text="OCR Printed Text", command=lambda: perform_ocr('printed'))
ocr_handwritten_btn = ttk.Button(button_frame, text="OCR Handwritten Text", command=lambda: perform_ocr('handwritten'))

export_btn = ttk.Button(button_frame, text="Export Text", command=export_text)

result_text = tk.Text(frame_bottom, wrap=tk.WORD, font=('Helvetica', 12), bg='#f7f7f7', fg='#333333')

# Initialize global variables
img = None
img_for_ocr = None

# Start the main loop
root.mainloop()