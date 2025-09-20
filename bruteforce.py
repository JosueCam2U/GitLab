#Primer Intento----------------------------------------------------------------------
import time
def bruteforce():
    contraseña = "a1."
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890@."
    intentos = 0
    inicio = time.time()
    print("Buscando la contraseña: {contraseña}")
    for letra1 in alfabeto:
        for letra2 in alfabeto:
            for letra3 in alfabeto:
                intento = letra1 + letra2 + letra3 
                intentos +=1
                print(f"Intento {intentos}: Probando: {intento}")

                if intento == contraseña:
                    fin = time.time()
                    print(f"Se a encontrtado la contraseña: {intento}")
                    tiempo = fin - inicio
                    print(f"Tiempo total:{tiempo:.2f} segundos")
                    return
#bruteforce()
#-----------------------------------------------------------------------------------                
#Segundo Intento
import time

def bruteforce2(contraseña):

    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890@."
    intentos = 0
    inicio = time.time()

    for largo in range(1, len(contraseña)+ 1):
        print(f"combinaciones {largo}")

        indices = [0] * largo

        while True:
            intento = ""
            for i in range(largo):
                intento += alfabeto[indices[i]]

            intentos += 1
            print(f"Intento {intentos}: {intento}")

            if intento == contraseña:
                fin = time.time()
                print(f"La contraseña es: {intento}")
                tiempo = fin - inicio
                print(f"Tiempo total:{tiempo:.2f} segundos")
                return
            
            for i in range(largo - 1, -1, -1):
                indices[i] += 1
                if indices[i] < len(alfabeto):
                    break
                indices[i] = 0
            else:
                break
bruteforce2("a1.")
#---------------------------------------------------------------------------------

#Investigaccion requiere instalaciones extra
#preguntar

from concurrent.futures import ProcessPoolExecutor, as_completed
import itertools
import time

#def bruteforce3(longitud, objetivo):
#    caracteres = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890@."
#    for intento in itertools.product(caracteres, repeat=longitud):
#        intento_str = ''.join(intento)
#        if intento_str == objetivo:
#            print(f"Contraseña encontrada: {intento_str}")
#            return intento_str
#    return None

#if __name__ == '__main__':
#    objetivo = input("Ingrese la contraseña a descifrar: ")
#    nucleos = int(input("Ingrese el número de núcleos de CPU a usar: "))
#    tiempo_inicio = time.perf_counter()
    
#    with ProcessPoolExecutor(max_workers=nucleos) as ejecutor:
#        resultados = [ejecutor.submit(intentar_coincidencia, longitud, objetivo) 
#                     for longitud in range(1, len(objetivo)+1)]
        
#        for futuro in as_completed(resultados):
#            coincidencia = futuro.result()
#            if coincidencia:
#                break
    
    #tiempo_fin = time.perf_counter()
    #tiempo_total = tiempo_fin - tiempo_inicio
    #print(f"Tiempo total transcurrido: {tiempo_total} segundos")
