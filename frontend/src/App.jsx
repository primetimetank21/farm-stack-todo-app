import { useState, useEffect } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import api from "./api";

function App() {
  const [count, setCount] = useState(0);

  const healthCheck = async () => {
    try {
      const response = await api.get("/");
      // console.log(response.data);
      // return response.data;
      return response;
    } catch (error) {
      console.error(error);
    }
  };

  // Try to fetch data from the backend -- health check
  useEffect(() => {
    if (count !== 0) {
      healthCheck()
        .then((response) => {
          console.log(`Response: ${JSON.stringify(response)}`);
          // console.log(`Response Data: ${JSON.stringify(response)}`);
          // response.json()
          return response.data;
        })
        .then((data) => console.log(data))
        .catch((error) => console.error(error));
    }
  }, [count]);

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  );
}

export default App;
