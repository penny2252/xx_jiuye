--连接查询
	--inner join ... on
	--查询 有能够对应班级的学生及班级信息
	select * from students inner join classes on students.cls_id=classes.id;
	--按照要求显示姓名、班级
	select students.name,classes.name from students inner join classes on students.cls_id=classes.id;
	--给数据表起名字
	select students.name as 姓名,classes.name as 班级 from students inner join classes on students.cls_id=classes.id;
	select s.name as 姓名,c.name as 班级 from students as s inner join classes as c on s.cls_id=c.id;
	--查询 有能够对应班级的学生及班级信息，显示学生的所有信息，只显示班级名称
	select s.*,c.name from students as s inner join classes as c on s.cls_id=c.id;

	--在以上的查询中，将班级姓名显示在第1列
	select c.name ,s.* from students as s inner join classes as c on s.cls_id=c.id;

	--查询 有能够对应班级的学生及班级信息，按照班级进行排序
	select c.name ,s.* from students as s inner join classes as c on s.cls_id=c.id order by s.cls_id;

	--当是同一个班级的时候，按照学生id从小到大排序
	select c.name ,s.* from students as s inner join classes as c on s.cls_id=c.id order by s.cls_id,s.id;

	--查询每位学生对应的班级信息 left join
	select * from students as s left join classes as c on s.cls_id=c.id;
	select * from classes as c left join students as s on s.cls_id=c.id;
	select * from students as s right join classes as c on s.cls_id=c.id;
	--查询没有对应班级信息的学生
	select c.name ,s.* from students as s left join classes as c on s.cls_id=c.id having c.name is null;
	select c.name ,s.* from students as s left join classes as c on s.cls_id=c.id where c.name is null;
	--将数据表名字互换位置