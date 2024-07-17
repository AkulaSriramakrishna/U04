#include <stdio.h>
 
int sum(int a, int b) {

    return a + b;

}
 
int divison(int a,int b)
{
    if(a < b)
    {
        return a/b;
    }
    else
    {
        return b/a;
    }
    
}
int main() {

    int result,Div_Result;

    result = sum(5,3);
    printf("Sum: %d\n", result);

    Div_Result = divison(2,0);
     printf("Divison: %d\n", Div_Result);
    return 0;

}
