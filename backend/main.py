from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
# Эта настройка важна для корректного отображения кириллицы в JSON
app.json.ensure_ascii = False
CORS(app)

# Путь к файлу внутри контейнера будет таким же, как и в проекте
EXCEL_FILE_PATH = 'financial_data.xlsx'


def load_financial_data():
    data = {}
    # Проверяем, существует ли файл внутри контейнера
    if not os.path.exists(EXCEL_FILE_PATH):
        print(f"Критическая ошибка: Файл Excel не найден по пути {os.path.abspath(EXCEL_FILE_PATH)}")
        return None

    try:
        # Загружаем данные из листов Excel
        expenses_df = pd.read_excel(EXCEL_FILE_PATH, sheet_name='Monthly_Expenses')
        data['expenses'] = expenses_df.to_dict(orient='records')

        revenue_df = pd.read_excel(EXCEL_FILE_PATH, sheet_name='Revenue')
        data['revenue'] = revenue_df.to_dict(orient='records')

        print("Финансовые данные из Excel загружены успешно.")
        return data

    except Exception as e:
        print(f"Ошибка при чтении файла Excel: {e}")
        return None


@app.route('/api/financial_summary', methods=['GET'])
def get_financial_summary():
    financial_data = load_financial_data()

    if financial_data:
        try:
            total_expenses = sum(item['Сумма'] for item in financial_data['expenses'])
            total_revenue = sum(item.get('Продажи', 0) + item.get('Услуги', 0) for item in financial_data['revenue'])

            summary = {
                'total_revenue': f"{total_revenue:,.2f} ₽".replace(",", " "),
                'total_expenses': f"{total_expenses:,.2f} ₽".replace(",", " "),
                'net_profit': f"{total_revenue - total_expenses:,.2f} ₽".replace(",", " "),
                'raw_expenses_data': financial_data['expenses'],
                'raw_revenue_data': financial_data['revenue']
            }
            return jsonify(summary)
        except KeyError as e:
            return jsonify({"error": f"Отсутствует необходимый столбец в Excel: {e}"}), 500
    else:
        return jsonify({"error": "Финансовые данные не могут быть загружены с сервера"}), 500


@app.route('/')
def home():
    return "Бэкенд работает. Используйте /api/financial_summary для получения данных."