from Lib import GA, Container
from PackagesInput import packages

container = Container(1000.0, 2.0, 3)
maxContainers = len(packages)
populationCount = 50

totalWeight = sum([p.weight for p in packages])
totalVolume = sum([p.volume for p in packages])

print(f"Total Weight {totalWeight}Kg\nTotal Volume {totalVolume:.2f}m^3")

ga = GA(
    domain=set(range(0, maxContainers)),
    containerType=container,
    packages=packages,
    populationCount=populationCount,
)

ga.run(5000, step=100)
