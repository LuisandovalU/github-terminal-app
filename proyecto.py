import requests as requests

# La función principal que hace el trabajo
def conseguir_info_perfil(nombre_usuario):
    # Construir la dirección web (URL) para la API de GitHub
    # Esta es la dirección que nos da la información de los usuarios
    url_api = f"https://api.github.com/users/{nombre_usuario}"
    
    # Ir a esa dirección y pedir los datos
    print(f"Buscando información de: {url_api}")
    respuesta = requests.get(url_api)
    
    # ¡Revisar si todo salió bien!
    # El código 200 significa "¡todo chido!"
    if respuesta.status_code == 200:
        
        datos_perfil = respuesta.json()
        
        # Devolver los datos para usarlos
        return datos_perfil
    else:
        # Si no es 200, algo salió mal jeje
        print("¡Error! No pude encontrar ese usuario o algo falló.")
        print(f"Código de error de GitHub: {respuesta.status_code}")
        return None # Devolvemos "Nada" para indicar el fallo

# --- Para la App de Terminal ---

# Le pedimos al usuario su nombre de GitHub
usuario_a_buscar = input("Dame el usuario de GitHub: ")

# Llamamos a nuestra función para conseguir la info
info_github = conseguir_info_perfil(usuario_a_buscar)

# Ahora revisamos si la función nos devolvió datos o si devolvió "None"
if info_github:
    print("------------------------------------------")
    print(" ¡Perfil Encontrado! ")
    print("------------------------------------------")
    
    # Imprimimos la información clave del diccionario que nos dio GitHub
    # Usamos .get() por si acaso el dato no existe, así no da error
    print(f"Nombre: {info_github.get('name', 'N/A')}")
    print(f"Usuario: {info_github.get('login', 'N/A')}")
    print(f"Ubicación: {info_github.get('location', 'No especificada')}")
    print(f"Biografía (Bio): {info_github.get('bio', 'Sin biografía')}")
    print(f"URL del perfil: {info_github.get('html_url', 'N/A')}")
    print(f"Repositorios públicos: {info_github.get('public_repos', 'N/A')}")
    print(f"Seguidores (Followers): {info_github.get('followers', 'N/A')}")
    print(f"Siguiendo (Following): {info_github.get('following', 'N/A')}")
    print(f"Fecha de creación: {info_github.get('created_at', 'N/A')}")

# Si no hubo info, el error ya se imprimió dentro de la función.