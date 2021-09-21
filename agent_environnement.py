import random as rd

class Environment:
    def __init__(self, agents=None, positions=None, end_positions=None):
        self.agents = agents
        self.positions = positions #(i, j)

    def down_neighbor(self, name):
        column, height = self.position[name]

        for key, value in self.positions.items():
            if value == (column, height-1):
                return self.agents[key]
        return None

    def up_neighbor(self, name):
        column, height = self.position[name]

        for key, value in self.positions.items():
            if value == (column, height+1):
                return self.agents[key]
        return None

    def goal(self, name):
        agent = self.agents[agent]
        agent_under = down_neighbor(name)
        agent_upper = upper_neighbor(name)
        if

    def move(self, name):











class Agent:
    def __init__(self, downside=None):
        self.downside = downside

        isinstance(self.downside, Agent)

    def move(self, x):
        pass

    def push(self):
        pass


    def is_satisfied(self):
        pass


