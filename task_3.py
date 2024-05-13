import time

class Album:

    albums = {}

    def __init__(self, name, date):

        self.name = name
        self.date = date
        self.tracks = {}

        Album.albums[self.name] = self
    
    def add_track(self, track):
        self.tracks[track.name] = track
    
    def remove_track(self, track):
        self.tracks.pop(track.name)
    
    def __str__(self):

        return f'Название: {self.name}, дата релиза: {self.date} г.'


class Track:

    def __init__(self, name, duration, performer, date_relise):

        self.name = name
        self.duration = duration
        self.performer = performer
        self.date_relise = date_relise
        self.rest_of_time = duration
    
    def __str__(self):
        res = f'название: {self.name}, продолжительность: {self.duration}, '
        res += f'исполнитель: {self.performer}, дата выпуска: {self.date_relise}'
        return res

album_1 = Album('Спокойная ночь', '13.05.2024')
album_2 = Album('Край земли', '30.09.2022')
track_1 = Track('Звёзды', 15, 'Василий Ной', '20.02.2002')
track_2 = Track('Небо', 20, 'Гарри Гончар', '15.12.2018')
track_3 = Track('Крестик', 100, 'Снич', '01.01.2020')

album_1.add_track(track_1)
album_1.add_track(track_2)
album_2.add_track(track_3)

while True:

    print()
    print('1. Выбрать альбом.')
    print('2. Завершить работу.')
    command = int(input('Введите номер команды: '))

    if command == 1:

        print()
        print('Доступные альбомы:')
        print(album_1)
        print(album_2)
        
        name_album = input('Введите название альбома, с которым хотите взаимодействовать: ')
        album = Album.albums[name_album]

        while True:
            
            print()
            print('Треки в альбоме:')
            for track in album.tracks:
                print(album.tracks[track])
            
            print()
            print('Возвможные функции:')
            print('1. Выбрать трек.')
            print('2. Вернуться к выбору альбомов.')
            func_1 = int(input('Введите номер функции: '))

            if func_1 == 1:
                
                print()
                name_track = input(('Введите название трека, с которым хотите взаимодействовать: '))
                track = album.tracks[name_track]

                flag = False
                track_playing_time = 0
                start_time = float('inf')
                full_playing_time = 0

                while True:
                    
                    
                    print('Возвможные функции:')
                    print('1. Удалить трек.')
                    print('2. Воспроизвести трек.')
                    print('3. Постваить трек на паузу.')
                    print('4. Остановить воспроизведение трека.')
                    print('5. Вернуться в альбом.')

                    

                    func_2 = int(input('Введите номер функции: '))

                    current_time = time.time()
                    track_playing_time = current_time - start_time

                    if track_playing_time >= track.rest_of_time:
                        print()
                        print('Трек доиграл до конца.')
                        flag = False
                        track.rest_of_time = track.duration
                        full_playing_time = 0

                    if func_2 == 1:
                        if flag:
                            print()
                            print('Нельзя удалить трек, когда он играет.')
                        else:
                            album.remove_track(album.tracks[name_track])
                            break

                    elif func_2 == 2:
                        if flag:
                            print()
                            print('Трек уже играет.')
                        else:
                            print()
                            print('Трек запущен.')
                            flag = True
                            start_time = time.time()
                    
                    elif func_2 == 3:
                        if flag:
                            track.rest_of_time -= track_playing_time
                            flag = False
                            start_time = float('inf')
                            full_playing_time += track_playing_time
                            print()
                            print(f'{full_playing_time} ------- {track.rest_of_time}')
                        else:
                            print()
                            print('Для начала воспроизведите трек.')

                    elif func_2 == 4:
                        if flag:
                            print()
                            print('Трек остановлен.')
                            flag = False
                            track.rest_of_time = track.duration
                            full_playing_time = 0
                        else:
                            print()
                            print('Для начала воспроизведите трек.')

                    else:
                        track.rest_of_time = track.duration
                        break

            else:
                break

    else:
        print('Спасибо за работу!')
        break
