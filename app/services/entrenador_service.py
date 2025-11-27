import app.repositories.entrenador_repo as entrenador_repo

def registrar_entrenador():
    entrenador_repo.crear_entrenador()
    return "Se ha creado el entrenador"

def autenticar_entrenador(nombre, contraseña):
    entrenador_aut = entrenador_repo.obtener_entrenador_por_nombre(nombre)
    contraseña = entrenador_repo.Entrenador.check_Password(contraseña)
    if entrenador_aut and contraseña:
        return entrenador_aut
    return None
