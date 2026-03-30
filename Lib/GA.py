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
        destinations = {}
        for i in range(len(individual)):
            package = self.packages[i]
            id = individual[i]
            destinations[id] = destinations.get(id, [])
            destinations[id].append(package.destination)
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

        uniqueDestinationsPerContainer = [len(set(d)) for d in destinations.values()]

        return score + sum(uniqueDestinationsPerContainer) / len(
            uniqueDestinationsPerContainer
        )

    def select(self):
        scores = np.apply_along_axis(axis=1, arr=self.population, func1d=self.fitness)

        penalized_value = 999999
        is_penalized = scores >= penalized_value

        if np.all(is_penalized):
            probs = np.ones(len(scores)) / len(scores)
        else:
            max_valid = np.max(scores[~is_penalized])

            weights = np.where(is_penalized, 1e-10, (max_valid - scores) + 1e-6)

            probs = weights / np.sum(weights)

        indices = np.random.choice(
            len(self.population), size=self.populationCount, p=probs
        )

        self.population = self.population[indices]

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

    def forward(self, mutationRate=0.05):
        offspring = self.crossover()

        mutatedOffspring = self.mutate(offspring, mutationRate=mutationRate)

        self.population = np.vstack([self.population, mutatedOffspring])

        self.select()

    def printIndividual(self, individual):
        containers = {}
        for i in range(len(individual)):
            containerId = individual[i]
            package = self.packages[i]
            containers[containerId] = containers.get(containerId, [])
            containers[containerId].append(package)

        for key in containers.keys():
            print(f"--Container #{key}")
            totalWeight = 0
            for p in containers[key]:
                print(f"\t{p}")
                totalWeight += p.weight
            print(f"Total Weight: {totalWeight}")
        print(f"Total Containers: {len(containers)}")

    def run(self, epochs=100, step=1):
        # firstFitness = self.fitness(self.population[0])
        mutationRate = 0.05
        x = []
        y = []
        for epoch in range(epochs):
            self.forward(mutationRate=mutationRate)
            fit = self.fitness(self.population[0])
            if (epoch + 1) % step == 0:
                print(f"Epoch {epoch + 1}")
                print(fit)
                x.append(epoch + 1)
                y.append(fit)
                # print(f"Error: {fit - firstFitness}")
        self.printIndividual(self.population[0])

        print(
            f'xychart-beta\n\ttitle "Fitness Evolution — pop={self.populationCount}, mut={mutationRate}"\n\tx-axis "Generation" {x}\n\ty-axis "Fitness" 0 --> 20\n\tline {y}'
        )
