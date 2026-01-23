# Avian Taste Optimizer for Molecular Terroir
# Goal: Maximize IMP (Inosine Monophosphate) and Umami-related FAAs

def calculate_avian_umami_overclock(glutamic_acid_level, imp_concentration):
    # Standard broiler baseline
    baseline_umami_index = 100
    
    # Calculate custom "Greatest Mind" Index
    current_index = (glutamic_acid_level * 0.6) + (imp_concentration * 0.4)
    
    if current_index > 150:
        print(f"Status: SUCCESS. Avian Umami Index is {current_index}. Overclocked.")
        return "Tuning complete: High-intensity savory profile achieved."
    else:
        adjustment = 150 - current_index
        return f"Warning: Average flavor detected. Increase IMP input by {adjustment}%"

# Running for Celestial Poultry Profile
print(calculate_avian_umami_overclock(180, 145))
