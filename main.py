import customtkinter as ctk
import os
import sys
import subprocess
from tkinter import messagebox, filedialog
import modules.recon as recon_module 

# --- CONFIGURACIÓN VISUAL ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class ChimeraToolkit(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("🐍 PROJECT CHIMERA - CIBERSEGURIDAD OFENSIVA")
        self.geometry("1000x700")
        
        # Layout: Columna 0 (Menú) - Columna 1 (Contenido)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ============================
        # 1. BARRA LATERAL (MENÚ)
        # ============================
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(6, weight=1)

        # Logo / Título
        self.logo = ctk.CTkLabel(self.sidebar, text="PROJECT\nCHIMERA", font=ctk.CTkFont(size=24, weight="bold"))
        self.logo.grid(row=0, column=0, padx=20, pady=(20, 30))

        # Botones de Navegación
        self.btn_recon = ctk.CTkButton(self.sidebar, text="👁️ RECON (Geo)", command=self.show_recon)
        self.btn_recon.grid(row=1, column=0, padx=20, pady=10)

        self.btn_crack = ctk.CTkButton(self.sidebar, text="🔨 CRACKING (Zip)", command=self.show_cracking)
        self.btn_crack.grid(row=2, column=0, padx=20, pady=10)

        self.btn_crypto = ctk.CTkButton(self.sidebar, text="🔐 CRYPTO (Ransom)", command=self.show_crypto)
        self.btn_crypto.grid(row=3, column=0, padx=20, pady=10)

        self.btn_attack = ctk.CTkButton(self.sidebar, text="💀 ATTACK (C2)", fg_color="#c0392b", hover_color="#e74c3c", command=self.show_attack)
        self.btn_attack.grid(row=4, column=0, padx=20, pady=10)

        # Botón Salir
        self.btn_exit = ctk.CTkButton(self.sidebar, text="SALIR", fg_color="transparent", border_width=1, command=self.destroy)
        self.btn_exit.grid(row=7, column=0, padx=20, pady=20)

        # ============================
        # 2. PANTALLAS (FRAMES)
        # ============================
        
        # --- PANTALLA 1: RECON (Geo-Tracker) ---
        self.frame_recon = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        ctk.CTkLabel(self.frame_recon, text="BULK GEO-TRACKER (OSINT)", font=("Arial", 22, "bold")).pack(pady=20)
        ctk.CTkLabel(self.frame_recon, text="Análisis masivo de metadatos GPS en imágenes.").pack(pady=10)
        
        # Botón para ejecutar la acción
        ctk.CTkButton(self.frame_recon, 
                      text="📁 Seleccionar Carpeta de Fotos", 
                      height=50, width=250,
                      fg_color="#8e44ad", hover_color="#9b59b6",
                      command=self.run_recon).pack(pady=30)

        # ETIQUETA DE ESTADO (FALTABA ESTO)
        self.label_status_recon = ctk.CTkLabel(self.frame_recon, text="Esperando objetivo...", font=("Consolas", 12))
        self.label_status_recon.pack(pady=10)

        # --- PANTALLA 2: CRACKING (Vault Breaker) ---
        self.frame_crack = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        ctk.CTkLabel(self.frame_crack, text="VAULT BREAKER (ZIP/PDF)", font=("Arial", 22, "bold")).pack(pady=20)
        ctk.CTkButton(self.frame_crack, text="📂 Cargar Archivo Protegido", command=lambda: print("Próximamente")).pack(pady=20)

        # --- PANTALLA 3: CRYPTO (Ransomware) ---
        self.frame_crypto = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        ctk.CTkLabel(self.frame_crypto, text="RANSOMWARE SIMULATOR (AES)", font=("Arial", 22, "bold")).pack(pady=20)
        
        self.box_crypto = ctk.CTkFrame(self.frame_crypto, fg_color="transparent")
        self.box_crypto.pack(pady=20)
        ctk.CTkButton(self.box_crypto, text="🔒 ENCRIPTAR", fg_color="#c0392b", command=lambda: print("Próximamente")).grid(row=0, column=0, padx=10)
        ctk.CTkButton(self.box_crypto, text="🔓 DESENCRIPTAR", fg_color="#27ae60", command=lambda: print("Próximamente")).grid(row=0, column=1, padx=10)

        # --- PANTALLA 4: ATTACK (C2 Server) ---
        self.frame_attack = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        ctk.CTkLabel(self.frame_attack, text="C2 COMMANDER (REVERSE SHELL)", font=("Arial", 22, "bold"), text_color="#e74c3c").pack(pady=20)
        
        self.console_fake = ctk.CTkTextbox(self.frame_attack, width=700, height=300)
        self.console_fake.pack(pady=20)
        self.console_fake.insert("0.0", "[INFO] Listo para iniciar servidor...\n")
        
        self.btn_launch_c2 = ctk.CTkButton(self.frame_attack, 
                                           text="▶ INICIAR SERVIDOR C2", 
                                           fg_color="#c0392b", 
                                           height=50,
                                           command=self.run_c2_server)
        self.btn_launch_c2.pack(pady=20)

        # Iniciar mostrando la pantalla de Recon
        self.show_recon()

    # ============================
    # 3. LÓGICA DE NAVEGACIÓN
    # ============================
    def hide_all(self):
        self.frame_recon.grid_forget()
        self.frame_crack.grid_forget()
        self.frame_crypto.grid_forget()
        self.frame_attack.grid_forget()

    def show_recon(self):
        self.hide_all()
        self.frame_recon.grid(row=0, column=1, sticky="nsew")

    def show_cracking(self):
        self.hide_all()
        self.frame_crack.grid(row=0, column=1, sticky="nsew")

    def show_crypto(self):
        self.hide_all()
        self.frame_crypto.grid(row=0, column=1, sticky="nsew")

    def show_attack(self):
        self.hide_all()
        self.frame_attack.grid(row=0, column=1, sticky="nsew")

    # ============================
    # 4. FUNCIONES DE LÓGICA
    # ============================
    
    # --- LÓGICA RECON) ---
    def run_recon(self):
        target_folder = filedialog.askdirectory(title="SELECCIONA CARPETA CON FOTOS")
        
        if target_folder:
            
            self.label_status_recon.configure(text="⏳ Analizando metadatos...", text_color="orange")
            self.update() 
            
            #Analizamos la carpeta pasada como argumento
            mensaje, ruta_mapa = recon_module.analizar_directorio(target_folder)
            
            #Una vez ceado el mapa, si se ha creado correctamente
            if ruta_mapa:
                self.label_status_recon.configure(text="✅ COMPLETADO", text_color="#2ecc71")
                if messagebox.askyesno("ÉXITO", f"{mensaje}\n\n¿Abrir mapa ahora?"):
                    recon_module.abrir_mapa(ruta_mapa)
            else:
                self.label_status_recon.configure(text="❌ SIN DATOS GPS", text_color="#e74c3c")
                messagebox.showwarning("Resultado", mensaje)

    # --- LÓGICA SERVER C2 ---
    def run_c2_server(self):
        python_exe = sys.executable 
        #
        script_path = os.path.join("modules", "server.py") 
        
        if not os.path.exists(script_path):
            messagebox.showerror("Error", f"No encuentro el archivo:\n{script_path}")
            return

        try:
            if sys.platform == "win32":
                subprocess.run(f'start cmd /k "{python_exe} {script_path}"', shell=True)
            else:
                subprocess.run(["gnome-terminal", "--", python_exe, script_path])
        except Exception as e:
            messagebox.showerror("Error", f"Fallo al lanzar terminal:\n{str(e)}")

if __name__ == "__main__":
    app = ChimeraToolkit()
    app.mainloop()