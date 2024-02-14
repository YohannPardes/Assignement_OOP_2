from User import User


class Post:
    """
    This class implements a post in our social network using a factory design pattern
    """

    def like(self, user: User):
        pass

    def comment(self, user: User, text: str):
        pass

    def create_post(self, kind: str, *args):
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


class TextPost(Post):

    def __init__(self, text):
        self.text = text


class ImagePost(Post):

    def __init__(self, img_path):
        self.img_path = img_path


class SalePost(Post):

    def __init__(self, product_name: str, price: int, city_sale: str):
        self.product_name = product_name
        self.price = price
        self.city_sale = city_sale

    def sold(self):
        pass
