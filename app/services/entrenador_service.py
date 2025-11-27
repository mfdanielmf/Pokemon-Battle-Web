from app.repositories.entrenador_repo import crear_entrenador, obtener_entrenador_por_nombre, check_pass


def registrar_entrenador(nombre, contraseña):
    if nombre and contraseña:
        entrenador_existente = obtener_entrenador_por_nombre(nombre)

        # Si no está en la base, lo creamos
        if not entrenador_existente:
            entrenador = crear_entrenador(nombre, contraseña)

            return entrenador

    return None


def autenticar_entrenador(nombre, contraseña):
    entrenador_aut = obtener_entrenador_por_nombre(nombre)

    if entrenador_aut:
        contraseña = check_pass(entrenador_aut, contraseña)

    if entrenador_aut and contraseña:
        return entrenador_aut

    return None
