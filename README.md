# Посетитли СТО в дни рождения
Потребовалось определить сколько клиентов совершают покупки в СТО в дни рождения и +7 дней после него. Отчёт предоставит информацию о совершённых заказ-нарядах за 5 лет и позволят таргетировать аудиторию по этому признаку

**Birthday Purchase Analysis (STO)**
Description

This project analyzes customer behavior in service centers by identifying how many clients make purchases on their birthday and within 7 days after.
The analysis is based on 5 years of historical service order data and is intended to support marketing decisions and improve customer targeting strategies.

Business Goal
The main objective is to determine whether birthdays can be used as an effective trigger for customer engagement and promotional campaigns.

Features
Data extraction from SQL database
Data preprocessing and cleaning (phone normalization)
Aggregation of customer visits and orders
Matching customer visits with birthday dates
Calculation of key metrics (birthday vs post-birthday visits)
Telegram notifications about script execution status
Tech Stack
Python
pandas
SQLAlchemy
pyTelegramBotAPI
tqdm
How It Works
Connects to a SQL database and loads customer and order data
Cleans and standardizes phone numbers
Aggregates customer visits
Matches visits with customer birthdays
Calculates metrics:
Visits on birthday
Visits within 7 days after birthday
Sends a Telegram notification after execution

Example / Demo
Input
Customer database (5 years of history)
Phone numbers
Birth dates
Service order records
Output
Percentage of customers visiting on their birthday
Percentage of customers visiting within 7 days after birthday
Aggregated dataset for further analysis
Use Case

This project can be used by:
Marketing teams for targeted campaigns
CRM analysts
Data analysts working with customer lifecycle data
Notes
Sensitive data (tokens, database credentials) should be stored in .env and not committed to the repository
The script is designed for internal analytics and can be adapted for other customer behavior studies
