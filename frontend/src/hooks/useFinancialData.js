import { useState, useEffect } from 'react';

export const useFinancialData = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchFinancialData = async () => {
      setLoading(true);
      try {
        const response = await fetch('/api/financial_summary');
        if (!response.ok) {
          throw new Error(`Ошибка сети: ${response.status}`);
        }
        const result = await response.json();
        setData(result);
      } catch (e) {
        console.error("Ошибка при получении данных:", e);
        setError(e.message);
      } finally {
        setLoading(false);
      }
    };

    fetchFinancialData();
  }, []);

  return { data, loading, error };
};