export const prepareChartData = (rawData, label, dataKey) => {
    const monthlyData = rawData.reduce((acc, item) => {
      const month = item["Месяц"];
      const amount = Array.isArray(dataKey) 
        ? dataKey.reduce((sum, key) => sum + (item[key] || 0), 0)
        : item[dataKey] || 0;
        
      acc[month] = (acc[month] || 0) + amount;
      return acc;
    }, {});
  
    return {
      labels: Object.keys(monthlyData),
      datasets: [
        {
          label,
          data: Object.values(monthlyData),
          backgroundColor: label === 'Расходы' ? 'rgba(239, 68, 68, 0.7)' : 'rgba(34, 197, 94, 0.7)',
          borderColor: label === 'Расходы' ? 'rgb(239, 68, 68)' : 'rgb(34, 197, 94)',
          borderWidth: 1,
          borderRadius: 5,
        },
      ],
    };
  };
  
  export const getChartOptions = (title) => ({
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { position: 'top' },
      title: {
        display: true,
        text: title,
        font: { size: 18, weight: '600' },
        color: '#111827',
      },
      tooltip: {
        callbacks: {
          label: (context) => `${context.dataset.label}: ${new Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB' }).format(context.parsed.y)}`,
        },
        backgroundColor: '#1f2937',
        titleFont: { size: 14, weight: 'bold' },
        bodyFont: { size: 12 },
        padding: 10,
      }
    },
    scales: {
      x: {
        ticks: { color: '#4b5563' },
        grid: { display: false },
      },
      y: {
        ticks: { color: '#4b5563' },
        grid: { color: '#e5e7eb' },
      }
    }
  });