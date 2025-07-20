import React from 'react';

const FinancialCard = ({ title, value, icon, colorClass }) => {
  return (
    <div className="bg-white p-6 rounded-2xl shadow-sm hover:shadow-xl transition-shadow duration-300 flex items-center space-x-4">
      <div className={`p-3 rounded-full ${colorClass.bg}`}>
        {icon}
      </div>
      <div>
        <h3 className="text-sm font-medium text-gray-500">{title}</h3>
        <p className={`text-2xl font-bold ${colorClass.text}`}>{value}</p>
      </div>
    </div>
  );
};

export default FinancialCard;