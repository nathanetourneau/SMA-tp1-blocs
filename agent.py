class Agent:
    def __init__(self, name):
        self.name = name
        self.goal = False
        self.pushing = False

    def is_satisfied(self, environment):
        if (environment.down_neighbor(self.name).pushing) or not (
            environment.goal(self.name)
        ):
            return False
        return True

    def move(self, environment, column):
        if self.is_free():
            environment.move(self.name)

    def push(self):
        self.pushing = True

    def action(self, environment):
        if not self.is_satisfied(environment):
            if self.is_free():
                self.move(environment)
                self.pushing = False
            else:
                self.push(environment)

            return True
        else:
            return False

    def is_free(self, environment):
        pass

