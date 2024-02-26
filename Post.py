from abc import ABC, abstractmethod
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from Notification import Notification


class Post(ABC):
    """
    This class implements a post in our social network using a factory design pattern
    """

    def __init__(self):
        self.__like = 0
        self.__comments = {}
        self._owner = None

    def like(self, user):
        """This function handle the behavior of a posted liked"""
        if user.connected:
            self.__like += 1
            Notification.notify("Like", self._owner, user)

        else:
            raise ValueError("This username is not connected!")

    def comment(self, user, text: str):
        """This function handle the behavior of a comment in the network"""
        if user.connected:
            Notification.notify("Comment", self._owner, user, text)

        else:
            raise ValueError("This username is not connected!")

    @classmethod
    def create_post(cls, owner, kind: str, *args):
        """This function handle the behavior of a new post created in the network
        using a factory like design pattern"""

        # create a different Post child according to the situation (inputted kind of post)
        if kind == "Text":
            text = args[0]
            return TextPost(owner, text)

        elif kind == "Image":
            img_path = args[0]
            return ImagePost(owner, img_path)

        elif kind == "Sale":
            product_name = args[0]
            price = args[1]
            sale_city = args[2]
            return SalePost(owner, product_name, price, sale_city)

    @abstractmethod
    def display(self):
        """This function is for displaying a picture"""
        pass

    @property
    def owner(self):
        """getter of self.owner"""
        return self._owner

    @owner.setter
    def owner(self, user):
        """setter of self.owner"""
        self._owner = user


class TextPost(Post):
    """This class implements the abstract class of Post
    and represent a text post"""

    def __init__(self, owner, text):
        super().__init__()
        self.text = text
        self._owner = owner

        print(self)
        Notification.notify("NewPost", owner)

    def __str__(self):
        return f"{self._owner.name} published a post:\n\"{self.text}\"\n"

    def display(self):
        raise TypeError(f"A {self.__class__.__name__} cannot be displayed, only ImagePost")


class ImagePost(Post):
    """This class implements the abstract class of Post
        and represent an image post"""

    def __init__(self, owner, img_path):
        super().__init__()
        self._owner = owner
        self.img_path = img_path

        print(self)
        Notification.notify("NewPost", owner)

    def __str__(self):
        return f"{self._owner.name} posted a picture\n"

    def display(self):
        """This function take the path of the image stored in img_path and display it using matplotlib"""
        img = mpimg.imread(f"{self.img_path}")
        plt.imshow(img)
        print("Shows picture")
        plt.show()


class SalePost(Post):
    """This class implements the abstract class of Post
        and represent a sale post"""

    def __init__(self, owner, product_name: str, price: int, city_sale: str):
        super().__init__()
        self._owner = owner
        self.product_name = product_name
        self.price = price
        self.city_sale = city_sale
        self.status = True

        print(self)
        Notification.notify("NewPost", owner)

    def __str__(self):
        string = "For sale" if self.status else "Sold"
        return (f"{self._owner.name} posted a product for sale:\n{string}! "
                f"{self.product_name}, price: {self.price}, pickup from: {self.city_sale}\n")

    def sold(self, password: str):
        """This function handle a sold event of a sale post"""
        if self._owner.check_password(password) and self.owner.connected:  # if the password is correct and the user is connected
            self.status = False
            print(f"{self._owner.name}'s product is sold")
        else:
            raise ValueError("Wrong password! or you are not connected")

    def discount(self, discount_perc, password: str):
        """This function handle a discount on a sale post"""
        if self._owner.check_password(
                password) and self.status and self.owner.connected:  # if the product is still to sale, the right password is inputed and the user is connected
            self.price = (self.price * (100 - discount_perc)) / 100
            print(f"Discount on {self._owner.name} product! the new price is: {self.price}")
        else:
            raise ValueError("Wrong password! or not connected or the product already has been sold")

    def display(self):
        raise TypeError(f"A {self.__class__.__name__} cannot be displayed, only ImagePost")
