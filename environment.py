import random as rd
import numpy as np


class Environment:
    def __init__(self, agents=None, input_pattern=None, end_pattern=None):
        nb_blocs = len(agents)

        self.agents = agents
        self.board = np.array([["-" for i in range(nb_blocs)] for j in range(3)])

        self.positions = {k: (0, v) for v, k in enumerate(input_pattern)}
        self.board[0, :] = input_pattern

        # We add None at the beggining and at the end of the list of
        # positions to make the check of is the goal reached easier
        end_pattern.append(None)
        end_pattern.insert(0, None)
        self.end_pattern = end_pattern

    def down_neighbor_id(self, name):
        column, height = self.positions[name]

        for key, value in self.positions.items():
            if value == (column, height - 1):
                return key
        return None

    def up_neighbor_id(self, name):
        column, height = self.positions[name]

        for key, value in self.positions.items():
            if value == (column, height + 1):
                return key
        return None

    def goal(self, name):
        agent_down = self.down_neighbor_id(name)
        agent_up = self.up_neighbor_id(name)
        agent_index = None

        for index, elt in enumerate(self.end_pattern):
            if elt == name:
                agent_index = index
                break
        else:
            raise Exception("The agent doesn't exist in the end positions")

        return (
            self.end_pattern[agent_index - 1] == agent_down
            and self.end_pattern[agent_index + 1] == agent_up
        )

    def move(self, name):
        columns = [0, 1, 2]
        column, _ = self.positions[name]
        columns.remove(column)
        new_column = rd.choice(columns)

        # Now, we will make sure that the block will go over the highest block
        max_height = -1
        for column, height in self.positions.values():
            if column == new_column:
                if height >= max_height:
                    max_height = height
        new_height = max_height + 1
        column, height = self.positions[name]
        self.positions[name] = (new_column, new_height)
        self.board[column, height] = "-"
        self.board[new_column, new_height] = name

    def is_pushing(self, name):
        if name:
            return self.agents[name].pushing
        return False

    def show_board(self):
        print(self.board)

