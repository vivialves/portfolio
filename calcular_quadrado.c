#include <stdio.h>

int main(){

	// receber valores do usuário para um vetor e calcular o quadrado dos valores montando outro vetor.

	float A[5];
	float B[5];
	float numero;

	for(int i = 0; i < 5; i++){
		printf("Informe 5 números para o vetor {%d}: ", i + 1);
		scanf("%f", &numero);
		A[i] = numero;
		B[i] = numero * numero;
	}

	printf("Os valores do primeiro vetor são: ");

	for(int i = 0; i < 5; i++){
		printf("%.2f ", A[i]);
	}

	printf("\n");

	printf("Os valores do segundo vetor são: ");

	for(int i = 0; i < 5; i++){
		printf("%.2f ", B[i]);
	}

	return 0;
}
