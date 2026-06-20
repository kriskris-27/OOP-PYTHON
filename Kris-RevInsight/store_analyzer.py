import csv
import sys

# --- CONFIGURABLE BUSINESS PARAMETERS ---
SALARY_PER_PERSON = 3
MARGIN_MULTIPLIER = 0.45  # 50% Gross Margin - 5% Variable Commission
CYCLE_LENGTH = 6
CURRENT_STAFF_COUNT = 6
CAPACITY_THRESHOLD = 23   # Units per staff member per month before hitting a bottleneck

def analyze_store(file_path):
    monthly_sales = []
    
    try:
        with open(file_path, mode='r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            header = [col.strip() for col in next(reader)] # 
            try:
                sales_index = next(i for i, col in enumerate(header) if 'sales' in col.lower())
            except StopIteration:
                
                sales_index = 1

            for row in reader:
                if row and len(row) > sales_index and row[sales_index].strip(): 
                    monthly_sales.append(float(row[sales_index]))
    except FileNotFoundError:
        print(f"Error: Target file '{file_path}' could not be located.")
        sys.exit(1)
    except Exception as e:
        print(f"Data Processing Error: {e}")
        sys.exit(1)

    if len(monthly_sales) < CYCLE_LENGTH * 2:
        print("Configuration Error: Insufficient historical data points for cycle evaluation.")
        return

    # 2. Extract Cycle Metrology
    recent_cycle = monthly_sales[-CYCLE_LENGTH:]
    projected_sales = sum(recent_cycle)
    avg_monthly_sales = projected_sales / CYCLE_LENGTH
    
    # 3. Dynamic Market Phase & Capacity Calculation
    
    historical_baseline = sum(monthly_sales[-int(CYCLE_LENGTH*2):]) / (CYCLE_LENGTH * 2)
    is_peak = recent_cycle[-1] >= historical_baseline
    
    
    load_per_staff = avg_monthly_sales / CURRENT_STAFF_COUNT 

    # 4. Core Decision Rule
    should_hire = is_peak and (load_per_staff > CAPACITY_THRESHOLD)

    # 5. Financial Modeling Scenario Generation
    margin_6 = (projected_sales * MARGIN_MULTIPLIER) - (6 * SALARY_PER_PERSON * CYCLE_LENGTH)
    margin_7 = (projected_sales * MARGIN_MULTIPLIER) - (7 * SALARY_PER_PERSON * CYCLE_LENGTH)

    # 6. Structured Output Generation
    print("=" * 55)
    print("           REVINSIGHT STAFFING ENGINE v1.1         ")
    print("=" * 55)
    print(f"Current Macro Market Phase : {'PEAK CYCLICAL' if is_peak else 'OFF-PEAK/VOID'}")
    print(f"Projected 6-Month Volume   : {projected_sales:.2f} units")
    print(f"Projected Load per Staff   : {load_per_staff:.2f} units/month")
    print(f"Proven Store Unit Ceiling  : {CAPACITY_THRESHOLD:.2f} units/month")
    print("-" * 55)
    print(f"Expected Margin (6 Staff)  : {margin_6:.2f} units")
    print(f"Expected Margin (7 Staff)  : {margin_7:.2f} units")
    print("-" * 55)
    
    if should_hire:
        print("RECOMMENDATION: ACTION REQUIRED -> HIRE REPLACEMENT.")
        print(f"Reasoning: Current unit load per capita ({load_per_staff:.1f}) breaks the")
        print(f"efficiency limit ({CAPACITY_THRESHOLD}). Understaffing will drop conversions.")
    else:
        print("RECOMMENDATION: OPTIMIZE MARGIN -> DO NOT HIRE.")
        print(f"Reasoning: Current unit load ({load_per_staff:.1f}) is within safe thresholds.")
        print(f"Operating with 6 staff captures maximum bottom-line margin.")
    print("=" * 55)

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else 'RevI-Test.csv'
    analyze_store(target)