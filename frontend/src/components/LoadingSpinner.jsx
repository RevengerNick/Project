import React from 'react';

const LoadingSpinner = () => {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-slate-50">
      <div className="w-16 h-16 border-4 border-dashed rounded-full animate-spin border-blue-500"></div>
      <p className="mt-4 text-lg font-medium text-slate-600">Загрузка финансовых данных...</p>
    </div>
  );
};

export default LoadingSpinner;