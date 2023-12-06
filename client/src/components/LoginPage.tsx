import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link, useNavigate } from 'react-router-dom';
import raincloud from '/raincloud.png'
import UserRegistrationForm from "./UserRegistrationForm.tsx";
import SaveDataToDatabase from "./SaveDataToDatabase.tsx";


const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const navigate = useNavigate(); // Use the correct hook


  const handleLogin = async () => {
    try {
      const response = await fetch('api/api/token/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      if (response.ok) {
        const data = await response.json();

        console.log('Login successful. Token:', data.token);
        navigate('/userprofile');


      } else {
        console.error('Login failed.');
      }
    } catch (error) {
      console.error('Error during login:', error);
    }
  };

  return (
    <div>

      <h1 className="mb-4 text-8xl font-semibold headingBackground">
        Personal Weather Station
      </h1>

         <img src={raincloud} alt="Raincloud" className="raincloudImage" />

      <h2>Log, compare and analyse your weatherdata using our personal accounts!</h2>
      <label style={{ fontWeight: 'bold' }}>
        Username:
        <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
      </label>
      <br />
      <label style={{ fontWeight: 'bold' }}>
        Password:
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      </label>
      <br />
      <button onClick={handleLogin}>Login</button>



    </div>
  );
};

export default Login;