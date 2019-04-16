import random
from collections import deque


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        for i in range(numUsers):
            self.addUser(f'User {i}')
        possibleFriendships = []
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))
        random.shuffle(possibleFriendships)
        for i in range(numUsers * avgFriendships // 2):
            friendship = possibleFriendships[i]
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        for i in self.bft(userID):
            visited[i] = self.bfs(userID, i, self.friendships)
        return visited

    def bft(self, v):
        q = deque([v])
        visited = set()
        while len(q) > 0:
            vertex = q.popleft()
            if vertex not in visited:
                visited.add(vertex)
                for i in self.friendships[vertex]:
                    q.append(i)
        return visited

    def bfs(self, v, goal_v, graph):
        q = deque([v])
        visited = set()
        while len(q) > 0:
            path = q.popleft()
            if isinstance(path, list):
                v = path[-1]
            if isinstance(path, int):
                v = path
            if v not in visited:
                if v == goal_v:
                    return path
                visited.add(v)
                for next_v in graph[v]:
                    if isinstance(path, list):
                        new_path = list(path)
                    if isinstance(path, int):
                        new_path = [path]
                    new_path.append(next_v)
                    q.append(new_path)
        return None

    # def bfs(self, v, goal_v, graph):
    #     q = deque([v])
    #     visited = set()
    #     firstRun = True
    #     while q:
    #         path = q.popleft()
    #         if firstRun:
    #             v = path
    #         if not firstRun:
    #             v = path[-1]
    #         if v not in visited:
    #             if v == goal_v:
    #                 if firstRun:
    #                     return [path]
    #                 return path
    #             visited.add(v)
    #             for next_v in graph[int(v)]:
    #                 if firstRun:
    #                     new_path = [path]
    #                 if not firstRun:
    #                     new_path = path
    #                 new_path.append(next_v)
    #                 q.append(new_path)
    #         firstRun = False
    #     return None


# def runMultiple():
#     averages = []
#     for i in range(50):
#         averages.append(get_average_separation())
#     total = 0
#     for i in averages:
#         total += i
#     print(total/len(averages))


# def get_average_separation():
#     sg = SocialGraph()
#     sg.populateGraph(1000, 5)
#     connections = []
#     for i in sg.users:
#         connections.append(len(sg.getAllSocialPaths(i)))
#     total = 0
#     for i in connections:
#         total += connections[i]
#     return total/len(connections)


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    # print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
    # print(len(connections))
    # runMultiple()
