from random import sample
from typing import List

import networkx as nx


class User:
    def __init__(self, name: str) -> None:
        self.id = None
        self.name = name
        self.friends = []

    def add_friends(self, friends: List['User']) -> None:
        for friend in friends:
            self.add_friend(friend)

    def add_friend(self, friend: 'User') -> None:
        self.friends.append(friend.id)
        friend.friends.append(self.id)


class Network:
    k = 3

    def __init__(self) -> None:
        self.users = set()
        self.network_graph = nx.Graph()
        self.count = 0

    def add_user(self, user: User) -> None:
        self.users.add(user)
        self.assign_id(user)
        self.add_friends(user)
        self.add_user_to_graph(user)

    def assign_id(self, user: User) -> None:
        user.id = self.count
        self.count += 1

    def add_user_to_graph(self, user: User) -> None:
        self.network_graph.add_node(user.id)
        edges = [(user.id, friend_id) for friend_id in user.friends]
        self.network_graph.add_edges_from(edges)

    def add_friends(self, user: User) -> None:
        if len(self.users) < 4:
            return
        friends = sample(self.users - {user}, Network.k)
        user.add_friends(friends)
