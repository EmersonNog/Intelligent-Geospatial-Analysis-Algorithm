import geopandas as gpd
import numpy as np

def selecionar_risco(risco, classes):
  risco_destaque = risco[risco['DN'].isin(classes)]
  return risco_destaque

def reprojetar_crs(rede_viaria, risco_destaque):
  if rede_viaria.crs != risco_destaque.crs:
    rede_viaria = rede_viaria.to_crs(risco_destaque.crs)
  return rede_viaria

def spatial_join(rede_viaria, risco_destaque):
  join = gpd.sjoin(rede_viaria, risco_destaque, predicate='intersects')
  return join

def tratar_infinitos(join):
  join = join.replace(np.inf, np.nan)
  return join

def selecionar_geometrias(join):
  join_clip = join[join['index_right'].notnull()]
  return join_clip

def recortar_linhas(join_clip, risco_destaque):
  join_clip = join_clip.clip(risco_destaque.geometry)
  return join_clip