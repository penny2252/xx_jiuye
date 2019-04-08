登录mysql
	mysql -u root -p
	输入密码
显示数据库版本
	mysql>select version();
显示时间
	mysql>show now():
查看所有数据库
	mysql>show databases;
查看正在使用的数据库
	mysql>select database(); 
新建数据库"python"
	mysql>create database python;
查看数据库"python"的创建语句
	mysql>show create database python; 
使用数据库"python"
	mysql>use python;
删除数据库"python"
	mysql>drop database python;
查看当前数据库的所有的表
	mysql>show tables;
创建数据表"student"
--create table "数据表名称"（字段 类型 约束）;
--auto_increment 表示自动增长，id等
--not null 表示不为空
--primary key 表示主键
--default 表示默认值
--unsigned 表示不带正负符号
--enum枚举
--default charset = utf8默认编码格式可以输入中文
	mysql>create table student(id int,name varchar(30));
--可以换行输入	
	create table student5(
		id int unsigned primary key not null auto_increment,
		name varchar(30) not null,
		age tinyint unsigned not null,
		high decimal(5,2),
		gerder enum("男","女","未知") default "未知",
		cls_id int unsigned
	)default charset = utf8;
查看"student"数据表结构
	mysql>desc student; 

显示"student5"数据表内容
	mysql>select * from student5;

删除"student5"数据表
	mysql>drop table student5;
修改"student5"数据表结构
--add添加
--modify不重命名
--change可以同时重命名修改表结构
	mysql>alter table student5 add birthday datetime;
	mysql>alter table student5 modify birthday date;
	mysql>alter table student5 change birthday birth datetime;
	mysql>alter table student5 change birth birthday  date default "1979-06-01";
删除数据表"student5"中"high"字段
	mysql>alter table student5 drop high;
查看数据表"student5"的创建语句
	mysql>show create table student5;
向"student5"数据表插入数据
--全部字段写入
	mysql>insert into student5 values(0,"潘越",16,"男",1,"1979-06-01");
--id字段可以写null、0、default
	mysql>insert into student5 values(null,"潘越",16,"男",1,"1979-06-01");
	mysql>insert into student5 values(default,"潘越",16,"男",1,"1979-06-01");
--gerder枚举字段可以用1\2\3代替	
	mysql>insert into student5 values(0,"潘越",16,1,1,"1979-06-01");
	mysql>insert into student5 values(0,"潘越",16,2,1,"1979-06-01");
	mysql>insert into student5 values(0,"潘越",16,3,1,"1979-06-01");
--部分插入,为需要插入的字段插入信息，插入多个字段，多条记录，每个记录在一个括号内，内部包含需要插入的字段
--如果要求字段不为空则必须写入，如果要求可以为空又没有设置默认字段，系统自动分配默认值
	mysql>insert into student5 (name,age) values("pp",18);
	mysql>insert into student5 (name,age) values("pp",18),("xx",18);
--全部字段写入同样可以一次性插入两条记录
	mysql>insert into student5 values(0,"潘越",16,1,1,"1979-06-01"),(0,"xx",18,2,1,"1977-09-20");
修改"student5"数据表中数据(update)
--修改所有记录的某个字段（gender）
	mysql>update student5 set gerder=2;
--可以一次修改多个字段
	mysql>update student5 set gerder=1,cls_id=1;
--可以修改相应记录的某个字段
	mysql>update student5 set birthday="1977-09-20" where name="xx";
	mysql>update student5 set gerder="2" where name="xx";
	mysql>update student5 set gerder="1",age=17 where name="pp";
查询"student5"数据表中的记录
--全部显示
	mysql>select * from student5;
--显示全部age为条件
	mysql>select * from student5 where age=16;
	mysql>select * from student5 where age>17;
--显示部分字段
	mysql>select id,name from student5 where age=16;
--显示时利用别名修改字段名
	mysql>select id as 序号,name as 姓名 from student5 where age=16;
--修改显示的默认顺序，写在前面的先显示
	mysql>select name as 姓名,id as 序号 from student5 where age=16;
删除"student5"数据表中的记录
物理删除
--删除全部记录
	mysql>delete from student5;
--删除"student5"数据表中"id=1"的内容
	mysql>delete from student5 where id=1;
--删除"student5"数据表中"name=pp"的内内容
	mysql>delete from student5 where name="pp";
逻辑删除
--设置逻辑删除标签
	mysql>alter table student5 add is_delete bit default 0;
--逻辑删除name="xx"
	mysql>update student5 set is_delete=1 where name="xx";
