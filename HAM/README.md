# REP_MouldRisk_Data_Analysis

## Overview:
This code simulates the heat and moisture transfer in building materials. It primarily focuses on the BM3 material from the Hamstad library, but also provides provisions to consider other materials like concrete and wood fibre.

## Data Transformation:
Before running the simulation, the code provides a transformation pipeline to convert a raw climate data file (`Nasa_UK_21-22.csv`) into a format suitable for the simulation (`BM3_climate_transformed.txt`).

The `BM3_climate_transformed.txt` file contains daily measurements of external temperature and humidity. This dataset serves as the external boundary conditions for heat and moisture transfer simulations in a specific building material (BM3 from the Hamstad library).

### Columns:
- **Time(d)**: Day of the year, starting from day 0.
- **Time (s)**: Time in seconds, a cumulative count of seconds from the start of the year.
- **Temperature**: External temperature in Kelvin.
- **Humidity**: External relative humidity as a fraction between 0 and 1.

## Setting up the Simulation:
1. **Choice of Materials and Geometry**: The default material is BM3 with a thickness of 0.2m, divided into 40 elements. You can modify this to use a combination of concrete and wood fibre.
2. **Climate Conditions**: Boundary conditions are set based on the `BM3_climate_transformed.txt` file for external conditions and a fixed set of values for internal conditions.
3. **Initial Conditions**: Initial temperature and humidity conditions within the material are defined.
4. **Time Discretisation**: The simulation is designed to run over 2400 hours with 15-minute intervals.

## Post-Processing:
After the simulation, the code extracts temperature, humidity, and moisture content profiles at specified locations within the material and plots the results.
