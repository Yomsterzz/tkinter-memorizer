import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfile

def open_file():
    filetoopen = askopenfile(mode="r", filetypes=[("Text files", "*.txt")])
    if filetoopen is not None:
        file_data = filetoopen.read()
        for line in file_data.splitlines():
            all_data.insert(tk.END, line)
        
def save_file():
    filetosave = asksaveasfile(filetypes=[("Text document", "*.txt"), ("All files", "*.*")], defaultextension=".txt")
    if filetosave is not None:
        for i in all_data.get(0, tk.END):
            print(i, file=filetosave)
            
def add_item():
    data = data_entry.get()
    if data:
        all_data.insert(tk.END, data)
    
def delete_data():
        all_data.delete(0, tk.END)

window = tk.Tk()
window.title("Memorizer")
window.geometry("600x450")
window.configure(bg="lightblue")

cool_font = ("Arial", 20)

button_frame = tk.Frame(window, bg="lightblue")
button_frame.pack(pady=10)

open_button = tk.Button(button_frame, text="OPEN", font=cool_font, width=10, command=open_file)
open_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="DELETE", font=cool_font, width=10, command=delete_data)
delete_button.grid(row=0, column=1, padx=5)

save_button = tk.Button(button_frame, text="SAVE", font=cool_font, width=10, command=save_file)
save_button.grid(row=0, column=2, padx=5)

data_entry = tk.Entry(window, font=cool_font, width=40)
data_entry.pack(pady=10)

add_button = tk.Button(window, text="ADD", font=cool_font, width=10, command=add_item)
add_button.pack(pady=5)

list_frame = tk.Frame(window, bg="lightblue")
list_frame.pack(pady=10)

all_data = tk.Listbox(list_frame, font=cool_font, width=50, height=15)
all_data.pack(side=tk.LEFT, fill=tk.BOTH)

window.mainloop()