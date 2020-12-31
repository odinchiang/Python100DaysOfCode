class User:
    def __init__(self, uid, name):
        # attributes
        self.uid = uid
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(1, "Mark")
user_2 = User(2, "John")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


