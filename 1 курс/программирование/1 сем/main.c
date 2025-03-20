#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include <ctype.h>

#define MEMORY 200


typedef struct Sentence {
    char *str;
    int len;
} Sentence;


typedef struct Text {
    struct Sentence **sents;
    int size;
    int len;
    int real_len;
} Text;

Sentence *readSentence() {
    int size = MEMORY;
    char *buf = malloc(size * sizeof(char));
    char temp;
    int n = 0;
    do {
        if (n >= size - 2) {
            char *t = realloc(buf, size * 2);
            if (t) {
                size *= 2;
                buf = t;
            }
        }
        temp = getchar();
        if (temp == '\n') {
            temp = ' ';
        }
        buf[n] = temp;
        n++;
    } while (temp != ';' && temp != '.' && temp != '?' && temp != '!');
    buf[n] = '\0';
    Sentence *sentence = malloc(sizeof(Sentence));
    sentence->str = buf;
    sentence->len = n;
    return sentence;
}

Text *readText() {
    int size = MEMORY;
    Sentence **text = malloc(size * sizeof(Sentence *));
    char end = '\0';
    int n = 0;
    int k = 0;
    Sentence *temp;
    do {
        if (n >= size - 2) {
            Sentence **t = realloc(text, size * 2);
            if (t) {
                text = t;
                size *= 2;
            }
        }
        temp = readSentence();
        int end_s = strlen(temp->str);
        if (temp->str[end_s - 1] != '?') {
            text[k] = temp;
            k++;
        }
        n++;
    } while ((temp->str[(temp->len) - 1]) != '!');
    Text *txt = malloc(sizeof(Text));
    txt->real_len = k;
    txt->len = n;
    txt->sents = text;
    txt->size = size;
    return txt;
}

void del_tab(Text txt, int n) {
    for (int i = 0; i < n; i++) {
        if (((((txt.sents)[i]->str)[0]) == '\t') || ((((txt.sents)[i]->str)[0]) == ' ')) {
            char *old_in = &txt.sents[i]->str[0];
            char *new_in = &(txt.sents[i]->str[0]) + 1;
            int l = strlen(txt.sents[i]->str);
            memmove(old_in, new_in, l);
        }
    }
}

int main() {
    Text *text = readText();
    Text t = *text;
    int size = t.size;
    int n = text->len;
    int k = t.real_len;

    del_tab(t, k);
    del_tab(t, k);
    puts("------------------------------");
    for (int i = 0; i < k; i++)
        printf("%s\n", t.sents[i]->str);
    printf("Количество предложений до %d и количество предложений после %d", n - 1, k - 1);
    return 0;
}