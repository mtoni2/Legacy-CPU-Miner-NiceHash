Legacy-CPU-Miner-NiceHash (Minero CPU para NiceHash - GUI Optimizada)

Esta es una Interfaz Gráfica de Usuario (GUI) en Python (usando tkinter) diseñada para simplificar el proceso de minería de CPU en la plataforma NiceHash, utilizando el popular minero XMRig. Está especialmente pensada para usuarios con equipos más antiguos que pueden enfrentar desafíos de compatibilidad o conectividad con el software oficial de NiceHash o con pools de minería tradicionales.

Características

Interfaz Intuitiva: Diseño limpio y fácil de usar para iniciar y detener la minería.

Integración con XMRig: Lanza y monitorea el proceso de XMRig en segundo plano.

Conexión Directa a NiceHash: Configuración predeterminada para el pool RandomX de NiceHash (pagos en Bitcoin).

Monitoreo en Tiempo Real: Muestra el estado de la minería, incluyendo shares aceptados y hashrate (velocidad de minado).

Mensajes de Ayuda Inteligentes: Proporciona retroalimentación clara sobre el estado de la conexión, errores comunes (como desconexiones de NiceHash) y recomendaciones.

Acceso Rápido a Estadísticas: Botón directo para ver tus estadísticas de minería en el panel de control de NiceHash.com.

Gestión Robusta del Minero: Intenta detener el proceso de XMRig de forma segura.

¿Por qué esta GUI?

Muchos usuarios con CPUs antiguas (como el AMD Turion II P560) pueden tener dificultades para minar debido a:

Falta de soporte para instrucciones modernas (ej. AES-NI, AVX): El software de minería más reciente, incluido NiceHash Miner, a veces requiere estas instrucciones, lo que puede impedir su funcionamiento o reducir drásticamente el rendimiento en hardware antiguo.

Bloqueos de puertos por ISP: Algunos Proveedores de Servicios de Internet (ISP) bloquean puertos de minería comunes, dificultando la conexión a pools. NiceHash, al usar el puerto 443 (HTTPS), a menudo sortea estas restricciones.

Inestabilidad con mineros de terceros: NiceHash puede cerrar conexiones de mineros que no son su software oficial, resultando en desconexiones frecuentes.

Esta GUI busca ser una solución práctica, permitiendo la minería directa con XMRig (que es más flexible con hardware antiguo) y proporcionando guía cuando surgen los problemas específicos de NiceHash.

Requisitos

Para ejecutar esta GUI y el minero XMRig, necesitarás:

Python 3.x: Descárgalo e instálalo desde python.org. Asegúrate de marcar la opción "Add Python to PATH" durante la instalación.

XMRig: Descarga la última versión de XMRig para Windows desde github.com/xmrig/xmrig/releases.

Importante: Descomprime el archivo ZIP de XMRig en una ubicación conocida en tu computadora (ej. C:\Users\TuUsuario\Desktop\NiceHash\xmrig\).

Una cuenta de NiceHash: Regístrate y completa la verificación KYC en nicehash.com. Necesitarás tu dirección de depósito de Bitcoin (BTC) de NiceHash (que comienza con 1, 3 o bc1).

Instalación y Uso

Descarga la GUI:

Guarda este código en un archivo llamado miner_gui.py en tu computadora.

Abre el archivo miner_gui.py con un editor de texto (ej. Bloc de Notas, VS Code).

Configura las rutas y la billetera:

Busca la línea XMRIG_PATH = r"C:\Users\Marcelo\Desktop\NiceHash\xmrig\xmrig.exe" y asegúrate de que la ruta apunte correctamente a donde descomprimiste xmrig.exe.

Busca la línea NICEHASH_WALLET = "PEGA_AQUI_TU_DIRECCION_DE_DEPOSITO_BTC_DE_NICEHASH" y reemplaza "PEGA_AQUI_TU_DIRECCION_DE_DEPOSITO_BTC_DE_NICEHASH" con tu dirección REAL de depósito de Bitcoin de NiceHash.

Puedes cambiar WORKER_NAME si lo deseas.

Guarda el archivo.

Ejecuta la GUI:

Abre el Símbolo del Sistema (CMD) o PowerShell.

Navega a la carpeta donde guardaste miner_gui.py (ej. cd C:\Users\TuUsuario\Desktop\).

Ejecuta el comando: python miner_gui.py

Inicia la Minería:

En la GUI, haz clic en el botón "▶️ Iniciar Minado".

Observa el "Log de XMRig" y el "Estado del Minero". El minero tardará unos segundos en inicializar el algoritmo RandomX (esto es normal en CPUs antiguas).

Si la conexión es exitosa, verás "Minando y Enviando Shares ✅" y el hashrate se actualizará.

Monitorea tus Estadísticas:

Haz clic en "🌐 Ver Estadísticas Online" para abrir tu panel de control de NiceHash en el navegador y verificar tus ganancias.

Solución de Problemas Comunes

"XMRig no encontrado en la ruta": Verifica que XMRIG_PATH en el código sea exactamente la ruta donde se encuentra xmrig.exe.

"Hashrate: 0 H/s" en la GUI (pero el log de XMRig muestra velocidad): Esto es un problema conocido que estamos trabajando en resolver. El minero sí está calculando, pero la GUI no lo muestra correctamente. Revisa el log de XMRig directamente para ver la velocidad.

"Estado: Error de Conexión ❌" / "read error: 'end of file'": NiceHash a menudo cierra las conexiones de mineros que no son su software oficial.

Recomendación: Si la conexión directa es inestable, considera usar el NiceHash Miner oficial. Puedes descargarlo desde el botón "Descargar NiceHash Miner" en la sección de Ayuda de la GUI o directamente desde nicehash.com/cpu-gpu-mining.

Compatibilidad de CPU: Ten en cuenta que NiceHash Miner oficial puede tener requisitos de hardware más estrictos (ej. instrucciones AVX) que tu CPU antigua podría no cumplir. Si el software oficial tampoco funciona, esta GUI con XMRig directo sigue siendo una opción para intentar, a pesar de las interrupciones.

Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar la GUI, solucionar problemas o añadir funcionalidades, no dudes en abrir un "issue" o enviar un "pull request" en el repositorio de GitHub (si se crea uno).

Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE.md para más detalles.
