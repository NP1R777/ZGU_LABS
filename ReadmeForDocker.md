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
6. ![Снимок экрана 2024-12-12 151429](https://github.com/user-attachments/assets/af763de1-a01d-45dc-8fb2-7379a5d08419)
7. Установите любимый текстовый редактор(vim, nano итд) с помощью apt-get.
![Снимок экрана 2024-12-12 151454](https://github.com/user-attachments/assets/8e8d9fb8-c08a-4b48-875a-5d5db6b1f86b)
9. Отредактируйте файл "/etc/nginx/conf.d/default.conf", заменив порт "listen 80" на "listen 81".
10. ![Снимок экрана 2024-12-12 151514](https://github.com/user-attachments/assets/d68dda67-2956-475c-9d66-808f5b2dee23)
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

