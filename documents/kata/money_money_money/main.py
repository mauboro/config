def calculate_years(principal, interest, tax, desired, times):
    current = principal + (principal * interest - (principal * interest * tax)) 
    year = 0
    if principal == desired:
        return 0
    while current <= desired:
        current += (current * interest - (current * interest * tax)) 
        year += 1
    return year

def calculate_years_refactored(principal, interest, tax, desired, times):
    year = 0
    
    while principal < desired:
        principal += (principal * interest) * (1 - tax)
        year += 1 

    return year
    
