#include<iostream>
using namespace std;
struct line{int s,e,v;}a[5005],mid;
int n,m,used[30005]={0};
void qsort(int L,int r)//快排
{  int i=L,j=r;mid=a[(L+r)/2];
   while(i<=j)
   {  while(a[i].e<mid.e)i++;
      while(a[j].e>mid.e)j--;
      if(i<=j)swap(a[i++],a[j--]);
   }
   if(L<j)qsort(L,j);
   if(i<r)qsort(i,r);
}
void Init()
{  int i;
   cin>>n>>m;
   for(i=1;i<=m;i++)cin>>a[i].s>>a[i].e>>a[i].v;
   qsort(1,m);
}
void Solve()
{  int i,j,k,ans=0;
   for(i=1;i<=m;i++)//依次处理m个区间
   {  k=0;
      for(j=a[i].s;j<=a[i].e;j++)if(used[j])k++;//统计区间内已标记的数
      if(k<a[i].v)
         for(j=a[i].e;j>=a[i].s;j--)
             if(!used[j]){used[j]=1;k++;ans++;if(k==a[i].v)break;}
   }
   cout<<ans<<endl;
}
int main()
{  Init();
   Solve();
}
# 还有其他算法，例如：树状数组，差分约束系统
