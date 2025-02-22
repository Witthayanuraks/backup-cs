#include <stdio.h>

void print_flag() {
    printf("Selamat! Anda menemukan flag: CTF{Format_String_Vuln}\n");
}

int main() {
    char input[64];

    printf("Masukkan sesuatu: ");
    fgets(input, sizeof(input), stdin);

    // Kerentanan: input pengguna langsung dimasukkan ke format string
    printf(input);

    printf("Terima kasih telah menggunakan program ini!\n");
    return 0;
}
