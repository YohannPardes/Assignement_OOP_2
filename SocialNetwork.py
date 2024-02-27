from User import User


class SocialNetwork:
    """
    This class implements a social network using a singleton pattern
    """
    instance = None

    def __new__(cls, name: str):
        if cls.instance is None:
            cls.instance = super(SocialNetwork, cls).__new__(cls)
            cls.instance.__initialized = False
            print(f"The social network {name} was created!")

        return cls.instance

    def __init__(self, name: str):
        if not self.__initialized:
            # network params
            self.__name = name

            # users parameters
            self.__user_list = {}
            self.__connected_users = set()
            self.__initialized = True

    def sign_up(self, user_name: str, password: str):

        # check username
        if user_name in self.__user_list.keys():
            raise ValueError("This username is already in use, please try another one")
        # check password length
        if not 4 <= len(password) <= 8:
            raise ValueError(f"The password '{password}' is {len(password)} long and should be between 4 to 8")

        # if everything is fine creating the user and add it to the user and connected list
        new_user = User(user_name, password)
        self.__user_list[user_name] = new_user
        self.__connected_users.add(user_name)

        return new_user

    def log_in(self, user_name: str, password: str):
        """ this function add the user to the logged user while checking it's a valid command"""

        try:
            user = self.__user_list[user_name]
        except KeyError:
            raise ValueError(f"The user {user_name} is not an existing user")  # if the username is not an existing user

        if user_name in self.__connected_users:  # check if the user is already connected
            raise ValueError("The user is already logged in")

        if not user.check_password(password):  # wrong password has been inputted
            raise ValueError("Wrong password")

        print(f"{user_name} connected")
        user.connected = True
        self.__connected_users.add(user_name)

    def log_out(self, user_name: str):
        """This function put the user in a logged out state"""

        print(f"{user_name} disconnected")
        self.__connected_users.remove(user_name)  # throw an error if the user is already logged out
        self.__user_list[user_name].connected = False

    def __str__(self):
        """The __str__ of SocialNetwork print all the users of the platform"""
        string = f"{self.__name} social network:\n"
        for user, obj in self.__user_list.items():
            string += str(obj) + "\n"

        return string
