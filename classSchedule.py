classes = ["Maths", "Marketing", "Boxing"]
time = ['9a.m.', '11a.m.', '4p.m.']

def schedule_classes(classes, time):
    schedule = []

    index = 0
    while index < len(classes):
        class_schedule = classes[index] + ":" + time[index]
        schedule.append(class_schedule)
        index += 1
    return schedule
schedule = schedule_classes(classes, time)
print("Monday's class schedule : {}".format(schedule))