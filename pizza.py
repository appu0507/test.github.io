# This program is a GUI for a pizza order.

import tkinter as tk
import tkinter as ttk
import tkinter.messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("1000x600")
root.minsize(height=600, width=1000)
root.maxsize(height=600, width=1000)

root.title("Sanna's Pizzeria")
root.iconbitmap("icon.ico")


menu = tk.Menu(root)
root.config(menu=menu)


# This function is to exit the program.
def exit1():
    tk.exit()


# This function is to change the size.
def change_size(sizeChosen):
    global sizee  # see
    sizee = sizeChosen
    print(sizee)


# This function is to place the final order.
def placeorder():
    print(sizee)
    str1 = ("Your %s pizza with toppings:" % sizee)
    str2 = ", ".join(toppings)
    str3 = " has succesfully been ordered!"
    tkinter.messagebox.showinfo("Order Status", str(str1 + str2 + str3))


var_size = tk.IntVar()
var_pepperoni = tk.IntVar()
var_mushrooms = tk.IntVar()
var_onions = tk.IntVar()
var_sausage = tk.IntVar()
var_bacon = tk.IntVar()
var_extra_cheese = tk.IntVar()
var_black_olives = tk.IntVar()
var_green_peppers = tk.IntVar()
var_pineapple = tk.IntVar()
var_spinach = tk.IntVar()
var_takeout = tk.IntVar()

# This is for the background image.
background = Image.open("image5.jpg")
photo = ImageTk.PhotoImage(background)

lab = tk.Label(root, image=photo)
lab.place(relwidth=1, relheight=1)

# The title label for this program.
SannaPizzeria = tk.Label(root, text="Sanna's Pizzeria", fg="red", bg="white", relief="solid",
                         font=("garamond", 48, "bold"))
SannaPizzeria.place(x=250, y=30)

# The size label and size options buttons.
size = tk.Label(root, text="Pizza Size :", fg="white", bg="red", relief="flat", width=12, font=("garamond", 14, "bold"))
size.place(x=180, y=160)

small = tk.Radiobutton(root, text="Small", selectcolor="red", font=("garamond", 12), fg="white", bg="black",
                       variable=var_size, value="small", command=lambda: change_size("Small")).place(x=350, y=160)
medium = tk.Radiobutton(root, text="Medium", selectcolor="red", font=("garamond", 12), fg="white", bg="black",
                        variable=var_size, value="medium", command=lambda: change_size("Medium")).place(x=440, y=160)
large = tk.Radiobutton(root, text="Large", selectcolor="red", font=("garamond", 12), fg="white", bg="black",
                       variable=var_size, value="large", command=lambda: change_size("Large")).place(x=550, y=160)

# This function adds toppings to the pizza and tells the user when added, or if they've been added previously.
toppings = []
sizee = ""


def add_topping(topping):
    if topping in toppings:
        toppings.pop(toppings.index(topping))
        print(toppings)
    else:
        toppings.append(topping)
        print(toppings)


imageHead = Image.open("image3.jpg")
imageHand = Image.open("image3.jpg")

imageHead.paste(imageHand, (1, 1), imageHand)

tkimage = ImageTk.PhotoImage(imageHead)

panel1 = tk.Label(root, image=tkimage)
panel1.place(width=320, height=204, x=0, y=400)

# The label for the toppings and the button for each individual topping.
topping = tk.Label(root, text="Toppings :  ", fg="white", bg="red", relief="flat", width=12,
                   font=("garamond", 14, "bold"))
topping.place(x=180, y=250)

pepperoni = tk.Checkbutton(root, text="Pepperoni", selectcolor="red", font=("garamond", 12), fg="white", bg="black",
                           variable=var_pepperoni, command=lambda: add_topping("Pepperoni"), onvalue=1,
                           offvalue=0).place(x=350, y=250)
mushrooms = tk.Checkbutton(root, text="Mushrooms", selectcolor="red", font=("garamond", 12), fg="white", bg="black",
                           variable=var_mushrooms, command=lambda: add_topping("Mushrooms"), onvalue=1,
                           offvalue=0).place(x=455, y=250)
onions = tk.Checkbutton(root, text="Onions", selectcolor="red", font=("garamond", 12), fg="white", bg="black",
                        variable=var_onions, command=lambda: add_topping("Onions"), onvalue=1, offvalue=0).place(x=570,
                                                                                                                 y=250)
sausage = tk.Checkbutton(root, text="Sausage", selectcolor="red", font=("garamond", 12), fg="white", bg="black",
                         variable=var_sausage, command=lambda: add_topping("Sausage"), onvalue=1, offvalue=0).place(
    x=660, y=250)
bacon = tk.Checkbutton(root, text="Bacon", selectcolor="red", font=("garamond", 12), fg="white", bg="black",
                       variable=var_bacon, command=lambda: add_topping("Bacon"), onvalue=1, offvalue=0).place(x=750,
                                                                                                              y=250)
extra_cheese = tk.Checkbutton(root, text="Extra Cheese", selectcolor="red", font=("garamond", 12), fg="white",
                              bg="black", variable=var_extra_cheese, command=lambda: add_topping("Extra Cheese"),
                              onvalue=1, offvalue=0).place(x=350, y=290)
black_olives = tk.Checkbutton(root, text="Black Olives", selectcolor="red", font=("garamond", 12), fg="white",
                              bg="black", variable=var_black_olives, command=lambda: add_topping("Black Olives"),
                              onvalue=1, offvalue=0).place(x=470, y=290)
green_peppers = tk.Checkbutton(root, text="Green Peppers", selectcolor="red", font=("garamond", 12), fg="white",
                               bg="black", variable=var_green_peppers, command=lambda: add_topping("Green Peppers"),
                               onvalue=1, offvalue=0).place(x=590, y=290)
pineapple = tk.Checkbutton(root, text="Pineapple", selectcolor="red", font=("garamond", 12), fg="white", bg="black",
                           variable=var_pineapple, command=lambda: add_topping("Pineapple"), onvalue=1,
                           offvalue=0).place(x=720, y=290)
spinach = tk.Checkbutton(root, text="Spinach", selectcolor="red", font=("garamond", 12), fg="white", bg="black",
                         variable=var_spinach, command=lambda: add_topping("Spinach"), onvalue=1, offvalue=0).place(
    x=820, y=290)


class OrderWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Order Placement")
        self.minsize(1000, 625)
        self.maxsize(1000, 625)
        self.iconbitmap("icon.ico")
        #self.configure(bg="#49a")

        self.background = tk.PhotoImage(file="image5.jpg")
        self.pic = tk.Label(OrderWindow, image=background)
        self.pic.place(x=0, y=0, relwidth=1, relheight=1)

        self.exitbutton = ttk.Button(self, text="Exit", width=20, bg="orange", fg="white",
                                     font=("garamond", 13, "bold"), command=exit)
        self.exitbutton.place(x=770, y=560)

        self.placeorderbutton = ttk.Button(self, text="Place Order", width=20, bg="orange", fg="white",
                                           font=("garamond", 13, "bold"), command=placeorder)
        self.placeorderbutton.place(x=770, y=520)

        self.label_takeout = ttk.Label(self, text="Takeout?:", fg="white", bg="black", relief="flat",
                                       font=("garamond", 16, "bold"))

        self.label_takeout.place(x=180, y=50)

        self.label_delivery = ttk.Label(self, text="Delivery?:", fg="white", bg="black", relief="flat",
                                        font=("garamond", 16, "bold"))

        self.label_delivery.place(x=180, y=90)

        self.label_name = ttk.Label(self, text="Full Name:", fg="black", bg="yellow", relief="flat",
                                    font=("garamond", 14, "bold"))
        self.label_name.place(x=180, y=200)

        self.label_phone = ttk.Label(self, text="Phone Number:", fg="black", bg="yellow", relief="flat",
                                     font=("garamond", 14, "bold"))
        self.label_phone.place(x=180, y=260)

        self.label_streetaddress = ttk.Label(self, text="Street Address:", fg="black", bg="yellow", relief="flat",
                                             font=("garamond", 14, "bold"))
        self.label_streetaddress.place(x=180, y=320)

        self.label_city = ttk.Label(self, text="City:", fg="black", bg="yellow", relief="flat",
                                    font=("garamond", 14, "bold"))
        self.label_city.place(x=550, y=320)

        self.label_province = ttk.Label(self, text="Province:", fg="black", bg="yellow", relief="flat",
                                        font=("garamond", 14, "bold"))
        self.label_province.place(x=180, y=380)

        self.label_country = ttk.Label(self, text="Country:", fg="black", bg="yellow", relief="flat",
                                       font=("garamond", 14, "bold"))
        self.label_country.place(x=550, y=380)

        # Functions to place and call the user's name, phone number, and address.
        def place_everything():
            place_name()
            place_phone()
            place_streetaddress()
            place_city()
            place_country()
            place_droplist()

        def place_name():
            self.name.place(x=350, y=200)
            place_phone()

        def place_phone():
            self.phone.place(x=350, y=260)

        def place_streetaddress():
            self.streetaddress.place(x=350, y=320)

        def place_city():
            self.city.place(x=655, y=320)

        def place_province():
            self.province.place(x=350, y=380)

        var_province = tk.IntVar()

        def place_country():
            self.country.place(x=655, y=380)

        # User entry text box details.
        self.name = ttk.Entry(self, font=("garamond", 14, "bold"), fg="white", bg="red", relief="sunken")

        self.phone = ttk.Entry(self, font=("garamond", 14, "bold"), fg="white", bg="red", relief="sunken")

        self.streetaddress = ttk.Entry(self, font=("garamond", 14, "bold"), fg="white", bg="red", relief="sunken")

        self.city = ttk.Entry(self, font=("garamond", 14, "bold"), fg="white", bg="red", relief="sunken")


        # Function for the drop-down list with each of the provinces and territories.
        def place_droplist():
            var_province.set("Select Province")

            listprovince = ["Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland and Labrador",
                            "Northwest Territories", "Nova Scotia", "Nunavut", "Ontario", "Prince Edward Island",
                            "Quebec",
                            "Saskatchewan", "Yukon"]
            droplist = tk.OptionMenu(self, var_province, *listprovince)
            droplist.place(x=350, y=380)

            droplist.config(width=20)

        self.country = ttk.Entry(self, font=("garamond", 14, "bold"), fg="white", bg="red", relief="sunken")

        # The takeout and delivery option buttons.
        self.takeout = ttk.Radiobutton(self, text="Takeout", selectcolor="red", fg="white", bg="black",
                                       variable=var_takeout, value="Takeout", command=place_name)
        self.takeout.place(x=300, y=55)

        self.delivery = ttk.Radiobutton(self, text="Delivery", selectcolor="red", fg="white", bg="black",
                                        variable=var_takeout, value="Delivery", command=place_everything)
        self.delivery.place(x=300, y=95)

    def Create_Toplevel(self):
        self.wm_attributes("-disabled", True)

        self.toplevel_dialog = ttk.Toplevel(self)
        self.toplevel_dialog.minsize(1000, 625)

        self.toplevel_dialog.transient(self)

        self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.Close_Toplevel)


    def Close_Toplevel(self):

        self.wm_attributes("-disabled", False)

        self.toplevel_dialog.destroy()

        self.deiconify()


def page2():
    app = OrderWindow()


submenu1 = tk.Menu(menu)
menu.add_cascade(label="Home", menu=submenu1)
submenu1.add_command(label="Exit", command=exit)

submenu2 = tk.Menu(menu)
menu.add_cascade(label="Order", menu=submenu2)
submenu2.add_command(label="Order Placement", command=page2)

# The place order button adn exit button details.
nextbutton = tk.Button(root, text="Next -->", width=20, bg="orange", fg="white", font=("garamond", 13, "bold"),
                       command=page2)
nextbutton.place(x=770, y=480)

exitbutton = tk.Button(root, text="Exit", width=20, bg="orange", fg="white", font=("garamond", 13, "bold"),
                       command=exit)
exitbutton.place(x=770, y=520)

root.mainloop()
