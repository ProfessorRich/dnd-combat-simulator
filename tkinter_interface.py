import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# Set window size to 1024x720 unless the screen is too small
window_width = min(1024, screen_width)
window_height = min(720, screen_height)
app.geometry(f"{window_width}x{window_height}")

def button_function():
    app.destroy()

# CTkButton example 
button = customtkinter.CTkButton(master=app, text="End!", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()