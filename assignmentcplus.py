#include <iostream>
#include <ctime>

using namespace std;

// Structure to store date
struct Date {
    int day;
    int month;
    int year;
};

// Function to check if a year is a leap year
bool isLeapYear(int year) {
    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))
        return true;
    return false;
}

// Function to get number of days in a month
int getDaysInMonth(int month, int year) {
    int daysInMonth[] = {31, 28, 31, 30, 31, 30,
                         31, 31, 30, 31, 30, 31};

    if (month == 2 && isLeapYear(year))
        return 29;

    return daysInMonth[month - 1];
}

// Function to validate date
bool isValidDate(Date d) {
    if (d.year < 0 || d.month < 1 || d.month > 12 || d.day < 1)
        return false;

    if (d.day > getDaysInMonth(d.month, d.year))
        return false;

    return true;
}

// Function to calculate age
void calculateAge(Date birth, Date current) {
    if (!isValidDate(birth) || !isValidDate(current)) {
        cout << "Invalid date entered.\n";
        return;
    }

    if (birth.year > current.year ||
        (birth.year == current.year && birth.month > current.month) ||
        (birth.year == current.year && birth.month == current.month && birth.day > current.day)) {
        cout << "Birth date cannot be after current date.\n";
        return;
    }

    int years = current.year - birth.year;
    int months = current.month - birth.month;
    int days = current.day - birth.day;

    // Adjust days if negative
    if (days < 0) {
        months--;
        int prevMonth = current.month - 1;
        int prevYear = current.year;

        if (prevMonth == 0) {
            prevMonth = 12;
            prevYear--;
        }

        days += getDaysInMonth(prevMonth, prevYear);
    }

    // Adjust months if negative
    if (months < 0) {
        years--;
        months += 12;
    }

    cout << "\nYour Age is: ";
    cout << years << " Years, "
         << months << " Months, "
         << days << " Days.\n";
}

int main() {
    Date birth, current;

    cout << "===== AGE CALCULATOR =====\n";

    // Input birth date
    cout << "Enter Birth Date (DD MM YYYY): ";
    cin >> birth.day >> birth.month >> birth.year;

    // Get current system date
    time_t t = time(0);
    tm *now = localtime(&t);

    current.day = now->tm_mday;
    current.month = now->tm_mon + 1;
    current.year = now->tm_year + 1900;

    cout << "Current Date: "
         << current.day << "/"
         << current.month << "/"
         << current.year << endl;

    // Calculate age
    calculateAge(birth, current);

    return 0;
}