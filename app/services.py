import pandas as pd
from app.utils import clean_value

def process_file(file):
    # Charger le fichier
    df = pd.read_excel(file, header=[2, 1])  # Lire avec un en-tête multi-niveau
    if df.empty:
        raise ValueError("The file is empty or invalid format")

    # Extraire les données
    employees = df.iloc[0].dropna().unique().tolist()
    result = []

    for idx, employee in enumerate(employees):
        employee_data = {"name": employee, "infos": []}  # Initialize infos as a ls
        for _, row in df.iloc[2:].iterrows():
            libelle = row.iloc[1]
            base_s = clean_value(row.iloc[2 + idx * 3])
            salarial = clean_value(row.iloc[3 + idx * 3])
            patronal = clean_value(row.iloc[4 + idx * 3])

            # Append (libelle and related infos)
            employee_data["infos"].append({
                "Libellé": libelle,
                "Base S.": base_s,
                "Salarial": salarial,
                "Patronal": patronal
            })
        result.append(employee_data)
    result.pop()
    return result