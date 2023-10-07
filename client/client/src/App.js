import logo from "./logo.svg";
import "./App.css";
import "./output.css";

function App() {
  return (
    // <div className="App">
    <div className="App">
      <form
        className="mt-8 mb-2 w-80 max-w-screen-lg sm:w-96"
        action="http://localhost:8080/login"
        method="post"
      >
        <div className="mb-4 flex flex-col gap-6">
          <p className="underline">Enter Login Info for LinkedIn:</p>
          <p>
            <input type="text" name="user" placeholder="username" />
          </p>
          <p>
            <input type="text" name="pass" placeholder="password" />
          </p>
          <p>
            <input type="submit" value="submit" />
          </p>
        </div>
      </form>
      <p>THIS THE APP</p>
    </div>
  );
}

export default App;
