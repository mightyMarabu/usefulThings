import geopandas as gpd
import matplotlib.pyplot as plt

gpkg_filepath = "example.gpkg"

try:
  data = gpd.read_file(gpkg_filepath)
except FileNotFoundError:
  print(f"Error: GeoPackage file not found at {gpkg_filepath}")
  exit(1)

# Define figure size 
plt.figure(figsize=(25,25))  # Adjust width and height as needed

data.plot(color="blue", linewidth=0.5)  # Customize color and line width

# Optional: Add title, labels, etc. (refer to matplotlib documentation)
# plt.title("GeoPackage Data")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")

# Set background color (optional)
plt.axis("off")  # Hide axes
plt.gca().set_facecolor('white')  # Set background to white

plt.savefig("output.png", dpi=300, bbox_inches='tight')  # Adjust DPI if needed

print("GeoPackage data saved as output.png")
