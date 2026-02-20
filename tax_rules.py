# tax_rules.py

from csv_utils import get_regional_rate

# IRPEF semplificata per 2026
IRPEF_BRACKETS = [
    (28000, 0.23),
    (50000, 0.33),
    (float("inf"), 0.43)
]

INPS_RATE = 0.0919  # contributo dipendente

def calculate_irpef(taxable_income):
    tax = 0
    previous_limit = 0
    for limit, rate in IRPEF_BRACKETS:
        if taxable_income > limit:
            tax += (limit - previous_limit) * rate
            previous_limit = limit
        else:
            tax += (taxable_income - previous_limit) * rate
            break
    return tax

def calculate_detrazioni(gross_salary):
    """
    Simulazione semplice delle detrazioni per lavoro dipendente.
    Qui possiamo fare una formula lineare semplificata.
    """
    if gross_salary == 0:
        return 0
    elif gross_salary <= 15000:
        return 1955
    elif gross_salary <= 28000:
        return 1910 + 1190 * (28000 - gross_salary) / (28000 - 15000)
    elif gross_salary <= 50000:
        return 1910 * (50000 - gross_salary) / (50000 - 28000)
    else:
        return 0

def calculate_net_salary(gross_salary, region):
    inps = gross_salary * INPS_RATE
    taxable_income = gross_salary - inps
    irpef = calculate_irpef(taxable_income)
    detrazioni = calculate_detrazioni(gross_salary)
    add_regionale = get_regional_rate(region, taxable_income) * taxable_income  

    net = gross_salary - inps - irpef + detrazioni - add_regionale

    return {
        "gross": gross_salary,
        "inps": inps,
        "irpef": irpef,
        "detrazioni": detrazioni,
        "addizionale_regionale": add_regionale,
        "net": net
    }
    
