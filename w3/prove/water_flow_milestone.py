"""
Author: 
    Karina Santos Felippe
Problem Statement:
    Getting clean water to all buildings in a city is a large and expensive task. Many cities will build an elevated water tank, and install a pump that pushes water up to the tank where the water is stored. In the city, when a thirsty person opens a water faucet, water runs from the tank through pipes to the faucet. Earth’s gravity pulling on the water in the elevated tank pressurizes the water and causes it to spray from the faucet.
    Before a city builds a water distribution system, an engineer must design the system and ensure water will flow to all buildings in the city. An engineer must choose the tower height, pipe type, pipe diameter, and pipe path. Engineers use software to help them make these choices and design a working water distribtuion system.
"""

def water_column_height(tower_height, tank_height):
    h = tower_height + ( (3*tank_height) / 4 )
    return h

def pressure_gain_from_water_height (height):
    p = (998.2 * 9.80665 * height) / 1000
    return p

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    p = (-friction_factor * pipe_length * 998.2 * (fluid_velocity ** 2)) / (2000 * pipe_diameter)
    return p