from Lib import Container


class GA:
    def __init__(
        self,
        domain: set,
        packages: list,
        containerType: Container,
        populationCount: int,
    ):
        self.domain = domain

    def select(self):
        raise NotImplemented()

    def mutate(self):
        raise NotImplemented()

    def crossOver(self):
        raise NotImplemented()

    def forward(self):
        raise NotImplemented()
