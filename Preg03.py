#Autor: Alexandra Huallcca
def cantidad_letras(frase):
    cantidad = len(frase) - frase.count(' ')
    print("Contiene {} letras".format(cantidad))

def run():
    print("CANTIDAD DE LETRAS")
    frase = input("Escriba aqui: ")
    cantidad_letras(frase)
    

if __name__ == "__main__":
    run()