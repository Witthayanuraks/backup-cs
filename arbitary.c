#include <stdio.h>
#include <stdlib.h>

int main() {
    char command[128];
 
    printf("Masukkan perintah yang ingin dijalankan: ");
    fgets(command, sizeof(command), stdin);
    command[strcspn(command, "\n")] = 0;  // Hapus newline character
    printf("Perintah yang dipilih: %s\n", command);
    printf("Hasil eksekusi perintah: ");
    fflush(stdout);  // Tunda output sebelum eksekusi perintah
    system(command);
}
