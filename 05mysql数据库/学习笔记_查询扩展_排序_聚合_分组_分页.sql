--排序
	-- order by 字段
	-- asc 从小到大排序
	-- desc 从大到小排序

	--查询年龄在18到34之间的男性，按照年龄从小到大排序
	select * from students where (age between 18 and 34)and gender=1 order by age asc;
	--查询年龄在18到34之间的女性，身高从高到矮排序
	select * from students where (age between 18 and 34)and gender=2 order by height desc;

	--order by 多个字段
	--年龄在18到34之间的女性,身高从高到矮排序，如果身高相同，按年龄从小到大排序
	select * from students where (age between 18 and 34)and gender=2 order by height desc , age asc;

	--年龄在18到34之间的女性,身高从高到矮排序，如果身高相同，按年龄从小到大排序
	--如果年龄相同按照id从大到小排序
	select * from students where (age between 18 and 34)and gender=2 order by height desc , age asc,id desc;
	--按照年龄从小到大，身高从高到矮排序
	select * from students  order by age asc,height desc;
--聚合函数
	--总数
	--count
	--查询男性有多少人，女性有多少人
	select count(*) as 男性人数 from students where gender=1;
	select count(*) as 女性人数 from students where gender=2;
	--最大值
	--max
	--查询最大的年龄
	select max(age) from students;
	--查询女性的最高
	select max(height) from students where gender=2;
	--最小值
	--min
	select min(age) from students;
	--求和
	--sum
	--计算所有人的年龄总和
	select sum(age) from students;
	--平均值
	--avg
	--计算平均年龄
	select avg(age) from students;
	--计算平均年龄sum(age)/count(*)
	select sum(age)/count(*) from students;
	--四舍五入 round（123.23,1）保留1位小数
	--计算所有人的平均年龄，保留2位小数
	select round(sum(age)/count(*),2) from students;
	select round(avg(age),2) from students;

	--计算男性的平均身高
	select avg(height) from students where gender=1;
--分组
	--group by
	--按照性别分组，查询所有的性别
	--失败select * from students group by gender;
	select gender from students group by gender;
	--计算每种性别中的人数
	select gender,count(*) from students group by gender;
	--性别中的年龄平均
	select gender,avg(age) from students group by gender;
	--计算男性的人数
	select gender,count(*) from students where gender=1 group by gender;
	select gender,count(*),group_concat(name) from students where gender=1 group by gender;
	select gender,count(*),group_concat(name,'_',id,'_',age) from students where gender=1 group by gender;
	--group_concat(...)
	--查询同种性别中的姓名
	select gender,group_concat(name) from students group by gender;
	--having
	--查询平均年龄超过30岁的性别。以及姓名having avg(age)
	select gender,avg(age),group_concat(name) from students group by gender having avg(age)>30;
	--查询每种性别中的人数多于2个的信息
	select gender,count(*),group_concat(name) from students group by gender having count(*)>2;
--分页
	--limit start, count
	--限制查询出来的个数
	select * from students  limit 2;
	select * from students where gender=1 limit 2;
	--查询5个数据
	select * from students limit 0,5;
	--查询id6-10(包含)的顺序
	select * from students limit 5,5
	--每页显示2个，第1个页面
	select * from students limit 0,2

	--每页显示2个，第2个页面
	select * from students limit 2,2
	--每页显示2个，第3个页面
	select * from students limit 4,2

	--每页显示2个，第4个页面
	--6=(4-1)*2;2=2
	select * from students limit 6,2

	--每页显示2个，第6个页面，按年龄从小到大排序
	select * from students order by age limit 10,2;
	--查询女性信息从高到矮排序，显示2个
	select * from students where gender=2 order by height desc limit 0,2;
