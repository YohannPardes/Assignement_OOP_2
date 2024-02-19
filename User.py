from Post import Post


def check_connection(func):
    def wrapper(obj, *args, **kwargs):
        if not obj.connected:
            raise PermissionError("You are not connected therefore this action is illegal")

        return func(*args, **kwargs)

    return wrapper


class User:
    """
    this class implements A user in the social network using the design pattern of observer (to the SocialNetwork class)
    """

    def __init__(self, name: str, password: str):
        self.__name = name
        self.__password = password
        self.__followed = set()
        self.__posts = []
        self.__connected = True

    @check_connection
    def follow(self, user):
        self.__followed.add(user)

    @check_connection
    def unfollow(self, user):
        self.__followed.remove(user)

    @check_connection
    def publish_post(self, kind: str, *args):  # this method is a post factory
        post = Post.create_post(kind, args)
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
