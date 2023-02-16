print("Pitsa yetkazib berish hizmati!")

size = input("Qanday kattalikdagi pitsa xohlaysiz? S, M, or L: ").upper()
while size != "S" and size != "M" and size != "L":
    print("Siz xohlagan pitsa topilmadi")
    size = input("Qayta urinib ko'ring: ").upper()
pepperoni = input("pepperonini qo'shishni xohlaysizmi? (kichik pitsa uchun $2 o'rtacha va katta pitsa uchun $3) yes/no: ").lower()
extra_cheese = input("extra cheeseni qo'shishni xohlaysizmi? (xohlagan pitsangiz uchun $1) yes/no: ").lower()

bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25
if pepperoni == "yes":
  if size == "S":
    bill += 2
  else:
    bill += 3
if extra_cheese == "yes":
  bill += 1
print(f"Sizning pitsangiz: ${bill}")
