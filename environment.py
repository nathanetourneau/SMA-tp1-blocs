import random as rd

class Environment:
    def __init__(self, agents=None, positions=None, end_positions=None):
        self.agents = agents
        self.positions = positions #(i, j)
        self.end_positions = end_positions

    def down_neighbor_id(self, name):
        column, height = self.position[name]

        for key, value in self.positions.items():
            if value == (column, height-1):
                return key
        return None

    def up_neighbor_id(self, name):
        column, height = self.position[name]

        for key, value in self.positions.items():
            if value == (column, height+1):
                return key
        return None



    def goal(self, name):
        agent = self.agents[agent]
        agent_under = down_neighbor(name)
        agent_upper = upper_neighbor(name)
        pass

    def move(self, name):
        pass











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


