import tkinter as tk
from PIL import ImageTk, Image
from tts import  convert_text_to_speech
from stt import convert_speech_to_text
from camera import start

# Create the main window
window = tk.Tk()
window.title("DEAF MUTE HELPER")
window.geometry("800x600")

# Set background image
background_image = Image.open(r"static\images\wal.jpg")  # Replace "background.jpg" with your own image file
background_image = background_image.resize((800, 600), Image.ANTIALIAS)
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def camera_start():
    start()

# Create the buttons
launch_button = tk.Button(window, text="Launch Camera", command=camera_start)
launch_button.place(x=100, y=50)

def submit():
    text = text_entry.get()
    convert_text_to_speech(text)
    if text == 'hello':
        # set image to hello.png
        image_path = "image.jpg"  # Replace "image.jpg" with your own image file
        image = Image.open(r"static\images\microphone.jpg")
        image = image.resize((350, 263), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(window, image=photo)
        image_label.place(x=80, y=180)
        

# on click of submit button
submit_button = tk.Button(window , text="Submit",command=submit)
submit_button.place(x=600, y=50)

# Create the text entry
text_entry = tk.Entry(window)
text_entry.place(x=400, y=50)

# Create the image on the right side
image_path = "image.jpg"  # Replace "image.jpg" with your own image file
image = Image.open(r"static\images\deaf.webp")
image = image.resize((200, 400), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(window, image=photo)
image_label.place(x=80, y=180)

# Create a label on the side of the window
label = tk.Label(window, text="Text")
label.place(x=450, y=80)

# Run the Tkinter event loop
window.mainloop()
