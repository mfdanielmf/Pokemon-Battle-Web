from app.models.entrenador import Entrenador
from app.models.exceptions import EntrenadorExistenteException, EntrenadorNoCreadoException, EntrenadorNotFoundException, ContraseñaIncorrectaException
from app.repositories.entrenador_repo import crear_entrenador, obtener_entrenador_por_nombre, check_pass, obtener_entrenador_por_id


def registrar_entrenador(nombre, contraseña):
    if nombre and contraseña:
        entrenador_existente = obtener_entrenador_por_nombre(nombre)

        # Si no está en la base, lo creamos
        if not entrenador_existente:
            entrenador = crear_entrenador(nombre, contraseña)

            if entrenador:
                return entrenador

        raise EntrenadorExistenteException()

    raise EntrenadorNoCreadoException()


def autenticar_entrenador(nombre, contraseña):
    entrenador_aut = obtener_entrenador_por_nombre(nombre)

    if entrenador_aut:
        contraseña = check_pass(entrenador_aut, contraseña)
        if contraseña is False:
            raise ContraseñaIncorrectaException()

    if entrenador_aut and contraseña:
        return entrenador_aut

    raise EntrenadorNotFoundException()


def obtener_entrenador_nombre_base(nombre) -> Entrenador | EntrenadorNotFoundException:
    entrenador = obtener_entrenador_por_nombre(nombre)

    if not entrenador:
        raise EntrenadorNotFoundException()

    return entrenador


def obtener_entrenador_id_base(id) -> Entrenador | EntrenadorNotFoundException:
    entrenador = obtener_entrenador_por_id(id)

    if not entrenador:
        raise EntrenadorNotFoundException()

    return entrenador
