import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.configuracoes_da_janela_inicial()
        self.tela_de_login()
    
    # Configurando a janela principal    
    def configuracoes_da_janela_inicial(self):
        self.geometry("700x400")
        self.title("Tela de Login")
        self.resizable(False, False)    

    def tela_de_login(self):
        # Criar a frame do formulario de login
        largura_frame = 350
        altura_frame = 380
        x_frame = (self.winfo_width() - largura_frame) // 2 - 80  
        y_frame = (self.winfo_height() - altura_frame) // 2 - 40 + 2  
        self.frame_login = ctk.CTkFrame(self, width=largura_frame, height=altura_frame)
        self.frame_login.place(x=x_frame, y=y_frame)
  
        # Colocando widget dentro do frame - formulario de login
        self.lbtitle = ctk.CTkLabel(self.frame_login, text="Faça seu Login", font=("Century Gothic bold", 22))
        self.lbtitle.grid(row=0, column=0, padx=10, pady=10)
        
        self.username_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Seu nome de usuário...", font=("Century Gothic bold", 16), corner_radius=15, border_color= "#005")
        self.username_login_entry.grid(row=1, column=0, pady=10, padx=10)
  
        self.senha_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Sua senha...", font=("Century Gothic bold", 16), corner_radius=15, border_color= "#005", show="*")
        self.senha_login_entry.grid(row=2, column=0, pady=5, padx=10)
        self.senha_visivel = False
    
        self.ver_senha_login = ctk.CTkCheckBox(self.frame_login, text="Clique para ver a senha", font=("Century Gothic bold", 12), corner_radius=20, command=self.mostrar_senha_login)
        self.ver_senha_login.grid(row=3, column=0, pady=10, padx=10)
        
        self.btn_login = ctk.CTkButton(self.frame_login, width=30, text="Fazer Login".upper(), font=("Century Gothic bold", 14), corner_radius=15)
        self.btn_login.grid(row=4, column=0, pady=10, padx=10)
        
        self.span = ctk.CTkLabel(self.frame_login, text="Se você não tem conta,\nclique no botão abaixo para cadastrar!", font=("Century Gothic", 10))
        self.span.grid(row=5, column=0, pady=10, padx=10)

        self.btn_cadastro = ctk.CTkButton(self.frame_login, width=300, fg_color="green", hover_color="#050", text="Fazer Cadastro".upper(), font=("Century Gothic bold", 14), corner_radius=15, command=self.tela_de_cadastro)
        self.btn_cadastro.grid(row=6, column=0, pady=10, padx=10)
        
    def mostrar_senha_login(self):
        if not self.senha_visivel:
            self.senha_login_entry.configure(show="")
            self.senha_visivel = True
        else:
            self.senha_login_entry.configure(show="*")
            self.senha_visivel = False
        
    def tela_de_cadastro(self):
        #Remover o formulario de login
        self.frame_login.place_forget()
    
        #Frame de formulario de cadastro
        largura_frame = 350
        altura_frame = 380
        x_frame = (self.winfo_width() - largura_frame) // 2 - 80 + 10  
        y_frame = (self.winfo_height() - altura_frame) // 2 - 40 - 20  
        self.frame_cadastro = ctk.CTkFrame(self, width=largura_frame, height=altura_frame)
        self.frame_cadastro.place(x=x_frame, y=y_frame)
    
        #Criando o titulo
        self.lbtitle_cadastro = ctk.CTkLabel(self.frame_cadastro, text="Faça seu Cadastro", font=("Century Gothic bold", 22))
        self.lbtitle_cadastro.grid(row=0, column=0, padx=10, pady=10)
    
        #Criar widgets da tela de cadastro
        self.username_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Seu nome de usuário...", font=("Century Gothic bold", 16), corner_radius=15, border_color= "#005")
        self.username_cadastro_entry.grid(row=1, column=0, pady=10, padx=10)
    
        self.email_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Email de usuário...", font=("Century Gothic bold", 16), corner_radius=15, border_color= "#005")
        self.email_cadastro_entry.grid(row=2, column=0, pady=10, padx=10)

        self.senha_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Senha do usuario...", font=("Century Gothic bold", 16), corner_radius=15, border_color= "#005", show="*")
        self.senha_cadastro_entry.grid(row=3, column=0, pady=10, padx=10)
        self.senha_visivel_cadastro = False
    
        self.confirma_senha_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Confirmar a senha de usuário...", font=("Century Gothic bold", 16), corner_radius=15, border_color= "#005", show="*")
        self.confirma_senha_entry.grid(row=4, column=0, pady=10, padx=10)
    
        self.ver_senha_cadastro = ctk.CTkCheckBox(self.frame_cadastro, text="Clique para ver a senha", font=("Century Gothic bold", 12), corner_radius=20, command=self.mostrar_senha_cadastro)
        self.ver_senha_cadastro.grid(row=5, column=0, pady=10, padx=10)
    
        self.btn_cadastrar_user = ctk.CTkButton(self.frame_cadastro, width=300, fg_color="green", hover_color="#050", text="Cadastrar".upper(), font=("Century Gothic bold", 16), corner_radius=15)
        self.btn_cadastrar_user.grid(row=6, column=0, pady=10, padx=10)
    
        self.btn_login_back = ctk.CTkButton(self.frame_cadastro, width=30, text="Voltar a Login".upper(), font=("Century Gothic bold", 14), corner_radius=15, fg_color="#444", hover="#333", command=self.voltar_para_login)
        self.btn_login_back.grid(row=7, column=0, pady=10, padx=10)
        
    def mostrar_senha_cadastro(self):
        if not self.senha_visivel_cadastro:
            self.senha_cadastro_entry.configure(show="")
            self.senha_visivel_cadastro = True
        else:
            self.senha_cadastro_entry.configure(show="*")
            self.senha_visivel_cadastro = False
        
    def voltar_para_login(self):
        # Limpa o frame de cadastro
        self.frame_cadastro.place_forget()
        # Exibe o frame de login novamente
        self.tela_de_login()

if __name__ == "__main__":
    app = App()
    app.mainloop()
