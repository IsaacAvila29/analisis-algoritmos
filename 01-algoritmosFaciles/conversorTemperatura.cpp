#include <iostream>
using namespace std;
int main() {

    float celcius, farenheit, kelvin;
    cout << "Celcius ";
    cin >> celcius;

    farenheit = (celcius * 1.8) + 32;
    kelvin = celcius + 273;

    cout << "Farenheit: " << farenheit << endl;
    cout << "Kelvin: " << kelvin << endl;



	return 0;
}
