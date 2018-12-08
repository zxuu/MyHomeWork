#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<fcntl.h>
#include<unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>
#include <fcntl.h>
#include <unistd.h>
#include<syslog.h>
/*
 *以上两个头文件包含了open(),close()等
 *函数的声明,以及相关的一些宏
 */

#include<errno.h>
void my_err(const char *err_string , int line){
//错误处理函数
    fprintf(stderr,"line: %d",line);
    perror(err_string);
    exit(0);
}
void Readfile(){
    //通过文件描述符来读取文件
    int fd,len,ret;
    char read_buf[64];
    if((fd=open("test.txt",O_RDONLY)) == -1){
     //这里一系列宏即表示文件打开方式
        my_err("open",__LINE__);
    }else{
        printf("打开文件成功!\n");
    }
    if(lseek(fd,0,SEEK_END) == -1){
    //先将文件内部指针从任意位置移到结尾
        my_err("lseek",__LINE__);
    }
    if((len=lseek(fd,0,SEEK_CUR)) == -1){
    //返回当前位置(结尾)距离文件开头的偏移值,即就是文件大小
        my_err("lseek",__LINE__);
    }
    if(lseek(fd,0,SEEK_SET) == -1){
    //将文件内部指针已到文件开头以便于后面读取
        my_err("lseek",__LINE__);
    }
    printf("文件长度: %d\n",len);
    if((ret=read(fd,read_buf,sizeof(read_buf))) == -1){
        my_err("read",__LINE__);
    }

    for(int i=0;i<len;i++){
        printf("%c",read_buf[i]);
    }
    printf("\n");
}
void Createfile(){
    int fd;
    //char write_buf[32] = "97520";
    if((fd=open("test.txt",O_CREAT)) == -1){
     //这里一系列宏即表示文件打开方式
        my_err("open",__LINE__);
    }else{
        printf("文件创建成功!\n");
    }
}

void Writetext(){
    int fd;
    char write_buf[32] = "zhaoxu";
    if((fd=open("test.txt",O_RDWR|O_APPEND)) == -1){
     //这里一系列宏即表示文件打开方式
        my_err("open",__LINE__);
    }else{
        printf("打开文件成功!\n");
    }
    if(write(fd,write_buf,strlen(write_buf)) != strlen(write_buf)){
    //向文件中写入一条数据
        my_err("open",__LINE__);
    }else{
         printf("写入文件成功！");
    }
}
void cppyfile(){
    char sfile[50], dfile[50];
	printf("输入要复制的文件\n");
	scanf("%s", sfile);
	printf("输入目的文件名\n");
	scanf("%s", dfile);
	char *path = "/bin/cp";
	char *argv[4] = {"cp", sfile, dfile, NULL};
	execv(path, argv);
}
void checkJurisdiction(){
     if(access("test.txt",R_OK) == 0)
     {
         printf("文件可读");
     }
     if(access("test.txt",W_OK) == 0)
     {
         printf("文件可写");
     }
     if(access("test.txt",W_OK) == 0)
     {
         printf("文件可执行");
     }
     
}
void ChangeJurisdiction(){
    char fileName[50];
	printf("输入要修改的文件:");
	scanf("%s", fileName);
	int c;
	mode_t mode = S_IWUSR;
	scanf("%d", &c);
	switch(c)
	{
		case 0:chmod(fileName, S_IRWXU);break;//读，写，执行
		case 1:chmod(fileName, S_IRUSR);break;//读
		case 2:chmod(fileName, S_IWUSR);break;//写
		case 3:chmod(fileName, S_IXUSR);break;//执行
		default:printf("选择有误\n");
	}
        printf("修改文件权限成功");	
}
void createSubdirectory(){
      if(mkdir("zxu",__S_IWRITE)!=-1)
      {
          printf("创建子目录成功\n");
      } else {
          printf("创建子目录不成功\n");
      }
}
void removeSubdirectory(){
    char *dir = "zxu";
     char cur_dir[] = ".";
    char up_dir[] = "..";
    char dir_name[128];
    DIR *dirp;
    struct dirent *dp;
    struct stat dir_stat;

    // 参数传递进来的目录不存在，直接返回
    if ( 0 != access(dir, F_OK) ) {
        printf("目录不存在\n");
    }

    // 获取目录属性失败，返回错误
    if ( 0 > stat(dir, &dir_stat) ) {
        perror("获取目录属性失败\n");
    }

    if ( S_ISREG(dir_stat.st_mode) ) {  // 普通文件直接删除
        remove(dir);
    } else if ( S_ISDIR(dir_stat.st_mode) ) {   // 目录文件，递归删除目录中内容
        dirp = opendir(dir);
        while ( (dp=readdir(dirp)) != NULL ) {
            // 忽略 . 和 ..
            if ( (0 == strcmp(cur_dir, dp->d_name)) || (0 == strcmp(up_dir, dp->d_name)) ) {
                continue;
            }

            //sprintf(dir_name, "%s/%s", dir, dp->d_name);
            removeSubdirectory(dir_name);   // 递归调用
        }
        closedir(dirp);

        rmdir(dir);     // 删除空目录
    } else {
        perror("unknow file type!");    
    }
    printf("删除子目录成功\n");
}
void changedirectory(){
    chdir("zxu");
    printf("改变当前目录到指定目录成功\n");
    int fd;
    if((fd=open("test2.txt",O_RDWR|O_CREAT|O_TRUNC)) == -1){
        my_err("open",__LINE__);
    }else{
        printf("文件创建成功!\n");
    }
}
void linkfile(){
    char ofile[50], nfile[50];
	printf("输入要创建链接的文件：\n");
	scanf("%s", ofile);
	printf("输入文件新的名字：\n");
	scanf("%s", nfile);
	if(link(ofile, nfile) == -1)
	{
		printf("创建失败\n");
		return;
	}
	else
		printf("文件链接创建成功\n");
}
int main(){
    int n=1;
    while(n){
        printf("\n**********************************************");
        printf("\n*               文件演示系统                 *");
        printf("\n**********************************************");
        printf("\n     1.创建新文件             2.写入文件内容   ");
        printf("\n     3.读出文件内容           4.复制文件       ");
        printf("\n     5.修改文件权限           6.查看文件权限    ");
        printf("\n     7.创建子目录             8.删除子目录      ");
        printf("\n     9.改变当前目录到指定目录  10.链接文件       ");
        printf("\n**********************************************");
        printf("\n请选择(1～10):");
        int xuhao = 0;
        scanf("%d",&xuhao);
        switch(xuhao)
            { case 0 : return 0;
              case 1: Createfile(); break;
              case 2 :Writetext(); break;
              case 3 :Readfile();break;
              case 4 :cppyfile();break;
              case 5 :ChangeJurisdiction();break;
              case 6 : checkJurisdiction(); break;
              case 7 : createSubdirectory(); break;
              case 8 : removeSubdirectory(); break;
              case 9 : changedirectory(); break;
              case 10: linkfile(); break;
              default: n=0;
              break;
            }
    }
    return 0;
}
