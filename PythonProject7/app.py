from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)
app.json.ensure_ascii = False  # <-- Вот здесь должна быть эта строка

# Определите путь к вашему файлу Excel
EXCEL_FILE_PATH = 'financial_data.xlsx'  # Make sure this file is in the same directory as app.py


def load_financial_data():
    data = {}
    try:
        print(f"Попытка загрузить файл Excel: {os.path.abspath(EXCEL_FILE_PATH)}")

        # Попробуем загрузить Monthly Expenses
        try:
            expenses_df = pd.read_excel(EXCEL_FILE_PATH, sheet_name='Monthly_Expenses')
            data['expenses'] = expenses_df.to_dict(orient='records')
            print("Лист 'Monthly_Expenses' загружен успешно.")
        except Exception as e_expenses:
            print(f"Ошибка при загрузке листа 'Monthly_Expenses': {e_expenses}")
            return None

            # Попробуем загрузить Revenue
        try:
            revenue_df = pd.read_excel(EXCEL_FILE_PATH, sheet_name='Revenue')
            data['revenue'] = revenue_df.to_dict(orient='records')
            print("Лист 'Revenue' загружен успешно.")
        except Exception as e_revenue:
            print(f"Ошибка при загрузке листа 'Revenue': {e_revenue}")
            return None

        return data
    except FileNotFoundError:
        print(f"Критическая ошибка: Файл Excel не найден по пути {os.path.abspath(EXCEL_FILE_PATH)}")
        return None
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке Excel данных: {e}")
        return None


@app.route('/api/financial_summary', methods=['GET'])
def get_financial_summary():
    financial_data = load_financial_data()
    if financial_data:
        # Ваши расчеты
        total_expenses = sum(item['Сумма'] for item in financial_data['expenses'])
        total_revenue = sum(item['Продажи'] + item['Услуги'] for item in financial_data['revenue'])

        summary = {
            'total_revenue': total_revenue,
            'total_expenses': total_expenses,
            'net_profit': total_revenue - total_expenses,
            'raw_expenses_data': financial_data['expenses'],
            'raw_revenue_data': financial_data['revenue']
        }
        return jsonify(summary)  # <-- Здесь оставляем просто jsonify(summary)
    else:
        return jsonify({"error": "Финансовые данные не могут быть загружены"}), 500


@app.route('/')
def home():
    return "Бэкенд работает. Доступ к /api/financial_summary для получения данных."


if __name__ == '__main__':
    app.run(debug=True)