import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [message, setMessage] = useState("Loading...");

  const [inputs, setInputs] = useState({
    pedal_force: "",
    pedal_ratio: "",
    front_mc_diameter: "",
    rear_mc_diameter: "",
    front_piston_count: "",
    rear_piston_count: "",
    front_caliper_diameter: "",
    rear_caliper_diameter: "",
    front_rotor_radius: "",
    rear_rotor_radius: "",
    front_balance_percent: "",
    vehicle_mass: "",
    front_tire_radius: "",
    rear_tire_radius: "",
    front_pad_mu: "",
    rear_pad_mu: "",
    wheelbase: "",
    cg_height: "",
    tire_mu: "",
    front_static_weight_percent: "",
  });

  const [result, setResult] = useState(null);

  function handleChange(e) {
    setInputs({
      ...inputs,
      [e.target.name]: e.target.value,
    });
  }

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/")
      .then((response) => {
        setMessage(response.data.message);
      })
      .catch((error) => {
        console.error(error);
        setMessage("Failed to connect to backend");
      });
  }, []);

  async function calculate() {
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/calculate",
        Object.fromEntries(
          Object.entries(inputs).map(([key, value]) => [
            key,
            Number(value),
          ])
        )
      );

      setResult(response.data);
    } catch (error) {
      console.error(error);
    }
  }

  const columns = [
    [
      { name: "pedal_force", label: "Pedal Force (N)" },
      { name: "front_mc_diameter", label: "Front MC Diameter (mm)" },
      { name: "front_piston_count", label: "Front Piston Count" },
      { name: "front_rotor_radius", label: "Front Rotor Radius (mm)" },
      { name: "front_tire_radius", label: "Front Tire Radius (mm)" },
    ],

    [
      { name: "pedal_ratio", label: "Pedal Ratio" },
      { name: "rear_mc_diameter", label: "Rear MC Diameter (mm)" },
      { name: "rear_piston_count", label: "Rear Piston Count" },
      { name: "rear_rotor_radius", label: "Rear Rotor Radius (mm)" },
      { name: "rear_tire_radius", label: "Rear Tire Radius (mm)" },
    ],

    [
      { name: "vehicle_mass", label: "Vehicle Mass (kg)" },
      { name: "front_balance_percent", label: "Front Balance (%)" },
      { name: "front_caliper_diameter", label: "Front Piston Diameter (mm)" },
      { name: "wheelbase", label: "Wheelbase (m)" },
      { name: "front_pad_mu", label: "Front Pad Mu" },
    ],

    [
      { name: "tire_mu", label: "Tire Mu" },
      { name: "front_static_weight_percent", label: "Front Weight Distribution (%)" },
      { name: "rear_caliper_diameter", label: "Rear Piston Diameter (mm)" },
      { name: "cg_height", label: "CG Height (m)" },
      { name: "rear_pad_mu", label: "Rear Pad Mu" },
    ],
  ];

  return (
    <div className="app-container">
      <h1>Formula Student Brake System Analysis Tool</h1>

      <div className="input-grid">
        {columns.map((column, colIndex) => (
          <div key={colIndex} className="column">
            {column.map((field) => (
              <div key={field.name} className="input-row">
                <label>{field.label}</label>

                <input
                  type="number"
                  name={field.name}
                  value={inputs[field.name]}
                  onChange={handleChange}
                />
              </div>
            ))}
          </div>
        ))}
      </div>

      <button className="calculate-btn" onClick={calculate}>
        Calculate
      </button>

      {result && (
        <div className="results-box">
          <div className="results-header">
            <span>Hydraulic and Braking Results</span>
            <span>Vehicle and Lock-Up Results</span>
          </div>

          <div className="results-content">

            <div>

              <p>Pushrod Force: {result.pushrod_force.toFixed(2)} N</p>

              <p>Front Pressure: {result.front_pressure.toFixed(2)} N/mm²</p>
              <p>Rear Pressure: {result.rear_pressure.toFixed(2)} N/mm²</p>

              <p>Front Clamp Force: {result.front_clamp_force.toFixed(2)} N</p>
              <p>Rear Clamp Force: {result.rear_clamp_force.toFixed(2)} N</p>

              <p>Front Brake Torque: {result.front_brake_torque.toFixed(2)} Nmm</p>
              <p>Rear Brake Torque: {result.rear_brake_torque.toFixed(2)} Nmm</p>

              <p>Front Bias: {result.front_bias.toFixed(2)} %</p>
              <p>Rear Bias: {result.rear_bias.toFixed(2)} %</p>

            </div>

            <div>

              <p>Deceleration: {result.deceleration_g.toFixed(2)} g</p>

              <p>Weight Transfer: {result.weight_transfer.toFixed(2)} N</p>

              <p>Dynamic Front Load: {result.dynamic_front_load.toFixed(2)} N</p>
              <p>Dynamic Rear Load: {result.dynamic_rear_load.toFixed(2)} N</p>

              <p>Front Available Grip: {result.front_available_grip.toFixed(2)} N</p>
              <p>Rear Available Grip: {result.rear_available_grip.toFixed(2)} N</p>

              <p>Front Required Force: {result.front_required_force.toFixed(2)} N</p>
              <p>Rear Required Force: {result.rear_required_force.toFixed(2)} N</p>

              <p>
                Front Tire Utilization:
                {" "}
                {result.front_utilization.toFixed(1)}%
                {" "}
                ({result.front_warning})
              </p>

              <p>
                Rear Tire Utilization:
                {" "}
                {result.rear_utilization.toFixed(1)}%
                {" "}
                ({result.rear_warning})
              </p>

              <p>Ideal Front Bias: {result.ideal_front_bias.toFixed(2)} %</p>

              <p>Bias Error: {result.bias_error.toFixed(2)} %</p>

              <p>Recommendation: {result.recommendation}</p>

              <p>Front Lock-Up Risk: {result.front_lockup}</p>

              <p>Rear Lock-Up Risk: {result.rear_lockup}</p>

            </div>

          </div>
        </div>
      )}
    </div>
  );
}

export default App;