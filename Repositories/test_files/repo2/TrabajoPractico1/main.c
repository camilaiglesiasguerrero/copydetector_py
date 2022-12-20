#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "funciones.h"

int main()
{
    char seguir = 's';
    int opcion = 0;

    float primerOperando = 0;
    float segundoOperando = 0;
    float operacion = 0;
    long int operacionFactorial;

    char auxiliarOpcionString[50];
    char auxiliarPrimerOperandoStr[50];
    char auxiliarSegundoOperandoStr[50];



    while (seguir == 's')
    {
        printf("\n1- Ingresar 1er operando (A=%.2f)\n", primerOperando);
        printf("2- Ingresar 2do operando (B=%.2f)\n", segundoOperando);
        printf("3- Calcular todas las operaciones\n");
        printf("4- Salir\n");

        if(!getStringNumeros("\nIngrese la opcion: ", auxiliarOpcionString))
        {
            system("clear");
            printf("\nLA OPCION DEBE SER NUMERICA\n");
            continue;
        }

        opcion = atoi(auxiliarOpcionString);

        switch(opcion)
        {
            default:

                system("clear");
                printf("\nLA OPCION DEBE SER ENTRE 1 y 9\n");
                break;

            case 1:

                if(!getStringNumeros("\nIngrese el primer operando: ", auxiliarPrimerOperandoStr))
                {
                    system("clear");
                    printf("\nEL OPERANDO DEBE SER NUMERICO\n");
                    break;
                }
                system("clear");
                primerOperando = atof(auxiliarPrimerOperandoStr);

                break;

            case 2:

                if(!getStringNumeros("\nIngrese el segundo operando: ", auxiliarSegundoOperandoStr))
                {
                    system("clear");
                    printf("\nEL OPERANDO DEBE SER NUMERICO\n");
                    break;
                }
                system("clear");
                segundoOperando = atof(auxiliarSegundoOperandoStr);
                break;


            case 3:

                system("clear");
                operacion = suma(primerOperando, segundoOperando),
                resta(primerOperando, segundoOperando),
                division(primerOperando, segundoOperando),
                multiplicacion(primerOperando, segundoOperando);
                operacionFactorial = factorial((int)primerOperando);
                break;

            case 4:

                seguir = 'n';
                break;
        }
    }

    return 0;
}
