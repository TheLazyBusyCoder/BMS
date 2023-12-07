
import tkinter as tk
from tkinter import ttk
from gui_add_frame import AddFrame
from gui_show_frame import ShowFrame

def on_dropdown_select(event):
    global window 
    selected_option = dropdown.get()
    if selected_option == "Add":
        window = 0
    elif selected_option == "Show":
        window = 1
    else:
        window = -1
    update_ui()
    
def update_ui():
    global window 
    global add_frame
    global show_frame
    
    add_frame.destroy()
    show_frame.destroy()
    
    if window == 0:
        add_frame = AddFrame(main_frame)
        add_frame.start(main_frame)
    if window == 1:
        show_frame = ShowFrame(main_frame)
        show_frame.start()
       
root = tk.Tk()
root.title("BMS by thelazybusycoder + chatgpt")
# root.wm_state('zoomed')
root.resizable(width=False, height=False)
root.geometry("890x620")

navbar_frame = tk.Frame(root, bg="black" , highlightthickness=1, highlightbackground="white")
navbar_frame.pack(side="top", fill="x")
company_label = tk.Label(navbar_frame, text="Company Name", font=("Arial", 30), padx=10, bg="black" , fg='white')
company_label.pack(side="left")
options = ["Add", "Show", "Update", "Delete"]
selected_option = tk.StringVar()
dropdown = ttk.Combobox(navbar_frame, textvariable=selected_option, values=options, state="readonly", width=10 , height=50)
dropdown.set("Options")
dropdown.configure(font=('Arial', 20))
dropdown.bind("<<ComboboxSelected>>", on_dropdown_select)
dropdown.pack(side="right", padx=10)

main_frame = tk.Frame(root, bg="black")
main_frame.pack(fill="both", expand=True)

add_frame = AddFrame(main_frame)
show_frame = ShowFrame(main_frame)

window = -1

root.mainloop()







