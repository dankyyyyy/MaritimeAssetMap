import netCDF4 as nc
import numpy as np
import logging

class BathymetryHelper:
    DATASET_PATH = '../bathymetric data/gebco_denmark.nc'

    def __init__(self):
        try:
            self.dataset = self.load_dataset(self.DATASET_PATH)
        except Exception as e:
            logging.error(f"Failed to load dataset: {e}")
            raise

    def load_dataset(self, dataset_path):
        """Load the NetCDF dataset."""
        try:
            return nc.Dataset(dataset_path)
        except Exception as e:
            logging.error(f"Error loading NetCDF dataset: {e}")
            raise

    def find_nearest_index(self, values, target):
        """Find the index of the nearest value in a list."""
        try:
            return np.abs(values - target).argmin()
        except Exception as e:
            logging.error(f"Error finding nearest index: {e}")
            raise

    async def get_depth_at_coordinates(self, lat, lon):
        """Get the depth at specified coordinates."""
        try:
            lat_idx = self.find_nearest_index(self.dataset.variables['lat'][:], lat)
            lon_idx = self.find_nearest_index(self.dataset.variables['lon'][:], lon)
            elevation = self.dataset.variables['elevation'][lat_idx, lon_idx]
            depth = -elevation if elevation < 0 else 0  # Convert elevation to depth
            return float(depth)  # Convert to standard Python float
        except Exception as e:
            logging.error(f"Error getting depth at coordinates ({lat}, {lon}): {e}")
            raise

# # Initialize logging
# logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
