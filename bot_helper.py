def get_temp_advice(temp):
    if 0 <= temp < 10:
        return 'Лучше сменить свои кроссовки на более теплую обувь, если у вас есть пальто, то это будет лучший выбор на сегодня!'
    elif 10 <= temp < 20:
        return 'На улице не тепло и не холодно, наденьте сверху куртку'
    elif 20 <= temp < 30:
        return 'Наденьте шорты или штаны, стоит также накинуть ветровку, или же легкую куртку'
    elif 30 <= temp <= 40:
        return 'Вам стоит надеть рубашку и шорты, также не забудьте головной убор'
    elif -10 <= temp < 0:
        return 'Стоит надеть ботинки или сапоги, теплую куртку, и не забудьте шапку!'
    elif -20 <= temp < -10:
        return 'Наденьте теплые сапоги, теплую шапку, и зимнюю куртку, не забудьте надеть что-то под штаны!'
    return 'Лучше не выходите из дома)'
