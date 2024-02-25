class Notification:

    @classmethod
    def new_post(cls, owner):

        message = f"{owner.name} has a new post"
        for f in owner.followers:
            f.update(message)

    @classmethod
    def add_like(cls, owner, liker):
        if owner != liker:
            print(f"notification to {owner.name}: {liker.name} liked your post")
            message = f"{liker.name} liked your post"
            owner.update(message)

    @classmethod
    def add_comment(cls, owner, commenter, comment):
        if owner != commenter:
            print(f"notification to {owner.name}: {commenter.name} commented on your post : {comment}")
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
                comment = args[1]
                cls.add_comment(owner, commenter, comment)

            case "NewPost":
                cls.new_post(owner)
