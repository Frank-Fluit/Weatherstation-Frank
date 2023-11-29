import React, { useState, ChangeEvent, FormEvent } from 'react';

const CorrelationCalculation: React.FC = () => {
  const [csvFile1, setCsvFile1] = useState<File | null>(null);
  const [csvFile2, setCsvFile2] = useState<File | null>(null);
  const [message, setMessage] = useState<string | null>(null);
  const [data, setData] = useState<string | null>(null);

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>, fileNumber: number) => {
    const file = e.target.files?.[0];
    if (fileNumber === 1) {
      setCsvFile1(file || null);
    } else {
      setCsvFile2(file || null);
    }
  };

  const handleFormSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (csvFile1 && csvFile2) {
      const formData = new FormData();
      formData.append('csv_file1', csvFile1);
      formData.append('csv_file2', csvFile2);

      try {
        const response = await fetch("api/dataprocessing/correlation/", {
          method: 'POST',
          body: formData,
        });

        if (response.ok) {
          const data = await response.json();
          setData(data);
          setMessage(data.message);
        } else {
          const errorData = await response.json();
          setMessage(`Error: ${errorData.error}`);
        }
      } catch (error) {
        console.error('Error:', error);
        setMessage('An error occurred while processing the request.');
      }
    }
  };

  return (
    <div className="my-4">
      <h2 className="text-xl font-semibold">Correlation calculation</h2>
      <form onSubmit={handleFormSubmit}>
        <input
          type="file"
          accept=".csv"
          onChange={(e) => handleFileChange(e, 1)}
          className="mt-2"
        />
        <input
          type="file"
          accept=".csv"
          onChange={(e) => handleFileChange(e, 2)}
          className="mt-2"
        />
        <button
          type="submit"
          className="bg-blue-500 text-white px-4 py-2 mt-2 rounded"
        >
          Upload CSVs for correlation calculation
        </button>
      </form>

      {message && <div className="mt-4">{message}</div>}

      {data && (
        <div className="mt-4" style={{ textAlign: 'left' }}>
          <h3>Data:</h3>
          <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
      )}

    </div>
  );
};

export default CorrelationCalculation;
