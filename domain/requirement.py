class Requirement(object):
    all = set()

    def __init__(self, identifier, description, sources):
        self.identifier = identifier
        self.description = description
        self.sources = sources
        self.all.add(self)

    @classmethod
    def from_source(cls, source):
        return [requirement for requirement in cls.all if source in requirement.sources]
