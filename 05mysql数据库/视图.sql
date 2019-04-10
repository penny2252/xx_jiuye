--作用
--1、提高了重用性，就像一个函数
--2、对于数据库重构，缺不影响程序的运行
--3、提高了安全性，可以对不同的用户
--4、让数据更加清晰


--建立步骤
--1、将所有表组成一个，
select * from goods as g left join goods_cates as c on g.cate_id=c.id left join goods_brands as b on g.brand_id=b.id;
--2、去掉附加表的id，并将附加表的字段名重新命名（把上一个命令中的*进行修改）
select g.*,c.name as cate_name,b.name as brand_name from goods as g left join goods_cates as c on g.cate_id=c.id left join goods_brands as b on g.brand_id=b.id;
--3、将之前查询的另存成一个视图（在上一条命令前加上新建视图的命令）
create view v_goods_info as select g.*,c.name as cate_name,b.name as brand_name from goods as g left join goods_cates as c on g.cate_id=c.id left join goods_brands as b on g.brand_id=b.id;
