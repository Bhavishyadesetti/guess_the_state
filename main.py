import turtle
import pandas
screen=turtle.Screen()
screen.addshape("India_map.gif")
turtle.shape("India_map.gif")
n=29
data=pandas.read_csv("states_data.csv")
state_list=data["state"].to_list()
while n>0:
    state_name=turtle.textinput(title="Guess the states",prompt=f"{29-n}/29 are guessed")
    if state_name.title() in state_list:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        row=data[data["state"]==state_name.title()]

        t.goto(int(row["x"]),int(row["y"]))
        t.write(arg=state_name)
        n-=1
        state_list.remove(state_name.title())
    elif state_name.lower()=="exit":
        remaining_states=pandas.DataFrame(state_list)
        remaining_states.to_csv("remaining_states.csv")
if state_list==[]:
    t_end=turtle.Turtle()
    t_end.hideturtle()
    t_end.pencolor("green")
    t_end.write(arg="You guessed all 29 states! That's impressive",align="center",font=("Arial", 20, "normal"))








turtle.mainloop()