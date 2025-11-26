import customtkinter as ctk
import os
import sys
import subprocess
from tkinter import messagebox

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
        self.sidebar.grid_rowconfigure(6, weight=1) # Espaciador al fondo

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
        ctk.CTkButton(self.frame_recon, text="📁 Seleccionar Carpeta de Fotos", command=lambda: print("Próximamente: Recon")).pack(pady=20)

        # --- PANTALLA 2: CRACKING (Vault Breaker) ---
        self.frame_crack = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        ctk.CTkLabel(self.frame_crack, text="VAULT BREAKER (ZIP/PDF)", font=("Arial", 22, "bold")).pack(pady=20)
        ctk.CTkLabel(self.frame_crack, text="Ataque de fuerza bruta multihilo.").pack(pady=10)
        ctk.CTkButton(self.frame_crack, text="📂 Cargar Archivo Protegido", command=lambda: print("Próximamente: Cracking")).pack(pady=20)

        # --- PANTALLA 3: CRYPTO (Ransomware) ---
        self.frame_crypto = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        ctk.CTkLabel(self.frame_crypto, text="RANSOMWARE SIMULATOR (AES)", font=("Arial", 22, "bold")).pack(pady=20)
        ctk.CTkLabel(self.frame_crypto, text="Cifrado de directorios y secuestro de sistema.").pack(pady=10)
        
        self.box_crypto = ctk.CTkFrame(self.frame_crypto, fg_color="transparent")
        self.box_crypto.pack(pady=20)
        ctk.CTkButton(self.box_crypto, text="🔒 ENCRIPTAR (Simulación)", fg_color="#c0392b", hover_color="#e74c3c", command=lambda: print("Próximamente: Encrypt")).grid(row=0, column=0, padx=10)
        ctk.CTkButton(self.box_crypto, text="🔓 DESENCRIPTAR (Rescue)", fg_color="#27ae60", hover_color="#2ecc71", command=lambda: print("Próximamente: Decrypt")).grid(row=0, column=1, padx=10)

        # --- PANTALLA 4: ATTACK (C2 Server) ---
        self.frame_attack = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        ctk.CTkLabel(self.frame_attack, text="C2 COMMANDER (REVERSE SHELL)", font=("Arial", 22, "bold"), text_color="#e74c3c").pack(pady=20)
        ctk.CTkLabel(self.frame_attack, text="Panel de control remoto y recepción de Keylogs.").pack(pady=5)
        
        # Consola visual (solo decorativa, el server real va en otra ventana)
        self.console_fake = ctk.CTkTextbox(self.frame_attack, width=700, height=300)
        self.console_fake.pack(pady=20)
        self.console_fake.insert("0.0", "[INFO] El servidor se lanzará en una terminal independiente para evitar bloqueos.\n[INFO] Esperando orden de inicio...\n")
        
        # EL BOTÓN QUE LANZA TU CÓDIGO
        self.btn_launch_c2 = ctk.CTkButton(self.frame_attack, 
                                           text="▶ INICIAR SERVIDOR C2 (PUERTO 4444)", 
                                           fg_color="#c0392b", 
                                           hover_color="#e74c3c", 
                                           height=50, 
                                           font=("Arial", 14, "bold"),
                                           command=self.run_c2_server) # <--- AQUÍ LA MAGIA
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
    # 4. FUNCIÓN LANZADORA (C2)
    # ============================
    def run_c2_server(self):
        python_exe = sys.executable 
        script_path = os.path.join("modules", "server.py")
        
        if not os.path.exists(script_path):
            messagebox.showerror("Error", f"No encuentro el archivo:\n{script_path}")
            return

        print(f"[*] Lanzando servidor: {script_path}")
        
        try:
            if sys.platform == "win32":
                # 'start cmd /k' mantiene la ventana abierta aunque falle
                comando = f'start cmd /k "{python_exe} {script_path}"'
                subprocess.run(comando, shell=True)
            else:
                # Linux/Mac
                subprocess.run(["gnome-terminal", "--", python_exe, script_path])
                    
        except Exception as e:
            messagebox.showerror("Error", f"Fallo al lanzar terminal:\n{str(e)}")

if __name__ == "__main__":
    app = ChimeraToolkit()
    app.mainloop()