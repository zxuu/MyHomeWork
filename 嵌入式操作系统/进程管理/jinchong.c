#include <stdio.h>
//#include <conio.h>p
#include <stdlib.h>
struct PCB_type
{  int pid;
   int youxianji;
   int daxiao;
   char neirong[10];
   int state;     /* 0��ʾ�����ڴ棬1��ʾ���ڴ棬2��ʾ����*/ 
};
struct PCB_type neicun[20];
int num=0,guaqi=0,bj,i,j,pid;/*������ز�������*/
/*********************�����½���*************************/
void create()
{  
    if(num>=20)   /*�ж��Ƿ��д洢�ռ�*/
        printf("\n �ڴ���������ɾ���������������");
    else{
        for(i=0;i<20;i++)
         if(neicun[i].state==0) break; /*��˳�����ڴ���Ѱ�Ҵ����½��̵Ŀռ�*/
           printf("\n�������½����̵�pidֵ\n");
           scanf("%d",&neicun[i].pid);
           for(j=0;j<i;j++)   /*�ж��Ƿ�֮ǰ�Ѵ洢��ͬpid����*/
              if(neicun[j].pid==neicun[i].pid)
              {  printf("\n�ý����Ѵ������ڴ���");
                  return;
              }
              printf("\n�������½��̵����ȼ� \n" ); 
            scanf("%d",&neicun[i].youxianji);
            printf("\n�������½��̵Ĵ�С\n" ); 
          scanf("%d",&neicun[i].daxiao);
          printf("\n�������½��̵�����\n" ); 
          scanf("%s",&neicun[i].neirong);
              neicun[i].state=1;    /*������״̬��Ϊ1����ʾ���ڴ���*/
             num++;/*�ڴ��н�����Ŀ��һ*/
    }
}
/********************�鿴��ǰ���н���**************************/
void run()
{  bj=0;
    for(i=0;i<20;i++)
if(neicun[i].state==1)   /*������״̬��Ϊ1����ʾ���ڴ��У�����鿴*/
{printf("\n pid=%d",neicun[i].pid);
 printf("   youxianji=%d",neicun[i].youxianji);
 printf("   daxiao=%d",neicun[i].daxiao);
 printf("   neirong=%s",neicun[i].neirong);
 bj=1;/*�������ڴ��еĽ��̱��Ϊ1 */
}
 if(bj==0)  
 printf("\n��ǰû�����иý���\n" );/*���Ϊ0����ʾ�ý���δ�������ڴ���*/ 

}
/********************��������***************************/

void huanchu()
{if(num==0)  /*num=0,��ʾ�ڴ����޽���*/
  { printf("\n��ǰû�����еĽ���\n" );
    return;
  } 
    printf("\n������Ҫ�����Ľ��̵�pidֵ\n" );
    scanf("%d",&pid);
    bj=0;
    for(i=0;i<20;i++)
      {
        if(pid==neicun[i].pid)
         { if(neicun[i].state==1)
           {neicun[i].state=2; /*���ý��̵�״̬��Ϊ����*/
            guaqi++;
            printf("\n�ý����ѳɹ����𻻳�\n" );
           }
           else if(neicun[i].state==0)
           printf("\nҪ�����Ľ��̲�����\n" );
           else printf("\nҪ�����Ľ����Ѿ�������\n" ); 
           bj=1;break;
         }
    }
    if(bj==0) printf("\nҪ�����Ľ��̲�����\n" );
}  
/********************ɱ������***************************/
void kill()
{
  if(num==0)
  { printf("\n��ǰû�����еĽ���\n" );
    return;
  }
 printf("\n������Ҫɱ���Ľ��̵�pidֵ\n" );
    scanf("%d",&pid);
    bj=0;
    for(i=0;i<20;i++)
      {
        if(pid==neicun[i].pid)
         { if(neicun[i].state==1)
           {neicun[i].state=0; /*���ý��̵�״̬��Ϊ�����ڴ���*/
            num--;  /*�ڴ��еĽ�����Ŀ����һ��*/
           printf("\n�ý����ѳɹ�ɱ��\n" );
           }
           else if(neicun[i].state==0)
           printf("\nҪɱ���Ľ��̲�����\n" );
           else printf("\nҪɱ���Ľ����Ѿ�������\n" );/*ʣ��״̬Ϊ2������*/
        bj=1;break;
        }
      } 
    if(bj==0) printf("\nҪɱ���Ľ��̲�����\n" );
  }
/********************���ѽ���***************************/
void huanxing()
{ 
  if(num==0) 
  { printf("��ǰû�����еĽ���\n");
    return;
  }
  if(guaqi==0)  /*guaqi=0,��ʾû�й���Ľ���*/
  { printf("\n��ǰû�л����Ľ���\n");
    return;
  }
  printf("\n������Ҫ���ѵĽ��̵�pidֵ:\n");
  scanf("%d",&pid);
    for(i=0;i<20;i++){
    if(pid==neicun[i].pid)
    {
          if(neicun[i].state==2)
           {neicun[i].state=1; /*���ý��̵�״̬��Ϊ����*/
            guaqi--;
            num++;
            printf("\n�ý����ѳɹ�����\n" );
           }
           else if(neicun[i].state==0)
           printf("\nҪ���ѵĽ��̲�����\n" );
           else printf("\nҪ���ѵĽ����Ѿ����ڴ���\n" );
         }
    }
  } 
/********************������***************************/
void main()
{int xuhao,n=1,i;
for(i=0;i<20;i++)
   neicun[i].state=0; /*ʹ���н��̶���ʼ��Ϊ�����ڴ���*/
while(n){
printf("\n**********************************************");
printf("\n*               ������ʾϵͳ                 *");
printf("\n**********************************************");
printf("\n     1.�����µĽ���             2.�鿴���н���");
printf("\n     3.����ĳ������             4.ɱ�����н���");
printf("\n     5.����ĳ������             6.�˳�����    ");
printf("\n**********************************************");
printf("\n��ѡ��(1��6):");
       scanf("%d",&xuhao);
       switch(xuhao)
            { 
              case 1: create( ); break;
              case 2 :run(); break;
              case 3 :huanchu();break;
              case 4 :kill();break;
              case 5 :huanxing();break;
              case 6 :exit(0);
              default: n=0;
              break;
             }
}
}
