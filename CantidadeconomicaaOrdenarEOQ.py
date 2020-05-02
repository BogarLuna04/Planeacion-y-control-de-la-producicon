########################Cantidad económica a Ordenar (EOQ)########################
import math
def EOQ():
    Continuar="SI"
    while Continuar.upper() == "SI":
        Q=0
        A=0
        c=0
        i=0
        h=0
        D=0
        T=0
        print("Estás en Cantidad económica a Ordenar (EOQ)")
        print("Introduce el valor de A (costo de ordenar)")
        A=float(input())
        print("¿Conoce el valor de Q? SI/NO")
        decision=input()
        if decision.upper()=="SI":
            print("Introduce el valor de Q (número de unidades a ordenar)")
            Q=float(input())
        print("Si conoce el valor de D (demanda) presione 1, si conoce el valor de T (tiempo para hacer una orden) presione 2")
        decision=input()
        if decision == "1":
            print("Introduce el valor de D (demanda)")
            D=float(input())
            if Q !=0:
                T = Q/D
        elif decision == "2":
            print("Introduce el valor de T (tiempo para hacer una orden)")
            T=float(input())
            if Q !=0:
                D = Q/T
        else:
            print("Pues entonces no puedo hacer nada")
            break
        print("¿Conoce el valor de h (costo total anual de mantener inv $ por unidad por año)? SI/NO")
        decision=input()
        if decision.upper() == "SI":
            print("Introduce el valor de h (costo total anual de mantener inv)")
            h=float(input())
            print("Si conoce el valor de c (costo unitario $/Unidad) presione 1, si conoce i  (costo por mantener el inventario % por año) presione 2, caso contrario cualquier otro")
            if decision == "1":
                print("Introduce el valor de c (costo unitario)")
                c=float(input())
                i = h/c
            elif decision == "2":
                print("Introduce el valor de  i (costo por mantener el inventario % por año)")
                i=float(input())
                c=h/i
        else:
            print("Introduce el valor de c (costo unitario)")
            c=float(input())
            print("Introduce el valor de  i (costo por mantener el inventario % por año)")
            i=float(input())
            h = i*c
        if T !=0:
            print("Se debe colocar un pedido cada T=%f"%T)
        if c != 0 and h != 0 and Q !=0:
            costoCompra= c*D
            costoOrdenar=A*D/Q
            costoMantener=h*Q/2
            print("El Costo por compar es=%f"%costoCompra)
            print("El Costo por ordenar es=%f"%costoOrdenar)
            print("El Costo por mantener es=%f"%costoMantener)
            ###### Costo total anual promedio ####
            KQ = costoCompra+costoOrdenar+costoMantener
            print("El Costo total anual promedio es K(Q)=%f"%KQ)
            ###### Costo total anual promedio minimo ####
            KQÇ = costoCompra+math.sqrt(2*A*D*h)
            print("El Costo total anual promedio minimo es K(Q*)=%f"%KQÇ)

        elif c != 0 and h != 0:
            costoCompra= c*D
            KQÇ = costoCompra+math.sqrt(2*A*D*h)
            print("El Costo total anual promedio minimo es K(Q*)=%f"%KQÇ)

        if h != 0:
            QÇ = math.sqrt(2*A*D/h)
            print("El valor de EOQ o la cantidad económica a ordenar o lote económico Q*=%f"%QÇ)
            T = QÇ/D
            print("Se debe colocar un pedido cada T=%f"%T)
        print("Deseas realizar otro cálculo SI/NO")
        Continuar=input()

def sensibilidad():
    print("¿Desea calcular la sensibilidad? SI/NO")
    Q=0
    QÇ=0
    sensibilidad=0
    decision=input()
    if decision.upper() == "SI":
        print("Introduzca el valor de Q")
        Q=float(input())
        print("Introduzca el valor de Q*")
        QÇ=float(input())
        sensibilidad = (1/2)*(Q/QÇ + QÇ/Q)
        print("La sensibilidad es %f"%sensibilidad)

try:
    EOQ()
except ValueError:
    print('TODO LO QUE DEBES INGRESAR SON NÚMEROS')
