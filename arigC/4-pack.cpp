#include <stdio.h>
#include <vector>
#include <algorithm>
#include <functional>

float totalP = 0;

/// @brief 背包问题，每件商品有固定的价格p和重量w，在不大于总重量M求总价值最高
/// 每次选择单价sp最高的物品
/// 思路：对单价进行降序排序同时编排重量和价值,遍历单价
void pack(std::vector<float> &p, std::vector<float> &w, int M)
{
    std::vector<int> x(p.size());
    std::vector<float> sp(p.size());
    for (size_t i = 0; i < p.size(); i++)
    {
        sp[i] = p[i] / w[i];
    }
    // TODO 定位每个下标按上述编排重量和价值
    // 使用pair存储单价和索引，在排序后索引也指向原来的下标
    std::vector<std::pair<float,int>> sp_pair(sp.size());
    for (size_t i = 0; i < sp.size(); i++)
    {
        sp_pair.push_back({sp[i], i});
    }
    std::sort(sp_pair.begin(), sp_pair.end(), std::greater<std::pair<float, int>>());
    size_t i;
    for (i = 0; i < sp.size(); i++)
    {
        // 取出当前重量，与总重量相比较
        if (w[sp_pair[i].second] > M)
            break;
        x[i] = 1;
        M -= w[sp_pair[i].second];
    }
    // 最后一件商品比剩下的重量大，切开装
    if (i < p.size())
    {
        x[i] += M / w[sp_pair[i].second];
    }
    // 计算总价值
    for (size_t i = 0; i < x.size(); i++)
    {
        totalP += x[i] * p[i];
        std::printf("%d ", x[i]);
    }
    std::printf("\n");
}

int main(int argc, char const *argv[])
{
    std::vector<float> p = {20, 5, 10, 40, 15, 25}; // 价格
    std::vector<float> w = {10, 2, 5, 20, 8, 12};   // 重量
    int M = 50;                                     // 总重量
    pack(p, w, M);
    std::printf("the total value is: %f", totalP);
    return 0;
}
