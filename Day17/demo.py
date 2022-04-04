class User:
    def __init__(self, user_id, user_name):
        print("New user created")
        self.id = user_id
        self.name = user_name
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


user_1 = User(100, "Angela")
user_2 = User(100, "Yu")

user_1.follow(user_2)

print(user_1.following)
print(user_1.follower)

print(user_2.following)
print(user_2.follower)
