![Legacy CPU Miner GUI Screenshot]([https://placehold.co/800x500/aabbcc/ffffff?text=Captura+de+Pantalla+de+la+GUI](https://imgur.com/a/poMXjll)

---

## English

### Project Overview
This is a Graphical User Interface (GUI) in Python (using tkinter) designed to simplify the CPU mining process on the NiceHash platform, utilizing the popular XMRig miner. It is especially intended for users with older computers who may face compatibility or connectivity challenges with the official NiceHash software or with traditional mining pools.

### Features
* **Intuitive Interface:** Clean and easy-to-use design for starting and stopping mining.
* **XMRig Integration:** Launches and monitors the XMRig process in the background.
* **Direct NiceHash Connection:** Default configuration for NiceHash's RandomX pool (payments in Bitcoin).
* **Real-time Status:** Displays mining status, including accepted shares and common errors.
* **Smart Help Messages:** Provides clear feedback on connection status, common errors (like NiceHash disconnections), and recommendations.
* **Quick Stats Access:** Direct button to view your mining statistics on the NiceHash.com dashboard.
* **Robust Miner Management:** Attempts to safely stop the XMRig process.

### Why This GUI?
Many users with older CPUs (like the AMD Turion II P560) may encounter mining difficulties due to:

* **Lack of support for modern instructions (e.g., AES-NI, AVX):** Newer mining software, including NiceHash Miner, sometimes requires these instructions, which can prevent it from running or drastically reduce performance on older hardware.
* **ISP port blocking:** Some Internet Service Providers (ISPs) block common mining ports, making it difficult to connect to pools. NiceHash, by using port 443 (HTTPS), often bypasses these restrictions.
* **Instability with third-party miners:** NiceHash may close connections from miners that are not their official software, resulting in frequent disconnections.

This GUI aims to be a practical solution, allowing direct mining with XMRig (which is more flexible with older hardware) and providing guidance when specific NiceHash issues arise.

### Requirements
To run this GUI and the XMRig miner, you will need:

* **Python 3.x:** Download and install it from [python.org](https://www.python.org/). Make sure to check the "Add Python to PATH" option during installation.
* **XMRig:** Download the latest Windows version of XMRig from [github.com/xmrig/xmrig/releases](https://github.com/xmrig/xmrig/releases).
    * **Important:** Unzip the XMRig ZIP file to a subfolder named `xmrig` within the same directory as `miner_gui.py`.

* **A NiceHash account:** Register and complete KYC verification on [nicehash.com](https://www.nicehash.com/). You will need your NiceHash **Mining Address** (which typically starts with `NHbR...`), found in your mining dashboard.

### Installation and Usage
1.  **Download the GUI:**
    * Save this code in a file named `miner_gui.py` on your computer.
2.  **Configure Paths and Wallet:**
    * Open the `miner_gui.py` file with a text editor (e.g., Notepad, VS Code).
    * Find the line `XMRIG_PATH = r"C:\Users\Marcelo\Desktop\NiceHash\xmrig\xmrig.exe"` and ensure the path correctly points to where you unzipped `xmrig.exe`.
    * Find the line `NICEHASH_WALLET = "PEGA_AQUI_TU_DIRECCION_DE_MINADO_NHBR"` and **replace `"PEGA_AQUI_TU_DIRECCION_DE_MINADO_NHBR"` with your actual NiceHash Mining Address (the one that starts with `NHbR...`).**
    * You can change `WORKER_NAME` if desired.
    * Save the file.
3.  **Run the GUI:**
    * Open a Command Prompt (CMD) or Git Bash.
    * Navigate to the folder where you saved `miner_gui.py` (e.g., `cd C:\Users\YourUser\Desktop\NiceHash`).
    * Execute the command: `python miner_gui.py`
4.  **Start Mining:**
    * In the GUI, click the "▶️ Iniciar Minado" button.
    * Observe the "Log de XMRig" and "Estado del Minero". The miner will take a few seconds to initialize the RandomX algorithm (this is normal on older CPUs).
    * If the connection is successful, you will see "Minando y Enviando Shares ✅".

### Common Troubleshooting & Notes
* **"XMRig not found at path"**: Verify that `XMRIG_PATH` in the code is exactly the path where `xmrig.exe` is located.
* **No Hashrate Display in GUI**: The real-time hashrate display in the GUI has been removed due to the intermittent nature of direct connections with NiceHash and the difficulty in reliably parsing it. You can check your actual hashrate and earnings on your NiceHash online dashboard.
* **"Estado: Error de Conexión ❌" / "read error: 'end of file'"**: This is a common and expected behavior when mining directly to NiceHash with XMRig. NiceHash often closes connections from miners that are not their official software. XMRig is designed to automatically reconnect, so your mining will continue and shares will be submitted.
    * **Recommendation:** If direct connection is unstable, consider using the official NiceHash Miner. You can download it from the "Descargar NiceHash Miner" button in the GUI's Help section or directly from [nicehash.com/cpu-gpu-mining](https://www.nicehash.com/cpu-gpu-mining).
    * **CPU Compatibility:** Be aware that the official NiceHash Miner may have stricter hardware requirements (e.g., AVX instructions) that your older CPU might not meet. If the official software also doesn't work, this GUI with direct XMRig is still an option to try, despite the interruptions.
* **Profitability**: CPU mining, especially on older hardware, yields very low profits. Manage your expectations.

### Contributions
Contributions are welcome! If you have ideas to improve the GUI, troubleshoot issues, or add functionalities, feel free to open an "issue" or submit a "pull request" on the GitHub repository.

### License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Español

### Resumen del Proyecto
Esta es una Interfaz Gráfica de Usuario (GUI) en Python (usando tkinter) diseñada para simplificar el proceso de minería de CPU en la plataforma NiceHash, utilizando el popular minero XMRig. Está especialmente pensada para usuarios con equipos más antiguos que pueden enfrentar desafíos de compatibilidad o conectividad con el software oficial de NiceHash o con pools de minería tradicionales.

### Características
* **Interfaz Intuitiva:** Diseño limpio y fácil de usar para iniciar y detener la minería.
* **Integración con XMRig:** Lanza y monitorea el proceso de XMRig en segundo plano.
* **Conexión Directa a NiceHash:** Configuración predeterminada para el pool RandomX de NiceHash (pagos en Bitcoin).
* **Monitoreo de Estado:** Muestra el estado de la minería, incluyendo shares aceptados y errores comunes.
* **Mensajes de Ayuda Inteligentes:** Proporciona retroalimentación clara sobre el estado de la conexión, errores comunes (como desconexiones de NiceHash) y recomendaciones.
* **Acceso Rápido a Estadísticas:** Botón directo para ver tus estadísticas de minería en el panel de control de NiceHash.com.
* **Gestión Robusta del Minero:** Intenta detener el proceso de XMRig de forma segura.

### ¿Por qué esta GUI?
Muchos usuarios con CPUs antiguas (como el AMD Turion II P560) pueden tener dificultades para minar debido a:

* **Falta de soporte para instrucciones modernas (ej. AES-NI, AVX):** El software de minería más reciente, incluido NiceHash Miner, a veces requiere estas instrucciones, lo que puede impedir su funcionamiento o reducir drásticamente el rendimiento en hardware antiguo.
* **Bloqueos de puertos por ISP:** Algunos Proveedores de Servicios de Internet (ISP) bloquean puertos de minería comunes, dificultando la conexión a pools. NiceHash, al usar el puerto 443 (HTTPS), a menudo sortea estas restricciones.
* **Inestabilidad con mineros de terceros:** NiceHash puede cerrar conexiones de mineros que no son su software oficial, resultando en desconexiones frecuentes.

Esta GUI busca ser una solución práctica, permitiendo la minería directa con XMRig (que es más flexible con hardware antiguo) y proporcionando guía cuando surgen los problemas específicos de NiceHash.

### Requisitos
Para ejecutar esta GUI y el minero XMRig, necesitarás:

* **Python 3.x:** Descárgalo e instálalo desde [python.org](https://www.python.org/). Asegúrate de marcar la opción "Add Python to PATH" durante la instalación.
* **XMRig:** Descarga la última versión de XMRig para Windows desde [github.com/xmrig/xmrig/releases](https://github.com/xmrig/xmrig/releases).
    * **Importante:** Descomprime el archivo ZIP de XMRig en una subcarpeta llamada `xmrig` dentro del mismo directorio que `miner_gui.py`.

* **Una cuenta de NiceHash:** Regístrate y completa la verificación KYC en [nicehash.com](https://www.nicehash.com/). Necesitarás tu **Dirección de Minado** de NiceHash (que normalmente comienza con `NHbR...`), que se encuentra en tu panel de minería.

### Instalación y Uso
1.  **Descarga la GUI:**
    * Guarda este código en un archivo llamado `miner_gui.py` en tu computadora.
2.  **Configura Rutas y Billetera:**
    * Abre el archivo `miner_gui.py` con un editor de texto (ej. Bloc de Notas, VS Code).
    * Busca la línea `XMRIG_PATH = r"C:\Users\Marcelo\Desktop\NiceHash\xmrig\xmrig.exe"` y asegúrate de que la ruta apunte correctamente a donde descomprimiste `xmrig.exe`.
    * Busca la línea `NICEHASH_WALLET = "PEGA_AQUI_TU_DIRECCION_DE_MINADO_NHBR"` y **reemplaza `"PEGA_AQUI_TU_DIRECCION_DE_MINADO_NHBR"` con tu Dirección de Minado real de NiceHash (la que comienza con `NHbR...`).**
    * Puedes cambiar `WORKER_NAME` si lo deseas.
    * Guarda el archivo.
3.  **Ejecuta la GUI:**
    * Abre el Símbolo del Sistema (CMD) o Git Bash.
    * Navega a la carpeta donde guardaste `miner_gui.py` (ej. `cd C:\Users\TuUsuario\Desktop\NiceHash`).
    * Ejecuta el comando: `python miner_gui.py`
4.  **Inicia la Minería:**
    * En la GUI, haz clic en el botón "▶️ Iniciar Minado".
    * Observa el "Log de XMRig" y el "Estado del Minero". El minero tardará unos segundos en inicializar el algoritmo RandomX (esto es normal en CPUs antiguas).
    * Si la conexión es exitosa, verás "Minando y Enviando Shares ✅".

### Solución de Problemas Comunes y Notas
* **"XMRig no encontrado en la ruta"**: Verifica que `XMRIG_PATH` en el código sea exactamente la ruta donde se encuentra `xmrig.exe`.
* **No hay Hashrate en la GUI**: La visualización del hashrate en tiempo real en la GUI ha sido eliminada debido a la naturaleza intermitente de las conexiones directas con NiceHash y la dificultad para analizarlo de forma fiable. Puedes verificar tu hashrate real y tus ganancias en tu panel de control en línea de NiceHash.
* **"Estado: Error de Conexión ❌" / "read error: 'end of file'"**: Este es un comportamiento común y esperado al minar directamente a NiceHash con XMRig. NiceHash a menudo cierra las conexiones de mineros que no son su software oficial. XMRig está diseñado para reconectarse automáticamente, por lo que tu minería continuará y se enviarán los shares.
    * **Recomendación:** Si la conexión directa es inestable, considera usar el NiceHash Miner oficial. Puedes descargarlo desde el botón "Descargar NiceHash Miner" en la sección de Ayuda de la GUI o directamente desde [nicehash.com/cpu-gpu-mining](https://www.nicehash.com/cpu-gpu-mining).
    * **Compatibilidad de CPU:** Ten en cuenta que el NiceHash Miner oficial puede tener requisitos de hardware más estrictos (ej. instrucciones AVX) que tu CPU antigua podría no cumplir. Si el software oficial tampoco funciona, esta GUI con XMRig directo sigue siendo una opción para intentar, a pesar de las interrupciones.
* **Rentabilidad**: La minería de CPU, especialmente en hardware antiguo, genera ganancias muy bajas. Gestiona tus expectativas.

### Contribuciones
¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar la GUI, solucionar problemas o añadir funcionalidades, no dudes en abrir un "issue" o enviar un "pull request" en el repositorio de GitHub.

### Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

