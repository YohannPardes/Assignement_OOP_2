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

        print(self.__dict__)

        if user.connected:
            self.__like += 1
            Notification.notify("Like", self._owner, user)

        else:
            raise ValueError("This username is not connected!")

    def comment(self, user, text: str):

        if user.connected:
            Notification.notify("Comment", self._owner, user, text)

        else:
            raise ValueError("This username is not connected!")

    @classmethod
    def create_post(cls, owner, kind: str, *args):

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
        pass

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, user):
        self._owner = user


class TextPost(Post):

    def __init__(self, owner, text):
        super().__init__()
        self.text = text
        self._owner = owner

        Notification.notify("NewPost", owner)

    def display(self):
        raise TypeError(f"A {self.__class__.__name__} cannot be displayed, only ImagePost")


class ImagePost(Post):

    def __init__(self, owner, img_path):
        super().__init__()
        self._owner = owner
        self.img_path = img_path

        Notification.notify("NewPost", owner)
    """
    This function take the path of the image stored in img_path and display it using matplotlib"""

    def display(self):
        img = mpimg.imread(f"{self.img_path}")
        plt.imshow(img)
        plt.show()


class SalePost(Post):

    def __init__(self, owner, product_name: str, price: int, city_sale: str):
        super().__init__()
        self._owner = owner
        self.product_name = product_name
        self.price = price
        self.city_sale = city_sale
        self.status = True

        Notification.notify("NewPost", owner)

    def sold(self, password: str):
        if self._owner.check_password(password):
            self.status = False
        else:
            raise ValueError("Wrong password!")

    def discount(self, discount_perc, password: str):
        if self._owner.check_password(password) and self.status:
            self.price = (self.price * (100 - discount_perc)) / 100
        else:
            raise ValueError("Wrong password!")

    def display(self):
        raise TypeError(f"A {self.__class__.__name__} cannot be displayed, only ImagePost")
