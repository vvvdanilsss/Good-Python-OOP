cmd = input()

match cmd:
    case 'top' | 'Top' | 'TOP':
        print('Команда top')
    case 'bottom' | 'Bottom' | 'BOTTOM':
        print('Команда bottom')
    case 'right' | 'Right' | 'RIGHT':
        print('Команда right')
    case 'left' | 'Left' | 'LEFT':
        print('Команда left')
    case _:
        print('Неверная команда')