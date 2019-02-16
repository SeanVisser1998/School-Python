/*
  @Author: Sean Visser
  @Description:
          CPP variant van de Python code(opdracht1.py) =)
*/

#include <iostream>
using namespace std;
void primeFactors(long int number);

int main(){
        long int number = 578028320322400;
        primeFactors(number);
        return 0;
}


void primeFactors(long int number){
        cout << "Number: " << number << endl;
        for(int i =2; i <= number/i; i++){

                while (number %i ==0){
                        number = number/i;
                        cout << "Factor: " << i << endl;
                }
        }

        if(number >1){
                cout << "Factor: " << number << endl;
        }
}

