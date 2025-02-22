#include <stdio.h>
#include <string.h>

int check_password(char *password) {
    if (strlen(password) != 8) {
        return 0;
    }
    if (password[0] != 'C' || password[1] != 'T' || password[2] != 'F') {
        return 0;
    }
    if (password[3] != '{' || password[7] != '}') {
        return 0;
    }
    if (password[4] != '1' || password[5] != '2' || password[6] != '3') {
        return 0;
    }
    if (password[7] != '1' || password[8] != '2' || password[9] != '3') {
        return 0;
    }
    if (password[10] != '1' || password[11] != '2' || password[12] != '3'){
        return 0;
    }
    return 1;
}

int main() {
    char password[32];

    printf("Insert Password : ");
    scanf("%31s", password);

    if (check_password(password)) {
        printf("[O] : %s\n", password);
    } else {
        printf("[R] Salah \n");
    }


    return 0;

    // Tips: Gunakan fgets() jika inputan password bisa mengandung spasi.
    // Tanpa fgets(), karakter-karakter yang diinputkan user akan disimpan di password,
    // jadi pastikan password memiliki panjang yang sesuai.
    // Tanpa fgets(), password hanya akan terbatas pada panjang yang ditentukan (32).

    // Alternatif:
    while (true) {
        printf("ini dah benar")
        break;
    }
}
