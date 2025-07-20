import React from 'react';

const RawDataViewer = ({ title, data }) => {
  return (
    <div className="bg-white p-6 rounded-2xl shadow-sm">
      <h3 className="text-xl font-semibold text-slate-800 mb-4">{title}</h3>
      <pre className="bg-slate-800 text-green-300 p-4 rounded-lg overflow-x-auto text-sm custom-scrollbar">
        {JSON.stringify(data, null, 2)}
      </pre>
    </div>
  );
};

export default RawDataViewer;