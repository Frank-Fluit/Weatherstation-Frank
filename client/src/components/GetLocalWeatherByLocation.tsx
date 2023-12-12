import React, { useState } from 'react';



const GetLocalWeatherByLocation = () => {
  const [city, setCity] = useState('');
  const [countryCode, setCountryCode] = useState('');
  const [data, setData] = useState<string | null>(null);


  const handleRequest = async () => {
    try {
      const response = await fetch("api/dataprocessing/get_weather_based_on_loc/", {
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

      <h2>Find local weather using City and Country input</h2>
      <label style={{ fontWeight: 'bold' }}>
         City/Village:
        <input type="text" value={city} onChange={(e) => setCity(e.target.value)} />
      </label>
      <br />
      <label style={{ fontWeight: 'bold' }}>
        Country Code:
        <input type="text" value={countryCode} onChange={(e) => setCountryCode(e.target.value)} />
      </label>
      <br />
      <button onClick={handleRequest}>GetLocalWeather</button>
        {data}

    </div>
  );
};

export default GetLocalWeatherByLocation;

