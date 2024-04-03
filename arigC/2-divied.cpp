#include <stdio.h>
#include <vector>
#include <numeric>
#include <algorithm>

std::vector<int> path;
std::vector<std::vector<int>> result;
int order=0, sum=0;
void backtracking(int n, int startIndex){
    sum = std::accumulate(path.begin(), path.end(), 0);
    if (sum > n) {
        // TODO :  剪枝
        return;
    }
    if(sum==n) {
        std::for_each(path.begin(), path.end(), [](int i){printf("%d ", i);});
        printf("\n");
        order++;
        result.push_back(path);
        return;
    }

    for(int i=startIndex;i<=n;i++) {
        path.push_back(i);
        backtracking(n, i);
        path.pop_back();
    }
}
/**
 * @brief original version 1.0
 *      回溯: 指定要拆分的数和起始索引,若path之和大于等于n,则进入临界条件
*/
void test1() {
    int n=6;
    backtracking(n, 1);
    printf("order=%d\n", order);
}

int main()
{
    test1();
}
