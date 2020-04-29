def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False


print('start')

result = sleep_in(False, False)
if result == True:
    print('you are sleeping ')
else:
    print('you are working on weekends')
