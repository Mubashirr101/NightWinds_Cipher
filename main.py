from tkinter import *
import customtkinter

alphabet_mapping = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25,
}


def encode():
    plain_text = plain_text_entry.get("0.0", "end").strip().lower()
    keyword = keyword_entry.get().lower()
    if not keyword:
        plain_text_entry.delete("0.0", "end")
        return

    encoded_txt = ""
    for i in range(len(plain_text)):
        plaintxt_char = plain_text[i]
        if plaintxt_char == "\n":
            encoded_char = "\n"  # preserve newline
        else:
            keyword_char = keyword[i % len(keyword)]
            shift = alphabet_mapping[keyword_char]
            if plaintxt_char != " ":
                encoded_char = getChar(encode_char(plaintxt_char, shift))
            else:
                encoded_char = " "
        encoded_txt += encoded_char

    encoded_text_entry.delete("0.0", "end")
    encoded_text_entry.insert("0.0", encoded_txt)


def decode():
    encoded_txt = encoded_text_entry.get("0.0", "end").strip().lower()
    keyword = keyword_entry.get().lower()
    if not keyword:
        plain_text_entry.delete("0.0", "end")
        return

    decoded_txt = ""
    for i in range(len(encoded_txt)):
        encoded_char = encoded_txt[i]
        if encoded_char == "\n":
            decoded_char = "\n"
        else:
            keyword_char = keyword[i % len(keyword)]
            shift = alphabet_mapping[keyword_char]
            if encoded_char != " ":
                decoded_char = getChar(decode_char(encoded_char, shift))
            else:
                decoded_char = " "
        decoded_txt += decoded_char

    plain_text_entry.delete("0.0", "end")
    plain_text_entry.insert("0.0", decoded_txt)


def encode_char(char, shift):
    try:
        if char == " ":
            return " "
        plaintext_num = alphabet_mapping[char]
        encoded_val = (plaintext_num + shift) % 26
        return encoded_val
    except KeyError:
        return char


def decode_char(char, shift):
    try:
        if char == " ":
            return " "
        encoded_num = alphabet_mapping[char]
        decoded_val = (encoded_num - shift) % 26
        return decoded_val
    except KeyError:
        return char


def getChar(numerical_value):
    if numerical_value == " ":
        return " "
    for char, value in alphabet_mapping.items():
        if value == numerical_value:
            return char
    return ""


# Create the main window
customtkinter.set_appearance_mode("dark")
# customtkinter.set_appearance_mode("light")

customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: "blue" (standard), "green", "dark-blue"
window = customtkinter.CTk()
window.geometry("800x400")
window.title("NightWinds Cypher")
# Create labels and text entry fields
keyword_label = customtkinter.CTkLabel(
    window,
    text="Keyword:",
)
keyword_label.grid(row=0, column=0, padx=10, pady=10)

keyword_entry = customtkinter.CTkEntry(
    window,
    placeholder_text="Enter keyword",
    width=150,
    height=30,
    corner_radius=4,
    border_width=3,
    border_color="grey",
    font=("High Tower Text", 20),
)
keyword_entry.grid(row=0, column=1, sticky="w")

plain_text_label = customtkinter.CTkLabel(
    window, text="Plain Text:", fg_color="transparent"
)
plain_text_label.grid(row=1, column=0, padx=10, pady=10)

plain_text_entry = customtkinter.CTkTextbox(
    window,
    width=500,
    height=120,
    corner_radius=2,
    border_width=2,
    font=("High Tower Text", 20),
)
plain_text_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

encoded_text_label = customtkinter.CTkLabel(window, text="Encoded Text:")
encoded_text_label.grid(row=2, column=0, padx=10, pady=10)

encoded_text_entry = customtkinter.CTkTextbox(
    window,
    width=500,
    height=120,
    corner_radius=2,
    font=("High Tower Text", 20),
    border_width=2,
)
encoded_text_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")


# Create buttons for encoding and decoding
encode_button = customtkinter.CTkButton(window, text="Encode", command=encode)
encode_button.grid(row=1, column=2, padx=10, pady=10)

decode_button = customtkinter.CTkButton(window, text="Decode", command=decode)
decode_button.grid(row=2, column=2, padx=10, pady=10)


# Start the GUI event loop
window.mainloop()
