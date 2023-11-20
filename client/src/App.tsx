import raincloud from '/raincloud.png'
import './App.css';
import CsvUploadForm from './components/CsvUploadForm';
import UserRegistrationForm from './components/UserRegistrationForm';

function App() {

  return (
    <>

      <h1 className="mb-4 text-8xl font-semibold">Personal Weather station</h1>

        <img src={raincloud}
           style={{ width: '300px', height: 'auto' }}>
        </img>

      <h2>Log, compare and analyse your weatherdata using our personal accounts!</h2>

      <div className="card">

        <UserRegistrationForm />

        <CsvUploadForm />

      </div>

    </>
  );
}

export default App;
