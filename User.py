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

    def update(self, notif_message):
        self.__notifications.append(notif_message)

    def follow(self, user):
        if self.connected:
            self.__followed.add(user)
            user.__followers.add(self)

    def unfollow(self, user):
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

