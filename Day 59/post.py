class Post:
    def __init__(self, post: dict):
        self.post_id = post['id']
        self.title = post['title']
        self.subtitle = post['subtitle']
        self.body = post['body']
        self.author = post['author']
        self.date = post['date']
        self.image = post['image']
