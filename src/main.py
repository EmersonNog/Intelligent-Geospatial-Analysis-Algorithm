from utils.processing import *
from utils.utils import *
from utils.load_data import *

# Caminhos para os shapefiles
rede_viaria_path = "./assets/vector_data/camada_rede_viaria/rede_viaria.shp"
risco_path = "./assets/vector_data/camada_risco_inundacao/risco.shp"

# Carregar os shapefiles
rede_viaria, risco = carregar_shapefiles(rede_viaria_path, risco_path)

# Selecionar classes de risco (Alto e Médio)
classes = [2, 3]
risco_destaque = selecionar_risco(risco, classes)

# Reprojetar sistema de coordenadas (se necessário)
rede_viaria = reprojetar_crs(rede_viaria, risco_destaque)

# Realizar spatial join
join = spatial_join(rede_viaria, risco_destaque)

# Tratar valores infinitos
join = tratar_infinitos(join)

# Selecionar apenas geometrias sobrepostas
join_clip = selecionar_geometrias(join)

# Recortar linhas pela área de interseção
join_clip = recortar_linhas(join_clip, risco_destaque)

# Definir cores da legenda
cores = definir_cores()

# Plotar o mapa
plotar_mapa(rede_viaria, risco_destaque, join_clip, cores)