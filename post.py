class Post:

    def __init__(self, blog_post):
        self.id = blog_post['id']
        self.title = blog_post['title']
        self.subtitle = blog_post['subtitle']
        self.body = blog_post['body']
