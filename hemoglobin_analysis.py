# =============================================================
# hemoglobin_analysis.py
# Análisis de la secuencia de proteína de la hemoglobina beta humana
# Fuente: NCBI RefSeq NP_000509.1 / UniProt P68871
# Ejercicios 3 al 9
# =============================================================

import json

# ── Secuencia limpia (Ejercicio 2) ────────────────────────────
with open("hemoglobin_clean.txt", "r") as f:
    sequence = f.read().strip()


# Ejercicio 4: Información general de la secuencia

protein_name = "Hemoglobin subunit beta [Homo sapiens]"

print("=" * 55)
print("  ANÁLISIS DE PROTEÍNA")
print("=" * 55)
print(f"  Nombre    : {protein_name}")
print(f"  Accesión  : NP_000509.1 / P68871")
print(f"  Longitud  : {len(sequence)} aminoácidos")
print(f"  Secuencia : {sequence[:30]}...")
print("=" * 55)


# Ejercicio 5: Composición de aminoácidos

amino_acids = [
    "A", "R", "N", "D", "C",
    "Q", "E", "G", "H", "I",
    "L", "K", "M", "F", "P",
    "S", "T", "W", "Y", "V"
]

amino_count = {aa: sequence.count(aa) for aa in amino_acids}

print("\n COMPOSICIÓN DE AMINOÁCIDOS")
print("-" * 35)
for aa, count in sorted(amino_count.items()):
    bar = "//" * count
    print(f"  {aa}: {count:3d}  {bar}")


# Ejercicio 6: Pesos moleculares de aminoácidos (g/mol)

molecular_weights = {
    "A":  89.09,  "R": 174.20,  "N": 132.12,  "D": 133.10,
    "C": 121.16,  "Q": 146.15,  "E": 147.13,  "G":  75.03,
    "H": 155.16,  "I": 131.17,  "L": 131.17,  "K": 146.19,
    "M": 149.20,  "F": 165.19,  "P": 115.13,  "S": 105.09,
    "T": 119.12,  "W": 204.23,  "Y": 181.19,  "V": 117.15
}


# Ejercicio 7: Función reutilizable para calcular peso molecular

def calculate_molecular_weight(seq: str, weights: dict) -> float:
    """
    Calcula el peso molecular aproximado de una secuencia proteica.

    Args:
        seq     : cadena de aminoácidos en código de una letra
        weights : diccionario {aminoácido: peso_molecular}

    Returns:
        Peso molecular total en g/mol (menos agua por cada enlace peptídico)
    """
    water = 18.02                        # peso del agua (Da)
    total = sum(weights.get(aa, 0) for aa in seq)
    total -= water * (len(seq) - 1)      # restar enlaces peptídicos
    return round(total, 2)


mol_weight = calculate_molecular_weight(sequence, molecular_weights)

print(f"\n  PESO MOLECULAR")
print("-" * 35)
print(f"  Peso molecular estimado: {mol_weight:,.2f} g/mol")


# Ejercicio 9: Porcentaje de aminoácidos hidrofóbicos

hydrophobic = ["A", "V", "I", "L", "M", "F", "W", "Y"]

hydrophobic_count = sum(sequence.count(aa) for aa in hydrophobic)
hydrophobic_pct   = round((hydrophobic_count / len(sequence)) * 100, 2)

print(f"\n AMINOÁCIDOS HIDROFÓBICOS  (A, V, I, L, M, F, W, Y)")
print("-" * 35)
print(f"  Cantidad    : {hydrophobic_count}")
print(f"  Porcentaje  : {hydrophobic_pct}%")


# Ejercicio 8: Guardar resultados en JSON

results = {
    "protein_name"          : protein_name,
    "accession"             : "NP_000509.1",
    "sequence_length"       : len(sequence),
    "amino_acid_count"      : amino_count,
    "molecular_weight_g_mol": mol_weight,
    "hydrophobic_count"     : hydrophobic_count,
    "hydrophobic_percentage": hydrophobic_pct
}

with open("hemoglobin_results.json", "w") as f:
    json.dump(results, f, indent=4)

print(f"\n Resultados guardados en: hemoglobin_results.json")
print("=" * 55)
