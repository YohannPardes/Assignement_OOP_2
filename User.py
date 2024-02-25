from Post import Post


class User:
    """
    this class implements A user in the social network using the design pattern of observer (to the SocialNetwork class)
    """

    def __init__(self, name: str, password: str):
        self.__notifications = []
        self.__name = name
        self.__password = password
        self.__followed = set()
        self.__followers = set()
        self.__posts = []
        self.__connected = True

    def __str__(self):
        return f"User name: {self.name}, Number of posts: {len(self.__posts)}, Number of followers: {len(self.__followers)}"

    def update(self, notif_message):
        self.__notifications.append(notif_message)

    def follow(self, user):
        if self.connected:
            print(f"{self.name} started following {user.__name}")
            self.__followed.add(user)
            user.__followers.add(self)

    def unfollow(self, user):
        print(f"{self.name} unfollowed {user.name}")
        if self.connected:
            self.__followed.remove(user)
            user.__followers.remove(self)

    def publish_post(self, kind: str, *args):  # this method is a post factory
        if self.connected:
            post = Post.create_post(self, kind, *args)
            self.__posts.append(post)
            return post

    def check_password(self, password: str):
        return self.__password == password


    @property
    def connected(self):
        return self.__connected

    @connected.setter
    def connected(self, flag: bool):
        self.__connected = flag

    @property
    def name(self):
        return self.__name

    @property
    def followers(self):
        return self.__followers

    def print_notifications(self):
        print(f"{self.name}'s notifications:")
        print(*self.__notifications, sep = "\n")


