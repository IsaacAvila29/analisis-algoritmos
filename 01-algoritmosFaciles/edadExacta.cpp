#include <iostream>
using namespace std;

void diasPasados(
    int iYear, int iMonth, int iDay, int iHour, int iMinute,
    int fYear, int fMonth, int fDay, int fHour, int fMinute
) {
    int YearsPassed = 0, MonthsPassed = 0, DaysPassed = 0, HoursPassed = 0, MinutesPassed = 0;
    const int initialDay = iDay;
    const int initialHour = iHour;
    const int initialMinute = iMinute;

    if (
        iYear > fYear ||
        (iYear == fYear && iMonth > fMonth) ||
        (iYear == fYear && iMonth == fMonth && iDay > fDay) ||
        (iYear == fYear && iMonth == fMonth && iDay == fDay &&
            (iHour > fHour || (iHour == fHour && iMinute > fMinute)))
    ) {
        return;
    }

    const int initialTimeInMinutes = iHour * 60 + iMinute;
    const int finalTimeInMinutes = fHour * 60 + fMinute;

    while (
        iYear != fYear ||
        iMonth != fMonth ||
        iDay != fDay ||
        iHour != fHour ||
        iMinute != fMinute
    ) {
        iMinute++;
        MinutesPassed++;

        if (iMinute >= 60) {
            iMinute = 0;
            MinutesPassed = 0;
            iHour++;
            HoursPassed++;
        }

        if (iHour >= 24) {
            iHour = 0;
            HoursPassed = 0;
            iDay++;
            DaysPassed++;
        }

        if (
            iDay == initialDay &&
            iHour == initialHour &&
            iMinute == initialMinute
        ) {
            MonthsPassed++;
            DaysPassed = 0;
            HoursPassed = 0;
            MinutesPassed = 0;
        }

        int daysInMonth;
        switch (iMonth) {
            case 2:
                daysInMonth = (iYear % 400 == 0 || (iYear % 4 == 0 && iYear % 100 != 0)) ? 29 : 28;
                break;
            case 4:
            case 6:
            case 9:
            case 11:
                daysInMonth = 30;
                break;
            default:
                daysInMonth = 31;
        }

        if (iDay > daysInMonth) {
            iDay = 1;
            DaysPassed = 0;
            iMonth++;
        }

        if (iMonth > 12) {
            iMonth = 1;
            iYear++;
        }

        if (MonthsPassed >= 12) {
            MonthsPassed = 0;
            YearsPassed++;
        }
    }

    int remainingMinutes = finalTimeInMinutes - initialTimeInMinutes;
    if (remainingMinutes < 0) remainingMinutes += 24 * 60;
    HoursPassed = remainingMinutes / 60;
    MinutesPassed = remainingMinutes % 60;

    cout << "Han pasado " << YearsPassed << " años, " << MonthsPassed << " meses, "
         << DaysPassed << " dias, " << HoursPassed << " horas y " << MinutesPassed << " minutos" << endl;
}

int main() {
    int iYear, iMonth, iDay, iHour, iMinute;

    cout << "Año de nacimiento: ";
    cin >> iYear;
    cout << "Mes de nacimiento: ";
    cin >> iMonth;
    cout << "Dia de nacimiento: ";
    cin >> iDay;
    cout << "Hora de nacimiento: ";
    cin >> iHour;
    cout << "Minuto de nacimiento: ";
    cin >> iMinute;

    time_t t = time(nullptr);
    tm* ahora = localtime(&t);

    int fYear = ahora->tm_year + 1900;
    int fMonth = ahora->tm_mon + 1;
    int fDay = ahora->tm_mday;
    int fHour = ahora->tm_hour;
    int fMinute = ahora->tm_min;

    diasPasados(iYear, iMonth, iDay, iHour, iMinute, fYear, fMonth, fDay, fHour, fMinute);

    return 0;
}
