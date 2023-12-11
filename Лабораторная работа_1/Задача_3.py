list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

middle_index = len(list_players) // 2  # середина списка

left_team = list_players[:middle_index]  # list_players[:3]
right_team = list_players[middle_index:]  # list_players[3:]

print(left_team)
print(right_team)
