class Agent:
    def __init__(self, name):
        self.name = name
        self.pushing = False

    def is_satisfied(self, environment):
        if (environment.is_pushing(environment.down_neighbor_id(self.name))) or not (
            environment.goal(self.name)
        ):
            return False
        return True

    def move(self, environment):
        if self.is_free(environment):
            environment.move(self.name)

    def push(self):
        self.pushing = True

    def is_free(self, environment):
        return environment.up_neighbor_id(self.name) is None

    def action(self, environment):
        if not self.is_satisfied(environment):
            if self.is_free(environment):
                self.move(environment)
                self.pushing = False
            else:
                self.push()

            return True
        else:
            return False

