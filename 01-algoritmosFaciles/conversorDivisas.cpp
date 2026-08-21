#include <iostream>
using namespace std;

int main() {
    float pesos, tipoCambioDolar, tipoCambioEuro, dolares, euros;

    tipoCambioDolar = 18.50;
    tipoCambioEuro = 20.10;

    cout << "Cantidad en pesos mexicanos: ";
    cin >> pesos;

    dolares = pesos / tipoCambioDolar;
    euros = pesos / tipoCambioEuro;

    cout << "Equivalente en Dolares: $" << dolares << endl;
    cout << "Equivalente en Euros: " << euros << endl;

    return 0;
}
