import tkinter as tk
from tkinter import messagebox, ttk
import subprocess
import os
import threading
import queue
import time
import webbrowser
import re # Import the regular expressions module
import sys # Import the sys module for clean exit

# --- Default NiceHash (RandomX) Configuration ---
# NiceHash pool for RandomX (port 443 with SSL/TLS)
POOL_URL = "randomxmonero.auto.nicehash.com:443"
# YOUR NICEHASH MINING ADDRESS (VERY IMPORTANT! Use the NHbR... address that works for mining)
# Based on your experience, the NHbR... address is the one that allows mining without "Invalid mining address".
NICEHASH_WALLET = "PEGA_AQUI_TU_DIRECCION_DE_MINADO_NHBR" # Placeholder for the mining address
WORKER_NAME = "NiceHashCPUWorker" # Name for your worker

# Path to the XMRig executable
# MAKE SURE THIS PATH IS CORRECT ON YOUR SYSTEM!
XMRIG_PATH = r"C:\Users\Marcelo\Desktop\NiceHash\xmrig\xmrig.exe" # Using the path you provided

class MinerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Minero CPU para NiceHash - GUI Optimizada")
        self.root.geometry("850x700") # Adjusted size
        self.root.resizable(True, True)

        self.process = None 
        self.log_queue = queue.Queue()
        self.log_thread = None

        self._setup_ui()
        # Bind the window closing protocol to on_closing
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing) 
        self.root.after(100, self._check_log_queue)

    def _setup_ui(self):
        """Configures all UI widgets."""
        # --- Styles (Tkinter ttk) ---
        style = ttk.Style()
        style.theme_use("clam") # A more modern theme than "default" or "alt"

        style.configure("TFrame", background="#e0e0e0")
        style.configure("TLabel", background="#e0e0e0", font=("Arial", 11))
        style.configure("TLabelFrame", background="#e0e0e0", font=("Arial", 12, "bold"))
        style.configure("TButton", font=("Arial", 11, "bold"), padding=6)
        
        # Style for the Start Mining button (green)
        style.configure("Green.TButton", background="#28a745", foreground="white")
        style.map("Green.TButton",
                  background=[('active', '#218838'), ('!disabled', '#28a745')],
                  foreground=[('active', 'white'), ('!disabled', 'white')])

        # Style for the Stop Mining button (red)
        style.configure("Red.TButton", background="#dc3545", foreground="white") # Default red background
        style.map("Red.TButton",
                  background=[('active', '#c82333'), ('!disabled', '#dc3545')],
                  foreground=[('active', 'white'), ('!disabled', 'white')])

        # Style for the Online Stats button (blue)
        style.configure("Blue.TButton", background="#007bff", foreground="white") # Default blue background
        style.map("Blue.TButton",
                  background=[('active', '#0056b3'), ('!disabled', '#007bff')],
                  foreground=[('active', 'white'), ('!disabled', 'white')])

        # --- Main Frame ---
        main_frame = ttk.Frame(self.root, padding="15 15 15 15")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # --- Configuration Section ---
        config_frame = ttk.LabelFrame(main_frame, text="Configuración de Minería NiceHash", padding="10 10")
        config_frame.pack(fill=tk.X, pady=10) 

        ttk.Label(config_frame, text="Dirección de Cartera (NiceHash BTC):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.wallet_entry = ttk.Entry(config_frame, width=60, font=("Arial", 11))
        self.wallet_entry.insert(0, NICEHASH_WALLET) # Initialize with the placeholder
        self.wallet_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(config_frame, text="Nombre del Worker:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.worker_entry = ttk.Entry(config_frame, width=30, font=("Arial", 11))
        self.worker_entry.insert(0, WORKER_NAME)
        self.worker_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        config_frame.grid_columnconfigure(1, weight=1) # Expandable input column

        # --- Control Buttons ---
        button_frame = ttk.Frame(main_frame, padding="5 0")
        button_frame.pack(fill=tk.X, pady=5)

        self.start_button = ttk.Button(button_frame, text="▶️ Iniciar Minado", command=self.start_mining, style="Green.TButton")
        self.start_button.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        # The stop button now calls stop_miner_button_action
        self.stop_button = ttk.Button(button_frame, text="⏹️ Detener Minado", command=self.stop_miner_button_action, state=tk.DISABLED, style="Red.TButton")
        self.stop_button.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        self.view_stats_button = ttk.Button(button_frame, text="🌐 Ver Estadísticas Online", command=self.update_workers, style="Blue.TButton")
        self.view_stats_button.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        self.view_stats_button.config(state=tk.NORMAL) # Ensure it's enabled

        # --- Miner Status Section (Hashrate removed) ---
        status_frame = ttk.LabelFrame(main_frame, text="Estado del Minero", padding="10 10")
        status_frame.pack(fill=tk.X, pady=10)

        self.status_label = ttk.Label(status_frame, text="Estado: Detenido", font=("Arial", 13, "bold"), foreground="red")
        self.status_label.pack(pady=2, anchor="w")

        # Hashrate removed from the GUI
        # self.hashrate_label = ttk.Label(status_frame, text="Hashrate: 0 H/s", font=("Arial", 13, "bold"), foreground="blue")
        # self.hashrate_label.pack(pady=2, anchor="w")

        # --- Log Console ---
        log_frame = ttk.LabelFrame(main_frame, text="Log de XMRig", padding="10 10")
        log_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        self.log_text = tk.Text(log_frame, height=15, font=("Courier New", 10), state='disabled', wrap=tk.WORD, bg="#f0f0f0", relief=tk.FLAT)
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        log_scrollbar = ttk.Scrollbar(log_frame, command=self.log_text.yview)
        log_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text.config(yscrollcommand=log_scrollbar.set)

        # --- Help and Troubleshooting Section ---
        troubleshooting_frame = ttk.LabelFrame(main_frame, text="Ayuda y Solución de Problemas", padding="10 10")
        troubleshooting_frame.pack(fill=tk.BOTH, expand=True, pady=10) 

        # Text widget for help - NO FIXED HEIGHT, just expand
        self.troubleshooting_text = tk.Text(troubleshooting_frame, font=("Arial", 10), state='disabled', wrap=tk.WORD, bg="#fffbe6", fg="#8a6d3b", relief=tk.FLAT)
        self.troubleshooting_text.pack(fill=tk.BOTH, expand=True) 

        # Concise initial help message, guiding the user to paste their address
        self.show_troubleshooting_message(
            "Pega tu dirección de minado (NHbR...) en el campo de arriba y haz clic en 'Iniciar Minado'.", "info")

    def _log_message(self, message):
        """Helper function to safely insert messages into the log text widget."""
        self.log_text.config(state='normal')
        self.log_text.insert(tk.END, message)
        self.log_text.config(state='disabled')
        self.log_text.see(tk.END)

    def _read_xmrig_output_threaded(self):
        """Function to read XMRig output in a separate thread."""
        if self.process and self.process.stdout:
            try:
                for line in iter(self.process.stdout.readline, ''):
                    self.log_queue.put(line)
            except ValueError:
                pass 
            except Exception as e:
                self.log_queue.put(f"Error inesperado en hilo de lectura XMRig: {e}\n")
        self.log_queue.put("---XMRIG_TERMINATED---")

    def _check_log_queue(self):
        """Checks the log queue and updates the GUI."""
        while not self.log_queue.empty():
            line = self.log_queue.get_nowait()
            self._process_log_line(line)
        self.root.after(100, self._check_log_queue)

    def _process_log_line(self, line):
        """Processes a line from the XMRig log to update the GUI and detect errors."""
        self._log_message(line)

        # Hashrate is no longer updated in the GUI. Debug lines can be removed.
        # if "miner speed" in line:
        #     print(f"DEBUG: Hashrate line detected: {line.strip()}")
        #     try:
        #         match = re.search(r"miner speed.*?([\d.]+)", line)
        #         if match:
        #             current_speed_str = match.group(1)
        #             print(f"DEBUG: Value captured by regex: '{current_speed_str}'")
        #             current_speed = float(current_speed_str)
        #             self.hashrate_label.config(text=f"Hashrate: {current_speed:.2f} H/s", foreground="blue")
        #         else:
        #             self.hashrate_label.config(text="Hashrate: N/A", foreground="gray")
        #             print("DEBUG: Regex found no match for hashrate.")
        #     except ValueError as ve:
        #         print(f"DEBUG: Float conversion error for '{current_speed_str}': {ve}")
        #         self.hashrate_label.config(text="Hashrate: Error (Float)", foreground="red")
        #     except Exception as e:
        #         print(f"DEBUG: Unexpected error parsing hashrate: {e}")
        #         self.hashrate_label.config(text="Hashrate: Error", foreground="red")
        #         pass

        # Detect accepted shares
        if "accepted (" in line:
            self.status_label.config(text="Estado: Minando y Enviando Shares ✅", foreground="green")
            self.show_troubleshooting_message("¡Minando! Tu equipo está enviando shares aceptados a NiceHash.", "info")
        elif "randomx dataset ready" in line:
            self.status_label.config(text="Estado: Minero Listo (Minando)...", foreground="orange")
            self.show_troubleshooting_message(
                "Minero listo. La inicialización de RandomX puede tardar en CPUs antiguas.", "info")


        # Detect specific NiceHash connection errors
        if "read error" in line or "connection refused" in line or "disconnected" in line or "Invalid mining address" in line:
            self.status_label.config(text="Estado: Error de Conexión ❌", foreground="red")
            error_message = f"Error: '{line.strip()}'\n"
            
            if "Invalid mining address" in line:
                error_message += "¡Dirección de minería rechazada! Asegúrate de usar la dirección NHbR... de NiceHash."
            elif "end of file" in line: # This is the recurring error with NiceHash
                error_message += "NiceHash cerró la conexión. XMRig intentará reconectar. Para más estabilidad, prueba el NiceHash Miner oficial."
            else: # Other generic connection errors
                error_message += "Problema de conexión. Verifica tu internet o intenta con una VPN."
            
            self.show_troubleshooting_message(error_message, "error")
        
        # XMRig terminated
        if line == "---XMRIG_TERMINATED---":
            self.status_label.config(text="Estado: Detenido", foreground="red")
            # self.hashrate_label.config(text="Hashrate: 0 H/s", foreground="blue") # Hashrate removed
            self.show_troubleshooting_message("El minero XMRig se ha detenido.", "warning")


    def show_troubleshooting_message(self, message, type="info"):
        """Displays help and troubleshooting messages in the designated area."""
        self.troubleshooting_text.config(state='normal')
        self.troubleshooting_text.delete(1.0, tk.END)
        self.troubleshooting_text.insert(tk.END, message)
        
        if type == "error":
            self.troubleshooting_text.config(bg="#f2dede", fg="#a94442")
        elif type == "warning":
            self.troubleshooting_text.config(bg="#fcf8e3", fg="#8a6d3b")
        else: # info
            self.troubleshooting_text.config(bg="#d9edf7", fg="#31708f")

        self.troubleshooting_text.config(state='disabled')


    def start_mining(self):
        """Starts the XMRig mining process."""
        # If an XMRig process is already running, do not start another
        if self.process and self.process.poll() is None:
            messagebox.showwarning("Miner already running", "El minero XMRig ya está en ejecución. Detenlo antes de iniciar uno nuevo.")
            self._log_message("Advertencia: Intento de iniciar XMRig mientras ya estaba en ejecución.\n")
            return

        wallet = self.wallet_entry.get().strip()
        worker = self.worker_entry.get().strip()

        # Fixed configuration for NiceHash
        pool_url = POOL_URL
        coin = "monero" # XMRig mines RandomX, NiceHash interprets it
        use_tls = True

        if not wallet or wallet == "PEGA_AQUI_TU_DIRECCION_DE_MINADO_NHBR": # Check against the new placeholder
            messagebox.showerror("Error", "Por favor, ingresa tu dirección de minado de NiceHash (NHbR...).")
            return

        if not os.path.exists(XMRIG_PATH):
            messagebox.showerror("Error", f"XMRig no encontrado en la ruta: {XMRIG_PATH}\nPor favor, verifica la ruta y asegúrate de que xmrig.exe esté allí.")
            self._log_message(f"Error: XMRig.exe no encontrado en {XMRIG_PATH}\n")
            return

        command = [
            XMRIG_PATH,
            "-o", pool_url,
            "-u", f"{wallet}.{worker}",
            "-p", "x", # Password, 'x' is common for NiceHash
            "--coin", coin,
            "--algo=rx/0" # Added to be explicit with the algorithm!
        ]
        if use_tls:
            command.append("--tls")

        self._log_message(f"Intentando iniciar XMRig con comando: {' '.join(command)}\n")
        self.status_label.config(text="Estado: Iniciando Minero (Preparando RandomX)...", foreground="orange") # Clearer message
        self.show_troubleshooting_message(
            "Iniciando XMRig. La inicialización de RandomX puede tardar en CPUs antiguas.", "info")

        try:
            # CREATE_NO_WINDOW so it doesn't open a separate console window
            self.process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
            time.sleep(1) # Small pause for the process to start

            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            
            self.log_thread = threading.Thread(target=self._read_xmrig_output_threaded)
            self.log_thread.daemon = True
            self.log_thread.start()

        except FileNotFoundError:
            messagebox.showerror("Path Error", f"El archivo XMRig.exe no fue encontrado en: {XMRIG_PATH}\nPor favor, verifica la ruta.")
            self._log_message(f"Error: XMRig.exe no encontrado en {XMRIG_PATH}\n")
            self._stop_miner_and_update_gui() # Call internal function to clean up state
            self.status_label.config(text="Estado: Detenido (Error de Ruta)", foreground="red")
            self.show_troubleshooting_message(
                f"Error: XMRig.exe no fue encontrado. Verifica la ruta en el código.", "error")
        except Exception as e:
            messagebox.showerror("Error starting XMRig", f"Ocurrió un error inesperado al intentar iniciar XMRig: {e}")
            self._log_message(f"Error inesperado al iniciar XMRig: {e}\n")
            self._stop_miner_and_update_gui() # Call internal function to clean up state
            self.status_label.config(text="Estado: Detenido (Error)", foreground="red")
            self.show_troubleshooting_message(f"Error al iniciar XMRig: {e}", "error")

    def _stop_miner_and_update_gui(self):
        """Internal function to stop the miner process and update GUI state."""
        if self.process:
            self._log_message("Enviando señal de terminación a XMRig...\n")
            try:
                self.process.terminate() # Attempt graceful termination
                time.sleep(0.05) # Small pause for the process to respond
                if self.process.poll() is None: # If the process is still running
                    self.process.kill() # Force termination
                    self._log_message("XMRig forzado a detenerse.\n")
                else:
                    self._log_message("XMRig detenido limpiamente.\n")
            except Exception as e:
                self._log_message(f"Error inesperado al detener XMRig: {e}\n")
            finally:
                self.process = None # Ensure self.process is set to None after attempting to stop
                # Attempt to join the log thread to ensure it finishes
                if self.log_thread and self.log_thread.is_alive():
                    self.log_thread.join(timeout=1) # Give it a short time to finish
                    if self.log_thread.is_alive():
                        self._log_message("Advertencia: El hilo de log no terminó limpiamente.\n")

            self._log_message("Minado detenido.\n")
        else:
            self._log_message("No hay un proceso de minería activo para detener.\n")

        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_label.config(text="Estado: Detenido", foreground="red")
        # self.hashrate_label.config(text="Hashrate: 0 H/s", foreground="blue") # Hashrate removed
        self.show_troubleshooting_message("El minero ha sido detenido.", "info")
        
    def stop_miner_button_action(self):
        """Function called by the 'Stop Mining' button."""
        self._stop_miner_and_update_gui()
        # The GUI remains open, no root.quit() or root.destroy() called here.

    def on_closing(self):
        """Function called when the user closes the window with the 'X' button."""
        if messagebox.askokcancel("Salir", "¿Estás seguro de que quieres salir?\nEl minero se detendrá."):
            self._stop_miner_and_update_gui() # Stop the miner
            self.root.destroy() # Close the Tkinter window
            sys.exit(0) # Terminate the Python script cleanly
        else:
            # If the user cancels, do nothing and the window remains open
            pass


    def update_workers(self):
        """
        Function to open the NiceHash dashboard in the browser.
        """
        dashboard_url = "https://www.nicehash.com/my/mining/rigs"
        webbrowser.open(dashboard_url)
        self.show_troubleshooting_message(
            "Abriendo el panel de control de NiceHash en tu navegador. Las estadísticas se verán allí.", "info")


if __name__ == "__main__":
    root = tk.Tk()
    app = MinerApp(root)
    root.mainloop()