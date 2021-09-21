#########################################
#           MONDE DES BLOCS             #
#########################################
import string
from environment import Environment
from agent import Agent


def main():
    agents = {k: Agent(k) for k in list("ABCD")}
    input_pattern = list("ABCD")
    end_pattern = list("DCBA")
    env = Environment(agents, input_pattern, end_pattern)

    end = False
    nb_rounds = 0

    while end == False:
        env.show_board()
        print("\n")

        if all([k.is_satisfied(env) for k in env.agents.values()]):
            end = True

        for name, agent in env.agents.items():
            agent.action(env)
        nb_rounds += 1

    print(f"Nombre de rounds pour te mettre KO : {nb_rounds}")


if __name__ == "__main__":
    main()
