import React from 'react';
import SaveDataToDatabase from "./SaveDataToDatabase.tsx";
import DataAnalysis from "./DataAnalysis.tsx";
import DataComparedToDatabaseData from "./DataComparedToDatabaseData.tsx";
import CorrelationCalculation from "./CorrelationCalculation.tsx";
import GetLocalWeather from "./GetLocalWeather.tsx";
import GetLocalWeatherByLocation from "./GetLocalWeatherByLocation.tsx";
import VegaLite from "./Vegalite.tsx";
import Vegalitetwo from "./Vegalitetwo.tsx";


const UserProfile: React.FC = () => {

  return (
    <div className="my-4">
      <h2 className="custom-text-size font-semibold">UserProfile</h2>
        <DataAnalysis />
        <SaveDataToDatabase />
        <DataComparedToDatabaseData/>
        <CorrelationCalculation/>
        <GetLocalWeather/>
        <GetLocalWeatherByLocation/>
      <br /><br />

        <VegaLite/>
      <Vegalitetwo/>

    </div>
  );
};

export default UserProfile;