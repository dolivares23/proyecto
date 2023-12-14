import streamlit as st
import sqlite3

usuarios = {'dolivares':'12345678', 'invitado':'123456'}
def main():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    for row in c.fetchall():
        st.write(row)
    conn.close()
    

with st.form("login"):
   st.write("Ingresa sus credenciales")
   usuario = st.text_input("Usuario")
   contraseña = st.text_input("Contraseña")

   # Every form must have a submit button.
   ingreso = st.form_submit_button("Ingresar")
   if ingreso:
       if usuario in usuarios and contraseña in usuarios[usuario]:
           st.success("Bienvenido")
           main()

