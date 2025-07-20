import React from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const BarChart = ({ data, options }) => {
  return (
    <div className="bg-white p-6 rounded-2xl shadow-sm h-96">
      <Bar data={data} options={options} />
    </div>
  );
};

export default BarChart;