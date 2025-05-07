## Template for telegram bot using aiogram

In .env:
```
BOT_TOKEN=123456:Your-Token
ADMINS=123456, 789876
USE_REDIS=False
```
Installing requirements:
```
pip install -r requirements.txt
```

Or just use Docker:
```
docker compose up --build
```

If whant to add redis and redis-insight
In .env:
```
USE_REDIS=True
```
And uncomment redis and redis-insight configuration in docker-compose.
