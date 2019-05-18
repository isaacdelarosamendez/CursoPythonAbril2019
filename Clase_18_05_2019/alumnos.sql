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

create table maestros(
    idMaestro serial not null,
    idCurso integer,
    nombres varchar(25) not null,
    apellidos varchar(25) not null,
	correo varchar(25) NOT NULL,
	telefono varchar(25) NOT NULL,
    PRIMARY KEY (idMaestro),
    FOREIGN KEY (idCurso) REFERENCES cursos (idCurso)
);
