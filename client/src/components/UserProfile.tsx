import React from 'react';
import SaveDataToDatabase from "./SaveDataToDatabase.tsx";
import DataAnalysis from "./DataAnalysis.tsx";

const UserProfile: React.FC = () => {

  return (
    <div className="my-4">
      <h2 className="text-xl font-semibold">UserProfile</h2>
      <DataAnalysis />
      <SaveDataToDatabase />
    </div>
  );
};

export default UserProfile;