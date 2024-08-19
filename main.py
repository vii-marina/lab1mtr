def calculate_utility(sunny_doma, rainy_doma, forest_sunny, forest_rainy, rain_probability):
    
    W_home = rain_probability * rainy_doma + (1 - rain_probability) * sunny_doma

    W_forest = rain_probability * forest_rainy + (1 - rain_probability) * forest_sunny

    print(f"Корисність рішення залишитись вдома: {W_home}")
    print(f"Корисність рішення піти в ліс: {W_forest}")

    if W_home > W_forest:
        return "Висновок: Краще залишитись вдома і пити чай під час дощу)"
    elif W_home == W_forest :
        return "Висновок: Я не знаю як тобі догодити("
    else :
        return "Висновок: Йди гуляй до лісу, бо ходити то корисно! "


sunny_doma = float(input("Як ти почуваєшся вдома за хорошої погоди? (1-10):"))
rainy_doma = float(input("Як ти почуваєшся вдома під час дощу? (1-10): "))

forest_sunny = float(input("Як ти почуваєшся в лісі за хорошої погоди? (1-10): "))
forest_rainy = float(input("Як ти почуваєшся в лісі під час дощу? (1-10): "))
rain_probability = float(input("Яка ймовірність дощу? (0-1): "))

decision = calculate_utility(sunny_doma, rainy_doma, forest_sunny, forest_rainy, rain_probability)
print(decision)
