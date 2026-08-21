#include <iostream>
using namespace std;

int main() {
    float consumo, porcentajePropina, propina, totalConPropina, pagoPorPersona;
    int personas;

    cout << "Costo total del consumo: ";
    cin >> consumo;
    cout << "Porcentaje de propina (%): ";
    cin >> porcentajePropina;
    cout << "Numero de personas: ";
    cin >> personas;

    propina = consumo * porcentajePropina / 100;
    totalConPropina = consumo + propina;
    pagoPorPersona = totalConPropina / personas;

    cout << "Propina: " << propina << endl;
    cout << "Total a pagar con propina: " << totalConPropina << endl;
    cout << "Pago por persona: " << pagoPorPersona << endl;

    return 0;
}
