import netCDF4
import matplotlib.pyplot as plt

# Load the netCDF file
data = netCDF4.Dataset('tasAnom_rcp45_land-prob_uk_region_sample_b6190_30y_ann_20091201-20991130.nc')

# Access the variables
regions = data['geo_region'][:]
regions = [''.join(region.astype(str)).strip() for region in regions]
tasAnom = data['tasAnom']  # Temperature anomaly data

# Create a figure and axis for the plot
fig, ax = plt.subplots()

# Iterate over the regions and plot the histogram for each region
for i, region in enumerate(regions):
    tasAnom_region = tasAnom[:, i, :].flatten()  # Get temperature anomaly data for the region

    # Plot the histogram for the region
    ax.hist(tasAnom_region, bins=50, label=region)

# Set the title and labels for the plot
ax.set_title('Distribution of Temperature Anomaly for Different Regions')
ax.set_xlabel('Temperature Anomaly (K)')
ax.set_ylabel('Frequency')

# Add a legend to distinguish the regions
ax.legend()

# Show the plot
plt.show()
