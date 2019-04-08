--数据准备
    create database jingdong charset=utf8;
    use jingdong
    create table goods(
        id int unsigned primary key auto_increment not null,
        name varchar(120) not null,
        cate_name varchar(40) not null,
        brand_name varchar(40) not null,
        price decimal(10,3) not null default 0,
        is_show bit not null default 1,
        is_saleoff bit not null default 0
    );
    insert into goods values(0,'r510vc 15.6英寸笔记本','笔记本','华硕','3399',default,default);
    insert into goods values(0,'y400n 14.0英寸笔记本电脑','笔记本','联想','4999',default,default);
    insert into goods values(0,'g150th 15.6英寸笔记本','游戏本','雷神','8499',default,default);
    insert into goods values(0,'x550cc 15.6英寸笔记本','笔记本','华硕','2799',default,default);
    insert into goods values(0,'x240 超级本','超级本','联想','4880',default,default);
    insert into goods values(0,'u330p 13.3英寸超级本','超级本','联想','4299',default,default);
    insert into goods values(0,'scp13226scv 触控超级本','超级本','索尼','7999',default,default);
    insert into goods values(0,'ipad mini 7.9英寸平板电脑','平板电脑','苹果','1998',default,default);
    insert into goods values(0,'ipad air 9.7英寸平板电脑','平板电脑','苹果','3388',default,default);
    insert into goods values(0,'iPad mini 配备 retina 显示屏','平板电脑','苹果','2788',default,default);
    insert into goods values(0,'ideacentre c340 20英寸一体电脑','台式机','联想','3499',default,default);
    insert into goods values(0,'vostro 3800-r1206 台式电脑','台式机','戴尔','2899',default,default);
    insert into goods values(0,'imac me086ch/a 21.5英寸一体电脑','台式机','苹果','9188',default,default);
    insert into goods values(0,'at7-7414lp 台式电脑 linux ）','台式机','宏碁','3699',default,default);
    insert into goods values(0,'z220sff f4f06pa工作站','服务器/工作站','惠普','4288',default,default);
    insert into goods values(0,'poweredge ii服务器','服务器/工作站','戴尔','5388',default,default);
    insert into goods values(0,'mac pro专业级台式电脑','服务器/工作站','苹果','28888',default,default);
    insert into goods values(0,'hmz-t3w 头戴显示设备','笔记本配件','索尼','6999',default,default);
    insert into goods values(0,'商务双肩背包','笔记本配件','索尼','99',default,default);
    insert into goods values(0,'x3250 m4机架式服务器','服务器/工作站','ibm','6888',default,default);
    insert into goods values(0,'商务双肩背包','笔记本配件','索尼','99',default,default);
--查询复习
    --超极本
    select * from goods where cate_name='超级本';
    --显示商品种类
    select cate_name from goods group by cate_name;
    select distinct cate_name from goods;
    --显示所有电脑产品的平均价格，并且保留两位小数
    select round(avg(price),2) as avg_price from goods;
    --查询每种商品的平均价格
    select cate_name,avg(price) from goods group by cate_name;
    --查询每种类型的商品中最贵、最便宜、平均价、数量
    select cate_name,max(price),min(price),avg(price),count(*) from goods group by cate_name;
    --查询所有价格大于平均价格的商品，并且按价格降序排序
    select * from goods where price>(select avg(price) from goods) order by price desc;
    --查询每种类型中最贵的电脑信息:3种方式
    select * from 
    (select cate_name,max(price) as max_price from goods group by cate_name) as a 
    inner join goods on goods.price=a.max_price and goods.cate_name=a.cate_name;

    select * from goods
    inner join
    (select cate_name,max(price)as max_price from goods group by cate_name) as a
    on goods.cate_name=a.cate_name and goods.price=a.max_price;

    select * from 
    (select cate_name,max(price) as max_price from goods group by cate_name) as a 
    left join goods on goods.price=a.max_price and goods.cate_name=a.cate_name;
--拆表
    --创建商品分类表
    create table if not exists goods_cates(
        id int unsigned primary key auto_increment,
        name varchar(40) not null
    );
    --查询商品种类
    select cate_name from goods group by cate_name;
    --将查询到的分组内容写入到goods_cates数据表
    insert into goods_cates (name) select cate_name from goods group by cate_name;
    --将goods表中的cate_name改成goods_cates表中的id
    update goods as g inner join goods_cates as c on g.cate_name =c.name set g.cate_name=c.id;
    --修改goods表结构，cate_name改名，并改为int
    alter table goods change cate_name cate_id int unsigned not null;
    --设置goods表中cate_id 设为外键
    alter table goods add foreign key (cate_id) references goods_cates(id);





    --创建品牌分类表
    create table if not exists goods_brands(
        id int unsigned primary key auto_increment,
        name varchar(40) not null
    );
    --查询厂家名称
    select brand_name from goods group by brand_name;
    --将查询到的分组内容写入到good_brands数据表中
    insert into goods_brands(name) select brand_name from goods group by brand_name;
    --将goods中brand_name字段改成good_brands中的id
    update goods as g inner join goods_brands as b on g.brand_name=b.name set g.brand_name=b.id;
    --修改goods表结构，brand_name改名改属性
    alter table goods change brand_name brand_id int unsigned not null;
    --设置goods中brand_id为外键
    alter table goods add foreign key (brand_id) references goods_brands(id);

    --创建表的同时导入数据，需要注意，导入表要用as使名称与新建表导入的字段名称一致才可以导入数据
    create table if not exists goods_brands(
        id int unsigned primary key auto_increment,
        name varchar(40) not null
    )select brand_name as name from goods group by brand_name;