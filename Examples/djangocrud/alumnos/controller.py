from alumnos import models



def GetAlumnos():
    helper = models.Helper()
    _listAlumnos = helper.GetSelect("select * from alumnos_alumnos")
    _result =  ""
    for alumno in _listAlumnos:
        for columna in alumno:
            _result += str(columna) + "<br>"
    return _result