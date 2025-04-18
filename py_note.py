import tkinter as tk
from tkinter import filedialog #for saving
from tkinter import colorchooser #changing background



def open_window():


    #Creating window
    window = tk.Tk()
    
    #Word counter boolean
    global isWord 
    isWord= tk.BooleanVar(value=True)

    global toggle_switch
    # Toggle variable to track whether we're showing words or characters
    toggle_switch = tk.StringVar(value="words")


    #title
    window.title("Harvest Note By Trevor Wooten")

    #making toolbar frame
    toolbar_frame = tk.Frame(window, height= 25, bg="black")
    toolbar_frame.pack(side="top", fill="x")

    # title label
    title_label = tk.Label(window, text="Harvest Note", font=("Arial", 20))

    # Centering title label
    title_label.pack(expand= True, pady=10)

    #Making text area variable
    global text_box
    text_box = text_area(window)

    #Showing toolbar
    toolbar_buttons(window, toolbar_frame, text_box, isWord)

    #Word counter
    word_counter(window, text_box)

    #Size of window width x height
    window.geometry("700x650")

    #Size limits
    window.minsize(200, 650)
    window.maxsize(1200, 650)

    #Window color
    window.configure(background="orange")




    #Running application
    window.mainloop()



def text_area(window):

    #text area frame
    text_frame = tk.Frame(window, width=1250, height=450)

    #Fitting frame the length of screen
    text_frame.pack(expand= True, fill= "x", padx= 5, pady=(0, 20))


    #making text box
    text_area = tk.Text(text_frame, font=("Arial", 12), wrap="word")
    text_area.pack(expand= True, fill="both")

    text_area.config(height=29)

    #returning this for the buttons
    return text_area



def toolbar_buttons(window, toolbar_frame, text_box, isWord):

    #Buttons and adding the methods
    save_button = tk.Button(toolbar_frame, text="Save", bg="white", command=lambda: save_file(text_box))
    open_button = tk.Button(toolbar_frame, text="Open", bg="white", command=lambda: open_file(text_box))
    style_button = tk.Button(toolbar_frame, text="Style", bg="white", command=lambda: change_bg(window))

    #Switch button
    change_count_button = tk.Button(toolbar_frame, text="Word/Character Count", bg="white", command=lambda: switch_count_display(isWord))


    #Positioning
    save_button.pack(side="left", padx= 10)
    open_button.pack(side="left", padx= 10)
    style_button.pack(side="left", padx= 10)
    change_count_button.pack(side="right", padx= 10)


def save_file(text_box):

    #Askinf user where to put file
    file_path = filedialog.asksaveasfilename( defaultextension= ".txt", filetypes=[("*.txt", "*.txt")], initialfile="Name your document here!")

    #When chosen path
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            content = text_box.get("1.0", "end-1c")
            file.write(content)


def open_file(text_box):

    #Asking user what file to open
    file_path = filedialog.askopenfilename(defaultextension= ".txt", filetypes=[("*.txt", "*.txt")])

    #When chosen path
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            #Reading file
            content = file.read()
            text_box.delete("1.0", "end")
            text_box.insert("1.0", content)


#Change background
def change_bg(window):

    new_color = colorchooser.askcolor(title = "Select a color")

    if new_color:
        hex_color = new_color[1]
        window.configure(bg= hex_color)



def word_counter(window, text_box):
    #Making it available to update counter
    global word_label 

    #Showing words
    word_label = tk.Label(window, text="Words: 0", fg="white", bg="black", font=("Arial", 12), padx= 1)
    word_label.pack(side="bottom", anchor="w", ipadx= 10)

    #Binding to key release
    text_box.bind("<KeyRelease>", update_counter)


    

def update_counter(event=None):

    text = text_box.get("1.0", "end-1c")

    #getting words
    words = len(text.split())

    #getting characters
    characters = len(text.replace(" ", ""))

    if isWord.get():
        #Binding it to the word label
        word_label.config(text=f"Words: {words}")
    else:
        word_label.config(text=f"Characters: {characters}")



def switch_count_display(isWord):
    isWord.set(not isWord.get())
    update_counter()



#Calling functino
def main():

    #opening window
    open_window()





if __name__ == "__main__":
    main()



