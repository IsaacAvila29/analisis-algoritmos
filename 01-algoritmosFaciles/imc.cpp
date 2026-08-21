#include "iostream"
using namespace std;
int main() {
    float peso, estatura, imc;
    cout << "Peso (kg): ";
    cin >> peso;
    cout << "Estatura (m): ";
    cin >> estatura;

    imc = peso / (estatura * estatura);

    cout << "IMC: " << imc << endl;

    if (imc < 18.5) {
        cout << "Clasificacion: Bajo peso" << endl;
    } else if (imc < 25) {
        cout << "Clasificacion: Peso normal" << endl;
    } else if (imc < 30) {
        cout << "Clasificacion: Sobrepeso" << endl;
    } else {
        cout << "Clasificacion: Obesidad" << endl;
    }

    return 0;
}
