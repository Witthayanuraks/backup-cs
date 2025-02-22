#include <stdio.h>
#include <string.h>


void print_secret() {
    printf("Selamat datang di tantangan CTF!\n");
}

void secret_function() {
    printf("Test any\n");
    print_secret();
}

void vulnerable_function() {
    char buffer[32];
    printf("Input:");
    fgets(buffer, sizeof(buffer), stdin);  // Buffer overflow
    buffer[strcspn(buffer, "\n")] = 0;  // Hapus newline character
    printf("Inputan: %s\n", buffer);
}
void print_flag() {
    char flag[] = "CTF{Buffer_Overflow_Exploitation}";
    printf("Flag: %s\n", flag);
}

int main() {
    printf("Selamat datang di tantangan CTF!\n");
    vulnerable_function();
    secret_function();
    print_flag();
    printf("Program selesai.\n");
    return 0;
}
