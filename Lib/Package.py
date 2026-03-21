import random
from enum import Enum


class PackageDestination(Enum):
    Other = -1
    Argentina = 0
    Chile = 1
    Uruguay = 2


class PackageType(Enum):
    Other = -1
    Electronics = 0
    Glassware = 1
    Textiles = 2
    Metals = 3


class Package:
    """
    weight -> KG
    volume -> m^3
    """

    def __init__(
        self,
        name: str = f"C{random.randint(10000, 99999)}",
        weight: float = random.random() * 200,
        volume: float = random.random(),
        isFragile: bool = False,
        destination: PackageDestination = PackageDestination.Other,
        type: PackageType = PackageType.Other,
    ):
        self.name = name
        self.weight = weight
        self.volume = volume
        self.isFragile = isFragile
        self.destination = destination
        self.type = type
