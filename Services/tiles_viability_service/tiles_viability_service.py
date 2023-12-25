import netCDF4 as nc
import numpy as np

class TilesViabilityService:
    DATASET_PATH = '../bathymetric data/gebco_denmark.nc'

    def __init__(self):
        self.dataset = self.load_dataset(self.DATASET_PATH)

    def load_dataset(self, dataset_path):
        """Load the NetCDF dataset."""
        return nc.Dataset(dataset_path)

    def find_nearest_index(self, values, target):
        """Find the index of the nearest value in a list."""
        return np.abs(values - target).argmin()

    async def get_depth_at_coordinates(self, lat, lon):
        """Get the depth at specified coordinates."""
        lat_idx = self.find_nearest_index(self.dataset.variables['lat'][:], lat)
        lon_idx = self.find_nearest_index(self.dataset.variables['lon'][:], lon)
        elevation = self.dataset.variables['elevation'][lat_idx, lon_idx]
        depth = -elevation if elevation < 0 else 0  # Convert elevation to depth
        return float(depth)  # Convert to standard Python float

