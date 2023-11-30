import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import UserProfile from './components/UserProfile';
import UserRegistrationForm from './components/UserRegistrationForm';
import LoginPage from "./components/LoginPage.tsx";


const App: React.FC = () => {
  return (

    <Router>
      <Routes>
         <Route
          path="/"
          element={
            <div>
              <LoginPage />
              <UserRegistrationForm />

            </div>
          }
        />
           <Route path="/userprofile" element={<UserProfile />} />
      </Routes>
    </Router>
  );
};

export default App;


