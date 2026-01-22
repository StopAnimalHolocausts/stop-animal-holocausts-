# 🧬 Protocol: Cell Expansion & Suspension Adaptation
**Version:** 1.0 (January 2026)
**Target:** High-efficiency expansion of Bovine Satellite Cells (BSCs) for Bioreactor Inoculation.

---

## 📌 Overview
To reach industrial scale, muscle cells must transition from 2D surfaces (flasks) to 3D suspension (stirred-tank bioreactors). This protocol utilizes the **"Cell Aggregate"** method to prevent anoikis (cell death from lack of attachment) while maintaining myogenicity.

---

## 🛠️ Phase 1: Pre-Adaptation (Flask Expansion)
Before moving to suspension, cells must reach a "Critical Mass" in 2D culture using the **B9-L Media** (see `MEDIA_PREP.md`).

1. **Seeding:** Seed BSCs at $5,000$ cells/$cm^2$ in T-175 flasks.
2. **Growth:** Incubate at $37$°C, $5$% $CO_2$.
3. **Harvesting:** Detach cells at $80$% confluence using **TrypLE Select** (10 mins). 
4. **Neutralization:** Neutralize with 2x volume of B9-L media. Do not use serum.

---

## 🚀 Phase 2: Suspension Adaptation (The "Step-Down" Method)
This phase transitions the cells into an agitated environment using a **Spinner Flask** or **Shaker Flask**.

### Step 1: Inoculation
* **Density:** Seed at $5 \times 10^5$ cells/mL in $100$ mL of B9-L media.
* **Vessel:** Use a siliconized spinner flask to prevent cells from sticking to the glass.

### Step 2: Agitation Strategy
* **Day 0-1:** Stationary incubation for 4 hours (allows micro-aggregate formation), then start stirring at **$30$ RPM**.
* **Day 2-4:** Increase speed to **$50$ RPM**. 
* **Day 5+:** Maintain **$60$–$70$ RPM**. 

### Step 3: Monitoring Aggregation
* **Target Size:** Aggregates should be $100$–$200$ μm in diameter.
* **Action:** If aggregates exceed $400$ μm, increase RPM slightly to introduce shear stress and prevent necrotic cores (cell death in the center of the clump).

---

## 📊 Phase 3: Bioreactor Scaling
Once cells maintain a doubling time of **<$24$ hours** in spinner flasks, they are ready for the **50L+ Bioreactor**.

| Parameter | Value | Note |
| :--- | :--- | :--- |
| **Dissolved Oxygen (DO)** | $40$% | Maintain via micro-sparging. |
| **pH** | $7.2$ | Controlled via $CO_2$ and $NaHCO_3$. |
| **Temperature** | $37$°C | Constant PID control. |
| **Feeding** | $25$% exchange | Replace media every 48h to maintain FGF2-G3 levels. |

---

## ⚠️ Troubleshooting
* **Issue: High Cell Death (Anoikis)**
    * *Solution:* Add **$10$ μM Y-27632 (ROCK Inhibitor)** during the first 24 hours of suspension transition.
* **Issue: Excessive Foaming**
    * *Solution:* Add **$0.1$% Pluronic F-68** to the media to protect cell membranes from bubbles.

---

## ✅ Quality Check
Cells are successfully adapted if:
1. Viability remains **>$90$%** after 3 passages in suspension.
2. Cells retain the ability to fuse into **multinucleated myotubes** when moved back to a 2D differentiation medium.
