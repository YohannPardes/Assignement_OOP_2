from User import User


class SocialNetwork:
    """
    This class implements a social network using a singleton pattern
    """

    def __init__(self, name: str):
        self.name = name

    def sign_up(self, user_name: str, password: str):  # this function is a user factory
        return User(user_name, password)

    def log_in(self):
        pass

    def log_out(self):
        pass

    def __str__(self):  # not sure about this one
        pass
