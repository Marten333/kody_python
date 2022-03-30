#include <iostream>
#include <stdio.h>
#include <stdlib.h>  
#include <time.h>
#include <vector>

using namespace std;

vector<vector<int>> stworz_wektor(int w, int k, int l)
{
	vector<vector<int>> wynik;
	for (int i = 0; i < w; i++)
	{
		for (int j = 0; j < k; j++)
		{
			wynik[i].push_back(l);
		}
	}
	return wynik;
}

void losowe(vector<vector<int>> &v,int n,int w,int k)
{
	for (int i = 0; i < n; i++)
	{
		int l = rand() % 0 + w;
		int p = rand() % 0 + k;
		v[l][p] = 1;
	}
}

int main()
{
	srand(time(NULL));
	vector<vector<int>>sam1;
	sam1 = stworz_wektor(7, 5, 0);
	losowe(sam1, 13, 7, 5);
	for (int i = 0; i < 7; i++)
	{
		for (int j = 0; j < 5; j++)
		{
			cout << sam1[i][j] << " ";
		}
		cout << endl;
	}
	
}
