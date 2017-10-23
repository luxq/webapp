-- init database

drop database if exists test;

create database test;

use test;

grant select, insert, update, delete on test.* to 'test'@'%' identified by 'Avl1108';

create table users (
    `id` varchar(50) not null,
    `email` varchar(50) not null,
    `password` varchar(50) not null,
    `admin` bool not null,
    `name` varchar(50) not null,
    `image` varchar(50) not null,
    `created_at` real not null,
    unique key `idx_email` (`email`),
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table blogs(
    `id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `user_image` varchar(50) not null,
    `name` varchar(50) not null,
    `summary` varchar(50) not null,
    `content` mediumtext not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table comments (
    `id` varchar(50) not null,
    `blog_id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `user_image` varchar(50) not null,
    `content` mediumtext not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;

-- email /password:
-- admin@example.com / password

insert into users (`id`,`email`,`password`,`admin`,`name`, `image` ,`created_at`) values ('10018336417540987fff4508f43ffbaed718e263442526000', 'admin@example.com', '5f4dcc3b5aa765d61d8327de882cf99', 1, 'Administrator', '/static/p1.ico', 1402909113.628);
