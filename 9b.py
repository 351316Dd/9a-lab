#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:29:33 2024

@author: doudouliu
"""

9b assignment:

#Create your own github repo
#Add a .py file
#Create a simple version of an agent based simulation, 
#based on the code in the last lecture, and the github repo linked at the end
#1. Create an Agent class
#2. Create a World class
#3. Initialize the world
#4. Create a loop
#Ask each agent in sequence to find an empty patch
#Move the agent to the empty patch
#5. End
#Keep it simple (small grid, small number of agents, small number of loops), 
#and utilize the code from the more complex example given in lecture. 



import random

class Agent:
    def __init__(self, id, world):
        self.id = id
        self.world = world

    def move(self):
        empty_patches = [(x, y) for x in range(self.world.size) for y in 
                         range(self.world.size) if self.world.grid[x][y] is None]
        if empty_patches:
            self.world.grid[random.choice(empty_patches)] = self

class World:
    def __init__(self, size):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.agents = [Agent(i, self) for i in range(3)]  # Small number of agents

    def run(self):
        for step in range(3):  # Small number of loops
            for agent in self.agents:
                agent.move()
            self.display()

    def display(self):
        for row in self.grid:
            print(" ".join(['A' if cell else '.' for cell in row]))
        print()

if __name__ == "__main__":
    world = World(5)  # Small grid size
    world.run()
