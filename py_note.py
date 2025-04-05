import tkinter as tk
import os

def openWindow():
    
    #Creating window
    window = tk.Tk()
    
  

    #title
    window.title("Harvest Note By Trevor Wooten")

    #Size of window width x height
    window.geometry("700x650")
    
    #Size limits
    window.minsize(200, 200)
    window.maxsize(1200, 1200)
    
    #Window color
    window.configure(background="orange")
    
    
    #label
    title_label = tk.Label(window, text="Harvest Note", font=("Arial", 20))
    
    # Centering
    title_label.pack(expand= True)
    
    #Calling other function parts
    textArea(window)
    

    #Running application
    window.mainloop()
    
def textArea(window):
    
    screen_width = window.winfo_screenwidth()
    
    
    #text area frame
    text_frame = tk.Frame(window, width=1250, height=450)
    
    #Fitting frame the length of screen
    text_frame.pack(expand= True, fill= "x", padx= 5, ipady= 50)
    
    
    #making text box
    text_area = tk.Text(text_frame, font=("Arial", 12), wrap="word")
    text_area.pack(expand= True, fill="both")
    # text_area.place(x=350, y=300, anchor="center")
    # text_area.config(height=30, width=100)
    

    
    
#Calling functino
def main():
    
    #opening window
    openWindow()
    

  
    
    
if __name__ == "__main__":
    main()
    


