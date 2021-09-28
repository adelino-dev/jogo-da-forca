from partida import Partida

debugar = input("Debugar?") 

if debugar == 's':
	pdb.set_trace()

partida = Partida()
partida.iniciar()