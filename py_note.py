import tkinter as tk
import os
from tkinter import filedialog #for saving

def open_window():
    
    #Creating window
    window = tk.Tk()
    
    #making toolbar frame
    toolbar_frame = tk.Frame(window, height= 25, bg="black")
    toolbar_frame.pack(side="top", fill="x")
    
    #Showing toolbar
    toolbar_buttons(window, toolbar_frame)
    
    
    #label
    title_label = tk.Label(window, text="Harvest Note", font=("Arial", 20))
    
    # Centering title label
    title_label.pack(expand= True)
    
    
    #Calling other function parts
    text_area(window)
    
    
    
    
    
    #title
    window.title("Harvest Note By Trevor Wooten")

    #Size of window width x height
    window.geometry("700x650")
    
    #Size limits
    window.minsize(200, 200)
    window.maxsize(1200, 700)
    
    #Window color
    window.configure(background="orange")

    
    
    

    #Running application
    window.mainloop()
    
    
    
def text_area(window):

    #text area frame
    text_frame = tk.Frame(window, width=1250, height=450)
    
    #Fitting frame the length of screen
    text_frame.pack(expand= True, fill= "x", padx= 5, ipady= 50)
    
    
    #making text box
    text_area = tk.Text(text_frame, font=("Arial", 12), wrap="word")
    text_area.pack(expand= True, fill="both")
    # text_area.place(x=350, y=300, anchor="center")
    # text_area.config(height=30, width=100)
    
    #returning this for the buttons
    return text_area
    
    
    
    
def toolbar_buttons(window, toolbar_area):
    
    screen_width = window.winfo_screenwidth()


    #Buttons
    save_button = tk.Button(toolbar_area, text="Save", bg="white")
    open_button = tk.Button(toolbar_area, text="Open", bg="white")
    
    #Positioning
    save_button.pack(side="left", padx= 10)
    open_button.pack(side="left", padx= 4)
    
    
def save_file(text_box):
    
    #Askinf user where to put file
    file_path = filedialog.askopenfilename( defaultextension= ".txt", filetypes=[("Text Files", "*.txt")])
    
    
    

    
    
#Calling functino
def main():
    
    #opening window
    open_window()
    

  
    
    
if __name__ == "__main__":
    main()
    


