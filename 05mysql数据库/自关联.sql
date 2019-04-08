--建立表单
    create table areas(aid int primary key auto_increment,
        atitle varchar(30),
        pid int
    );
    --查询出山东有哪些市
    select * from areas as p join areas as c on c.pid=p.aid having p.atitle='山东省';
    select p.atitle,c.* from areas as p join areas as c on c.pid=p.aid having p.atitle='山东省';
    select p.atitle,c.* from areas as p join areas as c on c.pid=p.aid having p.atitle='吉林省';
    select p.atitle,c.* from areas as p join areas as c on c.pid=p.aid having p.atitle='长春市';
--子查询
    --标量子查询
    --查询出高于平均身高的信息

    --查询最高的男生信息
    select * from students where gender=2 and height=(select max(height) from students where gender=2 );
    select * from students where gender=1 and height=(select max(height) from students where gender=1 );

    select * from students as s join (select max(height) as max from students where gender=1 ) as h on s.height=h.max;
    select * from areas where pid=(select aid from areas where atitle='吉林省');
    select * from areas where pid=(select aid from areas where atitle='河北省');