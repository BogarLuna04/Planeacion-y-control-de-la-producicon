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
            print("Entonces no puedo hacer nada")
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

def EOQsinfaltantes():
    Continuar="SI"
    while Continuar.upper() == "SI":
        Q=0
        QÇ=0
        A=0
        c=0
        i=0
        h=0
        D=0
        T=0
        Tp=0
        b=0 #nivel máximo de órdenes atrasadas 
        it=0 #pérdida de la buena voluntad $*unidad
        IT=0 #sanción $*unidad*tiempo
        psi=0 #Tasa de fabricación
        print("Estás en Cantidad económica a Ordenar(EOQ) sin faltantes o usado también para Lote económico de producción")
        print("Introduce el valor de A (costo de ordenar o por preparación)")
        A=float(input())
        print("Introduce el valor de Psi (Tasa de fabricación)")
        psi=float(input())
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
            print("Entonces no puedo hacer nada")
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

        if h != 0 and psi !=0 and psi!=D:
            ###### cantidad económica a ordenar ######
            print("ENTRE AL CALCULO DE Q*")
            x1 = it*D
            QÇ = math.sqrt((2*A*D)/(h*(1-(D/psi))))
            print("El valor de EOQ o la cantidad económica a ordenar o lote económico con faltante es Q*=%f"%QÇ)
            T = QÇ/D
            print("Se debe colocar un pedido cada T=%f"%T)
            Tp = QÇ/psi
            print("Tp=%f"%Tp)

        if c != 0 and h != 0 and Q !=0:
            print("ENTRE AL CALCULO DE K(Q,b*)")
            costoCompra= c*D
            costoOrdenar=A*D/Q
            costoMantener=h*Q*(1-(D/psi))/2
            print("El Costo por compar es=%f"%costoCompra)
            print("El Costo por ordenar es=%f"%costoOrdenar)
            print("El Costo por mantener es=%f"%costoMantener)
            ###### Costo total anual promedio ####
            KQ = costoCompra+costoOrdenar+costoMantener
            print("El Costo total anual promedio es K(Q)=%f"%KQ)

        if c != 0 and h != 0 and QÇ!=0:
            print("ENTRE AL CALCULO DE K(Q,b*)")
            costoCompra= c*D
            costoOrdenar=A*D/QÇ
            costoMantener=h*QÇ*(1-(D/psi))/2
            print("El Costo por compar es=%f"%costoCompra)
            print("El Costo por ordenar es=%f"%costoOrdenar)
            print("El Costo por mantener es=%f"%costoMantener)
            ###### Costo total anual promedio ####
            KQÇ = costoCompra+costoOrdenar+costoMantener
            print("El Costo total anual promedio es K(Q*)=%f"%KQÇ)
        print("Deseas realizar otro cálculo SI/NO")
        Continuar=input()





def EOQconfaltantes():
    Continuar="SI"
    while Continuar.upper() == "SI":
        Q=0
        QÇ=0
        A=0
        c=0
        i=0
        h=0
        D=0
        T=0
        Tp=0
        b=0 #nivel máximo de órdenes atrasadas 
        it=0 #pérdida de la buena voluntad $*unidad
        IT=0 #sanción $*unidad*tiempo
        psi=0 #Tasa de fabricación
        print("Estás en Cantidad económica a Ordenar(EOQ) con faltantes")
        print("Introduce el valor de A (costo de ordenar)")
        A=float(input())
        print("Introduce el valor de Psi (Tasa de fabricación)")
        psi=float(input())
        print("Introduce el valor de Pi (pérdida de la buena voluntad $*unidad)")
        it=float(input())
        print("Introduce el valor de Pi^ (costo de ordenar)")
        IT=float(input())

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
            print("Entonces no puedo hacer nada")
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

        if h != 0 and psi !=0 and psi!=D and IT!=0:
            ###### cantidad económica a ordenar ######
            print("ENTRE AL CALCULO DE Q*")
            x1 = it*D
            x = math.sqrt((2*A*D)/(h*(1-(D/psi))) - (x1**2)/(h*(h+IT)))
            y = math.sqrt((h+IT)/IT)
            QÇ = x*y
            print("El valor de EOQ o la cantidad económica a ordenar o lote económico con faltante es Q*=%f"%QÇ)
            T = QÇ/D
            print("Se debe colocar un pedido cada T=%f"%T)
            Tp = QÇ/psi
            print("Tp=%f"%Tp)

        if h !=0 and IT !=0:
            print("ENTRE AL CALCULO DE b*")
            ###### nivel máximo de órdenes atrasadas #####
            b=(((h*QÇ)-(it*D))*(1-(D/psi)))/(h*IT)
            print("El nivel máximo de órdenes atrasadas b* = %f"%b)

        if c != 0 and h != 0 and Q !=0 and b!=0:
            print("ENTRE AL CALCULO DE K(Q,b*)")
            costoCompra= c*D
            costoOrdenar=A*D/Q
            x=(Q*(1-D/psi)-b)**2
            costoMantener=(h*x)/(2*Q*(1-D/psi))
            costoFaltante = it*b*D/Q + IT*(b**2)/(2*Q*(1-D/psi))
            print("El Costo por compar es=%f"%costoCompra)
            print("El Costo por ordenar es=%f"%costoOrdenar)
            print("El Costo por mantener es=%f"%costoMantener)
            print("El Costo por mantener es=%f"%costoFaltante)
            ###### Costo total anual promedio ####
            KQb = costoCompra+costoOrdenar+costoMantener+costoFaltante
            print("El Costo total anual promedio es K(Q,b)=%f"%KQb)

        if c != 0 and h != 0 and QÇ!=0 and b!=0:
            print("ENTRE AL CALCULO DE K(Q,b*)")
            costoCompra= c*D
            costoOrdenar=A*D/QÇ
            x=(QÇ*(1-D/psi)-b)**2
            costoMantener=(h*x)/(2*QÇ*(1-D/psi))
            costoFaltante = it*b*D/QÇ + IT*(b**2)/(2*QÇ*(1-D/psi))
            print("El Costo por compar es=%f"%costoCompra)
            print("El Costo por ordenar es=%f"%costoOrdenar)
            print("El Costo por mantener es=%f"%costoMantener)
            print("El Costo por mantener es=%f"%costoFaltante)
            ###### Costo total anual promedio ####
            KQÇb = costoCompra+costoOrdenar+costoMantener+costoFaltante
            print("El Costo total anual promedio es K(Q*,b)=%f"%KQÇb)
        print("Deseas realizar otro cálculo SI/NO")
        Continuar=input()



try:
    print("Si desea calular la cantidad económica presione 1, si desea cálcular alguna de sus extensiones presione 2")
    decision=input()
    if decision == "1":
            EOQ()
            sensibilidad()
    elif decision =="2":
        print("Si desea calular EOQ con faltante presione 1, si desea cálcular EOQ sin faltante presione 2")
        decision=input()
        if decision == "1":
            EOQconfaltantes()
        elif decision =="2":
           EOQsinfaltantes()

except ValueError:
    print('TODO LO QUE DEBES INGRESAR SON NÚMEROS')
