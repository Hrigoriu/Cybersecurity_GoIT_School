"""
Пакетний менеджер надає доступ до великої кількості ресурсів. За допомогою pip ви маєте доступ до тисяч бібліотек, доступних на PyPI (Python Package Index), офіційному сховищі бібліотек Python.
https://pypi.org/
"""
#=========================================================================================
# скрипт: python -m pip list

#=========================================================================================
"""
py -m pip install SomePackage            # latest version
py -m pip install SomePackage==1.0.4     # specific version
py -m pip install 'SomePackage>=1.0.4'   # minimum version
"""

#=========================================================================================
"""
 pip install requests           встановлення останньої версії пакету requests   
pip install requests==2.28.2    конкретної версії пакету requests
pip install requests>=2.28.2    новішого за 2.28.2
pip install requests<=2.28.2    давнішого за 2.28.2

pip uninstall requests          видалення пакету requests
"""
