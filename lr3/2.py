def find_common_participants(participants_first, participants_second, separator=','):
    participants_first = participants_first.split(separator)
    participants_second = participants_second.split(separator)

    common_participants = list(set(participants_first).intersection(participants_second))
    common_participants.sort()

    return common_participants



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group, separator='|')
print('Общие участники', participants)
