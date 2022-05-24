from turtle import position
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


archivo = open("data/datos_jugadores.txt", "m")
registro2 = archivo.readlines()


for m in registro2:
  club = m.split(";")[0]
  position = m.split(";")[1]
  dorsal = m.split(";")[2]
  nombre = m.split(";")[3]

  jugador= Jugador(club_id=club, posicion=position, dorsal = dorsal, nombre = nombre)

  session.add(jugador)

session.commit()