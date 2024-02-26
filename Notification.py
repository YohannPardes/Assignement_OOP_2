
class Notification:
    """
    This class represent the notification par of the observer design pattern
    """
    @classmethod
    def new_post(cls, owner):
        """This function handle the "add_like" notification"""
        message = f"{owner.name} has a new post"
        for f in owner.followers:
            f.update(message)

    @classmethod
    def add_like(cls, owner, liker):
        """This function handle the "add_like" notification"""
        if owner != liker:
            print(f"notification to {owner.name}: {liker.name} liked your post")
            message = f"{liker.name} liked your post"
            owner.update(message)

    @classmethod
    def add_comment(cls, owner, commenter, comment):
        """This function handle the "add_comment" notification"""
        if owner != commenter:
            print(f"notification to {owner.name}: {commenter.name} commented on your post: {comment}")
            message = f"{commenter.name} commented on your post"
            owner.update(message)

    @classmethod
    def notify(cls, kind: str, owner, *args):
        """This function using a menu of possible notifications notify the user acordingly"""

        match kind:
            case "Like":
                liker = args[0]
                cls.add_like(owner, liker)

            case "Comment":
                commenter = args[0]
                comment = args[1]
                cls.add_comment(owner, commenter, comment)

            case "NewPost":
                cls.new_post(owner)
