import re

txt = """Tomás alias San Nicolas fue Capaz de ir con el Capataz
haciendolo andar de altas
"""

parrafo = txt.split()

for palabra in parrafo:
	coincidencia = re.findall("(á|a)(s|z)", palabra)
	if coincidencia:
		print(palabra)