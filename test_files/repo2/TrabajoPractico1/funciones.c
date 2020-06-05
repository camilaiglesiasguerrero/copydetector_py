#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "funciones.h"

/**
 * brief Solicita un texto al usuario y lo devuelve
 * char mensaje es el mensaje a ser mostrado
 * char input Array donde se cargara el texto ingresado
 * return void
 *
 */

void getString(char mensaje[], char input[])
{
    printf("%s", mensaje);
    scanf("%s", input);
}

/**
 * brief Verifica si el valor recibido es numerico
 * char str Array con la cadena a ser analizada
 * return 1 si es numerico, 0 si no lo es
 *
 */

int esNumerico(char str[])
{
    int i = 0;
    while(str[i] != '\0')
    {
        if((str[i] < '0' || str[i] > '9') && (str[i] != '-') && (str[i] != '.'))
        {
            return 0;
        }
        i++;
    }
    return 1;
}

/**
 * brief Solicita un texto al usuario y lo devuelve
 * char mensaje es el mensaje a ser mostrado
 * char input Array donde se cargara el texto ingresado
 * return 1 si el texto contiene solo numeros
 *
 */

int getStringNumeros(char mensaje[], char input[])
{
    char auxiliar[256];
    getString(mensaje, auxiliar);
    if(esNumerico(auxiliar))
    {
        strcpy(input, auxiliar);
        return 1;
    }
    return 0;
}

/**
 * brief Recibe los dos operandos y los suma
 * float x 1er operando
 * float y 2do operando
 * return Resultado de la suma
 */

float suma(float x, float y)
{
    float resultado;
    resultado = x + y;
    printf("\nRESULTADO DE LA SUMA: %.2f\n", resultado);
    return resultado;
}

/**
 * brief Recibe los dos operandos y los resta
 * float x 1er operando
 * float y 2do operando
 * return Resultado de la resta
 */

float resta(float x, float y)
{
    float resultado;
    resultado = x - y;
    printf("\nRESULTADO DE LA RESTA: %.2f\n", resultado);
    return resultado;
}

/**
 * brief Recibe los dos operandos, verifica que el divisor sea distinto de 0, y los divide
 * float x 1er operando
 * float y 2do operando
 * return Resultado de la division
 */

float division(float x, float y)
{
    float resultado;
    if (y == 0)
    {
        resultado = printf("\nRESULTADO DE LA DIVISION: MATH ERROR.\nIngrese un divisor distinto de 0.\n");
    }
    else
    {
        resultado = x / y;
        printf("\nRESULTADO DE LA DIVISION: %.2f\n", resultado);
    }
    return resultado;
}

/**
 * brief Recibe los dos operandos y los multiplica
 * float x 1er operando
 * float y 2do operando
 * return Resultado de la multiplicacion
 */

float multiplicacion(float x, float y)
{
    float resultado;
    resultado = x * y;
    printf("\nRESULTADO DE LA MULTIPLICACION: %.2f\n", resultado);
    return resultado;
}

/**
 * brief Recibe el 1er operando y calcula el factorial
 * int x 1er operando
 * return Factorial del 1er operando
 */

long int factorial(int x)
{
    long int resultado = 1;
    int i;

    if(x < 0 || x > 20)
    {
        resultado = printf("\nFACTORIAL: MATH ERROR.\nEl rango del operador, a calcular el factorial, debe ser entre 0 y 20\n");
    }
    else
    {
        if(x == 0)
        {
            resultado = 1;
            printf("\nFACTORIAL DE %d: %ld\n", x, resultado);
        }
        else
        {
            for (i = x; i > 0; i--)
            {
                resultado *= i;
            }
            printf("\nFACTORIAL DE %d: %ld\n", x, resultado);
        }
    }

    return resultado;
}
