class Source(object):
    all = set()

    def __init__(self, identifier, title, version=None):
        self.identifier = identifier
        self.title = title
        self.version = version
        self.all.add(self)
