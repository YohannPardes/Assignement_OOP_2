from abc import ABC, abstractmethod
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class Post(ABC):
    """
    This class implements a post in our social network using a factory design pattern
    """

    def __init__(self):
        self.__like = 0
        self.__comments = {}

    def like(self, user):

        if user.connected():
            self.__like += 1

        else:
            raise ValueError("This username is not connected!")

    def comment(self, user, text: str):

        if user.connected():
            if user in self.__comments.keys():  # TODO - why like this?
                self.__comments[user] = [text]

            else:
                self.__comments[user].append(text)

        else:
            raise ValueError("This username is not connected!")

    @classmethod
    def create_post(cls, kind: str, *args):

        if kind == "Text":
            text = args[0]
            return TextPost(text)

        elif kind == "Image":
            img_path = args[0]
            return ImagePost(img_path)

        elif kind == "Sale":
            product_name = args[0]
            price = args[1]
            sale_city = args[2]
            return SalePost(product_name, price, sale_city)

    @abstractmethod
    def display(self):
        pass


class TextPost(Post):

    def __init__(self, text):
        super().__init__()
        self.text = text

    def display(self):
        raise TypeError(f"A {self.__class__.__name__} cannot be displayed, only ImagePost")


class ImagePost(Post):

    def __init__(self, img_path):
        super().__init__()
        self.img_path = img_path

    """
    This function take the path of the image stored in img_path and display it using matplotlib, Pillow and numpy"""

    def display(self):
        img = mpimg.imread('your_image.png')
        imgplot = plt.imshow(img)
        plt.show()


class SalePost(Post):

    def __init__(self, product_name: str, price: int, city_sale: str):
        super().__init__()
        self.product_name = product_name
        self.price = price
        self.city_sale = city_sale

    def sold(self):
        pass

    def display(self):
        raise TypeError(f"A {self.__class__.__name__} cannot be displayed, only ImagePost")
