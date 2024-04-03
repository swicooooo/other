#include <stdio.h>
#include <vector>

// 条件检验
bool constrait(std::vector<int> v) {
    int A=v[0],B=v[1],C=v[2],D=v[3],E=v[4];
     if(A+B+C+D+E==15 && A*B*C*D*E==120) {
        if(((A==1)+(B==2)+(C==3)+(D==4)+(E==5)==0) && ((B-A)==1)+((C-B)==1)+((D-C)==1)+((E-D)==1)==0) {
            if(((D==1)+(A==2)+(E==3)+(C==4)+(B==5)==2) && (((A-D)==1)+((E-A)==1)+((C-E)==1)+((B-C)==1))==2) {
                printf("%d%d%d%d%d\n",A,B,C,D,E);
                return true;
            }
        } 
    }
    return false;
}


std::vector<int> path;
/**
 * @param n     数字个数
 * @param used  当前数字是否使用过
*/
void backtracking(int n, bool used[]) {
    if(path.size() == n) {
        int A=path[0],B=path[1],C=path[2],D=path[3],E=path[4];
        printf("A:%d B:%d C:%d D:%d E:%d\n",A,B,C,D,E);
        if(constrait(path))
            exit(0);
        return;
    }
    for(int i=1; i<=n; i++) {
        if(used[i]) continue;
        used[i] =true;
        path.push_back(i);
        backtracking(n,used);
        used[i] = false;
        path.pop_back();
    }
}

/**
 * @brief 转换为给定一个数字 n, 取值[1,n],要求满足constrait, 输出唯一可能
 *      使用回溯算法,暴力递归,并记忆存储结果
*/
void test4() {
    bool used[6] = {false};
    backtracking(5, used);
}

/**
 * @brief promote version 1.1
 *      优化了最后一层循环E, 以及对数字的去重
 * 
 */
void test2() {

    int A,B,C,D,E=0;
    for(A=1;A<=5;A++) {
        for (B=1;B<=5; B++){
            if (B-A==0) continue;
            for (C=1;C<=5; C++){
                if ((C-B==0)||(C-A==0)) continue;
                for (D=1;D<=5; D++){
                    if ((D-C==0)||(D-B==0)||(D-A==0)) continue;

                    E=(15-(A+B+C+D));
                    printf("A:%d B:%d C:%d D:%d E:%d\n",A,B,C,D,E);
                     // constrait
                    if(A+B+C+D+E==15 && A*B*C*D*E==120) {
                        if(((A==1)+(B==2)+(C==3)+(D==4)+(E==5)==0) && ((B-A)==1)+((C-B)==1)+((D-C)==1)+((E-D)==1)==0) {
                            if(((D==1)+(A==2)+(E==3)+(C==4)+(B==5)==2) && (((A-D)==1)+((E-A)==1)+((C-E)==1)+((B-C)==1))==2) {
                                printf("%d%d%d%d%d\n",A,B,C,D,E);
                                return;
                            }
                        } 
                    }
                    
                }
            }   
        }  
    }
}

/**
 * @brief original version 1.0
 *      使用五层for循环实现数字搜索
 * 
 */
void test1() {
    int A,B,C,D,E;
    for(A=1;A<=5;A++) {
        for (B=1;B<=5; B++){
            for (C=1;C<=5; C++){
                for (D=1;D<=5; D++){
                    for (E=1;E<=5; E++){
                        // constrait
                        if(A+B+C+D+E==15 && A*B*C*D*E==120) {
                           if(((A==1)+(B==2)+(C==3)+(D==4)+(E==5)==0) && ((B-A)==1)+((C-B)==1)+((D-C)==1)+((E-D)==1)==0) {
                                if(((D==1)+(A==2)+(E==3)+(C==4)+(B==5)==2) && (((A-D)==1)+((E-A)==1)+((C-E)==1)+((B-C)==1))==2) {
                                    printf("%d%d%d%d%d\n",A,B,C,D,E);
                                }
                           } 
                        }
                        
                    }
                }
            }   
        }  
    }
}

int main()
{
    // test1();
    // test2();
    // test3();
    test4();
    return 0;
}
