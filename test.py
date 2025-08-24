from tkinter import *

# Function to display a warning pop-up
def show_warning(figura):
    kolor=figura[0]
    info=""
    if kolor=="b":
        info=="Biale Wygrały!!!"
    else:
        info=="Czarne wygrały!!!"
    warning_window = Toplevel(root)
    warning_window.geometry("300x200")
    warning_window.title("Zwyciestwo!")
    x="baile wygraly!"
    warning_label = Label(warning_window, text=x, fg="red")
    warning_label.pack(pady=20)
    
    reset_button = Button(warning_window, text="Zacznij od nowa", command=warning_window.destroy)
    reset_button.pack(pady=20)
    
    # Disable the window close button
    warning_window.protocol("WM_DELETE_WINDOW", lambda: None)
    
    # Lock the main root window until the pop-up is closed
    warning_window.transient(root) #zawsze na wieszchu, minimalizuje sie z root 
    warning_window.grab_set()
    root.wait_window(warning_window)

# Create the main root window
root = Tk()
root.geometry("800x800")

# Define the first button
button1 = Button(root, text="Button 1", command=show_warning)
button1.pack(pady=20)  # Add some padding for better spacing

# Define the second button
button2 = Button(root, text="Button 2")
button2.pack(pady=20)  # Add some padding for better spacing

# Start the Tkinter main loop
root.mainloop()
