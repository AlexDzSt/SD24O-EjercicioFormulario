from fastapi import FastAPI, Form, UploadFile, File
import os 
import uuid

app = FastAPI()

@app.post("/registro-usuario")
async def registrar_usuario(nombre:str=Form(...), direccion:str=Form(...), vip:bool=Form(False), foto:UploadFile=File(...)):
    print("Nombre", nombre)
    print("Direccion", direccion)
    
    home_usuario = os.path.expanduser("~")
    nombre_archivo = uuid.uuid4()
    extension_foto = os.path.splitext(foto.filename)[1]
    if vip:
        ruta_imagen = f'{home_usuario}/fotos-usuarios-vip/{nombre_archivo}{extension_foto}'
    else: 
        ruta_imagen = f'{home_usuario}/fotos-usuarios/{nombre_archivo}{extension_foto}'
    print ("Guardando la foto en ", ruta_imagen)
    with open (ruta_imagen, "wb") as imagen:
        contenido = await foto.read()
        imagen.write(contenido)
        
    respuesta = {
        "Nombre": nombre,
        "Direccion": direccion,
        "Ruta": ruta_imagen
    }
    return respuesta

# decorator
@app.get("/")
def hola_mundo():
    print("invocando a ruta /")
    respuesta = {
        "mensaje": "hola mundo!"
    }
    return respuesta