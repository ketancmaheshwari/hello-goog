#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char ** argv){

    char * astring;
    char * bstring;
    
    astring = malloc(200 * sizeof(char*));
    bstring = malloc(200 * sizeof(char*));

    strcpy(astring, "Hello world hello world abracadabra");
    strcpy(bstring, astring);

    puts(bstring);

    return 0;
}
