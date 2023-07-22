-- Schema Creation
DROP SCHEMA IF EXISTS load_testing CASCADE;
CREATE SCHEMA load_testing;
SET SCHEMA 'load_testing';

CREATE TABLE Person(
    id serial PRIMARY KEY,
    first_name varchar(20),
    last_name varchar(23),
    company_name varchar(40),
    address varchar(41),
    city varchar(29),
    county varchar(30),
    state varchar(15),
    zip char(5),
    phone1 char(12),
    phone2 char(12),
    email varchar(44),
    web varchar(52)
);
