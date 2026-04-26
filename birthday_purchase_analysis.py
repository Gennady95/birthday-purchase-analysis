import pandas as pd, time, re, glob, getpass, platform, telebot
from sqlalchemy import create_engine
from datetime import datetime, timedelta
from tqdm import tqdm

#Паттерны
engine = create_engine(*)                                                                                                # Коннектор SQL
date = datetime.now().strftime('%d.%m %H:%M:%S')                                                                         # Текущая дата
bot = telebot.TeleBot(*)                                                                                                 # Токен telegram бота
re_1 = r'[^0-9,.;/]'                                                                                                     # Регулярное выражение для отсева букв, пробелов
re_2 = r'[^0-9]'                                                                                                         # Регулярное выражение для отсева знаков

def SendTelegram(status):
	# Получение информации о компьютере
	UserName = getpass.getuser()                                                                                         # Имя пользователя (обычно оно User - не информативно)
	CompName = platform.node()                                                                                           # Имя компьютера
	chat_id = '5249664773'                                                                                               # ID моей телеги
	if status == "try": # Если связь с телегой установлена
		bot.send_message(chat_id, date+" пользователь "+UserName+" ("+CompName+") успешно воспользовался скриптом для подсчёта выручки по номерам телефонов") #Отправка сообщения
	elif status == "except1": # Если нет подключения к SQL серверу
		bot.send_message(chat_id, "ERROR: " + date+" пользователь "+UserName+" ("+CompName+") неудачно запустил скрипт для подсчёта выручки по номерам телефонов - не подключил VPN") #Отправка сообщения
	elif status == "except2": # Если нет подключения к SQL серверу
		bot.send_message(chat_id, "ERROR: " + date+" пользователь "+UserName+" ("+CompName+") неудачно запустил скрипт для подсчёта выручки по номерам телефонов - либо не закрыл файл, либо в файле нет подходящих колонок") #Отправка сообщения
def fun(x, year):
    try: return x.replace(year=year, hour=0, minute=0, second=0)
    except: return x
def CollectData(FileLocation):                                                                                           # Чтение одного или нескольких excel фалов .xlsx
	GroupFile = [item for item in glob.glob(FileLocation)]                                                               # Собираем файлы в список
	itter = 0                                                                                                            # Переменная для подсчёта удачных повторений скрипта
	for Filename in tqdm(GroupFile): # Вводные для progress bar
		if not 'Результат валидации' in str(Filename):
			print(Filename, "Началась загрузка excel файла: ", datetime.time(datetime.now()))
			try:
				File = pd.read_excel(Filename, usecols=['Номер телефона', 'День рождения']) # Чтение excel-файла
				dfEX = pd.DataFrame(File)                                                                                # Формирование dataframe
				#Обработка фрейма данных
				dfEX['День рождения'] = pd.to_datetime(dfEX['День рождения'], errors='coerce')
				dfEX['День рождения'] = pd.to_datetime(dfEX['День рождения'], dayfirst=True)                             # Преобразование столбца дат в даты SQL формата
				dfEX['День рождения 2019'] = dfEX['День рождения'].apply(lambda x: fun(x, 2019))  # Чистка поля с номером телефона (кто звонил)
				dfEX['День рождения 2019d1'] = dfEX['День рождения 2019'].apply(lambda x: x + timedelta(days=1))  # Чистка поля с номером телефона (кто звонил)
				dfEX['День рождения 2019d7'] = dfEX['День рождения 2019'].apply(lambda x: x + timedelta(days=7))  # Чистка поля с номером телефона (кто звонил)
				dfEX['День рождения 2020'] = dfEX['День рождения'].apply(lambda x: fun(x, 2020))  # Чистка поля с номером телефона (кто звонил)
				dfEX['День рождения 2020d1'] = dfEX['День рождения 2020'].apply(lambda x: x + timedelta(days=1))  # Чистка поля с номером телефона (кто звонил)
				dfEX['День рождения 2020d7'] = dfEX['День рождения 2020'].apply(lambda x: x + timedelta(days=7))  # Чистка поля с номером телефона (кто звонил)
				dfEX['День рождения 2021'] = dfEX['День рождения'].apply(lambda x: fun(x, 2021))  # Чистка поля с номером телефона (кто звонил)
				dfEX['День рождения 2021d1'] = dfEX['День рождения 2021'].apply(lambda x: x + timedelta(days=1))  # Чистка поля с номером телефона (кто звонил)
				dfEX['День рождения 2021d7'] = dfEX['День рождения 2021'].apply(lambda x: x + timedelta(days=7))  # Чистка поля с номером телефона (кто звонил)
				dfEX['День рождения 2022'] = dfEX['День рождения'].apply(lambda x: fun(x, 2022))  # Чистка поля с номером телефона (кто звонил)
				dfEX['День рождения 2022d1'] = dfEX['День рождения 2022'].apply(lambda x: x + timedelta(days=1))  # Чистка поля с номером телефона (кто звонил)
				dfEX['День рождения 2022d7'] = dfEX['День рождения 2022'].apply(lambda x: x + timedelta(days=7))  # Чистка поля с номером телефона (кто звонил)
				dfEX['День рождения 2023'] = dfEX['День рождения'].apply(lambda x: fun(x, 2023))  # Чистка поля с номером телефона (кто звонил)
				dfEX['День рождения 2023d1'] = dfEX['День рождения 2023'].apply(lambda x: x + timedelta(days=1))  # Чистка поля с номером телефона (кто звонил)
				dfEX['День рождения 2023d7'] = dfEX['День рождения 2023'].apply(lambda x: x + timedelta(days=7))  # Чистка поля с номером телефона (кто звонил)
				dfEX['День рождения 2024'] = dfEX['День рождения'].apply(lambda x: fun(x, 2024))  # Чистка поля с номером телефона (кто звонил)
				dfEX['День рождения 2024d1'] = dfEX['День рождения 2024'].apply(lambda x: x + timedelta(days=1))  # Чистка поля с номером телефона (кто звонил)
				dfEX['День рождения 2024d7'] = dfEX['День рождения 2024'].apply(lambda x: x + timedelta(days=7))  # Чистка поля с номером телефона (кто звонил)

				dfEX['День рождения']
				dfEX['Номер телефона'].astype('str')                                                                     # Преобразование столбца с номерами телефонов в строчный формат
				dfEX['Номер телефона'] = dfEX['Номер телефона'].apply(lambda x: max(re.sub(re_2, ',', re.sub(re_1, '', str(x))).lstrip(',').split(',', 10), key=len)[-10:])
				dfEX['Номер телефона'] = dfEX['Номер телефона'].loc[dfEX['Номер телефона'].str.len().between(10, 11)]    # Выбор номера телефона определённого формата
				dfEX = dfEX.groupby(pd.Grouper(key='Номер телефона')).min().reset_index()                                # Группировка с удалением дубликатов и выбором наименьшей даты

				# Создание списков для итерирования
				list_of_numbers = list(filter(None, dfEX['Номер телефона'].tolist()))                                    # Получение списка из номеров телефонов в excel файле
				list_of_date_2019 = list(filter(None, dfEX['День рождения 2019'].tolist()))                                  # Получение списка из номеров дат начала в excel файле
				list_of_date_2020 = list(filter(None, dfEX['День рождения 2020'].tolist()))                                  # Получение списка из номеров дат начала в excel файле
				list_of_date_2021 = list(filter(None, dfEX['День рождения 2021'].tolist()))                                  # Получение списка из номеров дат начала в excel файле
				list_of_date_2022 = list(filter(None, dfEX['День рождения 2022'].tolist()))                                  # Получение списка из номеров дат начала в excel файле
				list_of_date_2023 = list(filter(None, dfEX['День рождения 2023'].tolist()))                                  # Получение списка из номеров дат начала в excel файле
				list_of_date_2024 = list(filter(None, dfEX['День рождения 2024'].tolist()))                                  # Получение списка из номеров дат начала в excel файле

				list_of_date_2019d1 = list(filter(None, dfEX['День рождения 2019d1'].tolist()))                                  # Получение списка из номеров дат начала в excel файле
				list_of_date_2020d1 = list(filter(None, dfEX['День рождения 2020d1'].tolist()))                                  # Получение списка из номеров дат начала в excel файле
				list_of_date_2021d1 = list(filter(None, dfEX['День рождения 2021d1'].tolist()))                                  # Получение списка из номеров дат начала в excel файле
				list_of_date_2022d1 = list(filter(None, dfEX['День рождения 2022d1'].tolist()))                                  # Получение списка из номеров дат начала в excel файле
				list_of_date_2023d1 = list(filter(None, dfEX['День рождения 2023d1'].tolist()))                                  # Получение списка из номеров дат начала в excel файле
				list_of_date_2024d1 = list(filter(None, dfEX['День рождения 2024d1'].tolist()))                                  # Получение списка из номеров дат начала в excel файле

				list_of_date_2019d7 = list(filter(None, dfEX['День рождения 2019d7'].tolist()))                                  # Получение списка из номеров дат начала в excel файле
				list_of_date_2020d7 = list(filter(None, dfEX['День рождения 2020d7'].tolist()))                                  # Получение списка из номеров дат начала в excel файле
				list_of_date_2021d7 = list(filter(None, dfEX['День рождения 2021d7'].tolist()))                                  # Получение списка из номеров дат начала в excel файле
				list_of_date_2022d7 = list(filter(None, dfEX['День рождения 2022d7'].tolist()))                                  # Получение списка из номеров дат начала в excel файле
				list_of_date_2023d7 = list(filter(None, dfEX['День рождения 2023d7'].tolist()))                                  # Получение списка из номеров дат начала в excel файле
				list_of_date_2024d7 = list(filter(None, dfEX['День рождения 2024d7'].tolist()))                                  # Получение списка из номеров дат начала в excel файле


				print("Созданы списки для проверки по файлу " + FileLocation + " . Теперь начнём считать...")
				# Подготовка базы
				dfSQLstoNew = dfSQLsto.loc[(dfSQLsto['НомерТелефона'].isin(list(filter(None, list_of_numbers))))]  # Обрезка базы СТО по номерам телефонов
				dfSQLstoNew2019 = dfSQLstoNew.loc[((dfSQLstoNew['Дата'] >= datetime(2019, 1, 1)) & (dfSQLstoNew['Дата'] <= datetime(2019, 1, 1)))] # Обрезка базы по датам
				dfSQLstoNew2020 = dfSQLstoNew.loc[((dfSQLstoNew['Дата'] >= datetime(2020, 1, 1)) & (dfSQLstoNew['Дата'] <= datetime(2021, 1, 1)))] # Обрезка базы по датам
				dfSQLstoNew2021 = dfSQLstoNew.loc[((dfSQLstoNew['Дата'] >= datetime(2021, 1, 1)) & (dfSQLstoNew['Дата'] <= datetime(2022, 1, 1)))] # Обрезка базы по датам
				dfSQLstoNew2022 = dfSQLstoNew.loc[((dfSQLstoNew['Дата'] >= datetime(2022, 1, 1)) & (dfSQLstoNew['Дата'] <= datetime(2023, 1, 1)))] # Обрезка базы по датам
				dfSQLstoNew2023 = dfSQLstoNew.loc[((dfSQLstoNew['Дата'] >= datetime(2023, 1, 1)) & (dfSQLstoNew['Дата'] <= datetime(2024, 1, 1)))] # Обрезка базы по датам
				dfSQLstoNew2024 = dfSQLstoNew.loc[((dfSQLstoNew['Дата'] >= datetime(2024, 1, 1)) & (dfSQLstoNew['Дата'] <= datetime(2025, 1, 1)))] # Обрезка базы по датам


				print("В базе СТО " + str(len(dfSQLstoNew['НомерТелефона'])) + " подходящих записей по номерам телефонов")

				# Анализ по базе СТО
				STO2019 = pd.DataFrame(); print("STO2019"); i = 0
				for Num, Start, End in zip(list_of_numbers, list_of_date_2019, list_of_date_2019d1):                    # Цикл проходит по списку SQL n количество раз, равному len(list) базы excel
					i += 1;	print(i)
					try: STO2019 = pd.concat([STO2019, dfSQLstoNew2019.loc[((dfSQLstoNew2019['НомерТелефона'] == Num) & (dfSQLstoNew2019['Дата'] >= Start) & (dfSQLstoNew2019['Дата'] <= End))]], ignore_index=True)
					except: pass
				STO2020 = pd.DataFrame(); print("STO2020"); i = 0
				for Num, Start, End in zip(list_of_numbers, list_of_date_2020, list_of_date_2020d1):                    # Цикл проходит по списку SQL n количество раз, равному len(list) базы excel
					i += 1;	print(i)
					try: STO2020 = pd.concat([STO2020, dfSQLstoNew2020.loc[((dfSQLstoNew2020['НомерТелефона'] == Num) & (dfSQLstoNew2020['Дата'] >= Start) & (dfSQLstoNew2020['Дата'] <= End))]], ignore_index=True)
					except: pass
				STO2021 = pd.DataFrame(); print("STO2021"); i = 0
				for Num, Start, End in zip(list_of_numbers, list_of_date_2021, list_of_date_2021d1):                    # Цикл проходит по списку SQL n количество раз, равному len(list) базы excel
					i += 1;	print(i)
					try: STO2021 = pd.concat([STO2021, dfSQLstoNew2021.loc[((dfSQLstoNew2021['НомерТелефона'] == Num) & (dfSQLstoNew2021['Дата'] >= Start) & (dfSQLstoNew2021['Дата'] <= End))]], ignore_index=True)
					except: pass
				STO2022 = pd.DataFrame(); print("STO2022"); i = 0
				for Num, Start, End in zip(list_of_numbers, list_of_date_2022, list_of_date_2022d1):                    # Цикл проходит по списку SQL n количество раз, равному len(list) базы excel
					i += 1;	print(i)
					try: STO2022 = pd.concat([STO2022, dfSQLstoNew2022.loc[((dfSQLstoNew2022['НомерТелефона'] == Num) & (dfSQLstoNew2022['Дата'] >= Start) & (dfSQLstoNew2022['Дата'] <= End))]], ignore_index=True)
					except: pass
				STO2023 = pd.DataFrame(); print("STO2023"); i = 0
				for Num, Start, End in zip(list_of_numbers, list_of_date_2023, list_of_date_2023d1):                    # Цикл проходит по списку SQL n количество раз, равному len(list) базы excel
					i += 1;	print(i)
					try: STO2023 = pd.concat([STO2023, dfSQLstoNew2023.loc[((dfSQLstoNew2023['НомерТелефона'] == Num) & (dfSQLstoNew2023['Дата'] >= Start) & (dfSQLstoNew2023['Дата'] <= End))]], ignore_index=True)
					except: pass
				STO2024 = pd.DataFrame(); print("STO2024"); i = 0
				for Num, Start, End in zip(list_of_numbers, list_of_date_2024, list_of_date_2024d1):                    # Цикл проходит по списку SQL n количество раз, равному len(list) базы excel
					i += 1;	print(i)
					try: STO2024 = pd.concat([STO2024, dfSQLstoNew2024.loc[((dfSQLstoNew2024['НомерТелефона'] == Num) & (dfSQLstoNew2024['Дата'] >= Start) & (dfSQLstoNew2024['Дата'] <= End))]], ignore_index=True)
					except:	pass
				# Анализ по базе СТО (7 дней)
				STO2019_7 = pd.DataFrame(); print("STO2019_7")
				for Num, Start, End in zip(list_of_numbers, list_of_date_2019, list_of_date_2019d7):                    # Цикл проходит по списку SQL n количество раз, равному len(list) базы excel
					try: STO2019_7 = pd.concat([STO2019_7, dfSQLstoNew2019.loc[((dfSQLstoNew2019['НомерТелефона'] == Num) & (dfSQLstoNew2019['Дата'] >= Start) & (dfSQLstoNew2019['Дата'] <= End))]], ignore_index=True)
					except: pass
				STO2020_7 = pd.DataFrame(); print("STO2020_7")
				for Num, Start, End in zip(list_of_numbers, list_of_date_2020, list_of_date_2020d7):                    # Цикл проходит по списку SQL n количество раз, равному len(list) базы excel
					try: STO2020_7 = pd.concat([STO2020_7, dfSQLstoNew2020.loc[((dfSQLstoNew2020['НомерТелефона'] == Num) & (dfSQLstoNew2020['Дата'] >= Start) & (dfSQLstoNew2020['Дата'] <= End))]], ignore_index=True)
					except: pass
				STO2021_7 = pd.DataFrame(); print("STO2021_7")
				for Num, Start, End in zip(list_of_numbers, list_of_date_2021, list_of_date_2021d7):                    # Цикл проходит по списку SQL n количество раз, равному len(list) базы excel
					try: STO2021_7 = pd.concat([STO2021_7, dfSQLstoNew2021.loc[((dfSQLstoNew2021['НомерТелефона'] == Num) & (dfSQLstoNew2021['Дата'] >= Start) & (dfSQLstoNew2021['Дата'] <= End))]], ignore_index=True)
					except: pass
				STO2022_7 = pd.DataFrame(); print("STO2022_7")
				for Num, Start, End in zip(list_of_numbers, list_of_date_2022, list_of_date_2022d7):                    # Цикл проходит по списку SQL n количество раз, равному len(list) базы excel
					try: STO2022_7 = pd.concat([STO2022_7, dfSQLstoNew2022.loc[((dfSQLstoNew2022['НомерТелефона'] == Num) & (dfSQLstoNew2022['Дата'] >= Start) & (dfSQLstoNew2022['Дата'] <= End))]], ignore_index=True)
					except: pass
				STO2023_7 = pd.DataFrame(); print("STO2023_7")
				for Num, Start, End in zip(list_of_numbers, list_of_date_2023, list_of_date_2023d7):                    # Цикл проходит по списку SQL n количество раз, равному len(list) базы excel
					try: STO2023_7 = pd.concat([STO2023_7, dfSQLstoNew2023.loc[((dfSQLstoNew2023['НомерТелефона'] == Num) & (dfSQLstoNew2023['Дата'] >= Start) & (dfSQLstoNew2023['Дата'] <= End))]], ignore_index=True)
					except: pass
				STO2024_7 = pd.DataFrame(); print("STO2024_7")
				for Num, Start, End in zip(list_of_numbers, list_of_date_2024, list_of_date_2024d7):                    # Цикл проходит по списку SQL n количество раз, равному len(list) базы excel
					try: STO2024_7 = pd.concat([STO2024_7, dfSQLstoNew2024.loc[((dfSQLstoNew2024['НомерТелефона'] == Num) & (dfSQLstoNew2024['Дата'] >= Start) & (dfSQLstoNew2024['Дата'] <= End))]], ignore_index=True)
					except: pass
				try:
					with pd.ExcelWriter(Filename, engine='openpyxl', mode='a') as writer:                                # Дополнение excel файла новыми листами
						try:
							STO2019.to_excel(writer, sheet_name='STO2019', index=False)
							STO2020.to_excel(writer, sheet_name='STO2020', index=False)
							STO2021.to_excel(writer, sheet_name='STO2021', index=False)
							STO2022.to_excel(writer, sheet_name='STO2022', index=False)
							STO2023.to_excel(writer, sheet_name='STO2023', index=False)
							STO2024.to_excel(writer, sheet_name='STO2024', index=False)
							STO2019_7.to_excel(writer, sheet_name='STO2019_7', index=False)
							STO2020_7.to_excel(writer, sheet_name='STO2020_7', index=False)
							STO2021_7.to_excel(writer, sheet_name='STO2021_7', index=False)
							STO2022_7.to_excel(writer, sheet_name='STO2022_7', index=False)
							STO2023_7.to_excel(writer, sheet_name='STO2023_7', index=False)
							STO2024_7.to_excel(writer, sheet_name='STO2024_7', index=False)
							itter += 1
						except: pass
				except:	print("В файле" + Filename + " уже присутствуют листы с аналитикой :("); time.sleep(5)
			except Exception as e:
				print(f'Произошла ошибка: {e}'); print("Возможно у Вас открыт excel файл, который Вы пытаетесь валидировать или колонки названы неправильно"); time.sleep(5) #Обработка ошибки

	print("Все файлы обработаны")
	if itter > 0: SendTelegram("try")
	else: SendTelegram("except2")

#Получение данных из SQL
try:
	lightquery_2 = "SELECT * FROM sales_sto"                                                                             # SQL запрос в базу СТО
	print("Начинается загрузка SQL базы СТО (может занять пару минут)..."); dfSQLsto = pd.read_sql(lightquery_2, engine); print("База по СТО загружена") # Чтение MySQL СТО, получение dataframe
	dfSQLsto['НомерТелефона'] = dfSQLsto['НомерТелефона'].apply(lambda x: re.sub(re_1, '', str(x)))                 # Чистка БД СТО для подготовки к поиску
	print("Конвертация номеров телефонов в БД завершена, теперь возмусь за ваши файлы")
except Exception:
	print("Не могу подключится к SQL серверу. Проверьте подключение к VPN и перезапустите приложение")
	SendTelegram("except1")
	time.sleep(5); exit()

CollectData('*.xlsx')
