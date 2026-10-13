# Desafio 3 - Conversor de tempo
print("\n=== Desafio 3: Conversor de tempo ===")
total_segundos = int(input("Digite o tempo em segundos: "))

horas = total_segundos // 3600
minutos = (total_segundos % 3600) // 60
segundos = total_segundos % 60

print(
    f"{total_segundos} segundos = "
    f"{horas}h {minutos}min {segundos}s")
