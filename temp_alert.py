import sys
if len(sys.argv) == 2:
    script_name = sys.argv[0]
    temp_c = float(sys.argv[1])
    print("User provided input temperature (°C):")
else:
    script_name = sys.argv[0]
    temp_c = 25.0
    print("No input given – using default temperature (25°C):")

if temp_c < 15:
    status = "Cold"
elif temp_c <= 30:
    status = "Normal"
else:
    status = "Hot"

print("Script Name:", script_name)
print("Temperature (°C):", temp_c)
print("Status:", status)
