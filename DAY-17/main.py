class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.userName = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.followers += 1
        user.following += 1
        # print(
        #     "new user being created..."
        # )  # this will printted evrey time when new instance is created


user_1 = User("100", "jibril A.")
user_2 = User("100", "jemal S.")

# user_1.name = "jibril"
# user_1.id = "1000"
# print(user_1.userName)
# print(user_1.followers)
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
