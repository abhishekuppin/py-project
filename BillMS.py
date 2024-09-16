from tkinter import *
from tkinter import messagebox
import os

root = Tk()
root.geometry("1500x1600")
root.title("COFFEE HOUSE")
root.resizable(True, True)

def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

def exit_fullscreen(event=None):
    root.attributes("-fullscreen", False)

root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", exit_fullscreen)

def Reset():
    entry_Espresso.delete(0, END)
    entry_Latte.delete(0, END)
    entry_Cappuccino.delete(0, END)
    entry_Americano.delete(0, END)
    entry_Mocha.delete(0, END)
    entry_Caramel.delete(0, END)
    entry_ColdBrew.delete(0, END)
    entry_VanillaCream.delete(0, END)
    entry_StawberriesCreme.delete(0, END)
    entry_DoubleChocolateChip.delete(0, END)
    entry_ColdCoffee.delete(0, END)
    entry_HotCoffee.delete(0, END)

    entry_total.delete(0, END)

def Total():
    try: a1 = int(Espresso.get())
    except: a1 = 0

    try: a2 = int(Latte.get())
    except: a2 = 0

    try: a3 = int(Cappuccino.get())
    except: a3 = 0

    try: a4 = int(Americano.get())
    except: a4 = 0

    try: a5 = int(Mocha.get())
    except: a5 = 0

    try: a6 = int(Caramel.get())
    except: a6 = 0

    try: a7 = int(ColdBrew.get())
    except: a7 = 0
    
    try: a8 = int(VanillaCream.get())
    except: a8 = 0

    try: a9 = int(StawberriesCreme.get())
    except: a9 = 0

    try: a10 = int(DoubleChocolateChip.get())
    except: a10 = 0

    try: a11 = int(ColdCoffee.get())
    except: a11 = 0

    try: a12 = int(HotCoffee.get())
    except: a12 = 0

    # define cost of each item per quantity
    c1 = 150 * a1
    c2 = 180 * a2
    c3 = 200 * a3
    c4 = 170 * a4
    c5 = 220 * a5
    c6 = 200 * a6
    c7 = 260 * a7
    c8 = 275 * a8
    c9 = 305 * a9
    c10 = 305 * a10
    c11 = 280 * a11
    c12 = 290 * a12

    totalcost = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10 + c11 + c12
    string_bill = "Rs. " + str('%.2f' % totalcost)
    Total_bill.set(string_bill)

def Save():
    try:
        total_cost = Total_bill.get()
        if not total_cost:
            messagebox.showwarning("Warning", "Please calculate the total before saving.")
            return
        
        save_path = ""
        os.makedirs(save_path, exist_ok=True)
        file_path = os.path.join(save_path, "bill.txt")
        
        with open(file_path, "w") as file:
            file.write("BILL\n")
            file.write(f"Espresso: {Espresso.get()} cups\n")
            file.write(f"Latte: {Latte.get()} cups\n")
            file.write(f"Cappuccino: {Cappuccino.get()} cups\n")
            file.write(f"Americano: {Americano.get()} cups\n")
            file.write(f"Mocha: {Mocha.get()} cups\n")
            file.write(f"Caramel: {Caramel.get()} cups\n")
            file.write(f"Cold Brew: {ColdBrew.get()} cups\n")
            file.write(f"Vanilla Cream: {VanillaCream.get()} cups\n")
            file.write(f"Strawberries & Crème: {StawberriesCreme.get()} cups\n")
            file.write(f"Double Chocolate Chip: {DoubleChocolateChip.get()} cups\n")
            file.write(f"Cold Coffee: {ColdCoffee.get()} cups\n")
            file.write(f"Hot Coffee: {HotCoffee.get()} cups\n")

            file.write(f"Total Cost: {total_cost}\n")
        messagebox.showinfo("Saved", "Bill saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving bill: {str(e)}")

Label(text="THE COFFEE HOUSE", bg="#6F4F28", fg="white", font=("Gabriola", 33), width="300", height="1").pack()

# Menu card
f = Frame(root, bg="#8B5E3C", highlightbackground="black", highlightthickness=1, width=480, height=700)  # Increased height
f.place(x=15, y=110)

Label(f, text="Menu", font=("Gabriola", 40, "bold"), fg="white", bg="#8B5E3C").place(x=150, y=0)
Label(f, font=("Lucida Calligraphy", 17, 'bold'), text="Espresso..............................Rs.150/cup", fg="white", bg="#8B5E3C").place(x=10, y=120)
Label(f, font=("Lucida Calligraphy", 17, 'bold'), text="Latte......................................Rs.180/cup", fg="white", bg="#8B5E3C").place(x=10, y=160)
Label(f, font=("Lucida Calligraphy", 17, 'bold'), text="Cappuccino.........................Rs.200/cup", fg="white", bg="#8B5E3C").place(x=10, y=200)
Label(f, font=("Lucida Calligraphy", 17, 'bold'), text="Americano............................Rs.170/cup", fg="white", bg="#8B5E3C").place(x=10, y=240)
Label(f, font=("Lucida Calligraphy", 17, 'bold'), text="Mocha...................................Rs.220/cup", fg="white", bg="#8B5E3C").place(x=10, y=280)
Label(f, font=("Lucida Calligraphy", 17, 'bold'), text="Caramel................................Rs.200/cup", fg="white", bg="#8B5E3C").place(x=10, y=320)
Label(f, font=("Lucida Calligraphy", 17, 'bold'), text="Cold Brew.............................Rs.260/cup", fg="white", bg="#8B5E3C").place(x=10, y=360)
Label(f, font=("Lucida Calligraphy", 17, 'bold'), text="Vanilla Cream.......................Rs.275/cup", fg="white", bg="#8B5E3C").place(x=10, y=400)
Label(f, font=("Lucida Calligraphy", 17, 'bold'), text="Strawberries & Crème........Rs.305/cup", fg="white", bg="#8B5E3C").place(x=10, y=440)
Label(f, font=("Lucida Calligraphy", 17, 'bold'), text="Double Chocolate Chip....Rs.305/cup", fg="white", bg="#8B5E3C").place(x=10, y=480)
Label(f, font=("Lucida Calligraphy", 17, 'bold'), text="Cold Coffee..........................Rs.280/cup", fg="white", bg="#8B5E3C").place(x=10, y=520)
Label(f, font=("Lucida Calligraphy", 17, 'bold'), text="Hot Coffee.............................Rs.290/cup", fg="white", bg="#8B5E3C").place(x=10, y=560)


# Bill
f2 = Frame(root, bg="#D2B48C", highlightbackground="black", highlightthickness=1, width=450, height=700)  # Increased height
f2.place(x=1010, y=110)

Bill = Label(f2, text="Total Bill", font=("Gabriola", 40, "bold"), bg="#D2B48C")
Bill.place(x=140, y=3)

# ENTRY WORK
f1 = Frame(root, bd=8, height=500, width=450, relief=RAISED)
f1.place(x=530, y=150)  # Adjusted placement to align with Menu and Total Bill sections

Espresso = StringVar()
Latte = StringVar()
Cappuccino = StringVar()
Americano = StringVar()
Mocha = StringVar()
Caramel = StringVar()
ColdBrew = StringVar()
VanillaCream = StringVar()
StawberriesCreme = StringVar()
DoubleChocolateChip = StringVar()
ColdCoffee = StringVar()
HotCoffee = StringVar()

Total_bill = StringVar()

# Labels
lbl_Espresso = Label(f1, font=("aria", 22, 'bold'), text="Espresso", width=15, fg="#4B2E2B")
lbl_Latte = Label(f1, font=("aria", 22, 'bold'), text="Latte", width=15, fg="#4B2E2B")
lbl_Cappuccino = Label(f1, font=("aria", 22, 'bold'), text="Cappuccino", width=15, fg="#4B2E2B")
lbl_Americano = Label(f1, font=("aria", 22, 'bold'), text="Americano", width=15, fg="#4B2E2B")
lbl_Mocha = Label(f1, font=("aria", 22, 'bold'), text="Mocha", width=15, fg="#4B2E2B")
lbl_Caramel = Label(f1, font=("aria", 22, 'bold'), text="Caramel", width=15, fg="#4B2E2B")
lbl_ColdBrew = Label(f1, font=("aria", 22, 'bold'), text="Cold Brew", width=15, fg="#4B2E2B")
lbl_VanillaCream = Label(f1, font=("aria", 22, 'bold'), text="Vanilla Cream", width=15, fg="#4B2E2B")
lbl_StawberriesCreme = Label(f1, font=("aria", 22, 'bold'), text="Strawb&Crème", width=15, fg="#4B2E2B")
lbl_DoubleChocolateChip = Label(f1, font=("aria", 22, 'bold'), text="Chocolate Chip", width=15, fg="#4B2E2B")
lbl_ColdCoffee = Label(f1, font=("aria", 22, 'bold'), text="Cold Coffee", width=15, fg="#4B2E2B")
lbl_HotCoffee = Label(f1, font=("aria", 22, 'bold'), text="Hot Coffee", width=15, fg="#4B2E2B")

lbl_total = Label(f2, font=("aria", 20, 'bold'), text="Total", width=16, fg="black", bg="#D2B48C")

# Place Labels
lbl_Espresso.grid(row=1, column=0)
lbl_Latte.grid(row=2, column=0)
lbl_Cappuccino.grid(row=3, column=0)
lbl_Americano.grid(row=4, column=0)
lbl_Mocha.grid(row=5, column=0)
lbl_Caramel.grid(row=6, column=0)
lbl_ColdBrew.grid(row=7, column=0)
lbl_VanillaCream.grid(row=8, column=0)
lbl_StawberriesCreme.grid(row=9, column=0)
lbl_DoubleChocolateChip.grid(row=10, column=0)
lbl_ColdCoffee.grid(row=11, column=0)
lbl_HotCoffee.grid(row=12, column=0)


# Entries
entry_Espresso = Entry(f1, font=("aria", 20, 'bold'), textvariable=Espresso, bd=6, width=8, bg="#F5DEB3")
entry_Latte = Entry(f1, font=("aria", 20, 'bold'), textvariable=Latte, bd=6, width=8, bg="#F5DEB3")
entry_Cappuccino = Entry(f1, font=("aria", 20, 'bold'), textvariable=Cappuccino, bd=6, width=8, bg="#F5DEB3")
entry_Americano = Entry(f1, font=("aria", 20, 'bold'), textvariable=Americano, bd=6, width=8, bg="#F5DEB3")
entry_Mocha = Entry(f1, font=("aria", 20, 'bold'), textvariable=Mocha, bd=6, width=8, bg="#F5DEB3")
entry_Caramel = Entry(f1, font=("aria", 20, 'bold'), textvariable=Caramel, bd=6, width=8, bg="#F5DEB3")
entry_ColdBrew = Entry(f1, font=("aria", 20, 'bold'), textvariable=ColdBrew, bd=6, width=8, bg="#F5DEB3")
entry_VanillaCream = Entry(f1, font=("aria", 20, 'bold'), textvariable=VanillaCream, bd=6, width=8, bg="#F5DEB3")
entry_StawberriesCreme = Entry(f1, font=("aria", 20, 'bold'), textvariable=StawberriesCreme, bd=6, width=8, bg="#F5DEB3")
entry_DoubleChocolateChip = Entry(f1, font=("aria", 20, 'bold'), textvariable=DoubleChocolateChip, bd=6, width=8, bg="#F5DEB3")
entry_ColdCoffee = Entry(f1, font=("aria", 20, 'bold'), textvariable=ColdCoffee, bd=6, width=8, bg="#F5DEB3")
entry_HotCoffee = Entry(f1, font=("aria", 20, 'bold'), textvariable=HotCoffee, bd=6, width=8, bg="#F5DEB3")

entry_total = Entry(f2, font=("aria", 20, 'bold'), textvariable=Total_bill, bd=6, width=15, bg="white")

# Place Entries
entry_Espresso.grid(row=1, column=1)
entry_Latte.grid(row=2, column=1)
entry_Cappuccino.grid(row=3, column=1)
entry_Americano.grid(row=4, column=1)
entry_Mocha.grid(row=5, column=1)
entry_Caramel.grid(row=6, column=1)
entry_ColdBrew.grid(row=7, column=1)
entry_VanillaCream.grid(row=8, column=1)
entry_StawberriesCreme.grid(row=9, column=1)
entry_DoubleChocolateChip.grid(row=10, column=1)
entry_ColdCoffee.grid(row=11, column=1)
entry_HotCoffee.grid(row=12, column=1)

entry_total.place(x=100, y=130)  # Adjusted y to fit new items

# Buttons
btn_reset = Button(f1, bd=5, fg="black", bg="#C69C6D", font=("arial", 16, 'bold'), width=10, text="Reset", command=Reset)
btn_reset.grid(row=15, column=0)

btn_total = Button(f1, bd=5, fg="black", bg="#C69C6D", font=("arial", 16, 'bold'), width=10, text="Total", command=Total)
btn_total.grid(row=15, column=1)

btn_save = Button(f2, bd=5, fg="black", bg="#C69C6D", font=("arial", 16, 'bold'), width=10, text="Save", command=Save)
btn_save.place(relx=0.5, rely=1.0, anchor='s', y=-10)  # Centered at the bottom with a small margin from the bottom

root.mainloop()
