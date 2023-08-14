# REP_MouldRisk_Data_Analysis
Overview:
This code simulates the heat and moisture transfer in building materials. It primarily focuses on the BM3 material from the Hamstad library, but also provides provisions to consider other materials like concrete and wood fibre.

Data Transformation:
Before running the simulation, the code provides a transformation pipeline to convert a raw climate data file (Nasa_UK_21-22.csv) into a format suitable for the simulation (BM3_climate_transformed.txt).

Columns in Nasa_UK_21-22.csv:
Date: Date in MM/DD/YY format.
TS: Temperature in Celsius.
RH2M: Relative Humidity in percentage.
Setting up the Simulation:
Choice of Materials and Geometry: The default material is BM3 with a thickness of 0.2m, divided into 40 elements. You can modify this to use a combination of concrete and wood fibre.
Climate Conditions: Boundary conditions are set based on the BM3_climate_transformed.txt file for external conditions and a fixed set of values for internal conditions.
Initial Conditions: Initial temperature and humidity conditions within the material are defined.
Time Discretisation: The simulation is designed to run over 2400 hours with 15-minute intervals.
Post-Processing:
After the simulation, the code extracts temperature, humidity, and moisture content profiles at specified locations within the material and plots the results.
