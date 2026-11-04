
import math
import matplotlib.pyplot as plt

# ==========================================
# 1. SYSTEM PARAMETERS
# ==========================================

# Moment of inertia of the platform (kg*m^2)
J_platform = 0.003

# Moment of inertia of the reaction wheel (kg*m^2)
J_wheel = 0.0000735

# Magnitude of motor torque (N*m)
motor_torque = 0.005

# Desired platform rotation (degrees)
target_angle = 30

# Convert degrees to radians for calculations
target_rad = math.radians(target_angle)


# ==========================================
# 2. CALCULATE MANEUVER TIME
# ==========================================

# Reaction torque acts opposite to motor torque.
# Magnitude of platform angular acceleration:
alpha = motor_torque / J_platform

# For an ideal maneuver:
# Accelerate for half the time, then brake for
# an equal amount of time.
#
# Total rotation = alpha * half_time^2

half_time = math.sqrt(target_rad / alpha)
total_time = 2 * half_time

print(f"Total maneuver time: {total_time:.3f} s")


# ==========================================
# 3. INITIAL CONDITIONS
# ==========================================

# Platform starts at 0 degrees and at rest
theta = 0.0            # Platform angle (rad)
omega = 0.0            # Platform angular speed (rad/s)

# Wheel speed relative to the platform
wheel_speed = 0.0      # rad/s

# Simulation settings
steps = 1000
dt = total_time / steps

# Lists for storing results
times = []
angles = []
velocities = []
wheel_speeds = []


# ==========================================
# 4. SIMULATION LOOP
# ==========================================

for i in range(steps + 1):

    time = i * dt

    # Record current state
    times.append(time)
    angles.append(math.degrees(theta))
    velocities.append(math.degrees(omega))

    # Convert wheel speed from rad/s to RPM
    wheel_speeds.append(wheel_speed * 60 / (2 * math.pi))

    if i == steps:
        break

    # First half: accelerate platform toward +30 degrees
    # Second half: brake platform to zero angular speed
    #
    # Motor and platform experience opposite torques.

    if i < steps / 2:
        torque = -motor_torque
    else:
        torque = motor_torque

    # Platform angular acceleration (rad/s^2)
    alpha_platform = -torque / J_platform

    # Wheel acceleration relative to the platform
    alpha_wheel = torque * (1 / J_wheel + 1 / J_platform)

    # Update angular position using constant acceleration
    theta += omega * dt + 0.5 * alpha_platform * dt**2

    # Update platform angular velocity
    omega += alpha_platform * dt

    # Update reaction-wheel speed
    wheel_speed += alpha_wheel * dt


# ==========================================
# 5. PLOT RESULTS
# ==========================================

fig, axes = plt.subplots(3, 1, figsize=(9, 9), sharex=True)

# Plot 1: Platform angle
axes[0].plot(times, angles, label="Platform angle")
axes[0].axhline(target_angle, color="red",
                linestyle="--", label="Target angle")
axes[0].set_ylabel("Angle (degrees)")
axes[0].set_title("Reaction-Wheel Attitude Control Simulation")
axes[0].legend()
axes[0].grid(True)

# Plot 2: Platform angular velocity
axes[1].plot(times, velocities)
axes[1].set_ylabel("Angular velocity (deg/s)")
axes[1].grid(True)

# Plot 3: Reaction-wheel speed
axes[2].plot(times, wheel_speeds)
axes[2].set_ylabel("Wheel speed (RPM)")
axes[2].set_xlabel("Time (seconds)")
axes[2].grid(True)

plt.tight_layout()
plt.show()


# ==========================================
# 6. FINAL RESULTS
# ==========================================

print(f"Final angle: {math.degrees(theta):.2f} degrees")
print(f"Final angular velocity: {math.degrees(omega):.3f} deg/s")
print(f"Maximum wheel speed: {max(abs(v) for v in wheel_speeds):.1f} RPM")
