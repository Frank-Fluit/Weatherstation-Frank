import React, {useState} from 'react';
import { VegaLite } from 'react-vega';

const Vegalite = () => {

  const [latitude, setLatitude] = useState<string>('');
  const [longitude, setLongitude] = useState<string>('');
  const [data, setData] = useState<string | null>(null);


  const timeSeriesData = [
    { time: '2023-01-01T00:00:00Z', value: 8 },
    { time: '2023-01-01T01:00:00Z', value: 9 },
    { time: '2023-01-01T02:00:00Z', value: 11 },
    { time: '2023-01-01T03:00:00Z', value: 12 },
    { time: '2023-01-01T04:00:00Z', value: 15 },

  ];


  const spec = {
    mark: { type: 'line' },
    encoding: {
      x: { field: 'time', type: 'temporal', title: 'Time' },
      y: { field: 'value', type: 'quantitative', title: 'Value' },
    },
    data: { values: timeSeriesData },
    width: 400,
    height: 300,
    title: 'Temperature prediction for next 5 days',
  };

    const handleRequest = async () => {
    try {
      const response = await fetch("api/dataprocessing/get_weather_based_on_lat_lon/", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ latitude, longitude }),
      });

      if (response.ok) {
        const data = await response.json();
        setData(data)


        console.log("request succesful");
        console.log(data)

      } else {
        console.error('request failed.');
      }
    } catch (error) {
      console.error('Error during request:', error);
    }
  };

  return (
    <div>
      <h2>Find weather forecast using coordinates</h2>
      <VegaLite spec={spec} />
          <div>


      <label style={{ fontWeight: 'bold' }}>
        Latitude:
        <input type="text" value={latitude} onChange={(e) => setLatitude(e.target.value)} />
      </label>
      <br />
      <label style={{ fontWeight: 'bold' }}>
        Longitude:
        <input type="text" value={longitude} onChange={(e) => setLongitude(e.target.value)} />
      </label>
      <br />
      <button onClick={handleRequest}>TempPrediction</button>
        {data}

    </div>
    </div>

  );
};

export default Vegalite;
