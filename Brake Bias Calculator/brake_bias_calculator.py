import math

# -----------------------------
# FUNCTIONS
# -----------------------------

def circle_area(diameter):
    return math.pi * (diameter / 2) ** 2


def line_pressure(force, area):
    return force / area


def clamp_force(pressure, piston_area):
    return pressure * piston_area

def vehicle_deceleration(force, mass):
    return force / mass

def wheel_force(brake_torque, tire_radius):
    return brake_torque / tire_radius

def brake_torque(clamp_force, rotor_radius, mu):
    return clamp_force * rotor_radius * mu

def weight_transfer(mass, deceleration, cg_height, wheelbase):
    return (mass * deceleration * cg_height) / wheelbase


# -----------------------------
# INPUTS
# -----------------------------


pedal_force = float(input("Enter pedal force (N): "))
pedal_ratio = float(input("Enter pedal ratio: "))

front_mc_diameter = float(input("Enter FRONT master cylinder diameter (mm): "))
rear_mc_diameter = float(input("Enter REAR master cylinder diameter (mm): "))

front_caliper_diameter = float(input("Enter FRONT caliper piston diameter (mm): "))
rear_caliper_diameter = float(input("Enter REAR caliper piston diameter (mm): "))

front_rotor_radius = float(input("Enter FRONT effective rotor radius (mm): "))
rear_rotor_radius = float(input("Enter REAR effective rotor radius (mm): "))

front_balance_percent = float(input("Enter front balance bar percentage (%): "))

vehicle_mass = float(input("Enter vehicle mass (kg): "))

front_tire_radius = float(input("Enter FRONT tire radius (mm): "))
rear_tire_radius = float(input("Enter REAR tire radius (mm): "))

front_pad_mu = float(input("Enter brake pad friction coefficient: "))
rear_pad_mu = float(input("Enter brake pad friction coefficient: "))

tire_mu = float(input("Enter tire-road friction coefficient: "))

front_static_weight_percent = float(input("Enter front static weight distribution (%): "))

wheelbase = float(input("Enter wheelbase (m): "))
cg_height = float(input("Enter CG height (m): "))

# -----------------------------
# CALCULATIONS
# -----------------------------


front_mc_area = circle_area(front_mc_diameter)
rear_mc_area = circle_area(rear_mc_diameter)

front_caliper_area = circle_area(front_caliper_diameter)
rear_caliper_area = circle_area(rear_caliper_diameter)

pushrod_force = pedal_force * pedal_ratio

front_force = pushrod_force * front_balance_percent / 100
rear_force = pushrod_force - front_force

front_line_pressure = line_pressure(front_force, front_mc_area)
rear_line_pressure = line_pressure(rear_force, rear_mc_area)

front_clamp_force = clamp_force(front_line_pressure, front_caliper_area)
rear_clamp_force = clamp_force(rear_line_pressure, rear_caliper_area)

front_brake_torque = brake_torque(front_clamp_force, front_rotor_radius, front_pad_mu)
rear_brake_torque = brake_torque(rear_clamp_force, rear_rotor_radius, rear_pad_mu)

total_torque = (front_brake_torque) + (rear_brake_torque)

front_bias = (front_brake_torque / total_torque) * 100
rear_bias = (rear_brake_torque / total_torque) * 100

front_wheel_force = wheel_force(front_brake_torque, front_tire_radius)
rear_wheel_force = wheel_force(rear_brake_torque, rear_tire_radius)

total_brake_force = ((2*front_wheel_force) + (2*rear_wheel_force))
deceleration = vehicle_deceleration(total_brake_force, vehicle_mass)

deceleration_g = deceleration / 9.81

dynamic_weight_transfer = weight_transfer(vehicle_mass, deceleration, cg_height,wheelbase)

g = 9.81

vehicle_weight = vehicle_mass * g

front_static_load = (vehicle_weight * front_static_weight_percent / 100)
rear_static_load = (vehicle_weight - front_static_load)

dynamic_front_load = (front_static_load + dynamic_weight_transfer)
dynamic_rear_load = (rear_static_load - dynamic_weight_transfer)

front_available_brake_force = (tire_mu * dynamic_front_load)

rear_available_brake_force = (tire_mu * dynamic_rear_load)

front_required_brake_force = (2 * front_wheel_force)

rear_required_brake_force = (2 * rear_wheel_force)

if front_required_brake_force > front_available_brake_force:
    front_lockup = "YES"
else:
    front_lockup = "NO"

if rear_required_brake_force > rear_available_brake_force:
    rear_lockup = "YES"
else:
    rear_lockup = "NO"


# -----------------------------
# RESULTS
# -----------------------------


print("\n===== RESULTS =====")

print(f"Pushrod Force = {pushrod_force:.2f} N")

print(f"Front Line Pressure = {front_line_pressure:.2f} N/mm²")
print(f"Rear Line Pressure = {rear_line_pressure:.2f} N/mm²")

print(f"Front Clamp Force = {front_clamp_force:.2f} N")
print(f"Rear Clamp Force = {rear_clamp_force:.2f} N")

print(f"Front Brake Torque = {front_brake_torque:.2f} Nmm")
print(f"Rear Brake Torque = {rear_brake_torque:.2f} Nmm")

print(f"Front Bias = {front_bias:.2f}%")
print(f"Rear Bias = {rear_bias:.2f}%")

print(f"Front Master Cylinder Force = {front_force:.2f} N")
print(f"Rear Master Cylinder Force = {rear_force:.2f} N")

print(f"Front Wheel Force = {front_wheel_force:.2f} N")
print(f"Rear Wheel Force = {rear_wheel_force:.2f} N")

print(f"Total Brake Force = {total_brake_force:.2f} N")

print(f"Deceleration = {deceleration:.2f} m/s²")
print(f"Deceleration = {deceleration_g:.2f} g")

print(f"Dynamic Weight Transfer = {dynamic_weight_transfer:.2f} N")

print(f"Dynamic Front Load = {dynamic_front_load:.2f} N")
print(f"Dynamic Rear Load = {dynamic_rear_load:.2f} N")

print(f"Front Available Grip = {front_available_brake_force:.2f} N")
print(f"Rear Available Grip = {rear_available_brake_force:.2f} N")

print(f"Front Required Brake Force = {front_required_brake_force:.2f} N")
print(f"Rear Required Brake Force = {rear_required_brake_force:.2f} N")

print(f"Front Lock-Up Risk = {front_lockup}")
print(f"Rear Lock-Up Risk = {rear_lockup}")