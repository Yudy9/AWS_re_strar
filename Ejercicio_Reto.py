def es_primo(n):
    """Determina si un número es primo."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Encontrar todos los números primos entre 1 y 250
primos = [n for n in range(1, 251) if es_primo(n)]

# Mostrar en pantalla
print("=" * 45)
print("   NÚMEROS PRIMOS ENTRE 1 Y 250")
print("=" * 45)
print(f"Total encontrados: {len(primos)}")
print("-" * 45)
for i, primo in enumerate(primos, 1):
    print(f"  {primo}", end="\t")
    if i % 6 == 0:
        print()
print("\n" + "=" * 45)

# Guardar en results.txt
with open("results.txt", "w") as f:
    f.write("=" * 45 + "\n")
    f.write("   NÚMEROS PRIMOS ENTRE 1 Y 250\n")
    f.write("=" * 45 + "\n")
    f.write(f"Total encontrados: {len(primos)}\n")
    f.write("-" * 45 + "\n")
    for i, primo in enumerate(primos, 1):
        f.write(f"  {primo}\t")
        if i % 6 == 0:
            f.write("\n")
    f.write("\n" + "=" * 45 + "\n")

print("\n Resultados guardados en: results.txt")
print(f"📍 Ruta absoluta del script: /home/claude/primos.py")