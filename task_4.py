class Timetable:

    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']

    week = {
        'Понедельник': [],
        'Вторник': [],
        'Среда': [],
        'Четверг': [],
        'Пятница': [],
        'Суббота': []
    }
    
    def __init__(self, group):

        self.group = group
    
    def add_lesson(self, lesson):

        Timetable.week[lesson.day].append(lesson)

    def __str__(self):

        res = f'Расиписание группы {self.group}:\n\n'
        for day in Timetable.days:
            res += f'{day}\n'
            for lesson in Timetable.week[day]:
                res += f'{lesson.time}\n'
                res += f'{lesson}\n'
            res += f'\n'
        
        return res
            


class Subject:

    def __init__(self, day, lesson, audience, time, f_name, s_name, last_name):

        self.day = day
        self.lesson = lesson
        self.audience = audience
        self.time = time
        self.f_name = f_name
        self.s_name = s_name
        self.last_name = last_name

    def __str__(self):
        
        if self.f_name != '':
            return f'   {self. lesson}, ауд. {self.audience}, {self.s_name} {self.f_name} {self.last_name}'
        else:
             return f'   {self. lesson}, ауд. {self.audience}'

with open('lessons.txt', encoding='utf-8') as file:
    group = file.readline()[:-1]
    timetable = Timetable(group)

    for line in file:

        subj = line.split(';')[:-1]
        lesson = Subject(subj[0], subj[1], subj[2], subj[3], subj[4], subj[5], subj[6])
        timetable.add_lesson(lesson)

print(timetable)
