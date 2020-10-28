import matplotlib.pyplot as plt

import Entities
import networkx as nx

if __name__ == "__main__":
    network = Entities.Network()
    for i in range(20):
        user = Entities.User(f"User {i}")
        network.add_user(user)

    nx.draw(network.network_graph)
    plt.show(block=False)
    plt.pause(1)

    while True:
        command = input()
        if command == 'q':
            plt.close("all")
            break
