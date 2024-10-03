countries = {"India":1393409038,"USA":331002651,"China":1444216107,"Brazil":213993437,"Russia":145912025}
high_population = 0
max_key = 0
for i in countries:
    if countries[i] > high_population:
        high_population = countries[i]
        max_key = i
#print(high_population)
print(max_key)
#print()

