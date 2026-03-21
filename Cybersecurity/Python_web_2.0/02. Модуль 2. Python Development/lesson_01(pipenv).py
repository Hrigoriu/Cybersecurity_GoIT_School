"""
    ! Pipenv !
Це сучасний інструмент для управління робочим середовищем у Python.

Pipenv поєднує в собі функціональність pip та virtualenv, надаючи розробникам зручний спосіб керувати залежностями та ізоляцією проектів.
"""
#====================================================================================================
"""
Основні можливості pipenv:
- Створення та управління віртуальним середовищем.
- Синхронізація пакетів у Pipfile під час встановлення та видалення пакетів.
- Автоматичне підвантаження змінних середовища з файлу .env.
"""
#====================================================================================================
"""
1. зайдемо в директорію ClassWork, а потім в терміналі встановляємо pipenv, 
виконуємо команду: pip install pipenv
2. створюємо нове віртуальне середовище для вашого проекту
2А. в терміналі пишемо cd project1 (переходимо глибше в цю директорію), 
2В. виконуємо команду: pip install pipenv
Ствоюється віртуальне середовище (там ще директоріїї створюються та файли Pipfile та Pipfile.lock)
3. встановлюємо необхідні пакети. Наприклад:
команди:pipenv --python 3.7
команди:pipenv install requests flask   
Ці команди створять віртуальне середовище з Python 3.7 та встановлять пакети requests та flask.
4. потрібно виконати команду: pipenv shell, яка активує віртуальне середовище для поточної директорії.

Щоб зайти в іншу директорію, потрібно виконати команду: cd ../project2, але перед цим потрібно вийти з поточного середовища, виконавши команду: exit.
Після цього можна виконати
команди: cd .. (щоб вийти на рівень вище) та cd project2 (щоб зайти в іншу директорію).
"""
#====================================================================================================
"""
pip install pipenv --user
pipenv --python 3.7
pipenv install requests
pipenv shell
"""
#====================================================================================================
"""
Якщо потрібно видалити середовище, можна скористатися командою:
команди:pipenv --rm
"""
#====================================================================================================
"""
Для встановлення пакетів, використовуючи pipenv, можна виконати команду:
команди:pipenv install Flask
"""
#====================================================================================================
"""
команди:pipenv install ipython --dev
Ця команда встановить пакет iPython, але відмітить його та всі його залежності як необов'язкові, і їх можна буде не встановлювати на цільовому пристрої.
"""
#====================================================================================================
"""
Під час роботи pipenv створює два файли: Pipfile та Pipfile.lock.
- Pipfile містить інформацію про те, звідки та яку версію пакета потрібно встановити. 
- Pipfile.lock ж зберігає інформацію про всі (включаючи залежність) встановлені пакети в середовищі.
"""
#====================================================================================================
"""
Для видалення пакета з середовища та всіх його залежностей ви можете виконати 
команди:pipenv uninstall package_name
"""
#====================================================================================================
"""
pipenv -h
Usage: pipenv [OPTIONS] COMMAND [ARGS]...

Options:
  --where                         Output project home information.
  --venv                          Output virtualenv information.
  --py                            Output Python interpreter information.
  --envs                          Output Environment Variable options.
  --rm                            Remove the virtualenv.
  --bare                          Minimal output.
  --man                           Display manpage.
  --support                       Output diagnostic information for use in
                                  GitHub issues.
  --site-packages / --no-site-packages
                                  Enable site-packages for the virtualenv.

  --python TEXT                   Specify which version of Python virtualenv
                                  should use.
  --clear                         Clears caches (pipenv, pip).
  -q, --quiet                     Quiet mode.
  -v, --verbose                   Verbose mode.
  --pypi-mirror TEXT              Specify a PyPI mirror.
  --version                       Show the version and exit.
  -h, --help                      Show this message and exit.


Usage Examples:
   Create a new project using Python 3.7, specifically:
   $ pipenv --python 3.7

   Remove project virtualenv (inferred from current directory):
   $ pipenv --rm

   Install all dependencies for a project (including dev):
   $ pipenv install --dev

   Create a lockfile containing pre-releases:
   $ pipenv lock --pre

   Show a graph of your installed dependencies:
   $ pipenv graph

   Check your installed dependencies for security vulnerabilities:
   $ pipenv check

   Install a local setup.py into your virtual environment/Pipfile:
   $ pipenv install -e .

   Use a lower-level pip command:
   $ pipenv run pip freeze

Commands:
  activate      Outputs the activation command for the virtualenv.
  audit         Audits packages for security vulnerabilities using pip-audit.
  check         Checks for PyUp Safety security vulnerabilities and against
                PEP 508 markers provided in Pipfile.
  clean         Uninstalls all packages not specified in Pipfile.lock.
  graph         Displays currently-installed dependency graph information.
  install       Installs provided packages and adds them to Pipfile, or (if no
                packages are given), installs all packages from Pipfile.
  lock          Generates Pipfile.lock.
  open          View a given module in your editor.
  pylock        Manage PEP 751 pylock.toml files.
  requirements  Generate a requirements.txt from Pipfile.lock.
  run           Spawns a command installed into the virtualenv.
  scripts       Lists scripts in current environment config.
  shell         Spawns a shell within the virtualenv.
  sync          Installs all packages specified in Pipfile.lock.
  uninstall     Uninstalls a provided package and removes it from Pipfile.
  update        Runs lock, then sync.
  upgrade       Resolves provided packages and adds them to Pipfile, or (if no
                packages are given), merges results to Pipfile.lock
  verify        Verify the hash in Pipfile.lock is up-to-date.

"""