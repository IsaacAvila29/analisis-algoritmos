#include <iostream>
using namespace std;

int main() {
    float p1, p2, p3;
    float pond1, pond2, pond3;
    float calificacionFinal;

    cout << "Calificacion Parcial 1: ";
    cin >> p1;
    cout << "Ponderacion Parcial 1 (%): ";
    cin >> pond1;

    cout << "Calificacion Parcial 2: ";
    cin >> p2;
    cout << "Ponderacion Parcial 2 (%): ";
    cin >> pond2;

    cout << "Calificacion Parcial 3: ";
    cin >> p3;
    cout << "Ponderacion Parcial 3 (%): ";
    cin >> pond3;

    calificacionFinal = (p1 * pond1 / 100) + (p2 * pond2 / 100) + (p3 * pond3 / 100);

    cout << "Calificacion final ponderada: " << calificacionFinal << endl;

    return 0;
}
