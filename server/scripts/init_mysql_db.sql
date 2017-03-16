use mysql;
delete from user where user='duel' and host='%';
flush privileges;

drop user 'duel'@'%';
flush privileges;

create user 'duel'@'%' identified by 'duel4kyt?';

drop database if exists duel;
create database if not exists duel;

GRANT insert, select, delete, update, create, drop on duel.* to duel@'%' identified by 'duel4kyt?';

USE duel;

CREATE TABLE user_info(
    uuid VARCHAR(36) NOT NULL PRIMARY KEY,
    name VARCHAR(20)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

