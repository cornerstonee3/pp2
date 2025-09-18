#repositories: пустая директория, в которой будут располагаться ваши репозитории.
#files: заранее упакованные файлы для того, чтобы вы могли продолжить работать с учебными материалами на любом этапе. Если вы застрянете, просто скопируйте нужный урок в свой репозиторий.
#Git — это программа с текстовым интерфейсом, с которой надо работать в командной строке. 
#Ветка — это параллельная версия репозитория. Ветки позволяют вам работать над отдельными функциями вашего проекта, не влияя на основную версию. Закончив работу над новой фичей, вы можете объединить эту ветку с основной версией проекта.
#git config --global user.name "Your Name"
#git config --global user.email "your_email@whatever.com"
#git config --global init.defaultBranch main
#git config --global core.autocrlf true
#git config --global core.safecrlf warn
#mkdir work
#cd work
#touch hello.html
#git init
#git add hello.html
#git commit -m "Initial Commit"
#git status
#git add hello.html
#git status
#git commit
#git log
#git log --pretty=oneline
#git log --pretty=format:"%h %ad | %s%d [%an]" --date=short
#--pretty="..." — определяет формат вывода.
#%h — укороченный хеш коммита.
#%ad — дата коммита.
#| — просто визуальный разделитель.
#%s — комментарий.
#%d — дополнения коммита («головы» веток или теги).
#%an — имя автора.
#--date=short — сохраняет формат даты коротким и симпатичным.
#git tag v1
#git log
#git checkout v1^
#cat hello.html
#git switch main
#git restore hello.html
#git status
#cat hello.html
