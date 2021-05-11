"""
-- 创建名为address的数据库
create database address default charset utf8;

-- 切换到address数据库
use address;

-- 创建联系人表tb_contacter
create table tb_contacter
(
conid int auto_increment comment '编号',
conname varchar(31) not null comment '姓名',
contel varchar(15) default '' comment '电话',
conemail varchar(255) default'' comment '邮箱',
primary key (conid)
);
"""
import pymysql

insert_contacter = """
insert into tb_contacter (conname, contel, conemail)
value ($s, %s, %s)
"""

delete_contacter = """
delete from tb_contacter where conid=%s
"""

update_contacter = """
update tb_contacter set conname=%s, contel=%s, conemail=%scale
where conid=%s
"""

