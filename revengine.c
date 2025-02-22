#include <stdio.h>
#include <string.h>

int main() {
    char password[32];
    char flag[] = "CTF{Reverse_Engineering_Flag}";

    printf("Masukkan password untuk mendapatkan flag: ");
    scanf("%31s", password);

    if (strcmp(password, "CTF12345") == 0) {
        printf("Selamat! Flag Anda: %s\n", flag);
    } else {
        printf("Password salah. Coba lagi!\n");
    }

    return 0;
}
