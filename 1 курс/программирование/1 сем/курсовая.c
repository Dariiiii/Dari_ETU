#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#define MEM_STPEP 5
//typedef ==//==
//{}название;
struct Sentence{
    char *str;
    size_t size;//!= strlen(str) размер буффера, не длина 
};
struct Text{
    struct Sentence **sents;
    int n;
    int size;
};

struct Sentence* readSentence();

void sentProc(struct Sentence* sent, int k,int m){
// sent->str === char*=== string
// k- индекс начиная с которого мы хотим удалить символы 
// m- сколько мы хотим удалить элементов
//удаление==сдвиг 
// memmove(куда,откуда,сколько) ++++ когда кусочки пересекаются
int len = strlen(sent->str);
memmove((sent->str)+k, (sent->str)+k+m, len-m-k+1);
}
struct Text readText(){//возвращаем не указатель (!)
    int size =MEM_STPEP;
    struct Sentence** text = malloc(size*sizeof(struct Sentence*));
    int n=0; 
    struct Sentence* temp;
    int nlcount=0;
    do{
            temp = readSentence();//храним указатели на предложения
            if(temp ->str[0]=='\n')
                nlcount++;
                //утечка памяти
            else{
                nlcount=0;
                text[n]=temp;
                n++;
               // puts(temp ->str);
            }
    }while(nlcount<2);
    struct Text txt;
    txt.size=size;
    txt.sents= text;
    txt.n=n;
    return txt;
    //struct Text txt = {.size = size, .sents = text, .n = n};
}

struct Sentence* readSentence(){
    int size = MEM_STPEP;
    char *buf =malloc(size*sizeof(char));
    char temp;
    int n=0;
    //printf("size=%d\n",size);
    do{
        if (n >= size-2){
            char *t=realloc(buf,size+MEM_STPEP);
            if (!t){/*  ERROR */}
            size+=MEM_STPEP;
            buf= t;
            //printf("size=%d\n",size);
        }
        temp =getchar();
        buf[n]=temp;
        n++;
        //printf(">%c\n",temp);
    }while( temp!='\n' && temp!='.' && temp!='!');

    buf[n]='\0';
    struct Sentence *sentence = malloc(sizeof(struct Sentence));
    sentence ->str = buf; //(*sentence).str=buf(точка главная, без скобок будет ошибка)
    sentence ->size = size;
    return sentence;
}
int main(){
    struct Text text= readText();
    sentProc(text.sents[0],2,5);
    for (int i =0;i<text.n;i++)
        puts(text.sents[i]->str);
    //struct Sentence *s = readSentence();
    //puts(s ->str);
    //free(s ->str);
    //free(s);

    return 0;
}