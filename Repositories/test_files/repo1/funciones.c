int suma(int a, int b)
{
    int resultado;
    resultado=a+b;
    return resultado;
}

int resta(int a, int b)
{
    return a-b;
}

float division(int a, int b)
{
    return (float)a/b;
}

int multiplicacion(int a, int b)
{
    return a*b;
}

int factorial(int a)
{
    int i;
    int acumulador;
    acumulador=1;
    for(i=1; i<=a; i++)
    {
        acumulador=acumulador*i;
    }
    return acumulador;
}
