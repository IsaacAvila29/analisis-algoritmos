#include <iostream>
using namespace std;

int main() {
    float distancia, velocidad, tiempoHoras;
    int horas, minutos;

    cout << "Distancia del viaje (km): ";
    cin >> distancia;
    cout << "Velocidad promedio (km/h): ";
    cin >> velocidad;

    tiempoHoras = distancia / velocidad;
    horas = (int) tiempoHoras;
    minutos = (int) ((tiempoHoras - horas) * 60);

    cout << "Tiempo estimado de llegada: " << horas << " horas y " << minutos << " minutos" << endl;

    return 0;
}
