#include <stdio.h>
#include <string.h>

void win() {
    printf("Selamat! Anda menemukan flag: CTF{Stack_Overflow}\n");
}

void vuln() {
    char buffer[32];
    printf("Masukkan input Anda: ");
    gets(buffer);
    printf("Inputan Anda: %s\n", buffer);
}

int main() {
    printf("Selamat datang di tantangan buffer overflow!\n");
    vuln();
    printf("Program selesai.\n");
    return 0;
}
