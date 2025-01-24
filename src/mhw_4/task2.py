n = int(input())
country_cities = {}

for _ in range(n):
    country, *cities = input().split()
    for city in cities:
        country_cities[city] = country

m = int(input())

for _ in range(m):
    city = input().strip()
    print(country_cities.get(city, "Город не найден"))