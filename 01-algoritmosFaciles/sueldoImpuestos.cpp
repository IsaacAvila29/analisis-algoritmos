#include "iostream"
using namespace std;

int main(void){
    float sueldoBruto, porcentajeImpuesto, descuento, sueldoNeto;

    cout << "Salario mensual bruto: ";
    cin >> sueldoBruto;
    cout << "Porcentaje de impuestos (%): ";
    cin >> porcentajeImpuesto;

    descuento = sueldoBruto * porcentajeImpuesto / 100;
    sueldoNeto = sueldoBruto - descuento;

    cout << "Descuento por impuestos: " << descuento << endl;
    cout << "Sueldo neto: " << sueldoNeto << endl;

    return 0;
}
