#include <stdio.h>
#include <stdlib.h>
#include "funciones.h"


int main()
{
    int x, y;
    int opcion;
    x=0;
    y=0;

    do
    {
        printf("\n Seleccione una opcion\n\n 1 - 1er operando (A=%d)\n 2 - 2do operando (B=%d)\n 3 - Calcular todas las operaciones\n", x, y);
        printf(" 4 - Informar resultados\n 5 - salir\n ");
        fflush(stdin);
        scanf("%d", &opcion);

        system("cls");
        switch(opcion)
        {
        case 1:
            printf("1- Ingresar 1er operando (A=x) ");
            scanf("%d", &x);
            break;
        case 2:
            printf("2- Ingresar 2do operando (B=y) ");
            scanf("%d", &y);
            break;
        case 3:
            printf("a- Calcular la suma (%d+%d)\n",x,y);
            printf("b- Calcular la resta (%d-%d)\n",x,y);
            printf("c- Calcular la division (%d/%d)\n",x,y);
            printf("d- Calcular la multiplicacion (%d*%d)\n",x,y);
            printf("e- Calcular el factorial (%d! %d!)\n", x, y);
            system("pause");
            system("cls");
            break;
        case 4:
            printf("El resultado de %d + %d es: %d \n", x, y, suma(x, y));
            printf("El resultado de %d - %d es: %d \n", x, y, resta(x, y));

            if(y==0)
            {
                printf("No es posible dividir por cero \n");
            }
            else
            {
                printf("El resultado de %d / %d es: %.2f \n", x, y, division(x, y));
            }

            printf("El resultado de %d * %d es: %d \n", x, y, multiplicacion(x, y));

            if(x<0 && y>-1)
            {

                printf("No es posible sacar el factorial de %d por que no es un numero natural y el factorial de %d es: %d\n\n", x, y, factorial(y));

            }
            else if(y<0 && x>-1)
            {
                printf("No es posible sacar el factorial de %d por que no es un numero natural y el factorial de %d es: %d\n\n", y, x, factorial(x));
            }
            else if(x<0 && y<0)
            {
                printf("No es posible sacar el factorial, por que los numero ingresados no son natural\n\n");
            }
            else
            {
                printf("El factorial de %d es: %d y el factorial de %d es: %d\n\n", x, factorial(x), y, factorial(y));
            }
            system("pause");
            system("cls");
            break;

        case 5:
            break;
        default:
            printf("opcion incorrecta");
            break;
        }
    }
    while(opcion!=5);

    return 0;
}
