-- scripts para executar na demonstração do BD;
create table funcionario (id int, nome varchar, sobrenome varchar, salario int);
create table animais (id int, nome varchar, idade int);
create table series (nome varchar, temporadas int);

-- populando as panelas;
insert into funcionario values (1, Augusto, Hert, 5000);
insert into funcionario values (2, Maria, Clara, 100);
insert into funcionario values (3, Joao, Pedro, 10000);
insert into funcionario values (4, Doroteia, Joaquina, 0);
insert into funcionario values (5, Faustao, Fausto, 0);
insert into funcionario values (6, Bruce, Wayne, 0);
insert into funcionario values (7, Clark, Kent, 0);

insert into animais values (1, Chu, 1);
insert into animais values (2, Mozo, 1);
insert into animais values (3, Bud, 1);
insert into animais values (4, Miranda, 1);
insert into animais values (5, Lulu, 1);

insert into series values (Supernatural, 12);
insert into series values (WalkingDead, 8);
insert into series values (Friends, 6);
insert into series values (Batman, 2);
insert into series values (Superman, 0);

update funcionario set sobrenome = Hertzog where id = 1;
update animais set idade = 5 where id = 1;
commit;

update funcionario set salario = 15000 where id = 7;
update funcionario set salario = 1000 where id = 6;
update funcionario set salario = 600 where id = 6;

start new;
update animais set idade = 4 where id = 2;
update series set temporadas = 4 where nome = Batman;
update animais set idade = 9 where id = 5;

checkpoint;

start new;
update funcionario set salario = 1500 where id = 4;
update funcionario set salario = 3500 where id = 4;
update funcionario set salario = 100 where id = 3;

start new;
update series set temporadas = 14 where nome = Friends;
update series set temporadas = 5 where nome = Superman;
commit;

-- start new;
