#include <stdio.h>

// Criar um vetor com valores recebido pelo usuario.

int main(){

	int valores[7];
	int numero;

	for(int i = 0; i < 6; i++){
		printf("informe 6 valores para o vetor {%d}: ", i + 1);
		scanf("%d", &numero);
		valores[i] = numero;
	}

	printf("Os valores do vetor são: ");

	for(int i = 0; i < 6; i++){
		printf("%d ", valores[i]);
	}
	return 0;
}
