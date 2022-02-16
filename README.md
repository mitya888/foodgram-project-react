
## foodgram-project-react
### Описание
Продуктовая социальная сеть для публикации рецептов и 
составление продуктовой корзины исходя из их ингридиентов

### Проект доступен по ссылке :
http://62.84.112.243/

## Описание Workflow

##### Workflow состоит из четырёх шагов:

1. Проверка кода на соответствие PEP8.
2. Сборка и публикация образа на DockerHub.
3. Автоматический деплой на сервер.
4. Отправка ботом уведомления в телеграм-чат.


## Подготовка и запуск проекта
##### Клонирование репозитория
```bash
git clone https://github.com/mitya888/foodgram-project-react
```

## Установка на удаленном сервере (Ubuntu):
##### Шаг 1. Вход на удаленный сервер
Подключаемся на удаленный сервер
```bash
ssh <username>@<ip_address>
```

##### Шаг 2. Установка docker:

```bash
sudo apt install docker.io 
```

##### Шаг 3. Установка docker-compose:

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

##### Шаг 4. Копирование docker-compose.yaml и nginx/default.conf:
Скопируйте подготовленные файлы `docker-compose.yaml` и `nginx/default.conf` из проекта на сервер в `home/<ваш_username>/docker-compose.yaml` и `home/<ваш_username>/nginx/default.conf` соответственно.


```bash
scp docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yml
scp -r nginx/ <username>@<host>:/home/<username>/
```

##### Шаг 5.  Добавление Github Secrets:
Для работы с Workflow добавьте в Secrets GitHub переменные окружения для работы:
```bash
SECRET_KEY=<SECRET_KEY> (django project)
DEBUG=<True/False>
ALLOWED_HOSTS=<hosts>

DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432

DOCKER_USERNAME=<login DockerHub>
DOCKER_PASSWORD=<pass DockerHub>

USER=<username для подключения к серверу>
HOST=<IP сервера>
PASSPHRASE=<passphrase для сервера, если он установлен>
SSH_KEY=<SSH ключ>

TELEGRAM_TO=<ID своего телеграм-аккаунта. Для инфо @myidbot>
TELEGRAM_TOKEN=<токен бота fatherbot>
```

##### Шаг 6. После успешного деплоя:

Статика и миграции применяются автоматически
