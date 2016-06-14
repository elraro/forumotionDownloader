class Forum:

    def __init__(self, id, name, link):
        self.id = id
        self.name = name
        self.link = link

    def __repr__(self):
        return "<Forum id:%s name:%s link:%s>" % (self.id, self.name, self.link)

    def __str__(self):
        return "<Forum id:%s name:%s link:%s>" % (self.id, self.name, self.link)
