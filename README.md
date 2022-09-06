# <p align="center">Тестовое задание: простой парсер json

---  

### Todo
Сделать простой парсер и конвертер структур

### Рекомендуемый стек:
* python3.6+
* pydantic
* pytest

### Рекомендуемая методология: TDD

### Входящие данные:
```json
{
 "description": "<ul><li>поддержка текущих проектов и сервисов компании,</li><li>разработка новых и доработка существующих функций по техническим заданиям,</li><li>активное взаимодействие с командой разработки,</li><li>освоение новых технологий и развитие профессиональных навыков под руководством опытного наставника.</li><li>Написание автотестов</li></ul>",
 "employment": "fullDay",
 "address": {
   "region": "Кировская",
   "city": "Киров",
   "street_type": "",
   "street": "",
   "house_type": "",
   "house": "",
   "value": "г Киров, ул Володарского, д 157",
   "lat": 58.593565,
   "lng": 49.672739
 },
 "name": "Junior Backend-developer",
 "salary": {
   "from": 30000,
   "to": 70000,
   "currency": "RUR",
   "gross": false
 },
 "contacts": {
   "fullName": "Журавлев Илья",
   "phone": "79536762399",
   "email": "ilya.zhuravlev@hrb.software"
 }
}
```

### Результат:
```json
{
 "address": "г Киров, ул Володарского, д 157",
 "allow_messages": true,
 "billing_type": "packageOrSingle",
 "business_area": 1,
 "contacts": {
   "email": "ilya.zhuravlev@hrb.software",
   "name": "Журавлев Илья",
   "phone": {
     "city": "953",
     "country": "7",
     "number": "676-23-99"
   }
 },
 "coordinates": {
   "latitude": 58.593565,
   "longitude": 49.672739
 },
 "description": "<ul><li>поддержка текущих проектов и сервисов компании,</li><li>разработка новых и доработка существующих функций по техническим заданиям,</li><li>активное взаимодействие с командой разработки,</li><li>освоение новых технологий и развитие профессиональных навыков под руководством опытного наставника.</li><li>Написание автотестов</li></ul>",
 "experience": {
   "id": "noMatter"
 },
 "html_tags": true,
 "image_url": "https://img.hhcdn.ru/employer-logo/3410666.jpeg",
 "name": "Junior Backend-developer",
 "salary": 70000,
 "salary_range": {
   "from": 30000,
   "to": 70000
 },
 "schedule": {
   "id": "fullDay"
 }
}
```

---

### Установка
1) В локальную папку клонируем файлы проекта:
```shell
git clone git@github.com:AlekseyGolikov/pydantic_test_task.git
```
2) Устанавливаем в папку .../pydantic_test_task виртуальное окружение. Далее устанавливаем все зависимости, используемые скриптом:
```shell
pip install -r requirements.txt
```
3) Запускаем тестирование в режиме показа полной информации о пройденном тесте  
```shell
pytest -v
```
*Прим.: PASSED - тестовая функция завершилась успешно
