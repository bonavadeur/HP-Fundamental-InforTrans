#include <iostream>
#include <cmath>
#include <stack>
#include <vector>
using namespace std;
void sort(double *a,int n){
    for(int i = 0; i < n; i++){
        for(int j = i+1; j < n; j++){
            if(a[j] > a[i]){
                double c = a[i];
                a[i] = a[j];
                a[j] = c;
            }
        }
    }
}
double entropy(double* a,int n){
    double H = 0;
    for(int i = 0; i < n; i++){
        H += -a[i]*log2(a[i]);
    }
    return H;
}
double ltuma(double* a, int* b, int n){
    double ltb = 0;
    for(int i = 0; i < n; i++){
        ltb += a[i] * b[i];
    }
    return ltb;
}
void nhiphan(double a, int n){
    for(int j = 0; j < n; j++){
        if(a * 2 >= 1){
            cout << 1;
            a = a * 2 - 1;
        }
        else {
            cout << 0;
            a = a * 2;
        }
    }
}
int main(){
    cout << "Nhap kich co cua nguon tin: ";
    int n; cin >> n;
    double *a;
    a = new double[n];
    cout << "Nhap cac xac suat cua nguon tin: " ;
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    sort(a, n);
    int *b = new int[n];
    for(int i = 0; i < n; i++){
        b[i] = ceil(-log(a[i])/log(2));
    }
    double Pi = 0;
    cout << "P(xi)\t\tPi\t\tNhi Phan\tli\tTu ma\n";
    for(int i = 0; i < n; i++){
        cout << a[i] << "\t\t" ;
        cout << Pi;
        cout << "\t\t0.";
        nhiphan(Pi, b[i]);
        cout << "\t\t" << b[i] ;
        cout << "\t"; nhiphan(Pi, b[i]);
        cout << "\n";
        Pi += a[i];
    }
    cout << "H(X) = " << entropy(a, n) << endl;
    cout << "Ltb = " << ltuma(a, b, n) << endl;
    cout << "Hieu suat nen toi uu Kt = " << entropy(a, n) / ltuma(a, b, n) * 100 << "%" << endl;
}
