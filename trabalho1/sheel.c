#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <string.h>

bool flag = false;

void signal_handler(int sigNumber)
{
  if (sigNumber == SIGUSR1){
    printf("Recebi um SIGUSR1\n");
    flag = true

  }
}

int main() {

while (true){
  flag = false;


  char *bin = "/bin/";
  char escrever[101];
  char *args[20];
  int num_arg;

  pid_t child_pid = fork();
  if (child_pid == 0) {
    printf("Qual o comando quer executar?\n");
    scanf("%100s",escrever);
    printf("Quantos argumentos voce quer digitar?\n");
    scanf("%d",&num_arg);

    for (int count = 0; count < num_arg; count++) {
      printf("Digite o argumento %d\n",count);
      scanf("%s",args[count]);
    }
    const char * destPtr = (const char *)args[0];
    strcat(bin,destPtr);
    const char * binconst = (const char *)bin;
    printf("%s",binconst);
    execlp("/bin/ping","ping","8.8.8.8","-c","50",NULL);//binconst,args[0],args[1],NULL);
    return 0;
  } else {
    wait(NULL);
    printf("Task is done\n");
    return 0;
  }
}


};
