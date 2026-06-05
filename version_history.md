# Brake System Analysis Tool - Changelog

All notable changes to this project will be documented in this file.

---

## Version 1.1.0 - Multi-Piston Support Update

Date: 05 June 2026

### Overview

Major update introducing multi-piston caliper support, enhanced brake system modeling, improved GUI organization, and tire lock-up prediction capabilities.

### Features Added

* Multi-piston caliper support
* Independent front and rear piston configurations
* Front and rear brake bias calculations
* Hydraulic line pressure calculations
* Caliper clamp force calculations
* Brake torque calculations
* Tire grip limitation analysis
* Front and rear lock-up prediction
* Dynamic weight transfer calculations
* Improved GUI layout
* Structured results display

### Inputs Added

* Front piston count
* Rear piston count
* Front piston diameter
* Rear piston diameter
* Tire friction coefficient
* Front weight distribution
* Front brake pad friction coefficient
* Rear brake pad friction coefficient
* Front brake balance percentage

### Outputs Added

* Front hydraulic pressure
* Rear hydraulic pressure
* Front clamp force
* Rear clamp force
* Front brake torque
* Rear brake torque
* Front brake bias
* Rear brake bias
* Available tire grip
* Required tire force
* Front lock-up prediction
* Rear lock-up prediction

### Improvements

* More realistic Formula Student brake system modeling
* Improved user interface organization
* Enhanced calculation visibility
* Better support for brake system design studies

### Remaining Limitations

* No brake bias optimization
* No aerodynamic effects
* No thermal analysis
* No tire utilization percentage
* No graphical visualizations
* Assumes equal piston diameters within each caliper

---

## Version 1.0.0 - Initial Release

Date: 04 June 2026

### Overview

First functional version of the Brake System Analysis Tool developed for Formula Student brake system calculations.

### Features Added

* Vehicle parameter input interface
* Static and dynamic axle load calculations
* Longitudinal weight transfer calculations
* Brake force estimation
* Brake torque calculations
* Pedal force estimation
* Basic hydraulic brake system calculations

### Inputs

* Vehicle mass
* Wheelbase
* Center of gravity height
* Tire radius
* Master cylinder diameter
* Caliper piston diameter
* Pedal ratio

### Outputs

* Front axle load
* Rear axle load
* Weight transfer
* Brake force
* Brake torque
* Required pedal effort

### Limitations

* Assumes single-piston calipers
* No brake bias optimization
* No aerodynamic effects
* No thermal analysis
* No tire grip limitations
* No lock-up prediction
* No graphical visualizations

### Notes

This release serves as the foundation for future development toward a comprehensive Formula Student brake system design and optimization tool.

---

## Planned Version 1.2.0

### Target Features

* Tire utilization analysis
* Brake bias optimization
* Recommended brake balance settings
* Automated setup suggestions
* Additional validation checks

---

## Planned Version 2.0.0

### Target Features

* Aerodynamic downforce integration
* Speed-dependent load transfer
* Advanced vehicle dynamics modeling
* Dynamic brake bias recommendations

---

## Planned Version 3.0.0

### Target Features

* Brake thermal analysis
* Rotor temperature estimation
* Brake fade risk prediction

---

## Planned Version 4.0.0

### Target Features

* Interactive graphs
* Tire utilization plots
* Brake bias plots
* Pedal force vs deceleration graphs
* Design optimization dashboard
