#include <stdio.h>
#include <vector>

int partitionForLarge(int s[], int left, int right)
{
    int i=left, j=right;
    int num = s[left];
    do
    {
        while(s[j]<num && i<j) j--; // j指针右移，找到比num大的数
        if(i<j) s[i++]=s[j];
        while(s[i]>num && i<j) i++;  // i指针左移，找到比num小的数
        if(i<j) s[j--]=s[i];
    } while (i<j);
    s[i]=num;
    return i;
}
/// @brief 5，3，7，4，10，1，20...  =>  给定一串数字求第k大
/// 分治思想：用快排(降序)确认left索引下的位置，并与k比较
/// 若k小于m则递归[left, m-1]，问题不变
/// 若k大于m则递归[m+1, right]，问题变为，求第k-m大
void largeForNumK(int s[], int left, int right, int k)
{
    int m = partitionForLarge(s, left, right);
    if(k < m) {
        largeForNumK(s,left,m-1,k);
    }else if(k > m) {
        largeForNumK(s,m+1,right,k-m);
    }else{
        printf("第 %d 大： %d", k, s[m]);
    }
}

int partitionForSmall(int s[], int left, int right)
{
    int i=left, j=right;
    int num = s[left];
    do
    {
        while(s[j]>num && i<j) j--; // j指针右移，找到比num小的数
        if(i<j) s[i++]=s[j];
        while(s[i]<num && i<j) i++;  // i指针左移，找到比num大的数
        if(i<j) s[j--]=s[i];
    } while (i<j);
    s[i]=num;
    return i;
}

/// @brief 10, 2, 30, 8, 58, 4, 7, 42, 9, 22  =>  给定一串数字求第k小
/// 分治思想：用一次快排(升序)确认left索引下位置m，并与k比较
/// 若k小于m则递归[left, m-1]，问题不变
/// 若k大于m则递归[m+1, right]，问题变为，求第k-m+1小
void smallForNumK(int s[], int left, int right, int k)
{
    int m = partitionForSmall(s, left, right);
    if(k < m) {
        smallForNumK(s,left,m-1,k);
    }else if(k > m) {
        smallForNumK(s,m+1,right,k-m);
    }else{
        printf("第 %d 小： %d", k, s[m]);
    }
}

int main()
{
    
    int myArray[10] = {10, 2, 30, 8, 58, 4, 7, 42, 9, 22};
    for (int i = 0; i < 10; ++i) {
        printf("%d ", myArray[i]);
    }
    printf("\n");
    smallForNumK(myArray,0,9,2);
    
    // largeForNumK(myArray,0,9,6);

    printf("\n");
}