from tkinter import *
from PIL import ImageTk, Image
import random
import math
# create window
root = Tk()
# set geometry for app
root.geometry("400x400")
# change logo
logo = PhotoImage(file="E:/mazenchannel/learn python with projects/0003-Number guessing game in python Tkinter/ico.png")
root.iconphoto(False, logo)
# change back ground color for window
root.config(bg="#669bbc")
# set window to fixed size
root.resizable(False, False)
# change window title
root.title("Number Guessing Game")
# create variables to we will use for our main app
# variable to count which click we in now
steps = 0
# variable count user played attempts
count = 0
# variable to ask user to input the upper range for game
upper_bound = 0
# variable to ask user to input the lower range for game
lower_bound = 0
# variable to program to generate random number
comp = 0
# variable to calculate available attempts to user based on calculation
attempts = 0
# define main function called start to our app what it will do after player click button
def start():
    # make variables global so we can update it out side the function  
    global steps 
    global count
    global upper_bound
    global lower_bound
    global comp
    global attempts
    # check if this is first click on button
    if steps == 0 :
        # if yes first click edit button text to be Enter
        b.config(text="Enter")
        # and change color to be same as beginning 
        b.config(bg="#780000", fg="black")
        # and change color to be same as beginning for info label
        info.config(bg="#43aa8b", fg= "black")
        # and change text for info label to ask user for upper range
        info.config(text="Please enter upper bound")
        # and add 1 to steps so the next click we will know it's second click
        steps += 1
    # check if this is second click
    elif steps == 1 :
        # get inputs and assign it to variable upper bound to be the upper of range
        upper_bound = e_txt.get()
        # change text in info label to ask player for enter lower for range
        info.config(text="Please enter lower bound")
        # add 1 to steps so next click will be third
        steps += 1
    # check if this third click
    elif steps == 2 :
        # get inputs and assign it to variable lower bound to be the lower of range
        lower_bound = e_txt.get()
        # generate random number and assign it to our comp variable
        comp = random.randint(lower_bound, upper_bound)
        # calculate attempts and assign it to our attempts variable
        attempts = round(math.log(upper_bound-lower_bound+1, 2)-2)
        # change button text to be check
        b.config(text="check")
        # change info label text to ask user to guess number and show him how many guess he can play before lose
        info.config(text=f"Try to guess the right number in {attempts} attempts")
        # add 1 to steps so we know the next click will be fourth
        steps += 1
    # check if we now in fourth click or more 
    elif steps >= 3:
        # player played first hand so we add 1 to count
        count += 1
        # check if played hands less than available hands to play
        if count < attempts:
            # get user input and assign it to guess variable
            guess = e_txt.get()
            # check winning condition if user guessed right number
            if guess == comp:
                # change info label text to congratulation you win and show number of hand  played to win
                info.config(text=f"Congratulations you did it in {count}")
                # change info label back ground color and text color
                info.config(bg="#c1121f", fg= "#fdf0d5")
                # change button text to be restart
                b.config(text="Restart")
                # change button color
                b.config(bg="#c1121f", fg="#fdf0d5", activebackground="#fdf0d5", activeforeground="#c1121f")
                # rest steps to be 0 so if button clicked app will start function for the above code lines
                steps = 0
            # check if guessed number > generated number
            elif guess > comp:
                # change info label text to be too high
                info.config(text=f"You guessed too high! used {count} from {attempts} attempts")
            else: # check if guessed number < generated number
                #change info label text to be too low
                info.config(text=f"You Guessed too small! used {count} from {attempts} attempts")
        # check if this played hand is last available hand
        elif count >= attempts:
            # change info label text
            info.config(text=f"The Number is {comp}")
            # change color for info label 
            info.config(bg="#c1121f", fg= "#fdf0d5")
            # change button text 
            b.config(text="Restart")
            # change button color
            b.config(bg="#003049", fg="#fdf0d5", activebackground="#fdf0d5", activeforeground="#003049")
            # reset steps to start from beginning 
            steps = 0
            # reset hand played 
            count = 0

# create label to welcome player and update it to show info
info = Label(root,text="Welcome To Number Guessing Game  ",# add text to our label
             font=("Arial","12", "bold", "italic"),# change font name and size and properties
             bg="#43aa8b",# to change label color
             fg="black",# to change text color
             width=40,
             wraplength=360,
             justify="left",
             height=3,
             padx=10,# label width from inside 
             pady=0,# label hight from inside
             bd=2,# border size 
             relief=GROOVE# label style
             )
# put label into screen
info.pack(padx=5, pady=1)
# create entry label to get entries fro user
e_txt = IntVar()
e = Entry(root,textvariable=e_txt,width=10,font="Arial 12 bold",border=1, bg="#43aa8b", fg="black", bd=1, relief=SUNKEN)
e.place(x=5, y=65, height=40, width= 120)
# create enter button
b = Button(root, text="Start", command = start, padx=18,font="Arial 12 bold",bg="#43aa8b", fg="black",width=15,
                activebackground="black",activeforeground="#43aa8b",relief=RAISED)
b.place(x=195, y=65, height=40, width=200)
# to add image need to create  label 
image_label = Label(root,image=logo,width=385, height=360,bg="#43aa8b",fg="black")
image_label.pack(padx=5, pady=50,)
# add footer
license_label = Label(text="Developed by Mazen Nafe for waycando channel",width=36,
                      font="Arial 10 bold", bg="#43aa8b", fg="black", padx=50, pady=5, bd=1, relief=RAISED)
# add label to window
license_label.place(x=5, y=375)
# create loop so it will not close until user close it
root.mainloop()