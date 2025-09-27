#include <stdlib.h>
#include <stdio.h>

struct Cadastros
{
    char Nome[50];
    int Idade;
    char Cargo[50];
    float Salario;
};

int main(){
    int Quant_Cadastros;
    printf("Digite quantos cadastros teremos: ");
    scanf("%d", &Quant_Cadastros);
    struct Cadastros Base[Quant_Cadastros];

    /*
    Registro
    */
    for (int i=0; i<Quant_Cadastros;i++){
        printf("Digite o Nome:  ");
        scanf("%s", Base[i].Nome);
        printf("Digite a Idade:  ");
        scanf("%i", &Base[i].Idade);
        printf("Digite o Cargo:  ");
        scanf("%s", Base[i].Cargo);
        printf("Digite o salario:  ");
        scanf("%f", &Base[i].Salario);
        printf("\n");
    }
    printf("/////////////////////////////////////////////\n");
    /*
    Demonstração do registro
    */
    for (int j=0; j<Quant_Cadastros;j++){
        printf("Cadastro [%i]", j+1);
        printf("\nNome:  %s", Base[j].Nome);
        printf("\nIdade: %i", Base[j].Idade);
        printf("\nCargo: %s", Base[j].Cargo);
        printf("\nSalario: %.2f", Base[j].Salario);
        printf("\n\n");
    }
    system("pause");
    return 0;    
}
