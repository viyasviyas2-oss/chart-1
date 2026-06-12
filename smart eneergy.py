import time
import random
import os

# --- System Configuration ---
VOLTAGE_NOMINAL = 230.0  # Standard grid voltage (V)
TARIFF_PER_KWH = 8.0     # Cost per unit of electricity (₹/kWh)

# --- Global Variables ---
total_energy_kwh = 0.0

def read_voltage_sensor():
    """
    Simulates reading from an AC Voltage Sensor (e.g., ZMPT101B).
    Real grids fluctuate slightly around the nominal voltage.
    """
    return VOLTAGE_NOMINAL + random.uniform(-4.0, 4.0)

def read_current_sensor():
    """
    Simulates reading from a Current Sensor (e.g., ACS712).
    Simulating a household load drawing between 1.0A and 6.0A.
    """
    return random.uniform(1.0, 6.0)

def clear_screen():
    # Clears the terminal screen for a clean, updating dashboard
    os.system('cls' if os.name == 'nt' else 'clear')

print("Starting Smart Energy Meter Interface...")
time.sleep(2)

try:
    # Main continuous loop (mimicking a microcontroller's loop function)
    while True:
        # 1. Read Raw Sensor Data
        voltage = read_voltage_sensor()
        current = read_current_sensor()
        
        # 2. Calculate Instantaneous Power (Watts)
        # Formula: Power (W) = Voltage (V) * Current (A)
        power_watts = voltage * current
        
        # 3. Calculate Energy Consumed (kWh)
        # We assume this loop updates every 2 seconds.
        # Formula: Energy (kWh) = Power (kW) * Time (hours)
        power_kw = power_watts / 1000.0
        time_hours = 2.0 / 3600.0  # 2 seconds converted to hours
        
        total_energy_kwh += (power_kw * time_hours)
        
        # 4. Calculate Estimated Bill
        estimated_bill = total_energy_kwh * TARIFF_PER_KWH
        
        # 5. Render the Dashboard
        clear_screen()
        print("=======================================")
        print("       SMART ENERGY METER LIVE         ")
        print("=======================================")
        print(f" Grid Voltage:    {voltage:.2f} V")
        print(f" Load Current:    {current:.2f} A")
        print(f" Active Power:    {power_watts:.2f} W")
        print("---------------------------------------")
        # Displaying 6 decimal places for kWh so you can see it incrementing live
        print(f" Total Energy:    {total_energy_kwh:.6f} kWh")
        print(f" Estimated Bill:  ₹ {estimated_bill:.4f}")
        print("=======================================")
        print("Press Ctrl+C to stop monitoring...")
        
        # Wait 2 seconds before taking the next sensor reading
        time.sleep(2)

except KeyboardInterrupt:
    print("\nSmart Energy Meter safely shut down.")
