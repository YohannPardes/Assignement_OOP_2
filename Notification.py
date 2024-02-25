class Notification:

    @classmethod
    def new_post(cls, owner):
        message = f"{owner.name} has a new post"
        for f in owner.followers:
            f.update(message)

    @classmethod
    def add_like(cls, owner, liker):

        if owner != liker:
            message = f"{liker.name} liked your post"
            owner.update(message)

    @classmethod
    def add_comment(cls, owner, commenter):
        if owner != commenter:
            message = f"{commenter.name} commented on your post"
            owner.update(message)

    @classmethod
    def notify(cls, kind: str, owner, *args):

        match kind:
            case "Like":
                liker = args[0]
                cls.add_like(owner, liker)

            case "Comment":
                commenter = args[0]
                comment= args[1]
                cls.add_comment(owner, commenter)

            case "NewPost":
                cls.new_post(owner)