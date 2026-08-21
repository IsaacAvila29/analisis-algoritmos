#include <iostream>
using namespace std;

int main() {
    float kilometros, litros, rendimiento;

    cout << "Kilometros recorridos: ";
    cin >> kilometros;
    cout << "Litros de gasolina consumidos: ";
    cin >> litros;

    rendimiento = kilometros / litros;

    cout << "Rendimiento del vehiculo: " << rendimiento << " km por litro" << endl;

    return 0;
}
