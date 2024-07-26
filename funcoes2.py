def loginUsuario(perfil):
        if perfil.lower() == 'admin':
            print ('Bem-vindo, Administrador')
        else:
            print('Bem-vindo, Usuário')

perfil = 'Admin'
loginUsuario(perfil)
perfil = 'admin'
loginUsuario(perfil)
perfil = 'User'
loginUsuario(perfil)
perfil = 'usuário'
loginUsuario(perfil)
perfil = 'etc.'
loginUsuario(perfil)