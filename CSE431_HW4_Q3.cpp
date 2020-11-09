#include <map>
#include <unordered_set>
#include <iostream>
#include <ctime>

int main()
{
	// set up
	std::clock_t start;
	int n = 1000000;

	// binary tree
	std::multimap<int, int> dict_bin;
	start = std::clock();
	for(int i = 0; i < n; i++)
	{
		dict_bin.insert({ n - i, i });
	}
	double dura_bin = (std::clock() - start) / (double)CLOCKS_PER_SEC;

	// hash table
	std::unordered_multiset<int> dict_hash;
	start = std::clock();
	for (int i = 0; i < n; i++)
	{
		dict_hash.insert(i);
	}
	double dura_hash = (std::clock() - start) / (double)CLOCKS_PER_SEC;

	// print results
	std::cout << "bt:" << dura_bin << "\nht: " << dura_hash << "\ndiff: " << dura_bin - dura_hash << std::endl;
}
