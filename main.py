import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr_code():
    data = qr_data_entry.get()
    if data:
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="darkblue", back_color="white")

        img = ImageTk.PhotoImage(qr_img)
        qr_label.config(image=img)
        qr_label.image = img
    else:
        messagebox.showerror("Fehler", "Bitte geben Sie Daten für den QR-Code ein.")

def animate_button(button):
    button.config(bg="darkblue", fg="white")
    button.after(200, lambda: button.config(bg="black", fg="lightblue"))

# GUI erstellen
root = tk.Tk()
root.title("QR-Code Generator")
root.geometry("400x500")

# Hintergrundfarbe auf Hellblau setzen
root.configure(bg="lightblue")

font_style = ("Helvetica", 16)

# Überschrift
header_label = tk.Label(root, text="QR-Code Generator", font=font_style, fg="black", bg="lightblue")
header_label.pack(fill=tk.X, pady=10)

# Eingabefeld für QR-Code-Daten
qr_data_label = tk.Label(root, text="Geben Sie die QR-Code-Daten ein:", font=font_style, fg="black", bg="lightblue")
qr_data_label.pack(pady=5)
qr_data_entry = tk.Entry(root, font=font_style, bg="white", fg="black", width=20)
qr_data_entry.pack(pady=5)

# QR-Code generieren-Button
generate_button = tk.Button(root, text="QR-Code generieren", font=font_style, bg="black", fg="lightblue", command=generate_qr_code)
generate_button.pack(pady=10)
generate_button.bind("<Enter>", lambda event, button=generate_button: animate_button(button))

# QR-Code-Anzeige
qr_label = tk.Label(root, font=font_style, fg="white", bg="lightblue")
qr_label.pack()

root.mainloop()
