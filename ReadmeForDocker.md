# Задание №1
- Установите docker и docker compose plugin на свою linux рабочую станцию или ВМ.
- Если dockerhub недоступен создайте файл /etc/docker/daemon.json с содержимым: ```{"registry-mirrors": ["https://mirror.gcr.io", "https://daocloud.io", "https://c.163.com/", "https://registry.docker-cn.com"]}```
- Зарегистрируйтесь и создайте публичный репозиторий  с именем "custom-nginx" на https://hub.docker.com;
- скачайте образ nginx:1.21.1;
- Создайте Dockerfile и реализуйте в нем замену дефолтной индекс-страницы(/usr/share/nginx/html/index.html), на файл index.html с содержимым:
```html
<html>
<head>
Hey, ZGU!
</head>
<body>
<p>I will be IT Engineer!</p>
</body>
</html>
```
- Соберите и отправьте созданный образ в свой dockerhub-репозитории c tag 1.0.0. \
_Ответ:_ https://hub.docker.com/repository/docker/np1r777/custom-nginx/general


# Задание №2
1. Запустите ваш образ custom-nginx:1.0.0 командой docker run в соответвии с требованиями:
- имя контейнера "ФИО-custom-nginx-t2"
- контейнер работает в фоне
- контейнер опубликован на порту хост системы 127.0.0.1:8080
![Снимок экрана 2024-12-12 124709](https://github.com/user-attachments/assets/67972ac5-ff95-4ec9-909c-bf746199232c)

2. Не удаляя, переименуйте контейнер в "custom-nginx-t2"
![Снимок экрана 2024-12-12 142011](https://github.com/user-attachments/assets/b106d440-d93a-4cbb-bab6-3b30b06d58cc)

3. Выполните команду ```date +"%d-%m-%Y %T.%N %Z" ; sleep 0.150 ; docker ps ; ss -tlpn | grep 127.0.0.1:8080  ; docker logs custom-nginx-t2 -n1 ; docker exec -it custom-nginx-t2 base64 /usr/share/nginx/html/index.html```
![Снимок экрана 2024-12-12 142720](https://github.com/user-attachments/assets/d49548e7-d65a-47c7-bc5d-49152ab38aef)

4. Убедитесь с помощью curl или веб браузера, что индекс-страница доступна.
![Снимок экрана 2024-12-12 142816](https://github.com/user-attachments/assets/28827f9d-a42a-4fa4-88cb-361335151779)


# Задание №3
1. Воспользуйтесь docker help или google, чтобы узнать как подключиться к стандартному потоку ввода/вывода/ошибок контейнера "custom-nginx-t2".
2. Подключитесь к контейнеру и нажмите комбинацию Ctrl-C.
3. Выполните ```docker ps -a``` и объясните своими словами почему контейнер остановился.
![Снимок экрана 2024-12-12 151205](https://github.com/user-attachments/assets/dca182c1-6f74-4eac-8c76-4fb80c93df72)

4. Перезапустите контейнер
![Снимок экрана 2024-12-12 151358](https://github.com/user-attachments/assets/6b8d4b68-2f3d-4039-bfa2-a9c686336fc2)

5. Зайдите в интерактивный терминал контейнера "custom-nginx-t2" с оболочкой bash.
![Снимок экрана 2024-12-12 151429](https://github.com/user-attachments/assets/af763de1-a01d-45dc-8fb2-7379a5d08419)
7. Установите любимый текстовый редактор(vim, nano итд) с помощью apt-get.
![Снимок экрана 2024-12-12 151454](https://github.com/user-attachments/assets/8e8d9fb8-c08a-4b48-875a-5d5db6b1f86b)
9. Отредактируйте файл "/etc/nginx/conf.d/default.conf", заменив порт "listen 80" на "listen 81".
![Снимок экрана 2024-12-12 151514](https://github.com/user-attachments/assets/d68dda67-2956-475c-9d66-808f5b2dee23)
11. Запомните(!) и выполните команду ```nginx -s reload```, а затем внутри контейнера ```curl http://127.0.0.1:80 ; curl http://127.0.0.1:81```.
![Снимок экрана 2024-12-12 151529](https://github.com/user-attachments/assets/6bd5d82d-af20-48e1-8c51-97d9bec0ae22)

9. Выйдите из контейнера, набрав в консоли  ```exit``` или Ctrl-D.
10. Проверьте вывод команд: ```ss -tlpn | grep 127.0.0.1:8080``` , ```docker port custom-nginx-t2```, ```curl http://127.0.0.1:8080```. Кратко объясните суть возникшей проблемы.
![Снимок экрана 2024-12-12 151541](https://github.com/user-attachments/assets/63979e86-a97a-48c6-bfaa-5f32fcbe3219)


# Задание №4
- Запустите первый контейнер из образа ***centos*** c любым тегом в фоновом режиме, подключив папку  текущий рабочий каталог ```$(pwd)``` на хостовой машине в ```/data``` контейнера, используя ключ -v.
- Запустите второй контейнер из образа ***debian*** в фоновом режиме, подключив текущий рабочий каталог ```$(pwd)``` в ```/data``` контейнера. 
- Подключитесь к первому контейнеру с помощью ```docker exec``` и создайте текстовый файл любого содержания в ```/data```.
- Добавьте ещё один файл в текущий каталог ```$(pwd)``` на хостовой машине.
- Подключитесь во второй контейнер и отобразите листинг и содержание файлов в ```/data``` контейнера. \
_Ответ:_ ![Снимок экрана 2024-12-12 152413](https://github.com/user-attachments/assets/fbad1913-f2e6-49e1-9105-75beed8f5744)


# Задание №5
1. Создайте отдельную директорию(например /tmp/ZGU/docker/task) и 2 файла внутри него.
"compose.yaml" с содержимым:

```
version: "3"
services:
  portainer:
    network_mode: host
    image: portainer/portainer-ce:latest
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
```

"docker-compose.yaml" с содержимым:

```
version: "3"
services:
  registry:
    image: registry:2

    ports:
    - "5000:5000"
```

И выполните команду "docker compose up -d". Какой из файлов был запущен и почему? (подсказка: https://docs.docker.com/compose/compose-application-model/#the-compose-file )
![Снимок экрана 2024-12-13 105213](https://github.com/user-attachments/assets/cdbee779-b60a-4600-b400-82a626f36025)

2. Отредактируйте файл compose.yaml так, чтобы были запущенны оба файла. (подсказка: https://docs.docker.com/compose/compose-file/14-include/)

3. Выполните в консоли вашей хостовой ОС необходимые команды чтобы залить образ custom-nginx как custom-nginx:latest в запущенное вами, локальное registry. Дополнительная документация: https://distribution.github.io/distribution/about/deploying/
4. Откройте страницу "https://127.0.0.1:9000" и произведите начальную настройку portainer.(логин и пароль адмнистратора)
5. Откройте страницу "http://127.0.0.1:9000/#!/home", выберите ваше local  окружение. Перейдите на вкладку "stacks" и в "web editor" задеплойте следующий компоуз:
```
version: '3'

services:
  nginx:
    image: 127.0.0.1:5000/custom-nginx
    ports:
      - "9090:80"
```
6. Перейдите на страницу "http://127.0.0.1:9000/#!/2/docker/containers", выберите контейнер с nginx и нажмите на кнопку "inspect". В представлении <> Tree разверните поле "Config" и сделайте скриншот от поля "AppArmorProfile" до "Driver".
![Снимок экрана 2024-12-13 131936](https://github.com/user-attachments/assets/84956094-dabf-48ed-9239-cf6c2664f78a)

7. Удалите любой из манифестов компоуза(например compose.yaml).  Выполните команду "docker compose up -d". Прочитайте warning, объясните суть предупреждения и выполните предложенное действие. Погасите compose-проект ОДНОЙ(обязательно!!) командой.
![Снимок экрана 2024-12-13 132607](https://github.com/user-attachments/assets/1899436b-637f-4aed-b411-361e411dbaf0)
![Снимок экрана 2024-12-13 132617](https://github.com/user-attachments/assets/fc31060b-4bd6-4b16-9a15-5fae53598b3b)
![Снимок экрана 2024-12-13 132624](https://github.com/user-attachments/assets/6c609755-d81a-4e1b-b39c-4d5dbd06163a)
