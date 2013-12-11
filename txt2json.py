import json
import sys

if __name__ == '__main__':

	# Leitura do mapa de itens
	filename = sys.argv[1]
	with open(filename,'r') as FILE:
		# lines = FILE.readlines()
		for i in FILE:
			ID_POSICAO = i[:3]
			COD_AREA = i[3:5]
			ID_ITEM = i[5:10]
			DS_GABARITO = i[10:11]
			ID_HABILIDADE = i[11:13]
			DS_COR = i[13:20]
			ID_PROVA = i[20:23]
			print(ID_POSICAO,COD_AREA,ID_ITEM,DS_GABARITO,ID_HABILIDADE,DS_COR,ID_PROVA)