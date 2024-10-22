from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def credit_form(request):
    if request.method == 'POST':
        # Получение данных для трех банков
        banks = []
        for i in range(1, 4):
            bank_name = request.POST[f'bank_name_{i}']
            credit_type = request.POST[f'credit_type_{i}']
            credit_sum = float(request.POST[f'credit_sum_{i}'])
            interest_rate = float(request.POST[f'interest_rate_{i}']) / 100
            credit_term = int(request.POST[f'credit_term_{i}'])


            # Расчет ежемесячного платежа
            monthly_payment = (credit_sum * interest_rate / 12) / (1 - (1 + interest_rate / 12) ** (-credit_term * 12))
            credit_term_years = round(credit_term / 12, 1)
            sum_rate = monthly_payment*credit_term - credit_sum
            sum_plat = monthly_payment*credit_term  #общая сумма выплат по кредиту

            # Форматируем значение с пробелами между тысячами
            sum_rate_formatted = f"{sum_rate:,.0f}".replace(",", " ")
            credit_sum_formated = f"{credit_sum:,.0f}".replace(",", " ")
            monthly_payment_formated = f"{monthly_payment:,.0f}".replace(",", " ")
            sum_plat_formated = f"{sum_plat:,.0f}".replace(",", " ")

            # Определение цвета в зависимости от процентной ставки
            if interest_rate * 100 < 22:
                card_color = 'bg-success'  # Зеленый для низких ставок
            elif interest_rate * 100 < 24:
                card_color = 'bg-warning'  # Желтый для средних ставок
            else:
                card_color = 'bg-danger'  # Красный для высоких ставок

            result = {
                'bank_name': bank_name,
                'credit_type': credit_type,
                'credit_sum_formated': credit_sum_formated,
                'interest_rate': interest_rate * 100,
                'credit_term': credit_term,
                'credit_term_years': credit_term_years,
                'monthly_payment_formated': monthly_payment_formated,
                'sum_rate': round(sum_rate, 1),
                'sum_rate_formatted': sum_rate_formatted,
                'sum_plat_formated': sum_plat_formated,
                'card_color': card_color  # Добавляем цвет карточки
            }

            banks.append(result)

        return render(request, 'main/credit_result.html', {'results': banks})

    return render(request, 'main/credit_form.html')

def credit_result(request):
    return render(request, 'main/credit_result.html')

def info_without_insurance(request):
    return render(request, 'main/info_without_insurance.html')


