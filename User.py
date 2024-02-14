from Post import*





class User:
    """
    this class implements A user in the social network using the design pattern of observer (to the SocialNetwork class)
    """

    def __init__(self, name: str, password: str):
        self.name = name
        self.__password = password

    def follow(self, user):
        pass

    def publish_post(self, kind: str, *args):  # this method is a post factory
        post = Post.create_post(kind, args)
        return post
