from Post import Post


class User:
    """
    this class implements A user in the social network using the design pattern of observer (to the SocialNetwork class)
    """
    def __init__(self, name: str, password: str):
        self.__notifications = []  # hold the notificatoin that the user will receive
        self.__name = name  # the user_name of the user
        self.__password = password  # the password of the user
        self.__followed = set()  # the followed users of the user
        self.__followers = set()  # the users the user has followed
        self.__posts = []  # the posts the user sent
        self.__connected = True  # the state of the user logged_in/logged_out

    def __str__(self):
        return f"User name: {self.name}, Number of posts: {len(self.__posts)}, Number of followers: {len(self.__followers)}"

    def update(self, notif_message):
        """this function add the notification to the notification list"""
        self.__notifications.append(notif_message)

    def follow(self, user):
        """This function handle the event of self following another user"""
        if self.connected:
            print(f"{self.name} started following {user.__name}")
            self.__followed.add(user)
            user.__followers.add(self)

    def unfollow(self, user):
        """This function handle the event of self following another user"""
        print(f"{self.name} unfollowed {user.name}")
        if self.connected:
            self.__followed.remove(user)
            user.__followers.remove(self)

    def publish_post(self, kind: str, *args):  # this method is a post factory
        """given a kind (string) return a post of the inputted kind using a post factory"""
        if self.connected:
            post = Post.create_post(self, kind, *args)
            self.__posts.append(post)
            return post

    def check_password(self, password: str):
        """given a password check whether this is the user's password"""
        return self.__password == password

    @property
    def connected(self):
        """return true of false whether the user is connected or not"""
        return self.__connected

    @connected.setter
    def connected(self, flag: bool):
        """self.connected setter"""
        self.__connected = flag

    @property
    def name(self):
        """self.name getter"""
        return self.__name

    @property
    def followers(self):
        """self.followers getter"""
        return self.__followers

    def print_notifications(self):
        """print all the notification that the user got"""
        print(f"{self.name}'s notifications:")
        print(*self.__notifications, sep="\n")
