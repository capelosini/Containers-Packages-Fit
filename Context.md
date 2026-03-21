# Container Packing Optimization for Export

---

## 1. Context

A Brazilian exporting company performs weekly shipments of goods to various countries. Each shipment consists of boxes of varying sizes and weights, which must be distributed into standard containers before being transported to the port. Manually allocating boxes to containers is a time-consuming task and frequently results in wasted space and the unnecessary use of extra containers—each additional container represents a significant freight cost.

You have been hired to develop a system based on a **Genetic Algorithm (GA)** capable of automatically finding the best distribution of boxes in containers, respecting all physical and logistical constraints while minimizing the number of containers used.

---

## 2. Problem Description

The company needs to ship **30 boxes** in standard capacity containers. Each container has a maximum capacity of **1,000 kg** and **2.0 m³** of volume. The boxes have varying weights and volumes, as well as logistical attributes such as fragility, destination, and product type.

The problem is a variant of the classic **Bin Packing Problem**, with additional constraints that bring it closer to real-world international logistics situations.

### 2.1 Boxes to be Shipped

| Box | Weight (kg) | Volume (m³) | Fragile | Destination | Type |
|---|---|---|---|---|---|
| C01 | 80 | 0.20 | No | Argentina | Electronics |
| C02 | 120 | 0.30 | Yes | Chile | Glassware |
| C03 | 50 | 0.10 | No | Argentina | Textiles |
| C04 | 200 | 0.40 | No | Uruguay | Metals |
| C05 | 30 | 0.08 | Yes | Chile | Glassware |
| C06 | 150 | 0.35 | No | Argentina | Metals |
| C07 | 90 | 0.25 | No | Uruguay | Textiles |
| C08 | 60 | 0.15 | Yes | Chile | Electronics |
| C09 | 110 | 0.28 | No | Argentina | Electronics |
| C10 | 75 | 0.18 | No | Uruguay | Textiles |
| C11 | 180 | 0.45 | No | Chile | Metals |
| C12 | 40 | 0.10 | Yes | Argentina | Glassware |
| C13 | 95 | 0.22 | No | Uruguay | Electronics |
| C14 | 130 | 0.32 | No | Argentina | Metals |
| C15 | 55 | 0.12 | Yes | Chile | Glassware |
| C16 | 170 | 0.42 | No | Uruguay | Metals |
| C17 | 45 | 0.11 | No | Argentina | Textiles |
| C18 | 100 | 0.26 | Yes | Chile | Electronics |
| C19 | 85 | 0.20 | No | Uruguay | Textiles |
| C20 | 140 | 0.34 | No | Argentina | Metals |
| C21 | 65 | 0.16 | Yes | Chile | Glassware |
| C22 | 115 | 0.29 | No | Uruguay | Electronics |
| C23 | 35 | 0.09 | No | Argentina | Textiles |
| C24 | 160 | 0.38 | No | Chile | Metals |
| C25 | 70 | 0.17 | Yes | Uruguay | Glassware |
| C26 | 125 | 0.31 | No | Argentina | Electronics |
| C27 | 90 | 0.23 | No | Chile | Textiles |
| C28 | 145 | 0.36 | No | Uruguay | Metals |
| C29 | 55 | 0.13 | Yes | Argentina | Glassware |
| C30 | 105 | 0.27 | No | Chile | Electronics |

**Total:** 2,970 kg | 7.22 m³

### 2.2 Standard Container Specifications

| Attribute | Value |
|---|---|
| Maximum Weight Capacity | 1,000 kg |
| Maximum Volume Capacity | 2.0 m³ |
| Max Number of Fragile Boxes per Container | 3 |

---

## 3. Constraints

* **C1 – Weight Capacity:** The sum of the weights of the boxes in a container cannot exceed **1,000 kg**.
* **C2 – Volume Capacity:** The sum of the volumes of the boxes in a container cannot exceed **2.0 m³**.
* **C3 – Fragile Stacking:** Boxes marked as **fragile** cannot be placed in a container that contains **Metals** type boxes. Additionally, each container can contain a maximum of **3 fragile boxes**.
* **C4 – Destination Grouping:** Boxes with the **same destination** should preferably be in the same container.
* **C5 – Incompatible Type Separation:** **Electronics** type boxes cannot be allocated to the same container as **Metals** type boxes.
* **C6 – Total Coverage:** All 30 boxes must be allocated; none can be left out.
* **C7 – Weight Balancing:** The difference between the heaviest and lightest container (total weight) must not exceed **300 kg**.

---

## 4. Fitness Function

The primary objective is to **minimize the number of containers used**:

$$\text{minimize} \quad N_{cont}$$

Secondary objective: **maximize the average occupancy rate**:

$$\text{maximize} \quad \frac{1}{N_{cont}} \sum_{k=1}^{N_{cont}} \frac{w_k}{1000}$$

**Evaluation Formula:**

$$f = V - \sum_{i} p_i \cdot n_i - \alpha \cdot N_{cont} + \beta \cdot \text{Avg Occupancy}$$

Where:
* $V$: High base value.
* $p_i, n_i$: Penalty weight and number of violations for constraint $i$.
* $\alpha$: Penalty for extra containers.
* $\beta$: Reward for high occupancy.

---

## 5. Expected Output

The output must list box allocation, totals per container, and a final summary.

```text
Container 1 — Predominant Destination: Argentina
  Boxes: C01, C03, C06, C09, C12, C17, C23
  Total Weight:  625 kg  (62.5%)
  Total Volume: 1.50 m³ (75.0%)
  Fragile: 1 | Types: Electronics, Textiles, Glassware
  Violations: 0

...

Summary:
  Containers used: X
  Average weight occupancy: XX.X%
  Average volume occupancy: XX.X%
  Violations: 0
```

## 6. Implementation Tips

### 6.1 Chromosome/Individual
Initialize using **First Fit Decreasing (FFD)**: sort boxes by weight (descending) and place them in the first available container. This provides a high-quality starting point for the GA.

### 6.2 Mutation
Randomly move a box to a different container or swap two boxes between containers to optimize weight balance and satisfy logistical constraints without necessarily increasing the container count.
