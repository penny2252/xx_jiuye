--数据准备
    --创建数据库
    create database python_test charset=utf8;
    --使用一个数据库
    use python_test;
    --显示使用的数据库是哪个？
    select database();
    --创建一个数据表
    --students表
    create table students(
        id int unsigned primary key not null auto_increment,
        name varchar(20) default '',
        age tinyint unsigned default 0,
        height decimal(5,2),
        gender enum('男','女','未知') default '未知',
        cls_id int unsigned default 0,
        is_delete bit default 0
    );
    --classer表
    create table classes(
        id int unsigned primary key not null auto_increment,
        name varchar(30) not null
    );
    --向students表中插入数据
    insert into students values
    (0,'aa',18,180.00,2,1,0),
    (0,'bb',18,180.00,2,2,1),
    (0,'cc',29,185.00,1,1,0),
    (0,'dd',59,175.00,1,2,1),
    (0,'ee',38,160.00,2,1,0),
    (0,'ff',28,150.00,3,2,1),
    (0,'gg',18,172.00,2,1,1),
    (0,'hh',36,null,1,1,0),
    (0,'ii',27,181.00,1,2,0),
    (0,'jj',25,166.00,2,2,0),
    (0,'kk',33,162.00,3,3,1),
    (0,'ll',12,180.00,2,4,0),
    (0,'mm',12,170.00,1,4,0),
    (0,'nn',34,176.00,2,5,0);
    --向classes 表中插入数据
    insert into classes values (0,'1班'),(0,'2班');
--查询
    --查询所有字段
    select * from students;
    select * from classes;
    --查询指定字段
    select name, age from students;
    --使用as将显示的字段起别名
    select name as 姓名, age as 年龄 from students;
    --select 表名.字段 from 表名；
    select students.name , students.age  from students;
    --使用as给表起别名
    --select 别名.字段 from 表名 as 别名；
    select stu.name , stu.age  from students as stu;
        --起别名以后再用原名将失败
        --select students.name , students.age  from students as stu;
    --去除重复项显示
    --distinct
    select distinct gender from students;
--条件查询
    --select ... from where ....
    --比较运算符'>','<','=','!=','<=','>='
        --查询>18岁
        select * from students where age>18;
        select id,name,gender from students where age>18;
        --查询<18岁
        select * from students where age<18;
        --查询等于18岁
        select * from students where age=18;
        --查询不等于18岁
        select * from students where age!=18;
    --逻辑运算符'and','or','not'
        --and
        --18到28之间
        select * from students where age>18 and age<28;
        --18以上的女性
        select * from students where age>18 and gender=2;
        --or
        --18以上或身高180（包含）以上
        select * from students where age>18 or height>=180.00;
        --not
        --不在18岁以上的女性这个范围内的
        select * from students where not(age>18 and gender=2);
        --年龄不是小于或者等于18 并且是女性
        select * from students where age>18 and gender=2;
        select * from students where not(age<18 or age =18)and gender=2;
    --模糊查询
        --like
        --%代替1个或者多个
        --_代替1个
        --查询姓名中以”小“开始的名字
        select name from students where name like "小%";
        --查询姓名中有”小“的名字
        select name from students where name like "%小%";
        --查询有2个字的名字
        select name from students where name like "__";

        --查询有3个字的名字
        select name from students where name like "___";    
        --查询至少有2个字的名字
        select name from students where name like "__%";
        --rlike 正则
        --查询以周开始的姓名    
        select name from students where name rlike "^周.*";    
        --查询以周开始，伦结尾的姓名
        select name from students where name rlike "^周.*伦$"; 

    --范围查询
        --in（1,3,8）表示在一个非连续的范围内
        --查询年龄18和34的姓名
        select age from students where age=18 or age=34;
        select age from students where age in (18,34);
        select age from students where age in (12,18,34);
        --not in 不非连续的范围内
        --年龄不是18\34之间的信息
        select age from students where age not in (18,34);
        --between ... and ...表示在一个连续的范围内
        --查询年龄在18到34之间的信息
        select age from students where age between 18 and 34;

        --not between ... and ...表示不在一个连续的范围内
        --查询年龄不在18到34之间的信息
        select age from students where age not between 18 and 34;
        --select age from students where age not (between 18 and 34);会失败
    -- 空判断
        --判空is null
        --查询身高为空的信息
        select height,name from students where height is null;
        --判非空 is not null
        select height,name from students where height is not null;
