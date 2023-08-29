version = 'v0.2'
creator = 'MaHivka (GitHub)'


def hello_screen():
    print(f'Добро пожаловать в программу подсчёта идеальной эпохи для нейромодели RVC {version}',
          'Приготовьте свои данные из Tensorboard для подсчёта', sep='\n')
    return None


def quit_func():
    input('Нажмите Enter чтобы выйти')
    quit()


def data_input():
    print('Если вам будет непонятен какой-то термин, то вернитесь в главное меню (Ctrl+C) и обратитесь в секцию FAQ')
    try:
        epoch_max = int(input('Введите общее количество эпох\n'))
        steps_max = int(input('Введите общее количество шагов\n'))
        ideal_step = int(input('Введите "Идеальный" шаг\n'))
    except KeyboardInterrupt:
        print('Возвращаемся в главное меню')
        main()
    except ValueError:
        print('Было введено неверное значение, введите всё ещё раз')
        data_input()
    ideal_percent = ideal_step / (steps_max / 100)
    ideal_epoch = (epoch_max / 100) * ideal_percent
    ideal_epoch = int(ideal_epoch)
    print(f'Ваша идеальная эпоха равна {ideal_epoch}')
    print('Хотите выйти в меню(1), посчитать ещё раз(2) или выйти из программы(3)?')

    try:
        choice = int(input())
    except ValueError:
        print('Видимо выходим')
        quit_func()

    if choice == 1:
        main_menu()
    elif choice == 2:
        data_input()
    else:
        quit_func()


def faq_content(choice):
    if choice < 2:
        print('Не найдено нулевого или отрицательного результата')
        input('Нажмите для продолжения')
        print()
    elif choice == 2:
        print('В Tensorboard шаги имеют вид 0,00k, как его перевести в значения, используемые в этой программе?')
        print('Берёте эти значения типа 0,00k, забываете про k и умножаете на 1000')
        input('Нажмите для продолжения')
        print()

    elif choice == 3:
        print('Что такое "Идеальный" шаг?')
        print('"Идеальный" шаг - это шаг в графе Tensorboard, после которого идёт рост, т.е., можно сказать, что это минимальное значение')
        print('Как он выглядит в консоле показать не возможно, сорян :). Ищите в инете или в одном из руководств из FAQ 4')
        input('Нажмите для продолжения')
        print()
    elif choice == 4:
        print('https://docs.google.com/document/d/13ebnzmeEBc6uzYCMt-QVFQk-whVrK4zw8k7_Lw3Bv_A/edit#heading=h.bjzhhhcn3f69 - Training guide')
        print('От туда есть ссылки на другие руководства, в том числе и по Tensorboard (А идеальный шаг (Или же Point of Overtraining) в самом руководстве)')
        input('Нажмите для продолжения')
        print()


def faq():
    print('Добро пожаловать в секцию FAQ (frequently asked questions',
          'Выбирете какой вопрос вас интересует:',
          '1. Вернуться в главное меню',
          '2. В Tensorboard шаги имеют вид 0,00k, как его перевести в значения, используемые в этой программе?',
          '3. Что такое "Идеальный" шаг?',
          '4. Есть какие-то руководства?', sep='\n')
    try:
        choice = int(input())
    except ValueError:
        print('Вам необходимо указать число')
        faq()
    if choice != 1:
        faq_content(choice)
    else:
        main_menu()
    faq()


def main_menu():
    print()
    print('Выбирите пункт из меню:',
          '1. Сделать подсчёт',
          '2. FAQ', sep='\n')
    try:
        choice = int(input())
    except ValueError:
        print('Вам необходимо указать цифру')
        main_menu()

    if choice == 1:
        data_input()
    elif choice == 2:
        faq()
    else:
        print('Укажите существующий раздел меню')
        main_menu()


def main():
    hello_screen()
    main_menu()


main()
