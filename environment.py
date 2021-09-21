import random as rd

class Environment:
    def __init__(self, agents=None, positions=None, end_positions=None):
        self.agents = agents
        self.positions = positions #(i, j)
        end_positions.append(None)
        end_positions.insert(0, None)
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
        agent_under = self.down_neighbor(name)
        agent_upper = self.up_neighbor(name)
        agent_index = None

        for index, elt in enumerate(self.end_positions):
            if elt == name:
                agent_index = index
                break
        else:
            raise Exception("The agent doesn't exist in the end positions")

        return self.end_positions[agent_index-1] == agent_under and self.end_positions[agent_index+1] == agent_upper



    def move(self, name):
        pass



