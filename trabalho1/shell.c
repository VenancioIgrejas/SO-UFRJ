#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <string.h>

int flag = 0;
//----------------------------------------------------//
void signal_handler(int sigNumber)
{
  if (sigNumber == SIGUSR1){
    printf("Recebi um SIGUSR1\n");
    flag = 1;

  }
}



int main() {

  signal(SIGTERM, signal_handler);
  while (1){
    flag = 0;


    char bin[100];
    char escrever[101];
    char *args[10];

    int num_arg;
    char arquivo[10];

    printf("Qual o comando quer executar?\n");
    scanf("%100s",escrever);
    strcpy(bin,"/bin/");
    strcat(bin,escrever);
    printf("aquii");
    strcat(args[0],escrever);

    if (flag == 1){continue;}
    printf("Quantos argumentos voce quer digitar?\n");
    scanf("%d",&num_arg);
    if (flag == 1){continue;}

    for (int count = 0; count < num_arg; count++) {
      printf("Digite o argumento %d\n",count);
      scanf("%s",arquivo);
      strcat(args[count+1],arquivo);
    }


    //printf("Digite o nome do arquivo para imprimira saida ou ENTER para imprimir na tela\n");
    //scanf("%s",arquivo);
    //printf("%s\n",arquivo);

    //const char * destPtr = (const char *)args[0];
    //strcat(bin,destPtr);
    //const char * binconst = (const char *)bin;
    //printf("%s",binconst);
    //strcat(args)

    pid_t child_pid = fork();
    if (child_pid == 0) {
      printf("%s\n",bin);
      printf("%s\n",args[0]);
      execv(bin,args);
      //execlp("/bin/ping","ping","8.8.8.8","-c","50",NULL);//binconst,args[0],args[1],NULL);
      return 0;
    } else {
      wait(NULL);
      printf("Task is done\n");
      return 0;
    }
  }
  sleep(1);

};
