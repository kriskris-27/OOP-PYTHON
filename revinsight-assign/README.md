# Retail Staffing Optimization Engine (v1.1)

An automated decision-support tool designed to transform reactive, calendar-based retail hiring practices into a predictive model optimized for margin protection and staff capacity management.

---

## Technical Features & Core Logic

The engine ingestion script processes historical transaction sheets through four algorithmic stages:

1. **Dynamic Schema Mapping:** To prevent hardcoded errors across different data variants, the script automatically reads and clean-strips the CSV header. It performs a case-insensitive match for columns containing `"sales"` or `"total"`. If no explicit column matches, it defaults gracefully to column index `1`. It also dynamically parses individual salesperson attributes (`"sale sp1"` through `"sale sp16"`) to calculate active historical staffing footprints based on non-zero entries.
2. **Year-over-Year (YoY) Seasonality Indexing:** Instead of blindly predicting upcoming performance based on immediate trailing data—which would leave the forecast blind to cyclical variations—the engine isolates the exact corresponding 6-month historical block from the previous year. It then applies a 5% organic year-over-year market adjustment to model an accurate, seasonally adjusted sales target.
3. **Per-Capita Load Stress-Testing:** A seasonal trend alone does not trigger a hire. The system projects average monthly volumes for the upcoming cycle and divides it by the unreplaced core team headcount (`6`). It flags a hiring recommendation **only if** the projected unit load per employee breaches the proven historical bottleneck ceiling (**23.00 units/staff/month**).
4. **Side-by-Side Profit Scenario Modeling:** The architecture models financial outcomes using the store's explicit gross margin constraint equation: `(Sales × 0.45) - (Staff × Salary × Cycle Length)`. It outputs a side-by-side net profit comparison between 6-staff and 7-staff operational states, visualizing capital and cost efficiency.

---

## Execution Instructions

### 1. Pre-requisites & Dependencies
* Built entirely on Python’s native standard libraries (`csv` and `sys`).
* **Zero external dependencies required** (No `pandas`, `numpy`, or `sklearn` installations needed).
* Fully compatible with any environment running **Python 3.x**.

### 2. File Directory Setup
Ensure that the execution script (`store_analyzer.py`) and your transaction logs (e.g., `RevI-Test.csv`) are placed within the **exact same folder/directory**.

### 3. Running from Terminal/Command Prompt
Open your system's terminal, navigate to your project directory, and enter one of the following commands:

* **Standard Run (Applies default target `RevI-Test.csv`):**
  ```bash
  python store_analyzer.py