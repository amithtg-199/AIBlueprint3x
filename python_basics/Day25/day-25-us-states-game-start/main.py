import pandas as pd
import turtle as t
import time

screen = t.Screen()
screen.title("U.S states game")
image = r"Day25\day-25-us-states-game-start\blank_states_img.gif"
screen.addshape(image)
t.shape(image)

'''Writer Turtle object for displaying answer at correct location'''
writer = t.Turtle()
writer.hideturtle()
writer.penup()
time.sleep(0.1)

guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 states correct", prompt="Whats Another states name").title()

    all_states = pd.read_csv(r"Day25\day-25-us-states-game-start\50_states.csv")
    if answer_state == "Exit":
        break
    '''Here the walrus operator := is used to assign a value to variable in if statement only'''
    '''.empty(), its a pandas property which is to check if the input provided exists in the DF or not'''
    if not (matches := all_states[all_states.state == answer_state]).empty:
        '''Here iloc is location ased indexing, or locate an index'''
        x = matches.x.iloc[0]
        y = matches.y.iloc[0]
        writer.goto(x,y)
        writer.write(answer_state)
        guessed_state.append(answer_state)
    else:
        t.clear()
        t.write("Oops! No Such State. Try Again!", align="center", font=("Arial", 15, "normal"))

unguessed_state = {
    "states": [],
    "x": [],
    "y": []
}
for s in all_states.state.to_list():
    if s not in guessed_state:
        missed_state = all_states[all_states.state == s]
        unguessed_state["states"].append(s)
        unguessed_state["x"].append(missed_state.x.item())
        unguessed_state["y"].append(missed_state.y.item())
    
df = pd.DataFrame(unguessed_state)
df.to_csv(r"Day25\day-25-us-states-game-start\unguessed_state.csv", index=False)

screen.exitonclick()

