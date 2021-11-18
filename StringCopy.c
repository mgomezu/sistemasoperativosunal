#include <stdio.h>

void so_strcpy(char str1[], char str2[]){

    for (int i = 0; str1[i]!='\0' ; i++) {
        str2[i] = str1[i];
    }
}

int main()
{
    char string1 []= "cadena1";
    char string2 [sizeof(string1)];
    so_strcpy(string1,string2);
    printf("String2 es %s", string2);

    return 0;
}
