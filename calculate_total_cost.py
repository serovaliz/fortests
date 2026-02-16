


def calculate_total_cost(price, tax=0.2):
    total_price = price * (1+tax)
    print(f"Итоговая стоимость с НДС  {total_price}")

calculate_total_cost(100)  # С использованием налога по умолчанию
calculate_total_cost(100, 0.1)  # С пользовательским налогом 10%
calculate_total_cost(200, 0.15)  # С пользовательским налогом 15%
calculate_total_cost(50)  # С использованием налога по умолчанию