import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib import font_manager

# Load the Excel file
file_path = 'FFFF.xlsx'  # Replace with your actual file path
df = pd.read_excel(file_path)

# Extract relevant columns and convert them to NumPy arrays for plotting
time = df['Time (s)'].to_numpy()
x_desired_position = df['X Desired Position'].to_numpy()
y_desired_position = df['Y Desired Position'].to_numpy()
x_actual_position = df['X Actual Position'].to_numpy()
y_actual_position = df['Y Actual Position'].to_numpy()
x_desired_velocity = df['X Desired Velocity'].to_numpy()
x_actual_velocity = df['X Actual Velocity'].to_numpy()
y_desired_velocity = df['Y Desired Velocity'].to_numpy()
y_actual_velocity = df['Y Actual Velocity'].to_numpy()

# Set the path to the Times New Roman font
font_path = '/usr/share/fonts/truetype/msttcorefonts/Times_New_Roman.ttf'
font_prop = font_manager.FontProperties(fname=font_path)

# Update font properties globally
plt.rcParams.update({
    'font.family': font_prop.get_name(),
    'font.size': 10,  # Adjust font size as needed
})

# Create a GridSpec object with 2 rows and 2 columns
fig = plt.figure(figsize=(14, 6))
gs = GridSpec(2, 2, width_ratios=[0.8, 1], height_ratios=[1, 1])

# First graph: Scatter and Line Plot spanning the entire left side
ax0 = plt.subplot(gs[:, 0])
ax0.scatter(y_desired_position, x_desired_position, color='green', label='XY Desired Position', s=20, alpha=1)
ax0.plot(y_actual_position, x_actual_position, color='orange', label='XY Actual Position', linewidth=2)
ax0.set_title('Position: Desired vs Actual', fontproperties=font_prop, fontsize=12)
ax0.set_xlabel('X Position', fontproperties=font_prop)
ax0.set_ylabel('Y Position', fontproperties=font_prop)
ax0.legend(prop=font_prop)
ax0.grid(True)

# Second graph: Time vs X Velocity (top right section)
ax1 = plt.subplot(gs[0, 1])
ax1.plot(time, x_desired_velocity, color='dodgerblue', label='X Desired Velocity', linewidth=2)
ax1.plot(time, x_actual_velocity, color='orange', label='X Actual Velocity', linewidth=2)
ax1.set_title('X Velocity: Desired vs Actual', fontproperties=font_prop, fontsize=12)
ax1.set_xlabel('Time (s)', fontproperties=font_prop)
ax1.set_ylabel('X Velocity', fontproperties=font_prop)
ax1.legend(prop=font_prop)
ax1.grid(True)

# Third graph: Time vs Y Velocity (bottom right section)
ax2 = plt.subplot(gs[1, 1])
ax2.plot(time, y_desired_velocity, color='dodgerblue', label='Y Desired Velocity', linewidth=2)
ax2.plot(time, y_actual_velocity, color='orange', label='Y Actual Velocity', linewidth=2)
ax2.set_title('Y Velocity: Desired vs Actual', fontproperties=font_prop, fontsize=12)
ax2.set_xlabel('Time (s)', fontproperties=font_prop)
ax2.set_ylabel('Y Velocity', fontproperties=font_prop)
ax2.legend(prop=font_prop)
ax2.grid(True)

# Adjust layout and show plot
plt.tight_layout()
plt.show()

