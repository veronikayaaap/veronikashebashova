print("Введите значение duration")
dur = int(input())
if dur < 60:
    print(f"{dur} сек")
elif dur < 3600:
    m = dur // 60
    print(f"{m} мин {dur - m * 60} сек")
elif dur < 8640:
    m = dur // 60
    h = dur // 3600
    m = m - h * 60
    s = dur - h * 3600 - m * 60
    print(f"{h} час {m} мин {s} сек")
else:
    d = dur // 86400
    dur = dur % 86400
    h = dur // 3600
    dur = dur % 3600
    m = dur // 60
    s = dur % 60
    print(f"{d} д {h} час {m} мин {s} сек")

