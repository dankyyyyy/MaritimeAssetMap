class WaterDepthValidator:
    def __init__(self, bathymetry_helper):
        self.bathymetry_helper = bathymetry_helper

    async def validate_and_get_depth(self, lat, lon):
        if lat is None or lon is None:
            return {"error": "Missing latitude or longitude parameter"}, 400

        depth = await self.bathymetry_helper.get_depth_at_coordinates(lat, lon)
        return {"latitude": lat, "longitude": lon, "depth": depth}, 200
