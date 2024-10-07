import Header from "./components/Header"
import Welcome from "./components/Welcome";
import Weather from "./components/Weather";

// import { useState } from "react";
// import * as ReactDOMClient from "react-dom/client";
// import axios from "axios";
//
// function App() {
//   const [city, setCity] = useState(null);
//
//   const fetchData = async () => {
//     const response = await axios.get(
//       "http://localhost:8000/api/?format=json"
//     );
//
//     setCity(response.data);
//   };
//
//   return (
//     <div className="App">
//       <h1>Game of Thrones Books</h1>
//       <h2>Fetch a list from an API and display it</h2>
//
//       {/* Fetch data from API */}
//       <div>
//         <button className="fetch-button" onClick={fetchData}>
//           Fetch Data
//         </button>
//         <br />
//       </div>
//
//       {/* Display data from API */}
//       <div className="cities">
//         {city &&
//           city.map((city, index) => {
//             const cleanedDate = new Date(city.released).toDateString();
//             const cities = city.name.join(", ");
//
//             return (
//               <div className="city" key={index}>
//                 <h3>City {index + 1}</h3>
//                 <h2>{city.name}</h2>
//
//                 <div className="details">
//                   <p>{cities}</p>
//                   <p>{cleanedDate}</p>
//                 </div>
//               </div>
//             );
//           })}
//       </div>
//     </div>
//   );
// }
//
// const rootElement = ReactDOMClient.createRoot(document.getElementById("site"));
// rootElement.render(<App />);
