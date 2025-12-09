import customtkinter as ctk
import os,sys
import subprocess,socket 
from tkinter import messagebox, filedialog
import modules.zipCracker as cracker_module
import modules.portScanner as scanner_module
import modules.recon as recon_module 


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class ChimeraToolkit(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la Ventana
        self.title("🐍 PROJECT CHIMERA - SECURITY SUITE")
        self.geometry("1100x750")
        
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ============================
        # 1. BARRA LATERAL (MENÚ)
        # ============================
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(6, weight=1)

        # Logo
        self.logo = ctk.CTkLabel(self.sidebar, text="PROJECT\nCHIMERA", font=ctk.CTkFont(size=24, weight="bold"))
        self.logo.grid(row=0, column=0, padx=20, pady=(20, 30))

        # Botones
        self.btn_recon = ctk.CTkButton(self.sidebar, text="👁️ RECON (Geo)", command=self.show_recon)
        self.btn_recon.grid(row=1, column=0, padx=20, pady=10)

        self.btn_crack = ctk.CTkButton(self.sidebar, text="🔨 CRACKING (Zip)", command=self.show_cracking)
        self.btn_crack.grid(row=2, column=0, padx=20, pady=10)

        # NUEVO BOTÓN NETWORK (Reemplaza a Crypto)
        self.btn_network = ctk.CTkButton(self.sidebar, text="📡 NETWORK (Scan)", command=self.show_network)
        self.btn_network.grid(row=3, column=0, padx=20, pady=10)

        self.btn_attack = ctk.CTkButton(self.sidebar, text="💀 ATTACK (C2)", fg_color="#c0392b", hover_color="#e74c3c", command=self.show_attack)
        self.btn_attack.grid(row=4, column=0, padx=20, pady=10)

        self.btn_exit = ctk.CTkButton(self.sidebar, text="SALIR", fg_color="transparent", border_width=1, command=self.destroy)
        self.btn_exit.grid(row=7, column=0, padx=20, pady=20)

        # ============================
        # 2. PANTALLAS (FRAMES)
        # ============================
        
        # --- PANTALLA 1: RECON ---
        self.frame_recon = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        ctk.CTkLabel(self.frame_recon, text="BULK GEO-TRACKER (OSINT)", font=("Arial", 22, "bold")).pack(pady=20)
        ctk.CTkLabel(self.frame_recon, text="Análisis masivo de metadatos GPS en imágenes.").pack(pady=5)
        ctk.CTkButton(self.frame_recon, text="📁 Seleccionar Carpeta de Fotos", height=50, width=250, fg_color="#8e44ad", command=self.run_recon).pack(pady=30)
        self.label_status_recon = ctk.CTkLabel(self.frame_recon, text="Esperando objetivo...", font=("Consolas", 12))
        self.label_status_recon.pack(pady=10)

        # --- PANTALLA 2: CRACKING ---
        self.frame_crack = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        ctk.CTkLabel(self.frame_crack, text="VAULT BREAKER (ZIP/PDF)", font=("Arial", 22, "bold")).pack(pady=20)
        ctk.CTkLabel(self.frame_crack, text="Ataque de diccionario contra archivos protegidos.").pack(pady=5)
        ctk.CTkButton(self.frame_crack, text="📂 Cargar Archivo Protegido + Diccionario", height=50, width=300, fg_color="#e67e22", command=self.run_crack).pack(pady=20)
        self.lbl_status_crack = ctk.CTkLabel(self.frame_crack, text="Sistema listo para fuerza bruta.", text_color="gray")
        self.lbl_status_crack.pack(pady=10)

        # --- PANTALLA 3: NETWORK ---
        self.frame_network = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        ctk.CTkLabel(self.frame_network, text="NETWORK PORT SCANNER", font=("Arial", 26, "bold")).pack(pady=20)
        ctk.CTkLabel(self.frame_network, text="Detecta servicios vulnerables y puertos abiertos (Multi-Threaded).").pack(pady=5)
        
        ctk.CTkButton(self.frame_network, text="📡 INICIAR ESCANEO", 
                      height=50, width=300, fg_color="#2980b9", hover_color="#3498db",
                      command=self.run_scanner).pack(pady=20)
        
        # 
        self.console_scanner = ctk.CTkTextbox(self.frame_network, width=700, height=350, fg_color="black", text_color="#00ff00", font=("Consolas", 12))
        self.console_scanner.pack(pady=10)
        self.console_scanner.insert("0.0", ">> Sistema listo. Esperando IP objetivo...\n")

        # --- PANTALLA 4: ATTACK ---
        self.frame_attack = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        ctk.CTkLabel(self.frame_attack, text="C2 COMMANDER (REVERSE SHELL)", font=("Arial", 22, "bold"), text_color="#e74c3c").pack(pady=20)
        self.console_fake = ctk.CTkTextbox(self.frame_attack, width=700, height=300)
        self.console_fake.pack(pady=20)
        self.console_fake.insert("0.0", "[INFO] Listo para iniciar servidor C2 en puerto 4444...\n")
        self.btn_launch_c2 = ctk.CTkButton(self.frame_attack, text="▶ INICIAR SERVIDOR C2", fg_color="#c0392b", height=50, command=self.run_c2_server)
        self.btn_launch_c2.pack(pady=20)

        # Iniciar mostrando la pantalla de Recon
        self.show_recon()

    # ============================
    # 3. LÓGICA DE NAVEGACIÓN
    # ============================
    def hide_all(self):
        self.frame_recon.grid_forget()
        self.frame_crack.grid_forget()
        self.frame_network.grid_forget()
        self.frame_attack.grid_forget()

    def show_recon(self):
        self.hide_all()
        self.frame_recon.grid(row=0, column=1, sticky="nsew")

    def show_cracking(self):
        self.hide_all()
        self.frame_crack.grid(row=0, column=1, sticky="nsew")

    def show_network(self):
        self.hide_all()
        self.frame_network.grid(row=0, column=1, sticky="nsew")

    def show_attack(self):
        self.hide_all()
        self.frame_attack.grid(row=0, column=1, sticky="nsew")

    # ============================
    # 4. FUNCIONES LÓGICAS
    # ============================
    
    # --- LÓGICA RECON ---
    def run_recon(self):
        target_folder = filedialog.askdirectory(title="SELECCIONA CARPETA CON FOTOS")
        if target_folder:
            self.label_status_recon.configure(text="⏳ Analizando metadatos...", text_color="orange")
            self.update() 
            try:
                mensaje, ruta_mapa = recon_module.analizar_directorio(target_folder)
                if ruta_mapa:
                    self.label_status_recon.configure(text="✅ COMPLETADO", text_color="#2ecc71")
                    if messagebox.askyesno("ÉXITO", f"{mensaje}\n\n¿Abrir mapa ahora?"):
                        recon_module.abrir_mapa(ruta_mapa)
                else:
                    self.label_status_recon.configure(text="❌ SIN DATOS GPS", text_color="#e74c3c")
                    messagebox.showwarning("Resultado", mensaje)
            except Exception as e:
                self.label_status_recon.configure(text="❌ ERROR", text_color="red")
                messagebox.showerror("Error", str(e))

    # --- LÓGICA CRACKING (GUI) ---
    def run_crack(self):
        zip_file = filedialog.askopenfilename(title="SELECCIONA EL ZIP", filetypes=[("Archivos ZIP", "*.zip")])
        if not zip_file: return
        diccionario = filedialog.askopenfilename(title="SELECCIONA EL DICCIONARIO", filetypes=[("Archivos de Texto", "*.txt")])
        if not diccionario: return

        self.lbl_status_crack.configure(text="Hackeando... (Mira la terminal)", text_color="orange")
        self.update()
        
        try:
            resultado = cracker_module.crack_zip(zip_file, diccionario)
        
            if "ENCONTRADA" in resultado or "ACCESO CONCEDIDO" in resultado:
                self.lbl_status_crack.configure(text="✅ CONTRASEÑA ENCONTRADA", text_color="#2ecc71")
                messagebox.showinfo("VAULT BREAKER", resultado)
            else:
                self.lbl_status_crack.configure(text="❌ FALLÓ EL ATAQUE", text_color="#e74c3c")
                messagebox.showwarning("Resultado", resultado)
        except Exception as e:
            messagebox.showerror("Error en módulo", str(e))

    # --- LÓGICA NETWORK SCANNER  ---
    def run_scanner(self):
        target = ctk.CTkInputDialog(text="Introduce IP o Dominio:\n(Usa 127.0.0.1 para auto-scan)", title="PORT SCANNER").get_input()
        if not target: return
        
        
        self.console_scanner.delete("0.0", "end")
        self.console_scanner.insert("0.0", f"[*] Resolviendo {target}...\n")
        self.update()
        
        try:
            target_ip = socket.gethostbyname(target)
            self.console_scanner.insert("end", f"[*] Iniciando escaneo multihilo en: {target_ip}\n")
            self.console_scanner.insert("end", "[*] Esto puede tardar unos segundos...\n\n")
            self.update()
            
            
            res = scanner_module.scan_obj(target_ip)
            
        
            self.console_scanner.insert("end", f"RESULTADOS:\n{'-'*40}\n{res}\n{'-'*40}\n")
            self.console_scanner.insert("end", "\n[✓] Operación finalizada.")
            
        except Exception as e:
            self.console_scanner.insert("end", f"\n[!] Error: {e}")

    # --- LÓGICA C2 SERVER ---
    def run_c2_server(self):
        python_exe = sys.executable 
        script_path = os.path.join("modules", "server.py") 
        if not os.path.exists(script_path):
            messagebox.showerror("Error", f"No encuentro: {script_path}")
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