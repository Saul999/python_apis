import requests
from tkinter import *

window = Tk()
window.title("Kanye once said...")
window.config(padx=20, pady=20)

def get_quote():
    data = requests.get(url="https://api.kanye.rest//")
    response = data.json()
    print(f"Kanye: {response["quote"]}")
    quote = response["quote"]
    canvas.itemconfig(quote_text, text=quote)

canvas = Canvas(width=300, height=400)
quote_text = canvas.create_text(150, 207, text="Kquote", width=250, font=("Arial"))
canvas.grid(row=0, column=0)

new_quote = Button(text="Click for Quote", command=get_quote)
new_quote.grid(column=1, row=1)
text = Label()




window.mainloop()