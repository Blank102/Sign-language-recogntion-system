import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tensorflow.keras.models import load_model
from collections import deque, Counter
import time

# ----------------------------
# CONFIG
# ----------------------------
IMG_SIZE = 128
CONFIDENCE_THRESHOLD = 0.7
SMOOTHING_WINDOW = 10
CHAR_DELAY = 1.0  # seconds between accepted characters

CLASS_NAMES = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    'del','nothing','space'
]

# ----------------------------
# LOAD MODEL
# ----------------------------
model = load_model("asl_model.h5")

prediction_buffer = deque(maxlen=SMOOTHING_WINDOW)
output_text = ""
last_char_time = time.time()

# ----------------------------
# TKINTER WINDOW
# ----------------------------
root = tk.Tk()
root.title("Sign Language to Text")

WINDOW_WIDTH = 750
WINDOW_HEIGHT = 600

root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# ----------------------------
# FRAMES
# ----------------------------
video_frame = tk.Frame(root, bg="#f0f0f0")
video_frame.pack(pady=8)

text_frame = tk.Frame(root, bg="#f0f0f0")
text_frame.pack(pady=6)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

# ----------------------------
# VIDEO PANEL
# ----------------------------
video_label = tk.Label(video_frame, bg="#f0f0f0")
video_label.pack(anchor="center")

# ----------------------------
# TEXT AREA
# ----------------------------
text_box = tk.Text(
    text_frame,
    height=3,
    width=75,
    font=("Arial", 14)
)
text_box.pack()

# ----------------------------
# BUTTON FUNCTIONS
# ----------------------------
def clear_text():
    global output_text
    output_text = ""
    text_box.delete("1.0", tk.END)

def save_text():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]
    )
    if file_path:
        with open(file_path, "w") as f:
            f.write(output_text)

def quit_app():
    cap.release()
    root.destroy()

# ----------------------------
# BUTTONS
# ----------------------------
tk.Button(
    button_frame,
    text="Clear All",
    width=15,
    height=2,
    bg="#e0e0e0",
    command=clear_text
).pack(side=tk.LEFT, padx=10)

tk.Button(
    button_frame,
    text="Save to Text File",
    width=20,
    height=2,
    bg="#4CAF50",
    fg="white",
    command=save_text
).pack(side=tk.LEFT, padx=10)

tk.Button(
    button_frame,
    text="Quit",
    width=10,
    height=2,
    bg="#f44336",
    fg="white",
    command=quit_app
).pack(side=tk.LEFT, padx=10)

# ----------------------------
# WEBCAM
# ----------------------------
cap = cv2.VideoCapture(0)

def update_frame():
    global output_text, last_char_time

    ret, frame = cap.read()
    if not ret:
        return

    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (650, 450))

    # ROI
    x1, y1, x2, y2 = 250, 100, 450, 300
    roi = frame[y1:y2, x1:x2]

    roi_resized = cv2.resize(roi, (IMG_SIZE, IMG_SIZE))
    roi_norm = roi_resized / 255.0
    roi_input = np.reshape(roi_norm, (1, IMG_SIZE, IMG_SIZE, 3))

    preds = model.predict(roi_input, verbose=0)
    confidence = np.max(preds)
    raw_label = CLASS_NAMES[np.argmax(preds)]

    if confidence >= CONFIDENCE_THRESHOLD:
        prediction_buffer.append(raw_label)
    else:
        prediction_buffer.append("nothing")

    label = Counter(prediction_buffer).most_common(1)[0][0]

    # ----------------------------
    # SENTENCE LOGIC (STABLE)
    # ----------------------------
    current_time = time.time()

    if current_time - last_char_time > CHAR_DELAY:
        if label == "space":
            output_text += " "
            last_char_time = current_time

        elif label == "del":
            output_text = output_text[:-1]
            last_char_time = current_time

        elif label != "nothing":
            if len(output_text) == 0 or output_text[-1] != label:
                output_text += label
                last_char_time = current_time

        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, output_text)

    # ----------------------------
    # DRAW ROI + LABEL
    # ----------------------------
    color = (0,255,0) if confidence >= CONFIDENCE_THRESHOLD else (0,0,255)

    cv2.rectangle(frame, (x1,y1), (x2,y2), color, 2)
    cv2.putText(
        frame,
        f"{label} ({confidence:.2f})",
        (x1, y1-10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        color,
        2
    )

    # ----------------------------
    # TKINTER IMAGE UPDATE
    # ----------------------------
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame_rgb)
    imgtk = ImageTk.PhotoImage(image=img)

    video_label.imgtk = imgtk
    video_label.configure(image=imgtk)

    root.after(10, update_frame)

# ----------------------------
# START
# ----------------------------
update_frame()
root.mainloop()

