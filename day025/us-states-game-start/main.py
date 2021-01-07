import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

correct_list = []
missing_list = []
while len(correct_list) < 50:
    answer_state = screen.textinput(title=f"{len(correct_list)}/{len(all_states)} States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        for state in all_states:
            if state not in correct_list:
                missing_list.append(state)
        new_data = pandas.DataFrame(missing_list)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states and answer_state not in correct_list:
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

        correct_list.append(answer_state)
        screen.title(f"{len(correct_list)}/50 States Correct")

