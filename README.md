# Formula Student Brake System Analysis Tool [V2.0.0]

A brake system analysis tool developed for Formula Student vehicles.

Originally this project was built as a Tkinter desktop application but I faced tons of issues with the GUI and scalability so I migrated to a React + FastAPI architectur.
This tool helps evaluate brake system performance, brake bias, tire utilization, vehicle deceleration, and lock-up tendencies using common Formula Student brake system parameters.

---

## What Does It Do?

Give the tool your brake system and vehicle parameters, and it will calculate:

* Hydraulic line pressures
* Caliper clamp forces
* Brake torques
* Front and rear brake bias
* Vehicle deceleration
* Dynamic weight transfer
* Tire utilization
* Lock-up risk
* Brake balance recommendations

The goal is to quickly evaluate whether a brake setup is balanced, efficient, and suitable for a Formula Student vehicle.

---

## Current Features

### Hydraulic System Analysis

* Front and rear master cylinder sizing
* Multi-piston caliper support
* Front and rear hydraulic pressure calculations
* Front and rear clamp force calculations

### Braking Performance

* Brake torque calculations
* Brake bias calculations
* Adjustable brake balance analysis
* Ideal brake bias calculations
* Brake bias error calculations
* Automated brake setup recommendations

### Vehicle Dynamics

* Vehicle deceleration estimation
* Dynamic weight transfer calculations
* Dynamic axle load calculations
* Tire grip estimation
* Tire utilization analysis
* Front and rear lock-up prediction

### User Interface

* React frontend
* FastAPI backend
* Engineering-focused desktop-style layout
* Structured input sections
* Split results display

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

### Optimization & Visualisation

* [ ] Performance graphs
* [ ] Tire utilization plots
* [ ] Brake bias plots
* [ ] Pedal force vs deceleration plots

### Engineering Enhancements

* [ ] Pedal travel calculation
* [ ] Master cylinder stroke analysis
* [ ] Brake efficiency calculation
* [ ] Brake system validation tools

---

There's a lot I am yet to add but I will keep working on this from time to time so uh, yeah :D