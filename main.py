from tkinter import *
import random
import time
import datetime

rules = "1- You must place your ship on a top space.\n " \
        "If it is hit by the opponent you lose.\n\n\n \
        2- You will have to shoot turn by turn to find your opponent's\n " \
        "boat and thus win the game \n\n\n \
        3- The game will turn green if you win, but if you \nlose it will turn red.\n\n\n \
        Good Luck"


enemy_boat_place = ""  # The case selected

# List of buttons
position_boat_player = []
position_boat_computer = []

choose_your_boat = True

# time_turn_enemy = 3


def choose_boat_position(button):
    global choose_your_boat, enemy_boat_place
    # Select player boat position
    if choose_your_boat:
        # Choose boat computer
        enemy_boat_place = random.choice(position_boat_computer)
        enemy_boat_place.config(bg="grey")
        print(enemy_boat_place)                                                     # Don't work...
        # Choose boat player
        button.config(bg="pink")
        button.config(text="Boat")
        label_info.config(text="Perfect ! It's time to attack")
        # enemy_ship_place()                                                       # Not sure if usefull
        label_rules.destroy()
    choose_your_boat = False


def enemy_turn():                                                                   # Don't work
    enemy_shoot()

    # Add a timer
    # global time_turn_enemy
    # time.sleep(3)

    # enemy_turn_bool = True
    # if enemy_turn_bool:
    #     if time_turn_enemy >= 0:
    #         time_turn_enemy = time_turn_enemy - 1
    #         root.after(1000, enemy_turn)
    #     if time_turn_enemy < 0:
    #         time_turn_enemy = 3
    #         enemy_shoot()
    # enemy_turn_bool = False

    # t = 2
    # while t:
    #     mins, secs = divmod(0, t)
    #     timer = '{:02d}:{:02d}'.format(mins, secs)
    #     print(timer, end="\r")
    #     time.sleep(1)
    #     t -= 1


def verify_my_boat(enemy_shoot_boat):
    if enemy_shoot_boat.cget("bg") == "pink":
        root.config(bg="red")
        label_info.config(text="You lose !")


def enemy_shoot():
    global position_boat_player
    enemy_shoot_boat = random.choice(position_boat_player)
    position_boat_player.remove(enemy_shoot_boat)
    # Verifier la couleur avant de changer la couleur
    verify_my_boat(enemy_shoot_boat)

    enemy_shoot_boat.config(bg="red")
    enemy_shoot_boat.config(text="BOOM")
    label_info.config(text="Your turn!")


def enemy_ship_place(place_shoot):
    global enemy_boat_place
    if enemy_boat_place == place_shoot:
        print("end of the game, you win")
        root.config(bg="green")
        label_info.config(text="You win !")


def button_clicked(button: Button):
    global enemy_boat_place
    button.config(bg="red")
    button.config(text="BOOM")
    place_shoot = button
    label_info.config(text="Enemy turn !")
    enemy_turn()
    enemy_ship_place(place_shoot)


root = Tk()
root.geometry("530x700")

# Label top informations
label_info = Label(root, bg="white", width=50, height=1, foreground="red",
                   text="position your boat", font=('Helvetica', 9, 'bold'))
label_info.pack()
label_info.place(x=80, y=0)

# Label 1
label_a1 = Button(root, bg="grey", width=5, height=2, text="A1")
label_a1.config(command=lambda button=label_a1: choose_boat_position(button))
label_a1.pack()
label_a1.place(x=120, y=40)
position_boat_player.append(label_a1)

label_b1 = Button(root, bg="grey", width=5, height=2, text="B1")
label_b1.config(command=lambda button=label_b1: choose_boat_position(button))
label_b1.pack()
label_b1.place(x=180, y=40)
position_boat_player.append(label_b1)

label_c1 = Button(root, bg="grey", width=5, height=2, text="C1")
label_c1.config(command=lambda button=label_c1: choose_boat_position(button))
label_c1.pack()
label_c1.place(x=240, y=40)
position_boat_player.append(label_c1)

label_d1 = Button(root, bg="grey", width=5, height=2, text="D1")
label_d1.config(command=lambda button=label_d1: choose_boat_position(button))
label_d1.pack()
label_d1.place(x=300, y=40)
position_boat_player.append(label_d1)

label_e1 = Button(root, bg="grey", width=5, height=2, text="E1")
label_e1.config(command=lambda button=label_e1: choose_boat_position(button))
label_e1.pack()
label_e1.place(x=360, y=40)
position_boat_player.append(label_e1)

# Label 2
label_a2 = Button(root, bg="grey", width=5, height=2, text="A2")
label_a2.config(command=lambda button=label_a2: choose_boat_position(button))
label_a2.pack()
label_a2.place(x=120, y=90)
position_boat_player.append(label_a2)

label_b2 = Button(root, bg="grey", width=5, height=2, text="B2")
label_b2.config(command=lambda button=label_b2: choose_boat_position(button))
label_b2.pack()
label_b2.place(x=180, y=90)
position_boat_player.append(label_b2)

label_c2 = Button(root, bg="grey", width=5, height=2, text="C2")
label_c2.config(command=lambda button=label_c2: choose_boat_position(button))
label_c2.pack()
label_c2.place(x=240, y=90)
position_boat_player.append(label_c2)

label_d2 = Button(root, bg="grey", width=5, height=2, text="D2")
label_d2.config(command=lambda button=label_d2: choose_boat_position(button))
label_d2.pack()
label_d2.place(x=300, y=90)
position_boat_player.append(label_d2)

label_e2 = Button(root, bg="grey", width=5, height=2, text="E2")
label_e2.config(command=lambda button=label_e2: choose_boat_position(button))
label_e2.pack()
label_e2.place(x=360, y=90)
position_boat_player.append(label_e2)

# Label 3
label_a3 = Button(root, bg="grey", width=5, height=2, text="A3")
label_a3.config(command=lambda button=label_a3: choose_boat_position(button))
label_a3.pack()
label_a3.place(x=120, y=140)
position_boat_player.append(label_a3)

label_b3 = Button(root, bg="grey", width=5, height=2, text="B3")
label_b3.config(command=lambda button=label_b3: choose_boat_position(button))
label_b3.pack()
label_b3.place(x=180, y=140)
position_boat_player.append(label_b3)

label_c3 = Button(root, bg="grey", width=5, height=2, text="C3")
label_c3.config(command=lambda button=label_c3: choose_boat_position(button))
label_c3.pack()
label_c3.place(x=240, y=140)
position_boat_player.append(label_c3)

label_d3 = Button(root, bg="grey", width=5, height=2, text="D3")
label_d3.config(command=lambda button=label_d3: choose_boat_position(button))
label_d3.pack()
label_d3.place(x=300, y=140)
position_boat_player.append(label_d3)

label_e3 = Button(root, bg="grey", width=5, height=2, text="E3")
label_e3.config(command=lambda button=label_e3: choose_boat_position(button))
label_e3.pack()
label_e3.place(x=360, y=140)
position_boat_player.append(label_e3)

# Label 4
label_a4 = Button(root, bg="grey", width=5, height=2, text="A4")
label_a4.config(command=lambda button=label_a4: choose_boat_position(button))
label_a4.pack()
label_a4.place(x=120, y=190)
position_boat_player.append(label_a4)

label_b4 = Button(root, bg="grey", width=5, height=2, text="B4")
label_b4.config(command=lambda button=label_b4: choose_boat_position(button))
label_b4.pack()
label_b4.place(x=180, y=190)
position_boat_player.append(label_b4)

label_c4 = Button(root, bg="grey", width=5, height=2, text="C4")
label_c4.config(command=lambda button=label_c4: choose_boat_position(button))
label_c4.pack()
label_c4.place(x=240, y=190)
position_boat_player.append(label_c4)

label_d4 = Button(root, bg="grey", width=5, height=2, text="D4")
label_d4.config(command=lambda button=label_d4: choose_boat_position(button))
label_d4.pack()
label_d4.place(x=300, y=190)
position_boat_player.append(label_d4)

label_e4 = Button(root, bg="grey", width=5, height=2, text="E4")
label_e4.config(command=lambda button=label_e4: choose_boat_position(button))
label_e4.pack()
label_e4.place(x=360, y=190)
position_boat_player.append(label_e4)


# 1
button_a1 = Button(root, bg="grey", width=10, height=5, text="A-1")
button_a1.config(command=lambda button=button_a1: button_clicked(button))
button_a1.pack()
button_a1.place(x=40, y=280)
position_boat_computer.append(button_a1)

button_b1 = Button(root, bg="grey", width=10, height=5, text="B-1")
button_b1.config(command=lambda button=button_b1: button_clicked(button))
button_b1.pack()
button_b1.place(x=130, y=280)
position_boat_computer.append(button_b1)

button_c1 = Button(root, bg="grey", width=10, height=5, text="C-1")
button_c1.config(command=lambda button=button_c1: button_clicked(button))
button_c1.pack()
button_c1.place(x=220, y=280)
position_boat_computer.append(button_c1)

button_d1 = Button(root, bg="grey", width=10, height=5, text="D-1")
button_d1.config(command=lambda button=button_d1: button_clicked(button))
button_d1.pack()
button_d1.place(x=310, y=280)
position_boat_computer.append(button_d1)

button_e1 = Button(root, bg="grey", width=10, height=5, text="E-1")
button_e1.config(command=lambda button=button_e1: button_clicked(button))
button_e1.pack()
button_e1.place(x=400, y=280)
position_boat_computer.append(button_e1)

# 2
button_a2 = Button(root, bg="grey", width=10, height=5, text="A-2")
button_a2.config(command=lambda button=button_a2: button_clicked(button))
button_a2.pack()
button_a2.place(x=40, y=380)
position_boat_computer.append(button_a2)

button_b2 = Button(root, bg="grey", width=10, height=5, text="B-2")
button_b2.config(command=lambda button=button_b2: button_clicked(button))
button_b2.pack()
button_b2.place(x=130, y=380)
position_boat_computer.append(button_b2)

button_c2 = Button(root, bg="grey", width=10, height=5, text="C-2")
button_c2.config(command=lambda button=button_c2: button_clicked(button))
button_c2.pack()
button_c2.place(x=220, y=380)
position_boat_computer.append(button_c2)

button_d2 = Button(root, bg="grey", width=10, height=5, text="D-2")
button_d2.config(command=lambda button=button_d2: button_clicked(button))
button_d2.pack()
button_d2.place(x=310, y=380)
position_boat_computer.append(button_d2)

button_e2 = Button(root, bg="grey", width=10, height=5, text="E-2")
button_e2.config(command=lambda button=button_e2: button_clicked(button))
button_e2.pack()
button_e2.place(x=400, y=380)
position_boat_computer.append(button_e2)

# 3
button_a3 = Button(root, bg="grey", width=10, height=5, text="A-3")
button_a3.config(command=lambda button=button_a3: button_clicked(button))
button_a3.pack()
button_a3.place(x=40, y=480)
position_boat_computer.append(button_a3)

button_b3 = Button(root, bg="grey", width=10, height=5, text="B-3")
button_b3.config(command=lambda button=button_b3: button_clicked(button))
button_b3.pack()
button_b3.place(x=130, y=480)
position_boat_computer.append(button_b3)

button_c3 = Button(root, bg="grey", width=10, height=5, text="C-3")
button_c3.config(command=lambda button=button_c3: button_clicked(button))
button_c3.pack()
button_c3.place(x=220, y=480)
position_boat_computer.append(button_c3)

button_d3 = Button(root, bg="grey", width=10, height=5, text="D-3")
button_d3.config(command=lambda button=button_d3: button_clicked(button))
button_d3.pack()
button_d3.place(x=310, y=480)
position_boat_computer.append(button_d3)

button_e3 = Button(root, bg="grey", width=10, height=5, text="E-3")
button_e3.config(command=lambda button=button_e3: button_clicked(button))
button_e3.pack()
button_e3.place(x=400, y=480)
position_boat_computer.append(button_e3)

# 4
button_a4 = Button(root, bg="grey", width=10, height=5, text="A-4")
button_a4.config(command=lambda button=button_a4: button_clicked(button))
button_a4.pack()
button_a4.place(x=40, y=580)
position_boat_computer.append(button_a4)

button_b4 = Button(root, bg="grey", width=10, height=5, text="B-4")
button_b4.config(command=lambda button=button_b4: button_clicked(button))
button_b4.pack()
button_b4.place(x=130, y=580)
position_boat_computer.append(button_b4)

button_c4 = Button(root, bg="grey", width=10, height=5, text="C-4")
button_c4.config(command=lambda button=button_c4: button_clicked(button))
button_c4.pack()
button_c4.place(x=220, y=580)
position_boat_computer.append(button_c4)

button_d4 = Button(root, bg="grey", width=10, height=5, text="D-4")
button_d4.config(command=lambda button=button_d4: button_clicked(button))
button_d4.pack()
button_d4.place(x=310, y=580)
position_boat_computer.append(button_d4)

button_e4 = Button(root, bg="grey", width=10, height=5, text="E-4")
button_e4.config(command=lambda button=button_e4: button_clicked(button))
button_e4.pack()
button_e4.place(x=400, y=580)
position_boat_computer.append(button_e4)

# Label rules before game
label_rules = Label(root, bg="grey", width=62, height=26, foreground="black",
                    text=rules, font=('Helvetica', 9, 'bold'))
label_rules.pack()
label_rules.place(x=40, y=270)

root.mainloop()
