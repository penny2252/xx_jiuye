--事务就是做一件事要有若干过程，要么执行，要么都不执行，所有过程步骤必须打包在一起，任何一个步骤失败就必须回滚所有的步骤
--四大特性（ACID) 
--原子性（atomicity）：一个事务必须被视为一个不可分割的最小工作单元，整个事务中的所有操作要么全部提交成功，要么全部失败回滚,对于一个事
	--务来说，不可能只执行其中的一部分操作。
--一致性(consistency)：数据库总是从一个一致性的状态转换到另一个一致性的状态。（例子中，一致性确保了，及时在指定第三、四条语句之间时
	--系统崩溃，支票账户中也不会损失200元，因为事务最终没有提交，事务中做的修改也不会保存到数据库） 
--隔离性(isolation)：通常来说，一个事务的修改在最终提交前，对其他事务是不可见的。（例子中，当执行三、四条语句前，有另外一个账户
	--总程序开始运行，则其看到支票账户的余额并没有被减去200元）
--持久性(durability)：一旦事务提交，其所作的修改会永久保存到数据库。（此时即使系统崩溃，修改的数据也不会丢失）


--以start transaction语句开始，要么使用commit提交将修改的的数据急救保存，要么使用rollback撤销所有修改，例如：
--1.start transaction; 
--2.select balance from checking where customer_id=10233276; 
--3.updata checking set balance=balance-200.00 where customer_id=10233276; 
--4.updata savings set balance=banlance+200.00 where customer_id=10233276; 
--5.commit;


--开启事务，如果不手动执行下面的命令直接修改默认开启事务，执行完后默认结束提交
begin；
start transaction; 

--确认提交
commit；

--回滚
rollback；