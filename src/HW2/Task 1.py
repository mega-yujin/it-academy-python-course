price_ruble = 3
price_kop = 20
quantity = 3

total_price_kop = price_ruble * 100 + price_kop
total_price_kop *= quantity

total_price_ruble = total_price_kop // 100
total_price_kop %= 100

print(f"Общая цена {total_price_ruble} рублей {total_price_kop} копеек")
