from tkinter import *
from tkinter import filedialog

# Adding comment to initiate github Action


def main():

    file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))

    window = Tk()

    window.title("Welcome to LikeGeeks app")
    window.geometry("400x300")

    lbl = Label(window, text=file, font=("arial bold", 50))

    lbl.grid(column=200, row=200)


    window.mainloop()



if __name__ == '__main__':
    main()
