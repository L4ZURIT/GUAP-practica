# GUAP-practica

Проект готов для тестирования и дальнейшей разработки.
_______________________________________________________ 

В целях предосторожности от утечки личных данных преподавателей, для сайта не был использован любой из известных хостингов.

Поэтому работы и запуска сайта следуйде инструкциям:
_______________________________________________________
Примечания:

1) команды для удобства будут взяты в кавычки, при вводе или копировании кавычки следует убрать!
2) настройка показана для windows
_______________________________________________________

Предтребования:

-- установленный python не ниже 3 версии (3.8.8 - рекомендуется)
-- установленный и настроенный pip (идет по усмолчанию с python)
Для проверки можно использовать следующие команды:

"python -V"
"pip -V"
# показывают версии
______________________________________________________

После успешной проверки работы python и pip:

-- установите модуль venv командой "pip install venv"

-- создайте виртуальную среду в папке проекта (в папке, в которой был размещена главная папка studyDB) при помощи команды "python -m venv venv"
(параментр -m позволяет дать среде свое имя - в данном случае 'venv')
Проверьте, что в папке появилась новая папка venv!

-- активируйте среду при помощи встроенного скрипта ".\venv\Scripts\activate" (может понадобиться настроить разрешение на выполнение PowerShell скрипта командами "Set-ExecutionPolicy RemoteSigned -Scope Process", чтобы дать разрешение для текущего сеанса оболочки или "Set-ExecutionPolicy RemoteSigned", чтобы разрешить запуск навсегда)

-- установите модули для работы для своей среды:
"pip install Django"
"pip install pandas"
"pip install docxtpl"

-- теперь можно работать с проектом при помощи скрипта manage.py, который находится в папке studyDB. Для удобства можно перейти в папку командой "cd studyDB".

-- проверим наличие всех необходимых модулей запустив сервер:
"python manage.py runserver"
(если все в порядке, то вы это увидете в командой строке и сможете перейти на сайт по выведенной ссылке).
Для завершения работы сервера нужно нажать CTRL+C
______________________________________________________

Дополнительный список команд для работы:

"python manage.py makemigrations" - если вы внесли изменения в структуру моделей и хотите применить их к бд, закрепляет необходимые измнения
"python manage.py migrate" - применяет закрепленные на прошлом шаге изменения к бд
