#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include<ctype.h>

#define MEMORY_1 1000
#define MEMORY_2 100
#define MEMORY_3 10

//--------------------------STRUCT--------------------------------

typedef struct Word {
    char *word;
    int len;
    char char_end;
    int size;
} Word;

typedef struct Sentence {
    Word *sent;
    int len_sen;
    int size;
} Sentence;


typedef struct Text {
    Sentence *text;
    int len_text;
    int size;
} Text;

//------------------FREE---------------------------------------

void free_Word(Word *word) {
    free(word->word);
    word->size = 0, word->len = 0, word->char_end = 0;
}

void free_Sentence(Sentence *sent) {
    for (int i = 0; i < sent->len_sen; ++i)
        free_Word(&sent->sent[i]);
    free(sent->sent);
    sent->size = 0, sent->len_sen = 0;
}

void free_Text(Text *txt) {
    for (int i = 0; i < txt->len_text; ++i)
        free_Sentence(&txt->text[i]);
    free(txt->text);
    txt->size = 0, txt->len_text = 0;
}

//-------------------READ----------------------------------------

Word read_Word(Word *word) {
    word->size = MEMORY_3;
    word->word = (char *) malloc(word->size * sizeof(char));
    word->len = 0;
    word->char_end = 'a';
    do {
        if (word->len > word->size - 2) {
            word->size *= 2;
            word->word = (char *) realloc(word->word, word->size * sizeof(char));
            if (word->word == NULL) {
                puts("Невозможно выделить память");
                exit(0);
            }
        }
        word->word[word->len] = getchar();
        word->len++;
    } while (word->word[word->len - 1] != ' ' && word->word[word->len - 1] != ',' && word->word[word->len - 1] != '.' &&
             word->word[word->len - 1] != '\n');
    word->word[word->len] = '\0';
    word->char_end = word->word[word->len - 1];
    return *word;
}

Sentence read_Sentence(Sentence *sent) {
    sent->size = MEMORY_2;
    sent->sent = (Word *) malloc(sent->size * sizeof(Word));
    char flag = 0;
    sent->len_sen = 0;
    do {
        if (sent->len_sen >= sent->size - 2) {
            sent->size = sent->size * 2;
            sent->sent = (Word *) realloc(sent->sent, sent->size * sizeof(Word));
            if (sent->sent = NULL) {
                puts("Невозможно выделить память");
                exit(0);
            }
        }
        sent->sent[sent->len_sen] = read_Word(&sent->sent[sent->len_sen]);
        flag = sent->sent[sent->len_sen].char_end;
        sent->len_sen++;
    } while (flag != '.' && flag != '\n');
    return *sent;
}

void read_Text(Text *txt) {
    txt->size = MEMORY_1;
    txt->text = (Sentence *) malloc(txt->size * sizeof(Sentence));
    char flag = 0;
    txt->len_text = 0;
    do {
        if (txt->len_text >= txt->size - 2) {
            txt->text = (Sentence *) realloc(txt->text, txt->size * 2 * sizeof(Sentence));
            txt->size = txt->size * 2;
            if (txt == NULL) {
                puts("Невозможно выделить память");
                exit(0);
            }
        }
        txt->text[txt->len_text] = read_Sentence(&txt->text[txt->len_text]);
        flag = txt->text[txt->len_text].sent->char_end;
        txt->len_text++;
    } while (flag != '\n');
}

//------------------------FUNC---------------------------------

char **tolower_word(Sentence *sent) {
    int k1 = sent->len_sen;
    char **res = (char **) malloc(sent->len_sen * sizeof(Word));
    for (int i = 0; i < k1; i++) {
        res[i] = (char *) malloc(100);
        for (int j = 0; j < strlen(sent->sent[i].word); j++)
            res[i][j] = tolower(sent->sent[i].word[j]);
    }

    return res;
}

char *tolower_sent(Sentence *sent) {
    int k1 = sent->len_sen;
    int k2 = sent->sent[0].len;
    char *res = (char *) malloc(sent->len_sen * sizeof(Word));
    char *sentence = (char *) malloc(sent->len_sen * sizeof(Word));
    sentence = strcat(sentence, sent->sent[0].word);
    for (int i = 1; i < k1; i++) {
        k2 += sent->sent[i].len;
        char *str = sent->sent[i].word;
        sentence = strcat(sentence, str);
    }
    for (int i = 0; i < k2; i++) {
        res[i] = tolower(sentence[i]);
    }
    return res;
}

int identical_sent(Sentence *sent_1, Sentence *sent_2) {
    char *s1 = tolower_sent(sent_1);
    char *s2 = tolower_sent(sent_2);
    if (strcmp(s1, s2) == 0)
        return 1;
    return 0;
}

void rm_sent(Text *txt, int id) {
    if (id < 0 || id >= txt->len_text)
        return;
    free_Sentence(&txt->text[id]);
    memmove(&txt->text[id], &txt->text[id + 1], (txt->len_text - id - 1) * sizeof(Sentence));
    txt->text = (Sentence *) realloc(txt->text, sizeof(Sentence) * (--txt->len_text));
    if (txt->text == NULL) {
        puts("Невозможно выделить память");
        exit(0);
    }
    txt->size = txt->len_text;
}

void rm_three_up(Text *txt) {
    int count_up = 0;
    for (int i = 0; i < txt->len_text; i++) {
        for (int j = 0; j < txt->text[i].len_sen; j++) {
            for (int k = 0; k < txt->text[i].sent[j].len; k++) {
                if (isupper(txt->text[i].sent[j].word[k]) != 0) {
                    count_up++;
                } else {
                    count_up = 0;
                }
                if (count_up == 3) {
                    count_up = 0;
                    rm_sent(txt, i);
                    i = 0;
                    k = 0;
                    j = 0;
                }
            }
        }
    }
}

void rm_identical_sent(Text *txt) {
    for (int i = 0; i < txt->len_text; ++i)
        for (int j = txt->len_text - 1; j > i; --j)
            if (identical_sent(&txt->text[i], &txt->text[j])) {
                rm_sent(txt, j);
            }
}

void dump_txt(Text *txt) {
    char **s = (char **) malloc(1000);
    char orig[] = "garbage";
    int count_garbage = 0;
    for (int i = 0; i < txt->len_text - 1; i++) {
        s = tolower_word(&txt->text[i]);
        for (int j = 0; j < txt->text[i].len_sen; j++) {
            if (strncmp(s[j], orig, 7) == 0)
                count_garbage++;
        }
        if (count_garbage == 0)
            puts("Clean");
        else if (count_garbage < 6 && count_garbage > 0)
            puts("Must be washed");
        else if (count_garbage > 5)
            puts("It is a dump");
        free(s);
        count_garbage = 0;
    }
}

int count_vowels_word(Sentence *sent) {
    int count_w = 0;
    const char *st = "AEIOUYaeiouy";
    for (int i = 0; i < sent->len_sen; i++) {
        char ch_0 = sent->sent[i].word[0];
        if (strchr(st, ch_0) != NULL) {
            count_w++;
        }
    }
    return count_w;
}

int sent_comparison(const void *s1, const void *s2) {
    Sentence *s_1 = (Sentence *) s1;
    Sentence *s_2 = (Sentence *) s2;
    int count_s_1 = count_vowels_word(s_1);
    int count_s_2 = count_vowels_word(s_2);
    return count_s_2 - count_s_1;
}

void sort_vowels_count(Text *txt) {
    qsort(txt->text, txt->len_text, sizeof(Sentence), sent_comparison);
}


void replace_numbers(Text *txt) {
    Word *str_r = (Word *) malloc(MEMORY_2 * sizeof(Word));
    *str_r = read_Word(str_r);
    str_r->word[str_r->len - 1] = '\0';
    for (int i = 0; i < txt->len_text; i++) {
        for (int j = 0; j < txt->text[i].len_sen; j++) {
            for (int k = 0; k < txt->text[i].sent[j].len; k++) {
                if (isdigit(txt->text[i].sent[j].word[k]) != 0) 
                    printf("%s", str_r->word);
                else
                    printf("%c", txt->text[i].sent[j].word[k]);


            }

        }

    }

}

void display_text(Text *txt) {
    for (int i = 0; i < txt->len_text; i++) {
        for (int j = 0; j < txt->text[i].len_sen; j++)
            printf("%s", txt->text[i].sent[j].word);
    }

}

//---------------------------MAIN-----------------------------

int main() {
    Text txt;
    puts("Введите текст:");
    read_Text(&txt);
    rm_identical_sent(&txt);
    char fn;
    puts("Введите 0, чтобы выйти из программы");
    puts("Введите 1, чтобы каждого предложения посчитать количество слов “garbage” в нем (без учета регистра).");
    puts("Введите 2_строкa , чтобы заменить все цифры в предложениях на введенную строку.");
    puts("Введите 3, чтобы удалить все предложения в которых есть три подряд идущие буквы в верхнем регистре.");
    puts("Введите 4, чтобы отсортировать по уменьшению количества слов начинающихся с гласной буквы.");
    printf("Ваш выбор: ");
    scanf("%c_", &fn);
    switch (fn) {
        case '0':
            puts("Вы покинули программу!");
            break;
        case '1':
            dump_txt(&txt);
            display_text(&txt);
            break;
        case '2':
            replace_numbers(&txt);
            break;
        case '3':
            rm_three_up(&txt);
            display_text(&txt);
            break;
        case '4':
            sort_vowels_count(&txt);
            display_text(&txt);
            break;
        default:
            puts("Ваш выбор некорректный");
            exit(0);
    }
    free_Text(&txt);
    return 0;

}