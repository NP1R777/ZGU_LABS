# Лабораторная работа №4
## Задача 1. Подготовка окружения:
1. Настройте `docker-compose.yaml` для сервисов:
   - **Jenkins**  
   - **GitLab**  
   - **SonarQube (с PostgreSQL)**  
   - **Nexus**

2. Поднимите все сервисы через `docker-compose up -d`
3. Протестируйте их доступность.

## Ход выполнения:
1. Сервисы были настроены при помощи 4 файлов docker-compose.yaml. С Их содрежимым можно ознакомиться ниже:
  - docker-compose для сервиса "Jenkins":
    ```
    version: '3'
    
    services:
      jenkins:
        image: jenkins/jenkins:lts
        ports:
          - "8080:8080"
          - "50000:50000"
        volumes:
          - jenkins_home:/var/jenkins_home
        networks:
          - devops-network
    
    networks:
      devops-network:
        driver: bridge

    volume:
      jenkins_home:
    ```
  - docker-compose для сервиса "Gitlab":
    ```
    version: '3'
    
    services:
      gitlab:
        image: gitlab/gitlab-ce:latest
        hostname: 'http://0.0.0.0:80'
        environment:
          GITLAB_OMNIBUS_CONFIG: |
            external_url 'https://gitlab.com/root/test-project.git'
        ports:
          - "80:80"
          - "443:443"
          - "22:22"
        volumes:
          - gitlab_config:/etc/gitlab
          - gitlab_data:/var/gitlab
          - gitlab_logs:/var/log/gitlab
        networks:
          - devops-network
    
    networks:
      devops-network:
        driver: bridge

    volumes:
      gitlab_config:
      gitlab_data:
      gitlab_logs:
    ```
  - docker-compose для сервиса "SonarQube + PostgreSQL":
    ```
    version: '3'

    services:
      sonarqube:
        image: sonarqube
        environment:
          - sonar.jdbc.url=jdbc:postgresql://db-sonarqube/sonar
        ports:
          - "9000:9000"
        networks:
          - devops-network

    networks:
      devops-network:
        driver: bridge

    volumes:
      sonarqube_db:
    ```
  - docker-compose для сервиса "Nexus":
    ```
    version: '3'
    
    services:
      nexus:
        image: sonatype/nexus3
        ports:
          - "8081:8081"
        volumes:
          - nexus_data:/nexus_data
        networks:
          - devops-network
    
    networks:
      devops-network:
        driver: bridge
    
    volumes:
      nexus_data:
    ```
2. После написания docker-compose файлов сервисы были запущены. Их работоспособность можно увидеть на скриншотах ниже:
   - Jenkins:
     ![image](https://github.com/user-attachments/assets/6d53ff6b-7bef-40f4-902a-9ea1bcc832ec)
     
   - Gitlab:
     ![Снимок экрана 2025-01-09 235324](https://github.com/user-attachments/assets/812b6dcf-89ca-4e35-9df8-ae5073dc89c6)
     
   - SonarQube:
     ![Снимок экрана 2025-01-10 003128](https://github.com/user-attachments/assets/9ce9a931-e9ae-4a97-89f5-104a7d4d9731)
     
   - Nexus:
     ![Снимок экрана 2025-01-10 004720](https://github.com/user-attachments/assets/b6a8282e-1302-4115-ad1c-23e6b2d9159f)
   
## Задача 2. Создание Python-приложения:
1. Во встроенном в "Debian" текстовом редакторе "nano", было написано 2 python файла со следующим содержанием:
   - "text_tool.py":
     ```python
     def count_words(text):
        return len(text.split())
     
     def longest_word(text):
        words = text.split()
        return max(words, key=len) if words else None
     ```
   - "test_text_tool.py":
     ```python
      import pytest
      from text_tool import count_words, longest_word
      
      def test_count_words():
          assert count_words("Hello world") == 2
          assert count_words("") == 0
      
      def test_longest_word():
          assert longest_word("Hello world") == "Hello"
          assert longest_word("") is None
     ```
 2. Так же был создан текстовый файл "requirements.txt":
    pytest==5.2.1

## Задача 3. Интеграция инструментов
  - GitLab CI/CD:
    Был написан файл ".gitlab-ci.yml" и создан gitlab-runner. Тесты были пройдены. С резулььтатами можно ознакомиться ниже:

    ![Снимок экрана 2025-01-25 121919](https://github.com/user-attachments/assets/0c25cf61-8563-474f-96f6-75c5561cb374)

    ![Снимок экрана 2025-01-25 121008](https://github.com/user-attachments/assets/1ae3106e-7cdb-405c-a28f-1cee60fb1c7d)


  - Jenkins:
    Был создан Jenkins-агент и Pipeline, тесты были пройдены. С результатами можно ознакомиться ниже:
    ![Снимок экрана 2025-01-24 133256](https://github.com/user-attachments/assets/85774543-c76c-40b3-9c69-a384aff6fde0)

    ![Снимок экрана 2025-01-25 132432](https://github.com/user-attachments/assets/7a228568-1372-4f8e-9573-bf1252a64fc5)

