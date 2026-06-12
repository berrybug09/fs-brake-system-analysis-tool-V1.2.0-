# Formula Student Brake System Analysis Tool [V2.0.0]

A brake system analysis tool developed for Formula Student vehicles using React, FastAPI, and Python.

This project originally started as a Tkinter desktop application. After spending far too much time fighting GUI limitations, I decided to rebuild the entire thing using a React frontend and a FastAPI backend.

The goal of the tool is simple: take a set of vehicle and brake system parameters and quickly evaluate how the braking system will behave before ever touching the car.

It's designed to calculate brake forces, brake bias, tire utilization, vehicle deceleration, and lock-up tendencies while providing recommendations to help improve the setup.

As the project grows, I plan to keep adding more detailed vehicle dynamics and brake system modelling features whenever I find the time.

---

## Current Features

### Hydraulic System Analysis

* Front and rear hydraulic pressure calculations
* Multi-piston caliper support
* Caliper clamp force calculations
* Master cylinder sizing analysis

### Braking Performance

* Brake torque calculations
* Front and rear brake bias analysis
* Ideal brake bias estimation
* Brake bias error calculations
* Automated setup recommendations

### Vehicle Dynamics

* Vehicle deceleration estimation
* Dynamic weight transfer calculations
* Dynamic axle load calculations
* Tire utilization analysis
* Front and rear lock-up prediction

### User Interface

* React frontend
* FastAPI backend
* Structured engineering workflow
* Split input and results layout
* Desktop-style design philosophy

---

## Technology Stack

### Frontend

* React
* JavaScript
* CSS

### Backend

* FastAPI
* Python

### Communication

* Axios
* REST API

---

## Development Roadmap

### Vehicle Dynamics

* [x] Tire utilization analysis
* [x] Brake bias optimization
* [x] Automated setup recommendations
* [ ] Aerodynamic downforce integration
* [ ] Speed-dependent load transfer
* [ ] Advanced vehicle dynamics modelling

### Thermal Analysis

* [ ] Rotor temperature estimation
* [ ] Brake fade assessment
* [ ] Heat generation calculations

### Visualization

* [ ] Tire utilization plots
* [ ] Brake bias plots
* [ ] Pedal force vs deceleration graphs
* [ ] Interactive performance visualizations

### Engineering Enhancements

* [ ] Pedal travel calculation
* [ ] Master cylinder stroke analysis
* [ ] Brake efficiency calculations
* [ ] Brake system validation tools

---

## Getting It Running

### 1. Clone the repository

```terminal
git clone <repo-url>
cd Formula-Student-Brake-System-Tool
```

### 2. Setup the backend

```terminal
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate

pip install -r requirements.txt
```

Start the backend server:

```terminal
uvicorn main:app --reload
```

The API will run on:

```text
http://localhost:8000
```

### 3. Setup the frontend

Open a new terminal:

```terminal
cd frontend

npm install
npm run dev
```

The frontend will run on:

```text
http://localhost:5173
```

### 4. Open the application

Open your browser and navigate to:

```text
http://localhost:5173
```

The frontend will automatically communicate with the FastAPI backend.

---

## Current Limitations

This tool is intended for early-stage brake system analysis and design validation.

It does not replace physical testing, data acquisition, driver feedback, or detailed vehicle simulations.

The vehicle dynamics model is intentionally simplified to keep calculations fast and easy to interpret.

As more advanced modelling features are added, the accuracy and scope of the analysis will continue to improve.

---

## Why I Built This

I originally built this as a way to combine software development with Formula Student engineering.

Most of my experience has been on the mechanical side of Formula Student projects, so this became an opportunity to learn modern web development while building something I would actually use.

Instead of creating another generic portfolio project, I wanted something that solved a real engineering problem and could continue growing over time.

---

## Future Plans

The long-term goal is to turn this into a more complete brake system design and validation platform.

That includes:

* More advanced vehicle dynamics models
* Brake thermal analysis
* Data visualization tools
* Setup optimization features
* Additional engineering validation checks

There's still a lot left to build, but that's part of the fun.
