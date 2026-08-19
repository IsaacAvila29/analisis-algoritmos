#include "iostream"
using namespace std;
int main() {
    float peso, estatura, imc;
    cout << "Peso: ";
    cin >> peso;
    cout << "Estatura: ";
    cin >> estatura;

    imc = peso / (estatura * estatura);

    cout << "IMC: " << imc << endl;

    return 0;
}
