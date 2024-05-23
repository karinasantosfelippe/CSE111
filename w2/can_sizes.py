"""
Author: Karina Santos Felippe
Team Activity
Problem Statement:
    In many countries, food is stored in steel cans (also known as tin cans) that are shaped like cylinders. There are many different sizes of steel cans. The storage efficiency of a can tells us how much a can stores versus how much steel is required to make the can. Some sizes of cans require a lot of steel to store a small amount of food. Other sizes of cans require less steel and store more food. A can size with a large storage efficiency is considered more friendly to the environment than a can size with a small storage efficiency.

    The storage efficiency of a steel can is computed by dividing the volume of a can by its surface area.
        
        storage_efficiency = volume / surface_area
    
    In other words, the storage efficiency of a can is the space inside the can divided by the amount of steel required to make the can. The formulas for the volume and surface area of a cylinder are:

        volume = π radius^2 height
        surface_area = 2π radius(radius + height)

    - π is the constant PI, the ratio of the circumference of a circle divided by its diameter (use math.pi)
    - radius is the radius of the cylinder
    - height is the height of the cylinder
"""

import math

def main():
    # Storage the can sizes data in a dictionary
    tin_can_sizes = [
        ["#1 Picnic", 6.83, 10.16, 0.28],
        ["#1 Tall", 7.78, 11.91, 0.43],
        ["#2", 8.73, 11.59, 0.45],
        ["#2.5", 10.32, 11.91, 0.61],
        ["#3 Cylinder", 10.79, 17.78, 0.86],
        ["#5", 13.02, 14.29, 0.83],
        ["#6Z", 5.40, 8.89, 0.22],
        ["#8Z short", 6.83, 7.62, 0.26],
        ["#10", 15.72, 17.78, 1.53],
        ["#211", 6.83, 12.38, 0.34],
        ["#300", 7.62, 11.27, 0.38],
        ["#303", 8.10, 11.11, 0.42]
    ]

    # tin_can_sizes = get_can_sizes()

    # Storage the most efficient and best cost
    best_storage_eff = [0, ""]
    best_cost = [0, ""]

    for can_size in tin_can_sizes:
        radius = can_size[1]
        height = can_size[2]
        cost = can_size[3]

        storage_efficiency = compute_storage_efficiency(radius, height)
        cost_efficiency = compute_cost_efficiency(radius, height, cost)

        print(can_size[0], f"{storage_efficiency:.2f}", f"{cost_efficiency:.2f}")

        # If the current storage efficiency is greater than the best, save the current in the variable
        if storage_efficiency > best_storage_eff[0]:
            best_storage_eff = [storage_efficiency, can_size[0]]
        
        # If the current cost efficiency is greater than the best, save the current in the variable
        if cost_efficiency > best_cost[0]:
            best_cost = [cost_efficiency, can_size[0]]

    print()
    print("Best can size in storage efficiency:", best_storage_eff[1])
    print("Best can size in cost efficiency:", best_cost[1])
    print()

def compute_volume(radius, height):
    volume = math.pi * (radius**2) * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(radius, height):
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)

    storage_efficiency = volume / surface_area

    return storage_efficiency

def compute_cost_efficiency(radius, height, cost):
    # Computing the volume
    volume = compute_volume(radius, height)

    # Provided formula
    cost_efficiency = volume / cost

    return cost_efficiency

def get_can_sizes():
    # Initialize the variable
    tin_can_sizes = []

    # Open the file
    with open("sources/tin_can_sizes.txt") as can_sizes_file:
            # Iterate each line of the file
            for line in can_sizes_file:
                # Storage each line as an object
                line_stripped = line.strip().split(sep="\t")
                # Parse the variables and storage the object formated
                can_size = [line_stripped[0], float(line_stripped[1]), float(line_stripped[2]), float(line_stripped[3].removeprefix("$"))]
                # Add the object to the list
                tin_can_sizes.append(can_size)

    return tin_can_sizes

main()