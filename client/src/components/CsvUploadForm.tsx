// CsvUploadForm.tsx
import React, { useState, ChangeEvent, FormEvent } from 'react';

const CsvUploadForm: React.FC = () => {
  const [csvFile, setCsvFile] = useState<File | null>(null);
  const [message, setMessage] = useState<string | null>(null);

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    setCsvFile(file || null);
  };

  const handleFormSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    // Perform actions with the CSV file, such as sending it to the server
    if (csvFile) {
      const formData = new FormData();
      formData.append('csv_file', csvFile);

      try {
        const response = await fetch("api/dataprocessing/csv/", {
          method: 'POST',
          body: formData,
        });

        if (response.ok) {
          const data = await response.json();
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
      <h2 className="text-xl font-semibold">CSV Upload Form</h2>
      <form onSubmit={handleFormSubmit}>
        <input
          type="file"
          accept=".csv"
          onChange={handleFileChange}
          className="mt-2"
        />
        <button
          type="submit"
          className="bg-blue-500 text-white px-4 py-2 mt-2 rounded"
        >
          Upload CSV
        </button>
      </form>

      {message && <div className="mt-4">{message}</div>}
    </div>
  );
};

export default CsvUploadForm;