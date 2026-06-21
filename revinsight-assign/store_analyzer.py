import csv
import sys

# --- CONFIGURABLE BUSINESS PARAMETERS ---
SALARY_PER_PERSON = 3
MARGIN_MULTIPLIER = 0.45  # 50% Gross Margin - 5% Variable Commission
CYCLE_LENGTH = 6
CURRENT_STAFF_COUNT = 6
CAPACITY_THRESHOLD = 23   # Units per staff member per month before hitting a bottleneck

def analyze_store(file_path):
    print(f"[1/4] Attempting to open data file: {file_path}...")
    monthly_sales = []
    historical_staffing = []
    
    # 1. Secure File Ingestion
    try:
        with open(file_path, mode='r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            header = [col.strip() for col in next(reader)]
            print(f"[2/4] Successfully read CSV Header: {header}")
            
            # Dynamically map columns based on exact names
            sales_index = None
            for i, col in enumerate(header):
                if 'sales' in col.lower() or 'total' in col.lower():
                    sales_index = i
                    break
            
            # Fallback if specific string isn't found
            if sales_index is None:
                print(" -> Warning: No explicit 'Sales' header column identified. Defaulting to Column Index 1.")
                sales_index = 1
            else:
                print(f" -> Successfully mapped target data column: '{header[sales_index]}' at Index {sales_index}")

            # Identify all individual salesperson columns
            sp_indices = [i for i, col in enumerate(header) if col.lower().startswith('sale sp')]

            # Read rows
            for row_num, row in enumerate(reader, start=2):
                if not row:
                    continue
                try:
                    # Parse aggregate sales
                    sales_value = float(row[sales_index])
                    monthly_sales.append(sales_value)
                    
                    # Calculate active staff count for this specific month (non-zero entries)
                    active_staff = sum(1 for idx in sp_indices if idx < len(row) and float(row[idx]) > 0)
                    historical_staffing.append(active_staff)
                except ValueError:
                    print(f" -> Skipping unparseable or empty data row at Line {row_num}")
                    continue
                    
    except FileNotFoundError:
        print(f"\n[FATAL ERROR]: Target file '{file_path}' could not be located in this directory.")
        sys.exit(1)
    except Exception as e:
        print(f"\n[DATA INGESTION ERROR]: {e}")
        sys.exit(1)

    print(f"[3/4] Data ingestion complete. Processed {len(monthly_sales)} valid operational months.")

    if len(monthly_sales) < CYCLE_LENGTH * 2:
        print(f"\n[ERROR]: Insufficient data history. Your file contains {len(monthly_sales)} records, but the system requires at least {CYCLE_LENGTH * 2} to run seasonality analysis.")
        return

    print("[4/4] Executing dynamic financial and capacity stress tests...\n")

    # 2. Extract Cycle Metrology (Year-over-Year Seasonal Index Calculation)
    recent_cycle = monthly_sales[-CYCLE_LENGTH:]
    
    # Baseline comparison using exact prior cyclical windows
    last_year_same_cycle = monthly_sales[-12:-6] if len(monthly_sales) >= 12 else monthly_sales[-6:]
    projected_sales = sum(last_year_same_cycle) * 1.05  # 5% YoY structural market adjustments
    avg_projected_monthly = projected_sales / CYCLE_LENGTH
    
    # 3. Dynamic Market Phase Checking
    historical_baseline = sum(monthly_sales[-int(CYCLE_LENGTH*2):]) / (CYCLE_LENGTH * 2)
    is_peak = recent_cycle[-1] >= historical_baseline
    
    # Individual personnel capacity stress load metrics
    load_per_staff = avg_projected_monthly / CURRENT_STAFF_COUNT 

    # 4. Core Decision Architecture Rule
    should_hire = is_peak and (load_per_staff > CAPACITY_THRESHOLD)

    # 5. Financial Modeling Scenario Generation
    margin_6 = (projected_sales * MARGIN_MULTIPLIER) - (6 * SALARY_PER_PERSON * CYCLE_LENGTH)
    margin_7 = (projected_sales * MARGIN_MULTIPLIER) - (7 * SALARY_PER_PERSON * CYCLE_LENGTH)

    # 6. Structured Architecture Output Generation
    print("=" * 60)
    print("         REVINSIGHT ADVANCED STAFFING ARCHITECTURE          ")
    print("=" * 60)
    print(f"Dataset History Length       : {len(monthly_sales)} Months")
    print(f"Projected 6-Month Volume     : {projected_sales:.2f} units (Seasonal Adjusted)")
    print(f"Projected Monthly Unit/Staff : {load_per_staff:.2f} units")
    print(f"Operational Stress Limit     : {CAPACITY_THRESHOLD:.2f} units/staff")
    print("-" * 60)
    print(f"Modeled Margin (6 Staff)     : {margin_6:.2f} units")
    print(f"Modeled Margin (7 Staff)     : {margin_7:.2f} units")
    print("-" * 60)
    
    if should_hire:
        print("RECOMMENDATION: ACTION REQUIRED -> HIRE REPLACEMENT.")
        print(f"Reasoning: Current unit load per capita ({load_per_staff:.1f}) breaks the")
        print(f"efficiency limit ({CAPACITY_THRESHOLD}). Understaffing will drop conversions.")
    else:
        print("RECOMMENDATION: OPTIMIZE MARGIN -> DO NOT HIRE.")
        print(f"Reasoning: Current unit load ({load_per_staff:.1f}) is within safe thresholds.")
        print(f"Operating with 6 staff captures maximum bottom-line margin.")
    print("=" * 60)

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else 'RevI-Test.csv'
    analyze_store(target)