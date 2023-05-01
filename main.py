isim: str = str(input("İsminiz: "))
vize: int = int(input("Vize Notunuz: "))
final: int = int(input("Final Notunuz: "))

sonuc: float = float((vize * 0.4) + (final * 0.6))

print(f"Ortalama: {sonuc}")
if sonuc > 84.9:
     print("AA")
elif sonuc > 74.9 and sonuc < 85:
     print("BA")
elif sonuc > 59.9 and sonuc < 75:
     print("CB")
elif sonuc > 49.9 and sonuc < 60:
     print("CC")
else:
     print("FF")




