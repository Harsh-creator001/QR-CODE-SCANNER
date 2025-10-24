import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from pyzbar.pyzbar import decode

def decode_qr(image_path):
    img = Image.open(image_path)
    decoded = decode(img)
    if decoded:
        return decoded[0].data.decode('utf-8')
    return "No QR code found!"

def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    if file_path:
        # Preview image
        img = Image.open(file_path)
        img.thumbnail((350, 350))
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk
        # Decode QR
        result = decode_qr(file_path)
        decoded_var.set(result)
        copy_button.config(state='normal' if result != "No QR code found!" else 'disabled')

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(decoded_var.get())
    messagebox.showinfo("Clipboard", "Decoded data copied to clipboard!")

root = tk.Tk()
root.title("QR Code Decoder")

# Window customization
root.geometry("500x600")
root.iconbitmap('incognito.ico')  # Replace with your logo file if needed

# Title
main_title = tk.Label(root, text="QR CODE DECODER", font=("Arial", 18, "bold"))
main_title.pack(pady=10)

# Upload button
upload_btn = ttk.Button(root, text="Upload Image", command=open_file)
upload_btn.pack(pady=10)

# Image preview
image_label = tk.Label(root, width=350, height=350, bg="#f0f0f0", relief="groove")
image_label.pack(pady=10)

# Decoded data display
decoded_var = tk.StringVar()
decoded_label = tk.Label(root, text="Decoded Data:", font=('Arial', 12))
decoded_label.pack(pady=(10,0))
decoded_text = ttk.Entry(root, textvariable=decoded_var, width=55, font=('Arial', 11))
decoded_text.pack(pady=(0,10))

# Copy button
copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, state='disabled')
copy_button.pack(pady=10)

root.mainloop()
