import geopandas as gpd 

def carregar_shapefiles(rede_viaria_path, risco_path):
  rede_viaria = gpd.read_file(rede_viaria_path)
  risco = gpd.read_file(risco_path)
  return rede_viaria, risco