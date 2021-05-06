# corregidos errores de salidas inesperadas y valores fuera de rango

import math


def Menu():

# funcion que muestra el menu

    print ("\033[1;36m"+"""\t \t*************************
\t \t FLAVIO CALC v1.2.3                          
\t \t*************************                          
                               
                     
                                                          
\t \tMenu                                                                                                     


1) Suma \t \t4) Division                                       
2) Resta\t \t5) Potencia                                           
3) Multiplicacion\t6) Raiz                                          
--------------------------------------------------------------------------------
7) Recta que pasa por dos puntos del plano\t 11) Grados a radianes
8) Raices reales ecuacion cuadratica\t \t 12) Radianes a grados
9) Logaritmo Natural\t \t \t \t 13) Seno y Coseno
10) Logaritmo base a eleccion\t \t \t 14) Arccoseno 
--------------------------------------------------------------------------------
15) Arcseno

0) Volver a menu\t \t-1) Salir\t \t-2) Ayuda
--------------------------------------------------------------------------------""")

def Calculadora():

# funcion principal

    Menu()
    try:
      opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
    except SyntaxError:
      Menu()
      opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
      
      
    while (opc != -1):


        if (opc==1):
            
            try:
              x = float(input("\033[0;32m"+"Ingrese Numero\n"))
              y = float(input("\033[0;32m"+"Ingrese Otro Numero\n"))
              print ("la Suma es :", float (x+y))
              try:
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
              except SyntaxError:
                Menu()
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))

            except SyntaxError:
              Menu()
              try:
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
              except SyntaxError:
                Menu()
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))

        elif(opc==2):
            try:
              x = float(input("\033[0;32m"+"Ingrese Numero\n"))        
              y = float(input("\033[0;32m"+"Ingrese Otro Numero\n"))
              print ("La Resta es:",float (x-y))
              try:
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
              except SyntaxError:
                 Menu()
                 opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))

            except SyntaxError:
              Menu()
              try:
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
              except SyntaxError:
                Menu()
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))


     
        elif(opc==3):
            try:
              x = float(input("\033[0;32m"+"Ingrese Numero\n"))           
              y = float(input("\033[0;32m"+"Ingrese Otro Numero\n"))

              print ("La Multiplicacion es:",float (x*y))
              try:
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
              except SyntaxError:
                Menu()
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))

            except SyntaxError:
              Menu()
              try:
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
              except SyntaxError:
                Menu()
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))

            
        elif(opc==4):
            try:
              x = float(input("\033[0;32m"+"Ingrese Numero\n"))           
              y = float(input("\033[0;32m"+"Ingrese Otro Numero\n"))

              try:

                print ("La Division es:", float (x)/y)

                try:
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
                except SyntaxError:
                  Menu()
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))

              except ZeroDivisionError:

                print ("No se Permite la Division Entre 0")

                try:
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
                except SyntaxError:
                  Menu()
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
            
            except SyntaxError:
              Menu()
              try:
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
              except SyntaxError:
                Menu()
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))


        elif(opc==5):
            try:
              x = float(input("\033[0;32m"+"ingrese un numero\n"))
              n = float(input("\033[0;32m"+"ingrese la potencia\n"))
              potencia = float(x**n)
              print (str(x)+" "+"elevado a la"+" "+str(n)+" "+"es"+" "+str(potencia))
              try:
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
              except SyntaxError:
                Menu()
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
            except SyntaxError:
              Menu()
              try:
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
              except SyntaxError:
                Menu()
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))

                            
        elif(opc==6):
            try:
              x = float(input("\033[0;32m"+"ingresa numero \n"))
              y = float(input("\033[0;32m"+"ingresa radical\n"))

              try:
                if x < 0 and (y % 2 != 0):
                  raiz = float(-(abs(x)**(1.0/y)))
                  print ("la raiz es"+" "+str(raiz))
                  try:
                    opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
                  except SyntaxError:
                    Menu()
                    opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))

                else:
                  raiz = float((x)**(1.0/y))
                  print ("la raiz es"+" "+str(raiz))
                  try:
                    opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
                  except SyntaxError:
                    Menu()
                    opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
            
              except ZeroDivisionError:
                print ("la raiz no esta definida")
                try:
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
                except SyntaxError:
                  Menu()
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))

              except ValueError:
                print ("la raiz no esta definida en los reales")
                try:
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
                except SyntaxError:
                  Menu()
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))

            except SyntaxError:
              Menu()
              try:
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
              except SyntaxError:
                Menu()
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))

        elif(opc==7):

            try:
              print ("ingrese las componentes de los pares a medida se le vayan pidiendo")
              x1 = float (input("\033[0;32m"+"ingrese x1\n"))
              y1 = float (input("\033[0;32m"+"ingrese y1\n"))
              x2 = float (input("\033[0;32m"+"ingrese x2\n"))
              y2 = float (input("\033[0;32m"+"ingrese y2\n"))
        
              try:
        
                pendiente = float (y2-y1)/(x2-x1)
                ordenada = float (y1 - (pendiente * x1))
                print ("la pendiente de la recta es:", pendiente)
                print ("la ordenada al origen es:", ordenada)
                print ("la ecuacion de la recta es:", "y =" + str (pendiente) + "x" + "+" + str (ordenada))
                try:
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
                except SyntaxError:
                  Menu()
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))

              except ZeroDivisionError:
                print ("x es constante para todo valor de y, no posee ordenada al origen")
                print ("la ecuacion de la recta es:", "x = ", str (x1))
                try:
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
                except SyntaxError:
                  Menu()
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
            except SyntaxError:
              Menu()
              try:
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
              except SyntaxError:
                Menu()
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))

        elif(opc==8):

            try:
              print ("ingrese coeficientes de la ecuacion de la forma y=ax^2+bx+c")
              a = float (input("\033[0;32m"+"ingrese valor de a\n"))
              b = float (input("\033[0;32m"+"ingrese valor de b\n"))
              c = float (input("\033[0;32m"+"ingrese valor de c\n"))
            
              try:

                discriminante = float((b**2)-(4*a*c))
                x1 = float((b+math.sqrt(discriminante))/(2*a))
                x2 = float((b-math.sqrt(discriminante))/(2*a))
                print ("las raices de y = "+ str(a)+"x^2+"+str(b)+"x +"+str(c))
                print ("son x1 ="+str(x1)+" "+"x2 ="+str(x2))
                try:
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
                except SyntaxError:
                  Menu()
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
            
              except ValueError :
                print ("la ecuacion tiene raices imaginarias")
                try:
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
                except SyntaxError:
                  Menu()
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
            except SyntaxError:
              Menu()
              try:
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
              except SyntaxError:
                Menu()
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))


        elif(opc==9):
            try:
              x = float(input("\033[0;32m"+"ingrese un numero\n"))
            
              try:
               ln = float(math.log(x))
               print ("el Ln de"+" "+str(x)+" "+"es"+" "+str(ln))
               try:
                 opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
               except SyntaxError:
                 Menu()
                 opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))

              except ValueError:
                print ("Logaritmo natural no esta definida en x=0")
                try:
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
                except SyntaxError:
                  Menu()
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
            except SyntaxError:
              Menu()
              try:
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
              except SyntaxError:
                Menu()
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))


        elif(opc==10):
            try:
              x = float(input("\033[0;32m"+"ingrese un numero\n"))
              y = float(input("\033[0;32m"+"ingrese la base\n"))

              try:

                logarit = float(math.log(x)/math.log(y))
                print ("el logaritmo de"+" "+str(x)+" "+"en base"+" "+str(y))
                print ("es"+" "+str(logarit))
                try:
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
                except SyntaxError:
                  Menu()
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))

              except ValueError:
            
                print ("logaritmo no esta definida en cero")
                try:
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
                except SyntaxError:
                  Menu()
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
            except SyntaxError:
              Menu()
              try:
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
              except SyntaxError:
                Menu()
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))


        elif(opc==11):
            try:
              x = float(input("\033[0;32m"+"ingrese el valor en grados\n"))
              radian = float(math.radians(x))
              print ("son "+" "+str(radian)+" "+"radianes")
              try:
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
              except SyntaxError:
                Menu()
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
            except SyntaxError:
              Menu()
              try:
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
              except SyntaxError:
                Menu()
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))


        elif(opc==12):
            try:
              x = float(input("\033[0;32m"+"ingrese el valor en radianes\n"))
              grados = float(math.degrees(x))
              print ("son"+" "+str(grados)+" "+"grados")
              try:
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
              except SyntaxError:
                Menu()
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
            except SyntaxError:
              Menu()
              try:
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
              except SyntaxError:
                Menu()
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))


        elif(opc==13):
            try:
              x = float(input("\033[0;32m"+"ingrese valor en grados\n"))
              coseno = float(math.cos(math.radians(x)))
              seno = float (math.sin(math.radians(x)))
              print ("coseno ="+" "+str(coseno))
              print ("seno ="+" "+str(seno))
              try:
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
              except SyntaxError:
                Menu()
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
            except SyntaxError:
              Menu()
              try:
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
              except SyntaxError:
                Menu()
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))

        elif(opc==14):
            try:
              x = float(input("\033[0;32m"+"ingrese coseno\n"))
            
              try:
                arcocos = float(math.degrees(math.acos(x)))
                print "el arccoseno es "+" "+str(arcocos)+" "+"grados"
                try:
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
                except SyntaxError:
                  Menu()
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
              except ValueError:
                print "el valor esta fuera de rango"
                try:
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
                except SyntaxError:
                  Menu()
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
            except SyntaxError:
              Menu()
              try:
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
              except SyntaxError:
                Menu()
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
 

        elif(opc==15):
            try:
              x = float(input("\033[0;32m"+"ingrese el seno\n"))
              try:
                arcseno = float(math.degrees(math.asin(x)))
                print "el arcseno es"+" "+str(arcseno)+" "+"grados"
                try:
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
                except SyntaxError:
                  Menu()
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
              except ValueError:
                print "el valor esta fuera de rango"
                try:
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
                except SyntaxError:
                  Menu()
                  opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
            except SyntaxError:
              Menu()
              try:
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
              except SyntaxError:
                Menu()
                opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))            


        elif(opc == -2):
            
            f = open("instruc.txt","r")
            text = f.read()
            print "\033[0;37m"+text
            try:
              opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
            except SyntaxError:
              Menu()
              opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))

        
        elif(opc <= -2 or opc > 15):
            Menu()
            try:
              opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
            except SyntaxError:
              Menu()
              opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))    


        elif(opc == 0):
            Menu()
            try:
              opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))
            except SyntaxError:
              Menu()
              opc = int(input("\033[1;33m"+"Seleccione Opcion o cero para volver a menu\n"))

           






Calculadora()
    
         
        

    

