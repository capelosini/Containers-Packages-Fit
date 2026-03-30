# Containers-Packages-Fit
A genetic algorithm that discovers the most optimized way of fitting some deliver packages inside containers.

### Problem Context
```./Context.md```

### Documentation
```./docs/```

---

### Best Output - Generation 10,000

**Final Fitness Score:** 8.2857  
**Total Containers Used:** 7  


#### -- Container #0 (Destination: Argentina)
* **C01:** (80Kg, 0.2m³, Fragile? False, Electronics, Argentina)
* **C03:** (50Kg, 0.1m³, Fragile? False, Textiles, Argentina)
* **C09:** (110Kg, 0.28m³, Fragile? False, Electronics, Argentina)
* **C12:** (40Kg, 0.1m³, Fragile? True, Glassware, Argentina)
* **C17:** (45Kg, 0.11m³, Fragile? False, Textiles, Argentina)
* **C26:** (125Kg, 0.31m³, Fragile? False, Electronics, Argentina)
* **C29:** (55Kg, 0.13m³, Fragile? True, Glassware, Argentina)  
**Total Weight:** 505Kg

#### -- Container #1 (Destination: Chile)
* **C02:** (120Kg, 0.3m³, Fragile? True, Glassware, Chile)
* **C15:** (55Kg, 0.12m³, Fragile? True, Glassware, Chile)
* **C21:** (65Kg, 0.16m³, Fragile? True, Glassware, Chile)  
**Total Weight:** 240Kg

#### -- Container #2 (Mixed: Uruguay/Chile)
* **C04:** (200Kg, 0.4m³, Fragile? False, Metals, Uruguay)
* **C10:** (75Kg, 0.18m³, Fragile? False, Textiles, Uruguay)
* **C24:** (160Kg, 0.38m³, Fragile? False, Metals, Chile)  
**Total Weight:** 435Kg

#### -- Container #3 (Destination: Chile)
* **C05:** (30Kg, 0.08m³, Fragile? True, Glassware, Chile)
* **C08:** (60Kg, 0.15m³, Fragile? True, Electronics, Chile)
* **C18:** (100Kg, 0.26m³, Fragile? True, Electronics, Chile)
* **C27:** (90Kg, 0.23m³, Fragile? False, Textiles, Chile)
* **C30:** (105Kg, 0.27m³, Fragile? False, Electronics, Chile)  
**Total Weight:** 385Kg

#### -- Container #4 (Destination: Argentina)
* **C06:** (150Kg, 0.35m³, Fragile? False, Metals, Argentina)
* **C14:** (130Kg, 0.32m³, Fragile? False, Metals, Argentina)
* **C20:** (140Kg, 0.34m³, Fragile? False, Metals, Argentina)
* **C23:** (35Kg, 0.09m³, Fragile? False, Textiles, Argentina)  
**Total Weight:** 455Kg

#### -- Container #5 (Destination: Uruguay)
* **C07:** (90Kg, 0.25m³, Fragile? False, Textiles, Uruguay)
* **C13:** (95Kg, 0.22m³, Fragile? False, Electronics, Uruguay)
* **C19:** (85Kg, 0.2m³, Fragile? False, Textiles, Uruguay)
* **C22:** (115Kg, 0.29m³, Fragile? False, Electronics, Uruguay)
* **C25:** (70Kg, 0.17m³, Fragile? True, Glassware, Uruguay)  
**Total Weight:** 455Kg

#### -- Container #6 (Mixed: Chile/Uruguay)
* **C11:** (180Kg, 0.45m³, Fragile? False, Metals, Chile)
* **C16:** (170Kg, 0.42m³, Fragile? False, Metals, Uruguay)
* **C28:** (145Kg, 0.36m³, Fragile? False, Metals, Uruguay)  
**Total Weight:** 495Kg

---
**Summary:** The Genetic Algorithm successfully optimized the shipment into just **7 containers**. The solution maximizes destination purity where possible (Argentina, Uruguay, and Chile have dedicated containers) while utilizing mixed containers to stay within the 7-unit limit.
