import { useState } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';

function App() {
  const [count, setCount] = useState(0);
  const [jsonResponse, setJsonResponse] = useState(null);
  const [makeUserResponse, setMakeUserResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [userData, setUserData] = useState({
    username: '',
    password: '',
    email: '',
  });

  async function getHello() {
    try {
      const response = await fetch("api/users/hello/", {
        method: "GET",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
      });

      if (response.ok) {
        const jsonresponse = await response.json();
        setJsonResponse(jsonresponse.message);
      } else {
        console.error(`HTTP error! Status: ${response.status}`);
      }
    } catch (error) {
      console.error('Fetch error:', error);
    }
  }

  async function postData() {
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
        setMakeUserResponse(makeUserResponse.message);
      } else {
        console.error(`HTTP error! Status: ${response.status}`);
      }
    } catch (error) {
      console.error('Fetch error:', error);
    } finally {
      setLoading(false);
    }
  }

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setUserData((prevUserData) => ({
      ...prevUserData,
      [name]: value,
    }));
  };

  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is this {count}
        </button>

        <button onClick={() => getHello()}>
          click this to test the http request
        </button>

        <label>
          Username:
          <input
            type="text"
            name="username"
            value={userData.username}
            onChange={handleInputChange}
          />
        </label>
        <label>
          Password:
          <input
            type="password"
            name="password"
            value={userData.password}
            onChange={handleInputChange}
          />
        </label>
        <label>
          Email:
          <input
            type="email"
            name="email"
            value={userData.email}
            onChange={handleInputChange}
          />
        </label>
        <button onClick={() => postData()} disabled={loading}>
          {loading ? 'Loading...' : 'Click to test the HTTP POST request'}
        </button>

        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
      <p>
        This is the result of the get request {jsonResponse}
      </p>
    </>
  );
}

export default App;
