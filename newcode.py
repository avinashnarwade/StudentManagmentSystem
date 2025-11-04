def showimage():
    global img
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select image file",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif"), ("All Files", "*.*")]
    )

    if filename:
        try:
            img = Image.open(filename)
            img = img.resize((190, 190), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)
            lbl.config(image=photo)
            lbl.image = photo
        except Exception as e:
            messagebox.showerror("Error", "The selected file could not be opened as an image.\nPlease select a valid image file.")
            print(e)

# Example of the rest of the code context
if __name__ == "__main__":
    root = Tk()
    root.title("Student Registration System")
    root.geometry("1250x700+210+100")
    root.config(bg=background)

    # Image frame
    f = Frame(root, bd=3, bg="black", width=200, height=200, relief=GROOVE)
    f.place(x=1000, y=150)

    img = PhotoImage(file="images/upload photo.png")
    lbl = Label(f, bg="black", image=img)
    lbl.place(x=0, y=0)

    # Upload Button
    Button(root, text="Upload", width=19, height=2, font="arial 12 bold", bg="lightblue", command=showimage).place(x=1000, y=370)

    root.mainloop()
