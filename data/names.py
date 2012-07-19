categories = {
    'general': 'Общее',
    'greek': 'Греческое',
    'information': 'Информация',
    'nature': 'Природа',
    'towns': 'Города'
}


def getCategoryNameByAlias(alias):
    return categories[alias]


articles = {
    'visit-bilhorod-dnistrovskyi': 'Посещение Белгород-Днестровского',
    'trip-to-olbia': 'Поездка в Ольвию',
    'trip-to-kinburn-peninsula': 'Поездка на Кинбурнский полуостров',
    'one-day-in-odessa': 'Один день в Одессе',
    'odessa-region-trains-timetable': 'Расписание пригородных поездов Одесского региона',
    'national-archaeological-park-olbia': 'Национальный археологический заповедник “Ольвия”',
    'introduction': 'Предисловие'
}

def getAticleNameByAlias(alias):
    return articles[alias]