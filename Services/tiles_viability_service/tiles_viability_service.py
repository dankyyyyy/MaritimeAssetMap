import netCDF4 as nc
import numpy as np
import logging

class TilesViabilityService:
    DATASET_PATH = '../bathymetric data/gebco_denmark.nc'

    def __init__(self):
        self.dataset = self.load_dataset(self.DATASET_PATH)

    def load_dataset(self, dataset_path):
        try:
            dataset = nc.Dataset(dataset_path)
            return dataset
        except Exception as e:
            logging.error(f"Error loading dataset: {str(e)}")
            raise  # Reraise the exception

    def find_nearest_index(self, values, target):
        """Find the index of the nearest value in a list."""
        return np.abs(values - target).argmin()

    async def get_depth_at_coordinates(self, lat, lon):
        try:
            lat_idx = self.find_nearest_index(self.dataset.variables['lat'][:], lat)
            lon_idx = self.find_nearest_index(self.dataset.variables['lon'][:], lon)
            elevation = self.dataset.variables['elevation'][lat_idx, lon_idx]
            depth = -elevation if elevation < 0 else 0  # Convert elevation to depth
            return float(depth)  # Convert to standard Python float
        except Exception as e:
            logging.error(f"Error retrieving depth at coordinates ({lat}, {lon}): {str(e)}")
            raise  # Reraise the exception

# Configure logging to print to the console
logging.basicConfig(level=logging.ERROR)