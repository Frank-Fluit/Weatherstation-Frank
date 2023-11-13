import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const [jsonResponse, setJsonResponse] = useState(null);
  const [makeUserResponse, setMakeUserResponse] = useState(null);

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  


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

    const userData = {
      username: 'example_user2',
      password: 'secure_password2',
      email: 'user@example2.com',
    };

    try {
      setLoading(true);
      setError(null);
  
      const response = await fetch("api/users/register/", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        // You can include a JSON payload in the body if needed
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
  )
}

export default App
