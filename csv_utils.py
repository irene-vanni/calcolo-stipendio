import pandas as pd
import math

def get_regional_rate(regione, taxable_income, csv_path="data/addizionale_regionale_2025.csv"):
    """
    Restituisce l'aliquota addizionale regionale per una regione e un reddito imponibile.
    
    Parameters:
        regione (str): nome della regione
        taxable_income (float): reddito imponibile
        csv_path (str): percorso del CSV
    
    Returns:
        float: aliquota decimale (es. 0.0165 per 1.65%)
    """
    # Leggi CSV
    df = pd.read_csv(csv_path, sep=';')
    
    # Filtra solo la regione
    df_region = df[df['REGIONE'].str.strip().str.lower() == regione.strip().lower()]
    
    if df_region.empty:
        raise ValueError(f"Regione '{regione}' non trovata nel CSV")
    
    # Se c'è solo una riga o FASCIA = "Aliquota Unica"
    if len(df_region) == 1 or df_region.iloc[0]['FASCIA'].strip().lower() == "aliquota unica":
        aliquota = float(df_region.iloc[0]['ALIQUOTA'].replace(',', '.')) / 100
        return aliquota
    
    # Altrimenti, più fasce → trovare quella giusta
    for _, row in df_region.iterrows():
        fascia = row['FASCIA'].strip().lower()
        aliquota = float(row['ALIQUOTA'].replace(',', '.')) / 100
        
        if "fino a" in fascia and "oltre" not in fascia:
            # es. "fino a 15000.00 euro"
            limite_sup = float(fascia.replace("fino a", "").replace("euro", "").strip())
            if taxable_income <= limite_sup:
                return aliquota
        
        elif "oltre" in fascia and "fino a" in fascia:
            # es. "oltre 15000.00 e fino a 28000.00 euro"
            parts = fascia.replace("oltre", "").replace("e fino a", ",").replace("euro", "").split(",")
            limite_inf = float(parts[0].strip())
            limite_sup = float(parts[1].strip())
            if limite_inf < taxable_income <= limite_sup:
                return aliquota
        
        elif "oltre" in fascia:
            # es. "oltre 50000.00 euro"
            limite_inf = float(fascia.replace("oltre", "").replace("euro", "").strip())
            if taxable_income > limite_inf:
                return aliquota
    
    # Se non trova fascia → errore
    raise ValueError(f"Nessuna fascia corrispondente trovata per {regione} con reddito {taxable_income}")