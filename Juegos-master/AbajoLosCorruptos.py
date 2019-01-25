import ScreenMaster as sm
from prejuego import Login, Escenarios, Personajes, prueba


def main():
    
    '''
    Asegurar comunicación con el servidor
    '''

    sc_login = Login.Login()
    sc_personajes = Personajes.Personajes()
    sc_escenarios = Escenarios.Escenarios()

    secuencia_principal = [('login','Abajo los corruptos'),
                          ('personajes','Abajo los corruptos'),
                          ('escenario','Abajo los corruptos')]



    '''
    #clave_publica_server = xxxxxxxxxxxxx
    #sc_login.set_clave_asimetrica_server(clave_publica_server)    
    '''
    
    ventana_juego = sm.ScreenMaster(sc_login)
    ventana_juego.set_bool_sgt_pnt(False) 
    ventana_juego.cambiar_fondo(secuencia_principal[0][0],secuencia_principal[0][1])


    #ventana_juego.loopear(True, 'login'):    
    while not ventana_juego._bool_sgt_pnt:
        ventana_juego.loopear_2()

        if ventana_juego.mensaje[0] is not None:
            #Enviar dato al servidor para corroborar credenciales
            rpta = True 

            if rpta:
                break
            else:
                ventana_juego.mensaje[0] = None



    
    ventana_juego.set_objeto(sc_personajes)
    ventana_juego.set_bool_sgt_pnt(False)
    ventana_juego.cambiar_fondo(secuencia_principal[1][0],secuencia_principal[1][1])

    while not ventana_juego._bool_sgt_pnt:
        ventana_juego.loopear_2()
    
    #ejecutar el engine






if __name__ == "__main__":
    main()

