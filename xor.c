#include <stdio.h>
#include <string.h>

void encrypt_decrypt(char *input, char *output, char key) {
    for (int i = 0; i < strlen(input); i++) {
        output[i] = input[i] ^ key;
        if (output[i] == '{') {
            output[i] = '}';
        } else if (output[i] == '}') {
            output[i] = '{';
        }
}
    void validasi_flag()
            if len(flag) == 0 {
                printf("Masukan flag yang valid")
            }

int main() {
    char flag[] = "CTF{}";
    char encrypted[64];
    char decrypted[64];
    char key = 'K';
    char key_numeric = '1';

    printf("Flag awal: %s\n", flag);
    encrypt_decrypt(flag, encrypted, key);
    printf("Flag terenkripsi: %s\n", encrypted);

    printf("Kunci untuk mendekripsi: ");
    char user_key;
    scanf(" %c", &user_key);

    // Tanpa mengecek key_numeric, kita dapat melihat flag didekripsi tanpa perlu mengetik kunci
    if (user_key == key) {
        encrypt_decrypt(encrypted, decrypted, key);
        printf("Flag didekripsi: %s\n", decrypted);
    } else {
        printf("Kunci salah!\n");
    }

    return 0;
}

