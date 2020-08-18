import re

txt = """Un buen día Adriana conocio a una 
mujer llamada Ariana no Ariadna por lo que le recordo 
que su hermana se llama Arlana y tiene una
tía nombrada Amanda"""

parrafoPalabraPorPalabra = txt.split()
#print(parrafoPalabraPorPalabra)

for palabra in parrafoPalabraPorPalabra:
	coincidencia = re.findall("""^A.*a$""", palabra)
	if coincidencia:
		print(palabra)