create table cities (
	city_code int,
	region_code int,
	name varchar
);
-- ###
create table regions (
	region_code int,
	name varchar
);
-- ###
create table comments (
	id auto_increment int,
	surname varchar,
	name varchar,
	patronim varchar,
	region,
	city,
	email varchar,
	phone int,
	msg varchar(300)
);
-- ###
insert into regions (region_code,name)
values (1,'Краснодарский край'),(2,'Ростовская область'),(3,'Ставропольский край')
-- ###
insert into cities (city_code,region_code,name)
values (1,1,'Краснодар'),(2,1,'Кропоткин'),(3,1,'Славянск'),
	(4,2,'Ростов'),(5,2,'Шахты'),(6,2,'Батайск'),
	(7,3,'Ставрополь'),(8,3,'Пятигорск'),(9,3,'Кисловодск')


create view statByRegions
as
select r.id,r.name,foo.cnt
from (
	select region_code,count(0) cnt
	from comments
	group by region_code
	having count(0) > 5
) as foo
join regions r
		on r.id = foo.region_code


