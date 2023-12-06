import React, { useState } from 'react';

const UserRegistrationForm: React.FC = () => {
  const [loading, setLoading] = useState(false);
  const [userData, setUserData] = useState({
    username: '', password: '', email: '',});

  const createNewUser = async () => {
    try {
      setLoading(true);

      const response = await fetch("api/users/register/", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify(userData),
      });

      if (response.ok) {
        const makeUserResponse = await response.json();
        console.log('User registration successful:', makeUserResponse);

      } else {
        console.error(`HTTP error! Status: ${response.status}`);

      }
    } catch (error) {
      console.error('Fetch error:', error);
    } finally {
      setLoading(false);
    }
  };







    const testHelloEndpoint = async () => {
    try {


      const response = await fetch("api/users/hello/", {
        method: "GET",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
      });

      if (response.ok) {

        console.log('hello was retrieved');

      } else {
        console.error(`HTTP error! Status: ${response.status}`);

      }
    } catch (error) {
      console.error('Fetch error:', error);
    }
  };







  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setUserData((prevUserData) => ({
      ...prevUserData,
      [name]: value,
    }));
  };

  return (
    <div>
      <h3>Make an account down below</h3>
      <label style={{ fontWeight: 'bold' }}>
        Username:
        <input
          type="text"
          name="username"
          value={userData.username}
          onChange={handleInputChange}
        />
      </label>

      <label style={{ fontWeight: 'bold' }}>
        Password:
        <input
          type="password"
          name="password"
          value={userData.password}
          onChange={handleInputChange}
        />
      </label>

      <label style={{ fontWeight: 'bold' }}>
        Email:
        <input
          type="email"
          name="email"
          value={userData.email}
          onChange={handleInputChange}
        />
      </label>

      <br />
      <button onClick={createNewUser} disabled={loading}>
        {loading ? 'Loading...' : 'Register'}
      </button>




    </div>
  );
};

export default UserRegistrationForm;