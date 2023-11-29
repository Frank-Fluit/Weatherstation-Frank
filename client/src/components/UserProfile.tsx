import React from 'react';
import SaveDataToDatabase from "./SaveDataToDatabase.tsx";
import DataAnalysis from "./DataAnalysis.tsx";
import DataComparedToDatabaseData from "./DataComparedToDatabaseData.tsx";
import CorrelationCalculation from "./CorrelationCalculation.tsx";

const UserProfile: React.FC = () => {

  return (
    <div className="my-4">
      <h2 className="text-xl font-semibold">UserProfile</h2>
        <DataAnalysis />
        <SaveDataToDatabase />
        <DataComparedToDatabaseData/>
        <CorrelationCalculation/>
    </div>
  );
};

export default UserProfile;