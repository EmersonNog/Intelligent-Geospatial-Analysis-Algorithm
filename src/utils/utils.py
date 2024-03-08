import matplotlib.pyplot as plt
from matplotlib_scalebar.scalebar import ScaleBar

def definir_cores():
  cores = {
    'Risco Alto': '#ff8001',
    'Risco Médio': '#ffff01',
    'Área Indicada ': '#33a02c',
    'Área não Indicada': '#ff010e'
  }
  return cores

def plotar_mapa(rede_viaria, risco_destaque, join_clip, cores):
  fig, ax = plt.subplots(figsize=(10, 10))

  rede_viaria.plot(ax=ax, color='#ff010e', alpha=1, linewidth=3)
  risco_destaque[risco_destaque['DN'] == 3].plot(ax=ax, color="#ffff01", alpha=1)
  risco_destaque[risco_destaque['DN'] == 2].plot(ax=ax, color="#ff8001", alpha=1)
  join_clip.plot(ax=ax, color="#33a02c", alpha=1, linewidth=3)

  for classe, cor in cores.items():
    plt.plot([], [], 'o-', color=cor, label=classe)
  plt.legend(loc='best', frameon=True)

  scalebar = ScaleBar(1000, 'm', location='lower right')
  ax.add_artist(scalebar)

  plt.title('Melhores locais para implantação de \ninfraestrutura verde', fontweight='bold')
  plt.show()

