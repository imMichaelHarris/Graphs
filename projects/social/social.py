import random
import collections
import time

class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            # print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # O(n)
        for i in range(num_users):
            self.add_user(f"User {i+ 1}")

        possible_friendships = []
        # O(n^2)
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        random.shuffle(possible_friendships)

        # O(n^2)
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def populate_graph_random_sample(self, num_users, avg_friendships):
                # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # O(n)
        for i in range(num_users):
            self.add_user(f"User {i+ 1}")

        # Pick two random friendships
        # While number of friendships < asverage friendsa * num_users / 2
        # Pick two random users
        # Try to create the friendship
        # If it fails, try again
        target_friendships = avg_friendships * num_users
        total_friendships = 0
        collisions = 0

        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            if self.add_friendship(user_id, friend_id):
                total_friendships += 2
            else:
                collisions +=1


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = collections.deque()
        q.appendleft([user_id])
        # Create an empty set to store visited vertices
        # While the queue is not empty 
        print("BFT")
        while len(q) > 0:
        #   dequeue the first vertex
            user = q.pop()
            new_user = user[-1]
        #   If that vertex hasn't been visited..
            if new_user not in visited:
                # print("User", user)
        #       Mark as visited
                visited[new_user] =  user
        #       Then add all of it's neighbors to back of the queue
                for friend in self.friendships[new_user]:
                    if friend not in visited:
                        new_path = list(user)
                        new_path.append(friend)
                        q.appendleft(new_path)

        return visited


    #         total_degrees = 0
    # for path in range(1, len(connections)):
    #     ## add total length of paths (degress sep)
    #     total_degrees += len(connections[path])
    #     # print(len(connections[path]))
    # ## divide total degress by total connects
    # avg_degrees = total_degrees / len(connections)
    # percent_connected = len(connections) / pop_total
    # print(f"avg_degrees : {avg_degrees}")
    # print(f"percent_connected : {percent_connected}")


if __name__ == '__main__':
    sg = SocialGraph()
    start_time = time.time()
    sg.populate_graph_random_sample(10, 2)
    end_time = time.time()
    print(f"Populate Grapg: {end_time - start_time} seconds")
    # print(sg.users)
    print("----------")
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

