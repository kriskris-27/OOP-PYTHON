# Staffing Optimization Engine (v1.1)

This automated decision-support tool evaluates retail transaction data to optimize staffing levels based on workload capacity and gross margin protection rather than traditional calendar dates.

---

## What the Script Does

1. **Dynamic Column Detection:** Scans the CSV file's header row to locate any column containing `"sales"` (case-insensitive). If an exact match isn't found, it defaults to column index `1`. This enables cross-compatibility for alternative shop data layouts.

2. **Market Phase Detection:** Calculates a trailing 12-month moving average baseline. If the most recent month’s sales outperform this average, the engine flags the market as **PEAK CYCLICAL**; otherwise, it registers as **OFF-PEAK/VOID**.

3. **Capacity Stress-Testing:** Projects the upcoming 6-month sales and divides it by the current team headcount (`6`) to calculate the average monthly workload per person. The system will recommend hiring **only if** this workload breaks the proven efficiency ceiling (**23.00 units/staff/month**).

4. **Financial Scenario Modeling:** Applies the exact corporate margin constraint formula: `(Sales × 0.45) - (Staff × 3 × 6)` to output a side-by-side net profit comparison between a 6-staff and 7-staff configuration.

---

## How to Run the Script

### 1. Requirements
* Written strictly using Python standard libraries (`csv` and `sys`).
* **Zero external dependencies** (no `pandas` or `numpy` required). 
* Compatible with any system running Python 3.x.

### 2. File Setup
Ensure that `store_analyzer.py` and your tracking data sheet (e.g., `RevI-Test.csv`) are saved in the **exact same folder**.

### 3. Execution Commands
Open your terminal or command prompt inside that directory and run:

* **Standard Run (Defaults to looking for `RevI-Test.csv`):**
  ```bash
  python store_analyzer.py