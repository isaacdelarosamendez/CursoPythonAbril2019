create table cursos(
    idCurso serial not null,
    nombre varchar(25) not null,
    PRIMARY KEY (idCurso)
);

create table alumnos(
    idAlumno serial not null,
    idCurso integer,
    nombres varchar(25) not null,
    apellidos varchar(25) not null,
    PRIMARY KEY (idAlumno),
    FOREIGN KEY (idCurso) REFERENCES cursos (idCurso)
);



INSERT INTO cursos(nombre)
VALUES ('Python'),
('PHP')

SELECT * FROM cursos

insert into alumnos(idcurso,nombres,apellidos)
values(1,'Isaac','De la rosa')



drop table cursos;
drop table alumnos;