import React from 'react';
import { FiAlertTriangle } from 'react-icons/fi';

const ErrorMessage = ({ message }) => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-red-50">
      <div className="max-w-md w-full bg-white p-8 rounded-2xl shadow-lg border-l-4 border-red-500 flex items-start space-x-4">
        <FiAlertTriangle className="h-8 w-8 text-red-500 flex-shrink-0" />
        <div>
          <h2 className="text-xl font-bold text-red-700 mb-1">Произошла ошибка</h2>
          <p className="text-slate-700">Не удалось загрузить данные. Пожалуйста, попробуйте обновить страницу.</p>
          <p className="mt-3 text-sm text-slate-500 bg-slate-100 p-2 rounded-md">
            Детали: {message}
          </p>
        </div>
      </div>
    </div>
  );
};

export default ErrorMessage;