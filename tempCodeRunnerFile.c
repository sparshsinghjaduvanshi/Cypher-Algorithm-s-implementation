#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>
#include <ctype.h>   

int main(int argc, char *argv[]){
    // Check if the user provided exactly one command-line argument
    if(argc == 2){

        // Convert the command-line argument to an integer
        int key = atoi(argv[1]) % 26;
        // Check if the key is a valid positive integer
        bool valid_key = false;

        //check validity of the key by checking if all characters in the argument are digits
        for(int i = 0; i < strlen(argv[1]); i++){

            if(isdigit(argv[1][i])){
                valid_key = true;
            }else{
                valid_key = false;
                break;
            }
        }

        if(valid_key == true){
            char input[500];
            printf("plaintext: ");
            fgets(input, sizeof(input),stdin);

           
            //check for upper and l0wer case letters and apply the caesar cipher accordingly
            for(int i = 0; i < strlen(input); i++){
                if(isupper(input[i])){
                    printf("input value: %d\n", input[i]);
                    input[i] = (input[i] - 'A' + key) % 26 + 'A';
                }else if(islower(input[i])){
                    printf("input value: %d\n", input[i]);
                    input[i] = (input[i] - 'a' + key) % 26 + 'a';
                }
            }
            printf("ciphertext: %s", input);
        }

    }else{
        printf("Usage ./caesar key\n");
    }
}