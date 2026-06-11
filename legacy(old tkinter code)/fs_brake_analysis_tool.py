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

        front_piston_count = int(front_piston_count_entry.get())
        rear_piston_count = int(rear_piston_count_entry.get())

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

        front_caliper_area = (front_piston_count * circle_area(front_caliper_diameter))
        rear_caliper_area = (rear_piston_count * circle_area(rear_caliper_diameter))

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

        ideal_front_bias = (dynamic_front_load /(dynamic_front_load + dynamic_rear_load)) * 100

        bias_error = front_bias - ideal_front_bias

        if bias_error < -3:
            setup_recommendation = "Increase Front Brake Bias"

        elif bias_error > 3:
            setup_recommendation = "Reduce Front Brake Bias"

        else:
            setup_recommendation = "Bias Near Optimal"

        front_available_grip = (tire_mu * dynamic_front_load)
        rear_available_grip = (tire_mu * dynamic_rear_load)

        front_required_force = (2 * front_wheel_force)
        rear_required_force = (2 * rear_wheel_force)

        front_utilization = (front_required_force / front_available_grip) * 100
        rear_utilization = (rear_required_force / rear_available_grip) * 100

        if front_utilization > 95:
            front_warning = "HIGH"

        elif front_utilization > 85:
            front_warning = "MODERATE"

        else:
            front_warning = "LOW"


        if rear_utilization > 95:
            rear_warning = "HIGH"

        elif rear_utilization > 85:
            rear_warning = "MODERATE"

        else:
            rear_warning = "LOW"

        front_lockup = ("YES" if front_required_force > front_available_grip else "NO")
        rear_lockup = ("YES" if rear_required_force > rear_available_grip else "NO")

    # calculations
    except ValueError:
        result_left.config(text="Please fill all fields correctly.")
        result_right.config(text="")
        return

    # ----------------------------
    # OUTPUT
    # ----------------------------


    # ----------------------------
# OUTPUT
# ----------------------------

    left_results = (
    f"Pushrod Force = {pushrod_force:.2f} N\n\n"

    f"Front Pressure = {front_line_pressure:.2f} N/mm²\n"
    f"Rear Pressure = {rear_line_pressure:.2f} N/mm²\n\n"

    f"Front Clamp Force = {front_clamp_force:.2f} N\n"
    f"Rear Clamp Force = {rear_clamp_force:.2f} N\n\n"

    f"Front Brake Torque = {front_brake_torque:.2f} Nmm\n"
    f"Rear Brake Torque = {rear_brake_torque:.2f} Nmm\n\n"

    f"Front Bias = {front_bias:.2f}%\n"
    f"Rear Bias = {rear_bias:.2f}%"
)

    right_results = (
    f"Deceleration = {deceleration_g:.2f} g\n"
    f"Weight Transfer = {dynamic_weight_transfer:.2f} N\n\n"

    f"Front Available Grip = {front_available_grip:.2f} N\n"
    f"Rear Available Grip = {rear_available_grip:.2f} N\n\n"

    f"Front Required Force = {front_required_force:.2f} N\n"
    f"Rear Required Force = {rear_required_force:.2f} N\n\n"

    f"Front Tire Utilization = {front_utilization:.1f}% ({front_warning})\n"
    f"Rear Tire Utilization = {rear_utilization:.1f}% ({rear_warning})\n\n"

    f"Ideal Front Bias = {ideal_front_bias:.1f}%\n"
    f"Bias Error = {abs(bias_error):.1f}%\n"

    f"Recommendation:\n{setup_recommendation}\n\n"

    f"Front Lock-Up Risk = {front_lockup}\n"
    f"Rear Lock-Up Risk = {rear_lockup}"
)

    result_left.config(text=left_results)
    result_right.config(text=right_results)



# --------------------------------
# GUI
# --------------------------------


window = tk.Tk()
window.title("Formula Student Brake System Analysis Tool")
window.state("zoomed")

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

tk.Label(input_frame, text="Vehicle Mass (kg)").grid(row=0, column=4, sticky="w")
vehicle_mass_entry = tk.Entry(input_frame)
vehicle_mass_entry.grid(row=0, column=5)

tk.Label(input_frame, text="Tire Mu").grid(row=0, column=6, sticky="w")
tire_mu_entry = tk.Entry(input_frame)
tire_mu_entry.grid(row=0, column=7)

# Row 1
tk.Label(input_frame, text="Front MC Diameter (mm)").grid(row=1, column=0, sticky="w")
front_mc_entry = tk.Entry(input_frame)
front_mc_entry.grid(row=1, column=1)

tk.Label(input_frame, text="Rear MC Diameter (mm)").grid(row=1, column=2, sticky="w")
rear_mc_entry = tk.Entry(input_frame)
rear_mc_entry.grid(row=1, column=3)

tk.Label(input_frame, text="Front Balance (%)").grid(row=1, column=4, sticky="w")
balance_entry = tk.Entry(input_frame)
balance_entry.grid(row=1, column=5)

tk.Label(input_frame, text="Front Weight Distribution (%)").grid(row=1, column=6, sticky="w")
front_weight_dist_entry = tk.Entry(input_frame)
front_weight_dist_entry.grid(row=1, column=7)

# Row 2
tk.Label(input_frame, text="Front Piston Count").grid(row=2, column=0, sticky="w")
front_piston_count_entry = tk.Entry(input_frame)
front_piston_count_entry.grid(row=2, column=1)

tk.Label(input_frame, text="Rear Piston Count").grid(row=2, column=2, sticky="w")
rear_piston_count_entry = tk.Entry(input_frame)
rear_piston_count_entry.grid(row=2, column=3)

tk.Label(input_frame, text="Front Piston Diameter (mm)").grid(row=2, column=4, sticky="w")
front_caliper_entry = tk.Entry(input_frame)
front_caliper_entry.grid(row=2, column=5)

tk.Label(input_frame, text="Rear Piston Diameter (mm)").grid(row=2, column=6, sticky="w")
rear_caliper_entry = tk.Entry(input_frame)
rear_caliper_entry.grid(row=2, column=7)

# Row 3
tk.Label(input_frame, text="Front Rotor Radius (mm)").grid(row=3, column=0, sticky="w")
front_rotor_entry = tk.Entry(input_frame)
front_rotor_entry.grid(row=3, column=1)

tk.Label(input_frame, text="Rear Rotor Radius (mm)").grid(row=3, column=2, sticky="w")
rear_rotor_entry = tk.Entry(input_frame)
rear_rotor_entry.grid(row=3, column=3)

tk.Label(input_frame, text="Wheelbase (m)").grid(row=3, column=4, sticky="w")
wheelbase_entry = tk.Entry(input_frame)
wheelbase_entry.grid(row=3, column=5)

tk.Label(input_frame, text="CG Height (m)").grid(row=3, column=6, sticky="w")
cg_height_entry = tk.Entry(input_frame)
cg_height_entry.grid(row=3, column=7)

# Row 4
tk.Label(input_frame, text="Front Tire Radius (mm)").grid(row=4, column=0, sticky="w")
front_tire_entry = tk.Entry(input_frame)
front_tire_entry.grid(row=4, column=1)

tk.Label(input_frame, text="Rear Tire Radius (mm)").grid(row=4, column=2, sticky="w")
rear_tire_entry = tk.Entry(input_frame)
rear_tire_entry.grid(row=4, column=3)

tk.Label(input_frame, text="Front Pad Mu").grid(row=4, column=4, sticky="w")
front_pad_mu_entry = tk.Entry(input_frame)
front_pad_mu_entry.grid(row=4, column=5)

tk.Label(input_frame, text="Rear Pad Mu").grid(row=4, column=6, sticky="w")
rear_pad_mu_entry = tk.Entry(input_frame)
rear_pad_mu_entry.grid(row=4, column=7)

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
# Results
result_frame = tk.Frame(
    window,
    relief="solid",
    borderwidth=1
)

result_frame.pack(pady=20)

# LEFT HEADING
title_left = tk.Label(
    result_frame,
    text="Hydraulic and Braking Results",
    font=("Arial", 10, "bold")
)
title_left.grid(row=0, column=0, padx=30, pady=10)

# RIGHT HEADING
title_right = tk.Label(
    result_frame,
    text="Vehicle and Lock-Up Results",
    font=("Arial", 10, "bold")
)
title_right.grid(row=0, column=1, padx=30, pady=10)

# LEFT RESULTS
result_left = tk.Label(
    result_frame,
    text="",
    justify="left",
    anchor="nw",
    font=("Consolas", 10)
)
result_left.grid(row=1, column=0, padx=30, pady=10)

# RIGHT RESULTS
result_right = tk.Label(
    result_frame,
    text="",
    justify="left",
    anchor="nw",
    font=("Consolas", 10)
)
result_right.grid(row=1, column=1, padx=30, pady=10)

window.mainloop()