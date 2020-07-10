#Autor: Alejandro Hermitaño

def run():
    correo = input("ingresar correo: ")
    if "@untels.edu.pe" in correo:
        print("SI ES UN CORREO DE LA UNTELS")
    else:
	    print("NO ES UN CORREO DE LA UNTELS")
run()