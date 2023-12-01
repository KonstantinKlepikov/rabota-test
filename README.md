# Кфищеф-еуые

## Тех.задание

По [url](https://gsr-rabota.ru/api/v2/Vacancies/All/List) расположен json c вакансиями.

Цель задания: создать «умную» кэширующую прослойку в виде отдельного веб-сервиса.

Необходимо реализовать python веб-сервер (можно использовать как чистый python, так и фреймворки Flask, Pyramid, Tornado, Django, FastAPI и подобные):

1. Метод загрузки/перезагрузки данных
2. Загрузка вакансий в локальную реляционную базу (можно SQLite, MySQL, Postgresql, Firebird). Таблицы базы должны создаваться на основании парсинга получаемого json (предполагаем, что как наименование, так и количество полей может со временем меняться)
3. В базе должны создаться таблицы со словарями:
   - клиенты (сейчас это поля clientid, clientname)
   - места работы (сейчас это поля placeid, placetitle, address, latitude, longitude)
   - профессии (сейчас это поля profid, proftitle)

Записи основной таблицы должны ссылаться на записи в словарях.

Для создания структуры базы нельзя иcпользовать генерацию таблиц средствами ORM.

### Методы поиска

Поиск должен проводиться по локальной базе, результат возвращается клиенту в таком же формате, как по изначальному url

Простой поиск, поисковая строка передается через параметры GET запроса, например:

- ашан казань
- комплектовщик озон
- склад

Параметризированный поиск через POST-запрос. В качестве параметров form-data может передаваться:

- clientid
- placeid
- profid
- searchstring

Если clientid и/или placeid и/или profid заполнены, то поиск ведется с учетом фильтра по словарям

## Ресурсы

### Запуск и остановка dev-стека

1. Go to service folder, f.e. `cd api/app` and create VSCode project by `code .`
2. Install poery dependencies and add environment for python linting. Use `poetry config virtualenvs.in-project true` for creation of env folder inside project. Then `poetry init` (if pyproject.toml not exist) and `poetry install --with dev`.
3. Inside container use:

    - `pytest -v -s -x` for all tests
    - use `python -m IPython` to check code
    - `mypy --install-types`
    - `mypy app` and `flake8 app`

- `make serve` to run dev mode
- `make down` to stop
- rebuild single service `docker compose up -d --no-deps --build <service-name>`

### Разработка локально

Для запуска необходимо клонирвоать репозиторий и поместить в корень репозитория `.env` файл следующего содержания

```bash
# mongo dev
DEV_ROOT_USERNAME=mongo-dev
DEV_ROOT_PASSWORD=mybrilliantpassword
ADMINUSERNAME=admin
ADMINPASSWORD=mybrilliantpassword
MONGODB_URL=mongodb://${DEV_ROOT_USERNAME}:${DEV_ROOT_PASSWORD}@rabota-mongo-dev:27017/
DB_NAME=dev-db

# test db
TEST_ROOT_USERNAME=mongo-test
TEST_ROOT_PASSWORD=mybrilliantpassword
TEST_MONGODB_URL=mongodb://${TEST_ROOT_USERNAME}:${TEST_ROOT_PASSWORD}@erabota-mongo-test:27021/
```

Вам потребуется `docker compose 3.8` и утилита `make` для запуска стека.

### Старт и остановка dev стека

- `make serve` to run dev mode services
- `make down` shut down all services
- rebuild and rerun single service `docker compose up -d --no-deps --build <service-name>`

### Ссылки на локальные ресурсы, которые вы можете использовать для контроля работоспособности стека.

- [api swagger docs](http://localhost:8192/docs/)
- [mongoDB admin panel](http://localhost:8191/)

### Общее затраченное время и выполненные задачи
