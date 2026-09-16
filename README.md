# CSPC Lab Report

## PW1 Lab A: Reproducible Foundations
**Simulation Speed:** 
* Pure Python: 1.8275s
* NumPy: 0.0012s
* Speed-up: NumPy is 1539.5x faster!

**Tests:** All 3 pytest checks are passing. 

**Conclusion:** Vectorizing the decay simulation with NumPy provides a massive performance increase over standard Python loops. Setting up a reproducible conda environment and automated testing ensures the code remains reliable.

## PW1 Lab B: Data, Plotting, and Automation
**Report:** The observed data strongly matches the analytical decay law. The scatter plot follows the shape of the exponential curve. 
**Automation:** A Snakemake pipeline was implemented to track dependencies and automatically regenerate the plot only if the source code or CSV data changes.