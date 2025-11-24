import app.repositories.entrenador_repo as entrenador_repo

def registrar_entrenador():
    entrenador_repo.crear_entrenador()
    return

def autenticar_entrenador():
    
    return entrenador_repo.obtener_entrenador_por_nombre()
