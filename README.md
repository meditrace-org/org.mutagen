![image](https://github.com/meditrace-org/org.mutagen/assets/65663748/18978857-dccf-412a-9159-03b5c2f44893)


# org.mutagen
Данный репозиторий содержит сервисы для главного воркера:
 - `org.mutagen.backend` - back-end API для запросов и взаимодействия с другими сервисами
 - `org.mutagen.clickhouse` - база данных
 - `org.mutagen.rabbitMQ` - брокер сообщений
 - `org.mutagen.vectorAPI` - сервис, преобразующий текст в векторы

Также в системе участвуют сервисы `audio-encoder` и `video-encoder`, преобразующие байты видео в векторы. Их реплики запускаются на отдельных worker-нодах.
В папке `upload` находится скрипт для загрузки в систему дата-сета организаторов хакатона.

### Конфигурация
Конфигурация сводится к указаниям переменных в `.env` файле. Все возможные переменные указаны в файле `.env.default`.

### Запуск
После настройки `.env`, для запуска достаточно выполнить команду
```bash
docker compose up -d
```
Спустя несколько секунд после запуска сервер будет готов к работе.

