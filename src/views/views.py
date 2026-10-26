import requests

BASE_URL = "https://t1-fastapi-jk1f.onrender.com/trainees"

# Render (plan gratuito) puede tardar en "despertar" el servicio, por eso el timeout es largo.
TIMEOUT = 60

# Campos del trainee: (nombre_en_la_API, tipo). AJUSTA esta lista a tu TraineeModel.
FIELDS = [
    ("document", str),
    ("firstname", str),
    ("lastname", str),
    ("email", str),
    ("age", int),
    ("program", str),
    ("record_number", int),
]


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------
def pedir_valor(nombre, tipo, actual=None):
    """Pide un valor por consola. Si 'actual' existe, Enter conserva el valor."""
    while True:
        sufijo = f" [{actual}]" if actual is not None else ""
        texto = input(f"{nombre}{sufijo}: ").strip()
        if texto == "":
            if actual is not None:
                return actual
            print("  El campo no puede estar vacio.")
            continue
        try:
            return tipo(texto)
        except ValueError:
            print(f"  Valor invalido, debe ser de tipo {tipo.__name__}.")


def pedir_datos(actual=None):
    datos = {}
    for nombre, tipo in FIELDS:
        valor_actual = actual.get(nombre) if actual else None
        datos[nombre] = pedir_valor(nombre, tipo, valor_actual)
    return datos


def mostrar_trainee(t):
    print("-" * 40)
    for clave, valor in t.items():
        print(f"{clave}: {valor}")


def manejar_respuesta(resp):
    """Devuelve el JSON si todo salio bien; si no, imprime el error y devuelve None."""
    if resp.status_code >= 400:
        try:
            detalle = resp.json()
        except ValueError:
            detalle = resp.text
        print(f"\nError {resp.status_code}: {detalle}")
        return None
    try:
        return resp.json()
    except ValueError:
        return {}


def llamar(metodo, url, **kwargs):
    try:
        resp = requests.request(metodo, url, timeout=TIMEOUT, **kwargs)
    except requests.exceptions.Timeout:
        print("\nLa API tardo demasiado en responder. Intenta de nuevo.")
        return None
    except requests.exceptions.ConnectionError:
        print("\nNo se pudo conectar con la API. Revisa tu internet o la URL.")
        return None
    return manejar_respuesta(resp)


# ---------------------------------------------------------------------------
# Opciones del menu
# ---------------------------------------------------------------------------
def listar_trainees():
    data = llamar("GET", BASE_URL + "/")
    if data is None:
        return
    if not data:
        print("\nNo hay trainees registrados.")
        return
    print(f"\nTotal: {len(data)}")
    for t in data:
        mostrar_trainee(t)


def buscar_trainee():
    id_ = input("ID del trainee: ").strip()
    data = llamar("GET", f"{BASE_URL}/{id_}")
    if data:
        mostrar_trainee(data)


def crear_trainee():
    print("\nDatos del nuevo trainee:")
    datos = pedir_datos()
    data = llamar("POST", BASE_URL + "/", json=datos)
    if data is not None:
        print("\nTrainee creado correctamente:")
        mostrar_trainee(data)


def actualizar_trainee():
    id_ = input("ID del trainee a actualizar: ").strip()
    actual = llamar("GET", f"{BASE_URL}/{id_}")
    if not actual:
        return
    print("\nPresiona Enter para conservar el valor actual.")
    datos = pedir_datos(actual)
    data = llamar("PUT", f"{BASE_URL}/{id_}", json=datos)
    if data is not None:
        print("\nTrainee actualizado:")
        mostrar_trainee(data)


def eliminar_trainee():
    id_ = input("ID del trainee a eliminar: ").strip()
    confirmar = input("Seguro que deseas eliminarlo? (s/n): ").strip().lower()
    if confirmar != "s":
        print("Operacion cancelada.")
        return
    data = llamar("DELETE", f"{BASE_URL}/{id_}")
    if data is not None:
        print("\nTrainee eliminado correctamente.")


# ---------------------------------------------------------------------------
# Menu principal
# ---------------------------------------------------------------------------
OPCIONES = {
    "1": ("Listar todos los trainees", listar_trainees),
    "2": ("Buscar trainee por ID", buscar_trainee),
    "3": ("Crear trainee", crear_trainee),
    "4": ("Actualizar trainee", actualizar_trainee),
    "5": ("Eliminar trainee", eliminar_trainee),
}


def menu():
    while True:
        print("\n===== GESTION DE TRAINEES =====")
        for clave, (texto, _) in OPCIONES.items():
            print(f"{clave}. {texto}")
        print("0. Salir")

        opcion = input("Elige una opcion: ").strip()
        if opcion == "0":
            print("Hasta luego!")
            break
        if opcion in OPCIONES:
            OPCIONES[opcion][1]()
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    menu()