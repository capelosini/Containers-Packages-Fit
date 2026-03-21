class Container:
    """
    maxWeight -> KG
    volume -> M^3
    """

    def __init__(
        self,
        maxWeight: float = 1000.0,
        volume: float = 2.0,
        maxFragilePackages: int = 3,
    ):
        self.maxWeight = float(maxWeight)
        self.volume = float(volume)
        self.maxFragilePackages = maxFragilePackages
