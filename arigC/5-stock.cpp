#include <stdio.h>
#include <vector>
#include <algorithm>
#include <functional>

/// @brief 给出一些数字，【13 7 8 16】，每次只能合并相邻两个数
/// 每次合并两个数会产生代码(两数之和)，求最小代价子母树
/// f(1,4)=min{f(1,3),f(1,2)+f(3,4),f(2,4)}+g(1,4)
/// f(1,n)=min{f(2,n),f(1,2)+f(3,n)...f(1,n-1)}+g(1,n)
/// 每次选一个idx划分区间，如idx=1，则代价为f(2,4)
int minStock(std::vector<int> w)
{
    // 获取每一段元素的和
    std::vector<std::vector<int>> g(w.size(), std::vector<int>(w.size(), 0));
    std::vector<std::vector<int>> f(w.size(), std::vector<int>(w.size(), 0));
    for (size_t i = 0; i < w.size(); i++)
    {
        for (size_t j = 0; j < w.size(); j++)
        {
            int sum = 0;
            std::for_each(w.begin(), w.end(), [&](int v){ sum += v; });
            g[i][j] = sum;
        }
    }
    // 构造左右两堆树
    for (size_t i = 1; i < w.size(); i++)
    {
        for (size_t j = 0; j < w.size()-1; j++)
        {
            int min = f[i-1][j] + f[0][j+i];        // f(1,3)的最小成本
            for (size_t k = i-2; k >= 0; k--)       // 用k划线
            {
                if(min > f[k][j] + f[i-k-1][j+k+1]) // 用min和左右两堆进行比较
                {
                    min = f[k][j] + f[i-k-1][j+k+1];
                }
            }
            f[i][j] = g[i][i+j] + min;              // 填充f(i,j)的最小成本
        }
    }
    return f[w.size()-1][0];
}

int main(int argc, char const *argv[])
{
    int min = minStock({13, 7, 8 , 16});
    std::printf("min: %d", min);
    return 0;
}
