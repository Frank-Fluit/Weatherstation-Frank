import React, { useState } from 'react';

const GetLocalWeather = () => {
  const [latitude, setLatitude] = useState<string>('');
  const [longitude, setLongitude] = useState<string>('');
   const [data, setData] = useState<string | null>(null);


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

      <h2>Find local weather using coordinates</h2>
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
      <button onClick={handleRequest}>GetLocalWeather</button>
        {data}

    </div>
  );
};

export default GetLocalWeather;