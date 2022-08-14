#include <iostream>
#include <vector>
#include "PermutationT.h"

using namespace std;

template<typename T> 
void Swap(T & a, T & b)
{
    T temp = a;
    a = b;
    b = temp;
}

template<typename T> 
void Permutation(vector<T> &data, vector< vector<T> > &result, const int &n, const int &r, int depth)
{
    if (depth == r) // escape condition
    {
        vector<T> resultElement(data.begin(), data.begin()+r);
        result.push_back(resultElement);
        return;
    }
    
    for(int i = depth; i < n; i++)
    {
        swap(data[i], data[depth]);
        Permutation<T>(data, result, n, r, depth + 1);
        swap(data[i], data[depth]);
    }
}

/*
template<typename T> 
vector<vector<T>> CreatePermutation(const vector<T> &list, const int &n, const int &p){
    vector<vector<T>> result;

    return result;
}
*/

int main()
{
    vector<int> ss;
    for (int i = 0; i < 10; i++)
        ss.push_back(i);
    int n = ss.size();
    int r = 3;
    vector< vector<int> > rs;
    // ToyBox::Algorithm::CreatePermutation<int>(ss,3,1);
    //ToyBox::Algorithm::CreatePermutation<int>(ss,3,3);
    cout << "vec :";
    for (int s : ss)
        cout << " " << s;
    cout << endl;
    int l = ss.size();
    Permutation<int>(ss, rs, n, r, 0);
    cout << "complete" << endl;
    for(auto v : rs){
        for(int i : v){
            cout << i;
        }
        cout << endl;
    }
    return 0;
}