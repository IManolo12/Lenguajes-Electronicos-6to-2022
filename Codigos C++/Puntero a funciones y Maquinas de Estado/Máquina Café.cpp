#include <iostream>
using namespace std;

int Cafe_Elegido;

void Latte(void)
{
    cout << "El latte tiene los siguiente ml de leche y cafe:\n";
    cout << "- 80ml de leche\n";
    cout << "- 20ml de cafe";
}
void Americano(void)
{
    cout << "El americano tiene los siguiente ml de agua y cafe:\n";
    cout << "- 30ml de cafe\n";
    cout << "- 30ml de agua";
}
void Lagrima(void)
{
    cout << "La lagrima  tiene los siguiente ml de leche y cafe:\n";
    cout << "- 90ml de leche\n";
    cout << "- 5ml de cafe";
}
void Negro(void)
{
    cout << "El negro tiene los siguiente ml de cafe:\n"
         << "- 100ml de cafe";
}
void Cortado(void)
{
    cout << "El cortado tiene los siguiente ml de leche y cafe:\n"
         << "- 50ml de leche\n"
         << "- 50ml de cafe";
}

void (*pCoffee) (void);

int main()
{
    
    cout << "Bienvenido a la maquina expendedora de Nescafe\nSeleccione la tecla correspondiente a cada cafe\n";
    cout << "A continuación le vamos a mostrar la cantidad de cada ingrediente para hacer cada tipo de cafe:\n";
    cout << "- Latte(1)\n- Americano(2)\n- Lagrima(3)\n- Negro(4)\n- Cortado(5)\n ";
    cin >> Cafe_Elegido;
    
    switch(Cafe_Elegido)
    {
        case 1:
        pCoffee = Latte;
        pCoffee();
        break;
        
        case 2: 
        pCoffee = Americano;
        pCoffee();
        break;
        
        case 3:
        pCoffee = Lagrima;
        pCoffee();
        break;
        
        case 4:
        pCoffee = Negro;
        pCoffee();
        break;
        
        case 5:
        pCoffee = Cortado;
        pCoffee();
        break;
    }
    return 0;
}








