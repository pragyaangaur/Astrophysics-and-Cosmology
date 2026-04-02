# Black Holes

## Projects

### 1. Black Hole Thermodynamics

**What it Does:**  
Models how temperature, horizon area, and entropy vary with black hole mass, spanning stellar-mass to supermassive regimes.

**Core Ideas:**
- Hawking temperature decreases with mass  
- Horizon area scales quadratically with mass  
- Entropy is proportional to horizon area  

**Approach:**
- Define a mass range across multiple orders of magnitude  
- Compute:
  - T ∝ 1/M  
  - A ∝ M²  
  - S ∝ M²  
- Visualize relationships using appropriate scaling (log-log for mass vs temperature)  

**How it Works:**  
The model evaluates thermodynamic quantities directly from analytical relations. By plotting these across a large mass range, it highlights how black holes differ from conventional thermodynamic systems, particularly the inverse relationship between mass and temperature.

**Key Insight:**  
Larger black holes are colder, while smaller black holes radiate more intensely.

**Stack:** Python, NumPy, SciPy, Matplotlib  
<p align="center">
<img src="../Assets/Black-Holes-Plots.jpeg" width="800"></p>

### 2. Black Hole Evaporation Dynamics

**What it Does:**  
Numerically solves the mass loss equation governing black hole evaporation and tracks the time evolution of mass and temperature.

**Core ideas:**  
- Mass loss follows: dM/dt ∝ −1/M²
- Temperature increases as mass decreases: T ∝ 1/M
- Lifetime scales as t ∝ M³  

**Approach:**  
The evaporation equation is solved using numerical integration. The model computes:  
- Mass as a function of time
- Temperature evolution derived from instantaneous mass
- Normalized evolution curves to reveal universal behavior  

**How it Works:**  
The simulation integrates the nonlinear differential equation for mass loss under semiclassical assumptions. The results show that black holes evolve slowly for most of their lifetime, followed by a rapid late-stage collapse where temperature diverges and the approximation breaks down.

**Key Insight:**  
Black hole evaporation is highly nonlinear: nearly all observable change occurs in the final fraction of the lifetime, reflecting the inverse-mass instability inherent in the system.

**Limitations**  
- Assumes perfect blackbody radiation  
- Neglects accretion and environmental effects  
- Breaks down near M → 0, where quantum gravity is expected to dominate  

**Stack:** Python, NumPy, SciPy, Matplotlib  
<p align="center">
<img src="../Assets/BH-Raw-Time-Evolution.png" width="800"><img src="../Assets/Universal-BH-Evaporation.png" width="800"></p>
