#!/usr/bin/python3
import tkinter as tk;

SECRET = 33

def decode():
    try:
        numbers = entry_decoder.get().strip().split("!")
        sentence= [chr(int(int(x)/SECRET)) for x in numbers]
        sentence = "".join(sentence)
        decode_to_encode_label.config(text=f"decoded value: {sentence}")
    except:
        print("some error occurred")


def encode():
    try:
        s = entry_encoder.get()
        numbers = [(str(ord(ch)*SECRET)) for ch in s ]
        numbers = "!".join(numbers)
        encode_to_decode_label.config(text=f"encoded value: {numbers}")
    except:
        print("some error occurred")

def copy_to_clipboard(event):
    app.clipboard_clear()
    widget = event.widget
    text = widget.cget("text")
    text = text.replace("encoded value: ", "") if "encoded value:" in text else text.replace("decoded value: ", "")
    app.clipboard_append(text)
    app.update()
    original_color = widget.cget("bg")
    widget.config(bg="lightblue")
    app.after(150, lambda: widget.config(bg=original_color))

app = tk.Tk()
app.geometry("800x800")  
app.title("encoder/decoder")


encoder_frame = tk.Frame(app, pady=20)
encoder_frame.pack(fill='x')

separator_frame = tk.Frame(app, height=2, bg='gray75')  
separator_frame.pack(fill='x', pady=30)  

decoder_frame = tk.Frame(app, pady=20)
decoder_frame.pack(fill='x')

'''
encoder
'''
label_encoder = tk.Label(encoder_frame,text="encoder: <enter text here>")
label_encoder.pack(pady=10)

entry_encoder = tk.Entry(encoder_frame,width=200)
entry_encoder.pack(pady=10)

encode_to_decode_label = tk.Label(encoder_frame, text="encoded value: ",cursor="hand2",wraplength=500)
encode_to_decode_label.pack(pady=10)
encode_to_decode_label.bind('<Button-1>', copy_to_clipboard)

compute_encode_button = tk.Button(encoder_frame, text="=>encode", command=encode)
compute_encode_button.pack(pady=10)

'''
encoder
'''



'''
decoder
'''
label_decoder = tk.Label(decoder_frame,text="decoder: <enter numbers here>")
label_decoder.pack(pady=10)

entry_decoder = tk.Entry(decoder_frame,width=200)
entry_decoder.pack(pady=10)

decode_to_encode_label = tk.Label(decoder_frame, text="decoded value:",cursor="hand2",wraplength=500)
decode_to_encode_label.pack(pady=10)
decode_to_encode_label.bind('<Button-1>', copy_to_clipboard)



compute_decode_button = tk.Button(decoder_frame, text="=>decode", command=decode)
compute_decode_button.pack(pady=10)
'''
decoder
'''

app.mainloop()
