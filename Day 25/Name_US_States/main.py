import turtle
from turtle import Turtle, Screen
import pandas as pd

states = pd.read_csv('./50_states.csv')

screen = Screen()
screen.title('U.S. States Game')
image = './blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

states_found = list()
while len(states_found) != 50:
    answer = screen.textinput(title=f'{len(states_found)}/50 Guess the state',
                              prompt='What\'s another State Name?').title()
    if answer == '':
        break

    if answer not in states['state'].to_list():
        continue

    state = states[states['state'] == answer].iloc[0]
    states_found.append(answer)
    timmy = Turtle()
    timmy.hideturtle()
    timmy.penup()
    timmy.goto(state['x'], state['y'])
    timmy.write(state['state'], align='center')

missing_states = [state for state in states['state'] if state not in states_found]

pd.DataFrame(missing_states,columns=['state']).to_csv('./states_to_learn.csv')
