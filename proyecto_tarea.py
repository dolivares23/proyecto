#importando biblioteca para trabajar
import streamlit as st
# para numero de telefono
import phonenumbers
from phonenumbers import NumberParseException
# para correo electronico
import re
#importando sqlite3 para base de datos
import sqlite3
#crear base de datos
conn = sqlite3.connect('mydatabase.db')

c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS users (nombre1 TEXT, nombre2 TEXT, apellido1 TEXT, apellido2 TEXT, cedula_de_identidad INTEGER, numero_de_telefono INTEGER, numero_de_telefono1 INTEGER, email TEXT, edad INTEGER, estatura INTEGER, discapacidad TEXT, discapacidad_1 TEXT, Sufre_Enfermedad TEXT, Sufre_Enfermedad_1 TEXT, lesion TEXT, lesion_1 TEXT, Alta_Competencia TEXT, Alta_Competencia_1 TEXT, Disponibilidad TEXT, disciplina_que_practica TEXT, disciplina_que_practica_1 TEXT)')

conn.commit()

conn.close()

def main():
    # Título de la aplicación
    st.title("Bienvenido al Registro de Disciplinas Deportivas del CFG")

    # Campo de entrada de texto obligatorio, nombre1
    nombre1 = st.text_input("Ingrese Primer Nombre")
    if nombre1.isalpha():
        pass
    elif nombre1 == "":
        pass
    else:
        st.error("El valor introducido en el campo anterior no es válido. Solo se permiten letras.")
        
    # Campo de entrada de texto opcional, nombre2
    nombre2 = st.text_input("Ingrese Segundo Nombre")
    if nombre2.isalpha():
        pass
    elif nombre2 == "":
        pass
    else:
        st.error("El valor introducido en el campo anterior no es válido. Solo se permiten letras.")

    # Campo de entrada de texto obligatorio, apellido1
    apellido1 = st.text_input("Ingrese Primer Apellido")
    if apellido1.isalpha():
        pass
    elif apellido1 == "":
        pass
    else:
        st.error("El valor introducido en el campo anterior no es válido. Solo se permiten letras.")
    

    # Campo de entrada de texto opcional, apellido2
    apellido2 = st.text_input("Ingrese Segundo Apellido")
    if apellido2.isalpha():
        pass
    elif apellido2 == "":
        pass
    else:
        st.error("El valor introducido en el campo anterior no es válido. Solo se permiten letras.")

    # Campo de entrada de texto obligatorio, numero de cedula
    cedula_de_identidad = st.text_input("Ingrese Número de Cedula de Identidad")
    if cedula_de_identidad.isdigit():
        pass
    elif cedula_de_identidad == "":
        pass
    else:
        st.error("El valor introducido en el campo anterior debe ser un número.")
    
     #widget de entrada de texto para el campo del número de teléfono
    numero_de_telefono = st.text_input("Ingrese Numero de Telefono:")

    # Validar el número de teléfono
    try:
        parsed_number = phonenumbers.parse(numero_de_telefono, "VE") # Ajusta el código de país según corresponda
        if not phonenumbers.is_valid_number(parsed_number):
            st.write("El número de teléfono no es válido.")
        else:
            st.write("El número de teléfono es válido.")
    except NumberParseException:
        st.write("El número de teléfono no es válido.")
    
   
    #widget de entrada de texto para el campo del número de teléfono
    numero_de_telefono1 = st.text_input("Confirme Numero de Telefono:")

    
    # Validar el número de teléfono
    try:
        parsed_number = phonenumbers.parse(numero_de_telefono1, "VE") # Ajusta el código de país según corresponda
        if not phonenumbers.is_valid_number(parsed_number):
            st.write("El número de teléfono no es válido.")
        else:
            st.write("El número de teléfono es válido.")
    except NumberParseException:
        st.write("El número de teléfono no es válido.")
        
    if numero_de_telefono != numero_de_telefono1:
        st.error("el numero de telefono no coincide")
        
        
    # Crear un campo de entrada para el correo electrónico
    email = st.text_input("Introduce tu correo electrónico")

    # Expresión regular para validar el correo electrónico
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Validar el correo electrónico
    if re.match(email_regex, email):
        st.write("El correo electrónico es válido.")
    else:
        st.write("El correo electrónico no es válido.")
              
    edades = ['']
    edades.extend(range(18, 76))
    
    # Campo de entrada de texto obligatorio, edad
    edad = st.selectbox("Ingrese Edad", edades)

    altura = ['']
    altura.extend(range(120, 220))

    # Campo de entrada de texto obligatorio, estatura
    estatura = st.selectbox("Ingrese Estatura en cms", altura)
    
    # Campo de entrada de texto obligatorio
    discapacidad = st.selectbox("¿Padece Usted de Alguna Discapacidad?", ["", "Sí", "No"])
    
    # Si la respuesta es "Sí", crear otra pregunta
    if discapacidad == "Sí":
        st.write("Por favor, indique su discapacidad.")
        discapacidad_1 = st.text_input("Indique su discapacidad")

    # Si la respuesta es "No", continuar con la siguiente pregunta
    elif discapacidad == "No":
        discapacidad_1 = "n/a"
        pass   
    
    # Campo de entrada de texto obligatorio
    Sufre_Enfermedad = st.selectbox("¿Sufre de Alguna Enfermedad Aguda o Cronica?", ["", "Sí", "No"])
    
    # Si la respuesta es "Sí", crear otra pregunta
    if Sufre_Enfermedad == "Sí":
        st.write("Por favor, indique que tipo de Enfermedad.")
        Sufre_Enfermedad_1 = st.text_input("Indique Enfermedad")

    # Si la respuesta es "No", continuar con la siguiente pregunta
    elif Sufre_Enfermedad == "No":
        Sufre_Enfermedad_1 = "n/a"
        pass
    

    # Campo de entrada de texto obligatorio
    lesion = st.selectbox("¿Actualmente Sufre de Alguna Lesión que Amerite Reposo o Atencion Medica?", ["", "Sí", "No"])
    
    # Si la respuesta es "Sí", crear otra pregunta
    if lesion == "Sí":
        st.write("Por favor, indique Tipo de Lesion.")
        lesion_1 = st.text_input("Indique Tipo de Lesion")

    # Si la respuesta es "No", continuar con la siguiente pregunta
    elif lesion == "No":
        lesion_1 = "n/a"
        pass
    

    # Campo de entrada de texto obligatorio
    Alta_Competencia = st.selectbox("¿Ha Practicado Alguna Disciplina Deportiva en Alta Competencia?", ["", "Sí", "No"])
     
    # Si la respuesta es "Sí", crear otra pregunta
    if Alta_Competencia == "Sí":
        st.write("Por favor, indique que disciplina.")
        Alta_Competencia_1 = st.text_input("Indique disciplina")

    # Si la respuesta es "No", continuar con la siguiente pregunta
    elif Alta_Competencia == "No":
        Alta_Competencia_1 = "n/a"
        pass
    
    
    # Campo de entrada de texto obligatorio
    Disponibilidad = st.selectbox("¿En Caso de que se Amerite su Presencia en Fines de Semana Para Disputar Torneos, Puede Asistir?", ["", "Sí", "No"])

    # Campo de entrada de texto obligatorio
    disciplina_que_practica = st.selectbox("Elija una Disciplina de la Lista a Continuación:", ["", "Baloncesto","Vóleibol","Bolas Criollas","Softbol","Futbol Sala","Ajedrez","Otra"])
    
    # Si la respuesta es "otra", crear otra pregunta
    if disciplina_que_practica == "Otra":
        st.write("Por favor, indique disciplina.")
        disciplina_que_practica_1 = st.text_input("Indique la otra disciplina")

    # Si la respuesta es "No", continuar con la siguiente pregunta
    elif disciplina_que_practica == "Baloncesto, Vóleibol, Bolas Criollas, Softbol, Futbol Sala, Ajedrez":
        disciplina_que_practica_1 = "n/a"  
        pass

    # Botón para enviar el formulario
    if st.button("Enviar"):
        st.success("“El movimiento es una medicina para crear el cambio físico, emocional y mental.” Carol Welch.")
        #st.success(f"¡Hola {nombre1}! Tienes {edad} años, mides {estatura} centimetros, practicas {disciplina_que_practica}, exitos.😍")
       
        #guardar en la base de datos
        conn = sqlite3.connect('mydatabase.db')

        c = conn.cursor()

        c.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (nombre1, nombre2, apellido1, apellido2, cedula_de_identidad, numero_de_telefono, numero_de_telefono1, email, edad, estatura, discapacidad, discapacidad_1, Sufre_Enfermedad, Sufre_Enfermedad_1, lesion, lesion_1, Alta_Competencia, Alta_Competencia_1, Disponibilidad, disciplina_que_practica, disciplina_que_practica_1))

        conn.commit()

        conn.close()


if __name__ == "__main__":
    main()