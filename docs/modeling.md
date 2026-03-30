### Chromosome
The chromosome is a **1D NumPy array** representing package assignments.
* **Gene Representation:** The integer value at index `i` is the Container ID for package `i`.
* **Length:** 30 (total packages).
* **Domain:** The user-defined set of available container IDs.

---

### Fitness Function
The fitness function uses a **Minimization** strategy, incorporating hard constraints and a multi-objective heuristic.

* **Hard Constraints (Death Penalty):** Any violation of weight (1000kg), volume (2.0m³), fragility (max 3), or material incompatibility (Metals vs. Electronics/Fragile) results in a penalty score of **99,999,999**.
* **Primary Objective:** Minimize the count of unique Container IDs used.
* **Secondary Objective (Logistics Optimization):** To prioritize shipping efficiency, the function adds the average number of unique destinations per container to the score. This encourages the GA to group packages destined for the same country into the same container.

---

### Operators

#### Selection: Fitness Proportionate Selection (Probabilistic)
Instead of a simple sort-and-trim, this implementation calculates a probability distribution across the population:
1. Valid individuals are assigned weights based on their distance from the worst valid score (`max_valid - score`).
2. Penalized individuals are given a near-zero probability (`1e-10`).
3. `np.random.choice` is used to sample the next generation based on these weights.
This preserves genetic diversity and allows the algorithm to explore more of the search space.

#### Crossover: Uniform Crossover
A vectorized uniform crossover is applied. A random binary mask determines, gene-by-gene, which parent provides the container ID for the offspring. This allows for a flexible exchange of grouping strategies.

#### Mutation: Random Resetting
At a 5% rate per gene, a package is reassigned to a completely random valid container ID. This prevents the algorithm from getting stuck in local optima.

---

### Initialization
* **Strategy:** Pure Random.
* **Constraint Handling:** The algorithm begins with random assignments. While most are initially invalid, the probabilistic selection quickly shifts the population toward valid, lower-scoring configurations.

---

### Stopping Criterion
The algorithm executes for a fixed number of **epochs**. Progress is tracked by comparing the best fitness of each generation against the initial random state.
