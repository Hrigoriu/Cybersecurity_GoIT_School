"""
    ! Poetry ! (https://python-poetry.org/docs/)
Це інструмент для управління залежностями у Python проектах (аналог вбудованого pip).
"""
#====================================================================================================
"""
    ! Щоб створити віртуальне середовище poetry: !
1. Створи директорію, де буде проект
2. Провірь чи встановлений Python командою:
python --version
3. Встанови poetry командою:
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
4. Провірь чи встановлений poetry командою:
poetry --version 
5. Створи файли:
pyproject.toml
.gitignore
README.md
6. Пропиши в них відповідний код: 
7. Щоб відкрити термінал у VS Code, просто натисніть Ctrl + ~ (тильда), щоб відкрити вбудований термінал.
8. Командами cd [відповідна директорія] та cd .. зайди терміналом в директорію, де лежить твій проект
9. Свори віртуальне середовище poetry у твоїй визначеній директорії командою:
poetry install
10. Перевірь результат командою:
poetry env info
Якщо бачиш Path і Valid: True — вітаю! Ти успішно ініціалізував професійне середовище.
11. Активація оболонки командою:
poetry shell
12. Запускай свій проект командою:
python main.py
13. Щоб вийти з оболонки poetry, напишіть команду:
exit
"""
#====================================================================================================
"""
Використання файлів pypoproject.toml та poetry.lock робить його схожим на Node Package Manager (npm) для Node.js
"""
#====================================================================================================
"""
Poetry можна встановити вручну за допомогою pip та модуля venv.

python3 -m venv $VENV_PATH
$VENV_PATH/bin/pip install -U pip setuptools
$VENV_PATH/bin/pip install poetry
"""
#====================================================================================================
"""
Припустимо, що ми ввели команду poetry new solution, тоді ми отримаємо наступну структуру каталогів:

solution
├── solution
│   └── __init__.py
├── pyproject.toml
├── README.rst
└── tests
    ├── __init__.py
    └── test_solution.py
"""
#====================================================================================================
"""
    ! pyproject.toml !
Цей файл - просунута альтернатива requirements.txt, який використовується для управління залежностями в Python проектах.
"""
#====================================================================================================
"""
Вміст файлу pyproject.toml буде наступним:

[tool.poetry]
name = "solution"
version = "0.1.0"
description = ""
authors = ["FirstName LastName <youremail@gmail.com>"]

[tool.poetry.dependencies]
python = "^3.9"

[tool.poetry.dev-dependencies]
pytest = "^5.2"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
"""
#====================================================================================================
"""
Розділ tool.poetry призначений для опису проекту: назва, версія, коротка інформація про проект тощо. 
Далі слідує tool.poetry.dependencies, саме тут вказані всі production залежності. 
Розділ tool.poetry.dev-dependencies призначений для залежностей, які використовуються під час розробки, наприклад pytest для тестів.
"""
#====================================================================================================
"""
Щоб ініціалізувати poetry у вже готовому проекті, потрібно виконати команду:
*poetry init

Для активації віртуального середовища необхідно виконати команду:
*poetry shell

Щоб додати до проекту залежність у вигляді aiosqlite. Необхідно виконати команду
*poetry add aiosqlite

Щоб додати залежність для розробки, достатньо вказати прапорець --dev:
*poetry add pytest --dev

Щоб видалити залежність, можна виконати команду:
*poetry remove aiosqlite

Оновити всі залежності до останніх версій:
*poetry update
"""
#====================================================================================================
"""
    ! CAUTION !
Не забудьте вказати параметр Poetry executable, щоб PyCharm знав, де встановлено poetry, і міг його використовувати для керування залежностями та віртуальними середовищами.
"""
#====================================================================================================
"""
poetry
Poetry (version 2.3.2)

Usage:
  command [options] [arguments]

Options:
  -h, --help                 Display help for the given command. When no command is given display help for the list command.
  -q, --quiet                Do not output any message.
  -V, --version              Display this application version.
      --ansi                 Force ANSI output.
      --no-ansi              Disable ANSI output.
  -n, --no-interaction       Do not ask any interactive question.
      --no-plugins           Disables plugins.
      --no-cache             Disables Poetry source caches.
  -P, --project=PROJECT      Specify another path as the project root. All command-line arguments will be resolved relative to the current working directory.
  -C, --directory=DIRECTORY  The working directory for the Poetry command (defaults to the current working directory). All command-line arguments will be resolved relative to the given directory.
  -v|vv|vvv, --verbose       Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug.

Available commands:
  about              Shows information about Poetry.
  add                Adds a new dependency to pyproject.toml and installs it.
  build              Builds a package, as a tarball and a wheel by default.
  check              Validates the content of the pyproject.toml file and its consistency with the poetry.lock file.
  config             Manages configuration settings.
  help               Displays help for a command.
  init               Creates a basic pyproject.toml file in the current directory.
  install            Installs the project dependencies.
  list               Lists commands.
  lock               Locks the project dependencies.
  new                Creates a new Python project at <path>.
  publish            Publishes a package to a remote repository.
  remove             Removes a package from the project dependencies.
  run                Runs a command in the appropriate environment.
  search             Searches for packages on remote repositories.
  show               Shows information about packages.
  sync               Update the project's environment according to the lockfile.
  update             Update the dependencies as according to the pyproject.toml file.
  version            Shows the version of the project or bumps it when a valid bump rule is provided.    

 cache
  cache clear        Clear Poetry's caches.
  cache list         List Poetry's caches.

 debug
  debug info         Shows debug information.
  debug resolve      Debugs dependency resolution.
  debug tags         Shows compatible tags for your project's current active environment.

 env
  env activate       Print the command to activate a virtual environment.
  env info           Displays information about the current environment.
  env list           Lists all virtualenvs associated with the current project.
  env remove         Remove virtual environments associated with the project.
  env use            Activates or creates a new virtualenv for the current project.

 python
  python install     Install the specified Python version from the Python Standalone Builds project. (experimental feature)
  python list        Shows Python versions available for this environment. (experimental feature)        
  python remove      Remove the specified Python version if managed by Poetry. (experimental feature)    

 self
  self add           Add additional packages to Poetry's runtime environment.
  self install       Install locked packages (incl. addons) required by this Poetry installation.        
  self lock          Lock the Poetry installation's system requirements.
  self remove        Remove additional packages from Poetry's runtime environment.
  self show          Show packages from Poetry's runtime environment.
  self show plugins  Shows information about the currently installed plugins.
  self sync          Sync Poetry's own environment according to the locked packages (incl. addons) required by this Poetry installation.
  self update        Updates Poetry to the latest version.

 source
  source add         Add source configuration for project.
  source remove      Remove source configured for the project.
  source show        Show information about sources configured for the project.
"""

