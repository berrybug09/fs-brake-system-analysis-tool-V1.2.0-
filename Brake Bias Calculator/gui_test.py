import tkinter as tk
import math


# --------------------------------
# FUNCTIONS
# --------------------------------

def circle_area(diameter):
    return math.pi * (diameter / 2) ** 2


def line_pressure(force, area):
    return force / area


def clamp_force(pressure, piston_area):
    return pressure * piston_area


def brake_torque(clamp_force, rotor_radius, mu):
    return clamp_force * rotor_radius * mu


def wheel_force(brake_torque, tire_radius):
    return brake_torque / tire_radius


def vehicle_deceleration(force, mass):
    return force / mass


def weight_transfer(mass, deceleration, cg_height, wheelbase):
    return (mass * deceleration * cg_height) / wheelbase


# --------------------------------
# CALCULATE
# --------------------------------

def calculate():

    try:

        pedal_force = float(pedal_force_entry.get())
        pedal_ratio = float(pedal_ratio_entry.get())

        front_mc_diameter = float(front_mc_entry.get())
        rear_mc_diameter = float(rear_mc_entry.get())

        front_caliper_diameter = float(front_caliper_entry.get())
        rear_caliper_diameter = float(rear_caliper_entry.get())

        front_rotor_radius = float(front_rotor_entry.get())
        rear_rotor_radius = float(rear_rotor_entry.get())

        front_balance_percent = float(balance_entry.get())

        vehicle_mass = float(vehicle_mass_entry.get())

        front_tire_radius = float(front_tire_entry.get())
        rear_tire_radius = float(rear_tire_entry.get())

        front_pad_mu = float(front_pad_mu_entry.get())
        rear_pad_mu = float(rear_pad_mu_entry.get())

        wheelbase = float(wheelbase_entry.get())
        cg_height = float(cg_height_entry.get())

        tire_mu = float(tire_mu_entry.get())

        front_static_weight_percent = float(front_weight_dist_entry.get())


# ----------------------------
# CALCULATIONS
# ----------------------------


        front_mc_area = circle_area(front_mc_diameter)
        rear_mc_area = circle_area(rear_mc_diameter)

        front_caliper_area = circle_area(front_caliper_diameter)
        rear_caliper_area = circle_area(rear_caliper_diameter)

        pushrod_force = pedal_force * pedal_ratio

        front_force = (pushrod_force * front_balance_percent / 100)
        rear_force = pushrod_force - front_force

        front_line_pressure = line_pressure(front_force, front_mc_area)
        rear_line_pressure = line_pressure(rear_force, rear_mc_area)

        front_clamp_force = clamp_force(front_line_pressure, front_caliper_area)
        rear_clamp_force = clamp_force(rear_line_pressure, rear_caliper_area)

        front_brake_torque = brake_torque(front_clamp_force, front_rotor_radius, front_pad_mu)
        rear_brake_torque = brake_torque(rear_clamp_force, rear_rotor_radius, rear_pad_mu)

        total_torque = (front_brake_torque + rear_brake_torque)

        front_bias = (front_brake_torque / total_torque) * 100
        rear_bias = (rear_brake_torque / total_torque) * 100

        front_wheel_force = wheel_force(front_brake_torque, front_tire_radius)
        rear_wheel_force = wheel_force(rear_brake_torque, rear_tire_radius)

        total_brake_force = (2 * front_wheel_force + 2 * rear_wheel_force)

        deceleration = vehicle_deceleration(total_brake_force, vehicle_mass)
        deceleration_g = deceleration / 9.81

        dynamic_weight_transfer = weight_transfer(vehicle_mass, deceleration, cg_height, wheelbase)

        g = 9.81

        vehicle_weight = vehicle_mass * g

        front_static_load = (vehicle_weight * front_static_weight_percent / 100)
        rear_static_load = (vehicle_weight - front_static_load)

        dynamic_front_load = (front_static_load + dynamic_weight_transfer)
        dynamic_rear_load = (rear_static_load - dynamic_weight_transfer)

        front_available_grip = (tire_mu * dynamic_front_load)
        rear_available_grip = (tire_mu * dynamic_rear_load)

        front_required_force = (2 * front_wheel_force)
        rear_required_force = (2 * rear_wheel_force)

        front_lockup = ("YES" if front_required_force > front_available_grip else "NO")
        rear_lockup = ("YES" if rear_required_force > rear_available_grip else "NO")

    # calculations
    except ValueError:
        result_label.config(text="Please fill all fields correctly.")

    # ----------------------------
    # OUTPUT
    # ----------------------------


    results = (
        f"Pushrod Force = {pushrod_force:.2f} N\n"
        f"Front Bias = {front_bias:.2f}%\n"
        f"Rear Bias = {rear_bias:.2f}%\n\n"
        f"Front Pressure = {front_line_pressure:.2f} N/mm²\n"
        f"Rear Pressure = {rear_line_pressure:.2f} N/mm²\n\n"
        f"Deceleration = {deceleration_g:.2f} g\n"
        f"Weight Transfer = {dynamic_weight_transfer:.2f} N\n\n"
        f"Front Lock-Up Risk = {front_lockup}\n"
        f"Rear Lock-Up Risk = {rear_lockup}"
    )

    result_label.config(text=results)



# --------------------------------
# GUI
# --------------------------------


window = tk.Tk()
window.title("Formula Student Brake System Analysis Tool")
window.geometry("900x700")

input_frame = tk.Frame(window)
title = tk.Label(
    window,
    text="Formula Student Brake System Analysis Tool",
    font=("Arial", 16, "bold")
)

title.pack(pady=10)
input_frame.pack(pady=20)

# Row 0
tk.Label(input_frame, text="Pedal Force (N)").grid(row=0, column=0, sticky="w")
pedal_force_entry = tk.Entry(input_frame)
pedal_force_entry.grid(row=0, column=1)

tk.Label(input_frame, text="Pedal Ratio").grid(row=0, column=2, sticky="w")
pedal_ratio_entry = tk.Entry(input_frame)
pedal_ratio_entry.grid(row=0, column=3)

# Row 1
tk.Label(input_frame, text="Front MC Diameter (mm)").grid(row=1, column=0, sticky="w")
front_mc_entry = tk.Entry(input_frame)
front_mc_entry.grid(row=1, column=1)

tk.Label(input_frame, text="Rear MC Diameter (mm)").grid(row=1, column=2, sticky="w")
rear_mc_entry = tk.Entry(input_frame)
rear_mc_entry.grid(row=1, column=3)

# Row 2
tk.Label(input_frame, text="Front Caliper Diameter (mm)").grid(row=2, column=0, sticky="w")
front_caliper_entry = tk.Entry(input_frame)
front_caliper_entry.grid(row=2, column=1)

tk.Label(input_frame, text="Rear Caliper Diameter (mm)").grid(row=2, column=2, sticky="w")
rear_caliper_entry = tk.Entry(input_frame)
rear_caliper_entry.grid(row=2, column=3)

# Row 3
tk.Label(input_frame, text="Front Rotor Radius (mm)").grid(row=3, column=0, sticky="w")
front_rotor_entry = tk.Entry(input_frame)
front_rotor_entry.grid(row=3, column=1)

tk.Label(input_frame, text="Rear Rotor Radius (mm)").grid(row=3, column=2, sticky="w")
rear_rotor_entry = tk.Entry(input_frame)
rear_rotor_entry.grid(row=3, column=3)

# Row 4
tk.Label(input_frame, text="Front Balance (%)").grid(row=4, column=0, sticky="w")
balance_entry = tk.Entry(input_frame)
balance_entry.grid(row=4, column=1)

tk.Label(input_frame, text="Vehicle Mass (kg)").grid(row=4, column=2, sticky="w")
vehicle_mass_entry = tk.Entry(input_frame)
vehicle_mass_entry.grid(row=4, column=3)

# Row 5
tk.Label(input_frame, text="Front Tire Radius (mm)").grid(row=5, column=0, sticky="w")
front_tire_entry = tk.Entry(input_frame)
front_tire_entry.grid(row=5, column=1)

tk.Label(input_frame, text="Rear Tire Radius (mm)").grid(row=5, column=2, sticky="w")
rear_tire_entry = tk.Entry(input_frame)
rear_tire_entry.grid(row=5, column=3)

# Row 6
tk.Label(input_frame, text="Front Pad Mu").grid(row=6, column=0, sticky="w")
front_pad_mu_entry = tk.Entry(input_frame)
front_pad_mu_entry.grid(row=6, column=1)

tk.Label(input_frame, text="Rear Pad Mu").grid(row=6, column=2, sticky="w")
rear_pad_mu_entry = tk.Entry(input_frame)
rear_pad_mu_entry.grid(row=6, column=3)

# Row 7
tk.Label(input_frame, text="Wheelbase (m)").grid(row=7, column=0, sticky="w")
wheelbase_entry = tk.Entry(input_frame)
wheelbase_entry.grid(row=7, column=1)

tk.Label(input_frame, text="CG Height (m)").grid(row=7, column=2, sticky="w")
cg_height_entry = tk.Entry(input_frame)
cg_height_entry.grid(row=7, column=3)

# Row 8
tk.Label(input_frame, text="Tire Mu").grid(row=8, column=0, sticky="w")
tire_mu_entry = tk.Entry(input_frame)
tire_mu_entry.grid(row=8, column=1)

tk.Label(input_frame, text="Front Weight Distribution (%)").grid(row=8, column=2, sticky="w")
front_weight_dist_entry = tk.Entry(input_frame)
front_weight_dist_entry.grid(row=8, column=3)

# Add spacing
for widget in input_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Calculate button
tk.Button(
    window,
    text="Calculate",
    command=calculate,
    font=("Arial", 12)
).pack(pady=20)

# Results
result_frame = tk.Frame(
    window,
    relief="solid",
    borderwidth=1
)

result_frame.pack(pady=20)

result_label = tk.Label(
    result_frame,
    text="Results will appear here",
    justify="left",
    anchor="w",
    font=("Consolas", 11)
)

result_label.pack(padx=20, pady=20)

result_label.pack(pady=10)

window.mainloop()