import React, { useState, useEffect } from 'react';
import './App.css'; // Теперь снова нужен, так как стили будут из App.css
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

// Регистрируем компоненты Chart.js, чтобы они были доступны для использования
ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

function App() {
  const [financialData, setFinancialData] = useState(null); // Состояние для хранения данных
  const [loading, setLoading] = useState(true); // Состояние для индикатора загрузки
  const [error, setError] = useState(null); // Состояние для ошибок

  useEffect(() => {
    const fetchFinancialData = async () => {
      try {
        // Запрос к вашему бэкенду. Используем относительный путь /api/,
        // потому что Vite-прокси перенаправит его на http://127.0.0.1:5000/api/
        const response = await fetch('/api/financial_summary'); 
        
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setFinancialData(data);
      } catch (e) {
        console.error("Ошибка при получении данных:", e);
        setError(e.message);
      } finally {
        setLoading(false);
      }
    };

    fetchFinancialData();
  }, []);

  if (loading) {
    return (
      <div className="App"> {/* Используем старый класс App */}
        <header className="App-header">
          <p>Загрузка финансовых данных...</p>
        </header>
      </div>
    );
  }

  if (error) {
    return (
      <div className="App">
        <header className="App-header">
          <p>Ошибка: {error}</p>
        </header>
      </div>
    );
  }

  if (!financialData) {
    return (
      <div className="App">
        <header className="App-header">
          <p>Данные не загружены.</p>
        </header>
      </div>
    );
  }

  // Подготовка данных для графика расходов по месяцам
  // Flask возвращает "raw_expenses_data" как список объектов с "Месяц" и "Сумма"
  const expensesByMonth = financialData.raw_expenses_data.reduce((acc, item) => {
    const month = item["Месяц"];
    const amount = item["Сумма"];
    if (acc[month]) {
      acc[month] += amount;
    } else {
      acc[month] = amount;
    }
    return acc;
  }, {});

  const expenseChartData = {
    labels: Object.keys(expensesByMonth), // Месяцы
    datasets: [
      {
        label: 'Расходы',
        data: Object.values(expensesByMonth), // Суммы расходов
        backgroundColor: 'rgba(255, 99, 132, 0.6)',
        borderColor: 'rgba(255, 99, 132, 1)',
        borderWidth: 1,
      },
    ],
  };

  const expenseChartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'top',
        labels: {
            color: 'black', // Цвет текста легенды для светлого фона
        }
      },
      title: {
        display: true,
        text: 'Расходы по месяцам',
        color: 'black', // Цвет заголовка для светлого фона
        font: {
            size: 18,
        }
      },
      tooltip: {
          callbacks: {
              label: function(context) {
                  let label = context.dataset.label || '';
                  if (label) {
                      label += ': ';
                  }
                  if (context.parsed.y !== null) {
                      label += new Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(context.parsed.y);
                  }
                  return label;
              }
          },
          backgroundColor: 'rgba(0,0,0,0.7)',
          titleColor: 'white',
          bodyColor: 'white',
          borderColor: 'rgba(255,255,255,0.2)',
          borderWidth: 1,
          borderRadius: 5,
      }
    },
    scales: {
      x: {
        ticks: {
          color: 'black' // Цвет меток на оси X для светлого фона
        },
        grid: {
            color: 'rgba(0, 0, 0, 0.1)' // Цвет сетки на оси X для светлого фона
        }
      },
      y: {
        ticks: {
          color: 'black' // Цвет меток на оси Y для светлого фона
        },
        grid: {
            color: 'rgba(0, 0, 0, 0.1)' // Цвет сетки на оси Y для светлого фона
        }
      }
    }
  };

  // Подготовка данных для графика выручки по месяцам
  const revenueByMonth = financialData.raw_revenue_data.reduce((acc, item) => {
    const month = item["Месяц"];
    const amount = (item["Продажи"] || 0) + (item["Услуги"] || 0); 
    
    if (acc[month]) {
      acc[month] += amount;
    } else {
      acc[month] = amount;
    }
    return acc;
  }, {});

  const revenueChartData = {
    labels: Object.keys(revenueByMonth), // Месяцы
    datasets: [
      {
        label: 'Выручка',
        data: Object.values(revenueByMonth), // Суммы выручки
        backgroundColor: 'rgba(75, 192, 192, 0.6)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1,
      },
    ],
  };

  const revenueChartOptions = {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
          legend: {
              position: 'top',
              labels: {
                  color: 'black',
              }
          },
          title: {
              display: true,
              text: 'Выручка по месяцам',
              color: 'black',
              font: {
                  size: 18,
              }
          },
          tooltip: {
              callbacks: {
                  label: function(context) {
                      let label = context.dataset.label || '';
                      if (label) {
                          label += ': ';
                      }
                      if (context.parsed.y !== null) {
                          label += new Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(context.parsed.y);
                      }
                      return label;
                  }
              },
              backgroundColor: 'rgba(0,0,0,0.7)',
              titleColor: 'white',
              bodyColor: 'white',
              borderColor: 'rgba(255,255,255,0.2)',
              borderWidth: 1,
              borderRadius: 5,
          }
      },
      scales: {
          x: {
            ticks: {
              color: 'black'
            },
            grid: {
                color: 'rgba(0, 0, 0, 0.1)'
            }
          },
          y: {
            ticks: {
              color: 'black'
            },
            grid: {
                color: 'rgba(0, 0, 0, 0.1)'
            }
          }
      }
  };

  return (
    <div className="App"> {/* Используем старый класс App */}
      <header className="App-header">
        <h1>Обзор Финансовых Показателей</h1>
        <p>Общая выручка: {financialData.total_revenue}</p>
        <p>Общие расходы: {financialData.total_expenses}</p>
        <p>Чистая прибыль: {financialData.net_profit}</p>

        {/* Графики */}
        <div style={{ width: '80%', margin: 'auto', marginTop: '20px' }}>
          <Bar data={expenseChartData} options={expenseChartOptions} />
        </div>
        <div style={{ width: '80%', margin: 'auto', marginTop: '40px' }}>
          <Bar data={revenueChartData} options={revenueChartOptions} />
        </div>

        {/* Сырые данные */}
        <h2>Сырые данные о расходах:</h2>
        <pre>{JSON.stringify(financialData.raw_expenses_data, null, 2)}</pre>

        <h2>Сырые данные о выручке:</h2>
        <pre>{JSON.stringify(financialData.raw_revenue_data, null, 2)}</pre>
      </header>
    </div>
  );
}

export default App;
