import random

POUND_TO_KG = 0.45359237
RATE_PER_KG = 2
PRIZE_THRESHOLD = 100
PRIZES = ["کلاه", "قلاب", "سطل"]

pounds = float(input("چند پوند ماهی گرفته‌اید؟ "))

kilograms = pounds * POUND_TO_KG
payment = kilograms * RATE_PER_KG

print(f"وزن ماهی: {kilograms:.2f} کیلوگرم")
print(f"مبلغ دریافتی: {payment:.2f} دلار")

if payment > PRIZE_THRESHOLD:
    prize = random.choice(PRIZES)
    print(f"تبریک! شما یک {prize} برنده شدید!")
