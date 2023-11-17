import { useState } from 'react';
// import reactLogo from './assets/react.svg';
//import viteLogo from '/vite.svg';
import raincloud from '/raincloud.png'
import './App.css';

import CsvUploadForm from './components/CsvUploadForm';

function App() {

  const [, setMakeUserResponse] = useState(null);
  const [stats,setstats] = useState(null)
  const [loading, setLoading] = useState(false);
  const [userData, setUserData] = useState({
    username: '',
    password: '',
    email: '',
  });





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


  const handleInputChange = (e: { target: { name: any; value: any; }; }) => {
    const { name, value } = e.target;
    setUserData((prevUserData) => ({
      ...prevUserData,
      [name]: value,
    }));
  };

  return (
    <>

      <h1 className="mb-4 text-8xl font-semibold">Personal Weather station</h1>

      <img src={raincloud}
      style={{ width: '300px', height: 'auto' }}>

      </img>


      <h2>Log, compare and analyse your weatherdata using our personal accounts!</h2>
      <div className="card">

        <h3> Make an account down below</h3>




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
        <br></br>



        <button onClick={() => postData()} disabled={loading}>
          {loading ? 'Loading...' : 'Register'}
        </button>

        <br></br>



        <h3> Do you already have an account? Login down below please!</h3>

                <label>
          Username:
          <input
            type="text"
            name="username"
          />
        </label>

        <label>
          Password:
          <input
            type="password"
            name="password"
          />
        </label>

        <br></br>

        <button onClick={() => postData()} disabled={loading}>
          {loading ? 'Loading...' : 'login'}
        </button>


        <CsvUploadForm />


      </div>


    </>
  );
}

export default App;
