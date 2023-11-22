import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import raincloud from '/raincloud.png'
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


// function App() {
//
//   return (
//     <>
//
//       <h1 className="mb-4 text-8xl font-semibold">Personal Weather station</h1>
//
//         <img src={raincloud}
//            style={{ width: '300px', height: 'auto' }}>
//         </img>
//
//       <h2>Log, compare and analyse your weatherdata using our personal accounts!</h2>
//
//       <div className="card">
//
//         <LoginPage/>
//
//         <UserRegistrationForm />
//
//         <CsvUploadForm />
//
//       </div>
//
//     </>
//   );
// }
//
// export default App;
