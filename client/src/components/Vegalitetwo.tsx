import React, {useState} from 'react';
import { VegaLite } from 'react-vega';

const Vegalitetwo = () => {

  const [latitude, setLatitude] = useState<string>('');
  const [longitude, setLongitude] = useState<string>('');
  const [data, setData] = useState<string | null>(null);
  const [city, setCity] = useState('');
  const [countryCode, setCountryCode] = useState('');





  const spec = {
    mark: { type: 'line' },
    encoding: {
      x: { field: 'time', type: 'temporal', title: 'Time' },
      y: { field: 'value', type: 'quantitative', title: 'Temp (C)' },
    },
    data: { values: data },
    width: 400,
    height: 300,
    title: 'Temperature prediction for next 5 days',
  };

  const handleRequest = async () => {
    try {
      const response = await fetch("api/dataprocessing/get_weather_pred_loc/", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ city, countryCode }),
      });

      if (response.ok) {
        const data = await response.json();
        setData(data)

        console.log("request succesful");


      } else {
        console.error('request failed.');
      }
    } catch (error) {
      console.error('Error during request:', error);
    }
  };

  return (
    <div>
      <h2>Find weather forecast using location name</h2>
      <VegaLite spec={spec} />
          <div>


      <label style={{ fontWeight: 'bold' }}>
        City:
        <input type="text" value={city} onChange={(e) => setCity(e.target.value)} />
      </label>
      <br />
      <label style={{ fontWeight: 'bold' }}>
        countryCode:
        <input type="text" value={countryCode} onChange={(e) => setCountryCode(e.target.value)} />
      </label>
      <br />
      <button onClick={handleRequest}>TempPrediction</button>


    </div>
    </div>

  );
};

export default Vegalitetwo;
