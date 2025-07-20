import React from 'react';
import { useFinancialData } from './hooks/useFinancialData';
import { prepareChartData, getChartOptions } from './utils/chartHelper';

import FinancialCard from './components/FinancialCard.jsx';
import BarChart from './components/BarChart.jsx';
import LoadingSpinner from './components/LoadingSpinner.jsx';
import ErrorMessage from './components/ErrorMessage.jsx';
import RawDataViewer from './components/RawDataViewer.jsx';

import { FiTrendingUp, FiTrendingDown, FiDollarSign } from 'react-icons/fi';

function App() {
  const { data: financialData, loading, error } = useFinancialData();

  if (loading) return <LoadingSpinner />;
  if (error) return <ErrorMessage message={error} />;
  if (!financialData) {
    return <div className="min-h-screen flex items-center justify-center bg-slate-50"><p>Данные не найдены.</p></div>;
  }

  const expenseChartData = prepareChartData(financialData.raw_expenses_data, 'Расходы', 'Сумма');
  const revenueChartData = prepareChartData(financialData.raw_revenue_data, 'Выручка', ['Продажи', 'Услуги']);
  
  const expenseChartOptions = getChartOptions('Расходы по месяцам');
  const revenueChartOptions = getChartOptions('Выручка по месяцам');
  
  const isProfitNegative = String(financialData.net_profit || '').startsWith('-');

  return (
    <div className="min-h-screen bg-slate-50 text-slate-800">
      <main className="max-w-7xl mx-auto p-4 sm:p-6 lg:p-8">
        <header className="mb-10">
          <h1 className="text-4xl font-bold tracking-tight text-slate-900 mb-2">Финансовый Дашборд</h1>
          <p className="text-lg text-slate-500">Обзор ключевых показателей вашего бизнеса</p>
        </header>

        <section className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-12">
          <FinancialCard 
            title="Общая выручка"
            value={financialData.total_revenue}
            icon={<FiTrendingUp size={24} className="text-green-700" />}
            colorClass={{ bg: 'bg-green-100', text: 'text-green-600' }}
          />
          <FinancialCard 
            title="Общие расходы"
            value={financialData.total_expenses}
            icon={<FiTrendingDown size={24} className="text-red-700" />}
            colorClass={{ bg: 'bg-red-100', text: 'text-red-600' }}
          />
          <FinancialCard 
            title="Чистая прибыль"
            value={financialData.net_profit}
            icon={<FiDollarSign size={24} className={isProfitNegative ? "text-red-700" : "text-green-700"} />}
            colorClass={{ 
              bg: isProfitNegative ? 'bg-red-100' : 'bg-green-100', 
              text: isProfitNegative ? 'text-red-600' : 'text-green-600' 
            }}
          />
        </section>

        <section className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-12">
          <BarChart data={revenueChartData} options={revenueChartOptions} />
          <BarChart data={expenseChartData} options={expenseChartOptions} />
        </section>

        <section className="space-y-8">
          <RawDataViewer title="Сырые данные о выручке" data={financialData.raw_revenue_data} />
          <RawDataViewer title="Сырые данные о расходах" data={financialData.raw_expenses_data} />
        </section>
      </main>
    </div>
  );
}

export default App;