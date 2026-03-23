import random

import numpy as np

from Lib import Container
from Lib.Package import PackageType


class GA:
    def __init__(
        self,
        domain: set,
        packages: list,
        containerType: Container,
        populationCount: int,
    ):
        self.domain = domain
        self.packages = packages
        self.containerType = containerType
        self.populationCount = populationCount
        self.population = np.empty(0)
        self.generatePopulation()

    def generatePopulation(self):
        self.population = np.random.choice(
            list(self.domain), size=(self.populationCount, len(self.packages))
        )

    def fitness(self, individual):
        totalContainers = len(set(individual))
        score = totalContainers
        weight = {}
        volume = {}
        fragilePackages = {}
        packageTypes = {}
        for i in range(len(individual)):
            package = self.packages[i]
            id = individual[i]
            weight[id] = package.weight + weight.get(id, 0)
            volume[id] = package.volume + volume.get(id, 0)
            fragilePackages[id] = fragilePackages.get(id, 0) + (
                1 if package.isFragile else 0
            )

            packageTypes[id] = packageTypes.get(id, {})
            packageTypes[id][package.type] = packageTypes[id].get(package.type, 0) + 1

            # Rigid Rules
            if (
                weight[id] > self.containerType.maxWeight
                or volume[id] > self.containerType.volume
                or fragilePackages.get(id, 0) > self.containerType.maxFragilePackages
                or (
                    packageTypes[id].get(PackageType.Metals, 0) > 0
                    and fragilePackages.get(id, 0) > 0
                )
                or (
                    packageTypes[id].get(PackageType.Electronics, 0) > 0
                    and packageTypes[id].get(PackageType.Metals, 0) > 0
                )
                or max(dict.values(weight)) - min(dict.values(weight)) > 300
            ):
                return 99999999

        return score

    def select(self):
        scores = np.apply_along_axis(axis=1, arr=self.population, func1d=self.fitness)
        self.population = self.population[np.argsort(scores)][: self.populationCount]

    def getRandomGeneIndex(self):
        return random.randint(0, self.population.shape[1] - 1)

    def mutate(self, offspring, mutationRate=0.05):
        mutationMask = np.random.rand(*offspring.shape) < mutationRate

        domainList = list(self.domain)
        randomGenes = np.random.choice(domainList, size=offspring.shape)

        mutated_offspring = np.where(mutationMask, randomGenes, offspring)

        return mutated_offspring

    def crossover(self):
        parentsIdx = np.random.permutation(self.population.shape[0])

        half = len(parentsIdx) // 2
        parentA = self.population[parentsIdx[:half]]
        parentB = self.population[parentsIdx[half : 2 * half]]

        mask = np.random.rand(*parentA.shape) < 0.5

        childA = np.where(mask, parentA, parentB)
        childB = np.where(mask, parentB, parentA)

        offspring = np.vstack([childA, childB])
        return offspring

    def forward(self):
        offspring = self.crossover()

        mutatedOffspring = self.mutate(offspring)

        self.population = np.vstack([self.population, mutatedOffspring])

        self.select()

    def run(self, epochs=100, step=1):
        firstFitness = self.fitness(self.population[0])
        for epoch in range(epochs):
            self.forward()
            fit = self.fitness(self.population[0])
            if epoch % step == 0:
                print(f"Epoch {epoch}")
                print(fit)
                print(f"Error: {fit - firstFitness}")
