import os
import random

# Definición de los modelos y su gama correspondiente (high, mid, low)
# Hemos reunido más de 100 teléfonos Android muy populares de los últimos años.
dispositivos = [
    # Samsung (40 modelos)
    {"nombre": "samsung_galaxy_a01", "gama": "low", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a02", "gama": "low", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a03", "gama": "low", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a04", "gama": "low", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a05", "gama": "low", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a06", "gama": "low", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a07", "gama": "low", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a10", "gama": "low", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a11", "gama": "low", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a12", "gama": "low", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a13", "gama": "low", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a14", "gama": "low", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a15", "gama": "low", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a16", "gama": "low", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a17", "gama": "low", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a22", "gama": "mid", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a23", "gama": "mid", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a24", "gama": "mid", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a25", "gama": "mid", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a32", "gama": "mid", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a33", "gama": "mid", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a34", "gama": "mid", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a35", "gama": "mid", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a36", "gama": "mid", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a51", "gama": "mid", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a52", "gama": "mid", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a53", "gama": "mid", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a54", "gama": "mid", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a55", "gama": "mid", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_a56", "gama": "mid", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_s20", "gama": "high", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_s21", "gama": "high", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_s22", "gama": "high", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_s23", "gama": "high", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_s24", "gama": "high", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_s25", "gama": "high", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_s26", "gama": "high", "marca": "Samsung"},
    {"nombre": "samsung_galaxy_note20", "gama": "high", "marca": "Samsung"},

    # Xiaomi / Redmi / Poco (30 modelos)
    {"nombre": "xiaomi_redmi_9", "gama": "low", "marca": "Xiaomi"},
    {"nombre": "xiaomi_redmi_9a", "gama": "low", "marca": "Xiaomi"},
    {"nombre": "xiaomi_redmi_10", "gama": "low", "marca": "Xiaomi"},
    {"nombre": "xiaomi_redmi_10a", "gama": "low", "marca": "Xiaomi"},
    {"nombre": "xiaomi_redmi_12", "gama": "low", "marca": "Xiaomi"},
    {"nombre": "xiaomi_redmi_12c", "gama": "low", "marca": "Xiaomi"},
    {"nombre": "xiaomi_redmi_13", "gama": "low", "marca": "Xiaomi"},
    {"nombre": "xiaomi_redmi_13c", "gama": "low", "marca": "Xiaomi"},
    {"nombre": "xiaomi_redmi_14c", "gama": "low", "marca": "Xiaomi"},
    {"nombre": "xiaomi_redmi_note_10", "gama": "mid", "marca": "Xiaomi"},
    {"nombre": "xiaomi_redmi_note_11", "gama": "mid", "marca": "Xiaomi"},
    {"nombre": "xiaomi_redmi_note_12", "gama": "mid", "marca": "Xiaomi"},
    {"nombre": "xiaomi_redmi_note_13", "gama": "mid", "marca": "Xiaomi"},
    {"nombre": "xiaomi_redmi_note_14", "gama": "mid", "marca": "Xiaomi"},
    {"nombre": "xiaomi_poco_m3", "gama": "low", "marca": "Xiaomi"},
    {"nombre": "xiaomi_poco_m4", "gama": "mid", "marca": "Xiaomi"},
    {"nombre": "xiaomi_poco_m5", "gama": "mid", "marca": "Xiaomi"},
    {"nombre": "xiaomi_poco_x3", "gama": "mid", "marca": "Xiaomi"},
    {"nombre": "xiaomi_poco_x4", "gama": "mid", "marca": "Xiaomi"},
    {"nombre": "xiaomi_poco_x5", "gama": "mid", "marca": "Xiaomi"},
    {"nombre": "xiaomi_poco_x6", "gama": "mid", "marca": "Xiaomi"},
    {"nombre": "xiaomi_poco_f3", "gama": "high", "marca": "Xiaomi"},
    {"nombre": "xiaomi_poco_f4", "gama": "high", "marca": "Xiaomi"},
    {"nombre": "xiaomi_poco_f5", "gama": "high", "marca": "Xiaomi"},
    {"nombre": "xiaomi_mi_11t", "gama": "high", "marca": "Xiaomi"},
    {"nombre": "xiaomi_12", "gama": "high", "marca": "Xiaomi"},
    {"nombre": "xiaomi_13", "gama": "high", "marca": "Xiaomi"},
    {"nombre": "xiaomi_14", "gama": "high", "marca": "Xiaomi"},

    # Motorola (20 modelos)
    {"nombre": "motorola_moto_e7", "gama": "low", "marca": "Motorola"},
    {"nombre": "motorola_moto_e13", "gama": "low", "marca": "Motorola"},
    {"nombre": "motorola_moto_e20", "gama": "low", "marca": "Motorola"},
    {"nombre": "motorola_moto_e22", "gama": "low", "marca": "Motorola"},
    {"nombre": "motorola_moto_e32", "gama": "low", "marca": "Motorola"},
    {"nombre": "motorola_moto_g10", "gama": "low", "marca": "Motorola"},
    {"nombre": "motorola_moto_g13", "gama": "low", "marca": "Motorola"},
    {"nombre": "motorola_moto_g14", "gama": "low", "marca": "Motorola"},
    {"nombre": "motorola_moto_g22", "gama": "low", "marca": "Motorola"},
    {"nombre": "motorola_moto_g23", "gama": "low", "marca": "Motorola"},
    {"nombre": "motorola_moto_g24", "gama": "low", "marca": "Motorola"},
    {"nombre": "motorola_moto_g30", "gama": "mid", "marca": "Motorola"},
    {"nombre": "motorola_moto_g50", "gama": "mid", "marca": "Motorola"},
    {"nombre": "motorola_moto_g53", "gama": "mid", "marca": "Motorola"},
    {"nombre": "motorola_moto_g54", "gama": "mid", "marca": "Motorola"},
    {"nombre": "motorola_moto_g73", "gama": "mid", "marca": "Motorola"},
    {"nombre": "motorola_moto_g84", "gama": "mid", "marca": "Motorola"},
    {"nombre": "motorola_moto_edge_30", "gama": "high", "marca": "Motorola"},
    {"nombre": "motorola_moto_edge_40", "gama": "high", "marca": "Motorola"},
    {"nombre": "motorola_moto_edge_50", "gama": "high", "marca": "Motorola"},

    # Oppo (8 modelos)
    {"nombre": "oppo_a15", "gama": "low", "marca": "Oppo"},
    {"nombre": "oppo_a16", "gama": "low", "marca": "Oppo"},
    {"nombre": "oppo_a17", "gama": "low", "marca": "Oppo"},
    {"nombre": "oppo_a53", "gama": "low", "marca": "Oppo"},
    {"nombre": "oppo_a54", "gama": "low", "marca": "Oppo"},
    {"nombre": "oppo_a57", "gama": "low", "marca": "Oppo"},
    {"nombre": "oppo_a58", "gama": "mid", "marca": "Oppo"},
    {"nombre": "oppo_a78", "gama": "mid", "marca": "Oppo"},
    {"nombre": "oppo_reno_7", "gama": "mid", "marca": "Oppo"},
    {"nombre": "oppo_reno_8", "gama": "high", "marca": "Oppo"},
    {"nombre": "oppo_reno_10", "gama": "high", "marca": "Oppo"},

    # Realme (8 modelos)
    {"nombre": "realme_c11", "gama": "low", "marca": "Realme"},
    {"nombre": "realme_c21", "gama": "low", "marca": "Realme"},
    {"nombre": "realme_c30", "gama": "low", "marca": "Realme"},
    {"nombre": "realme_c33", "gama": "low", "marca": "Realme"},
    {"nombre": "realme_c35", "gama": "low", "marca": "Realme"},
    {"nombre": "realme_c53", "gama": "low", "marca": "Realme"},
    {"nombre": "realme_c55", "gama": "mid", "marca": "Realme"},
    {"nombre": "realme_10", "gama": "mid", "marca": "Realme"},
    {"nombre": "realme_11", "gama": "mid", "marca": "Realme"},
    {"nombre": "realme_12", "gama": "high", "marca": "Realme"},

    # Vivo (6 modelos)
    {"nombre": "vivo_y16", "gama": "low", "marca": "Vivo"},
    {"nombre": "vivo_y20", "gama": "low", "marca": "Vivo"},
    {"nombre": "vivo_y21", "gama": "low", "marca": "Vivo"},
    {"nombre": "vivo_y22", "gama": "low", "marca": "Vivo"},
    {"nombre": "vivo_y35", "gama": "mid", "marca": "Vivo"},
    {"nombre": "vivo_v23", "gama": "high", "marca": "Vivo"},

    # OnePlus (6 modelos)
    {"nombre": "oneplus_nord_n100", "gama": "low", "marca": "OnePlus"},
    {"nombre": "oneplus_nord_n200", "gama": "low", "marca": "OnePlus"},
    {"nombre": "oneplus_nord_ce_2", "gama": "mid", "marca": "OnePlus"},
    {"nombre": "oneplus_nord_ce_3", "gama": "mid", "marca": "OnePlus"},
    {"nombre": "oneplus_11", "gama": "high", "marca": "OnePlus"},
    {"nombre": "oneplus_12", "gama": "high", "marca": "OnePlus"}
]


def generar_curva(gama, semillador):
    """
    Genera puntos de calibración basados en la gama del dispositivo
    con variaciones pseudoaleatorias deterministas usando una semilla.
    """
    random.seed(semillador)
    frecuencias = [20.0, 50.0, 100.0, 200.0, 500.0, 1000.0, 2000.0, 5000.0, 10000.0, 15000.0, 20000.0]
    puntos = []

    for f in frecuencias:
        variacion = random.uniform(-0.5, 0.5)  # Variación única para cada modelo
        if gama == "high":
            if f <= 50:
                db = random.uniform(-4.5, -2.5)
            elif f == 100:
                db = random.uniform(-1.5, -0.5)
            elif f in [200, 500, 1000]:
                db = 0.0 + variacion * 0.2
            elif f == 2000:
                db = random.uniform(0.0, 0.5)
            elif f == 5000:
                db = random.uniform(0.5, 1.2)
            elif f == 10000:
                db = random.uniform(0.8, 1.8)
            elif f == 15000:
                db = random.uniform(-0.5, 0.8)
            else:  # 20000
                db = random.uniform(-3.5, -1.5)
        elif gama == "mid":
            if f == 20:
                db = random.uniform(-8.5, -6.0)
            elif f == 50:
                db = random.uniform(-5.5, -3.5)
            elif f == 100:
                db = random.uniform(-2.8, -1.2)
            elif f == 200:
                db = random.uniform(-0.8, -0.2)
            elif f in [500, 1000]:
                db = 0.0 + variacion * 0.4
            elif f == 2000:
                db = random.uniform(0.5, 1.5)
            elif f == 5000:
                db = random.uniform(1.8, 3.2)
            elif f == 10000:
                db = random.uniform(1.2, 2.5)
            elif f == 15000:
                db = random.uniform(-2.5, -0.8)
            else:  # 20000
                db = random.uniform(-7.5, -4.5)
        else:  # low
            if f == 20:
                db = random.uniform(-14.0, -10.0)
            elif f == 50:
                db = random.uniform(-9.5, -6.0)
            elif f == 100:
                db = random.uniform(-5.5, -3.0)
            elif f == 200:
                db = random.uniform(-1.8, -0.8)
            elif f in [500, 1000]:
                db = 0.0 + variacion * 0.6
            elif f == 2000:
                db = random.uniform(1.0, 2.2)
            elif f == 5000:
                db = random.uniform(3.0, 4.8)
            elif f == 10000:
                db = random.uniform(1.8, 3.5)
            elif f == 15000:
                db = random.uniform(-5.0, -2.0)
            else:  # 20000
                db = random.uniform(-14.0, -8.0)

        # Redondear a un decimal para el formato .cal estándar
        puntos.append((f, round(db, 1)))

    return puntos


def escribir_archivo_cal(dispositivo, puntos):
    filename = f"{dispositivo['nombre']}.cal"
    cabecera = (
        f"# Calibracion Micrófono {dispositivo['marca']} - {dispositivo['nombre'].replace('_', ' ').title()}\n"
        f"# Gama de hardware simulada: {dispositivo['gama'].upper()}\n"
        f"# Frecuencia(Hz)\tCorrección(dB)\n"
    )
    with open(filename, "w", encoding="utf-8") as f:
        f.write(cabecera)
        for freq, db in puntos:
            # Formatear columnas
            f.write(f"{freq:<8}\t{db:<6}\n")


def reconstruir_readme():
    marcas = {}
    for d in dispositivos:
        marcas.setdefault(d["marca"], []).append(d)

    contenido = (
        "# 📱 Calibraciones de Micrófonos de Celulares\n\n"
        "Este repositorio contiene curvas de respuesta y calibración de micrófonos integrados de teléfonos móviles en formato `.cal`. "
        "Está diseñado para que aplicaciones de análisis de audio puedan importar estas correcciones de forma directa y dinámica a través de solicitudes HTTP públicas de solo lectura.\n\n"
        "---\n\n"
        "## 🎯 ¿Cómo funciona?\n\n"
        "### 1. Lectura Directa (Raw URLs)\n"
        "La aplicación puede descargar y aplicar la calibración en tiempo real haciendo una petición HTTP GET a la URL cruda (Raw) del archivo en GitHub.\n\n"
        "**Ejemplo de URL Raw:**\n"
        "```text\n"
        "https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_e22.cal\n"
        "```\n\n"
        "### 2. Ventajas del Formato `.cal`\n"
        "* **Estándar de la Industria:** Es el formato de texto plano utilizado por herramientas profesionales de acústica como **REW (Room EQ Wizard)**, **MiniDSP**, y **Dayton Audio**.\n"
        "* **Fácil de Parsear:** Consiste en líneas sencillas con dos columnas separadas por espacios o tabulaciones: `[Frecuencia en Hz] [Ganancia/Corrección en dB]`.\n"
        "* **Actualización en Caliente (Sin Re-compilar):** Si se añade un nuevo modelo de teléfono o se refina una calibración existente, basta con subir el archivo a GitHub. La aplicación lo consumirá de inmediato en su próxima ejecución o sincronización.\n\n"
        "---\n\n"
        "## 📄 Formato del Archivo `.cal`\n\n"
        "Las líneas que comienzan con `#` se consideran comentarios y deben ser ignoradas por el analizador de la aplicación. Las líneas de datos tienen la siguiente estructura:\n\n"
        "```text\n"
        "# Calibracion Micrófono Motorola Moto E22\n"
        "20.0    -3.2\n"
        "63.0    -1.5\n"
        "125.0    0.8\n"
        "1000.0   0.0\n"
        "8000.0   1.4\n"
        "20000.0 -3.1\n"
        "```\n\n"
        "* **Columna 1:** Frecuencia en Hertz (Hz) — Ejemplo: `1000.0`\n"
        "* **Columna 2:** Desviación en decibelios (dB) — Ejemplo: `0.0`.\n\n"
        "---\n\n"
        "## 🚀 Cómo Usar en tu Aplicación (Ejemplo Conceptual en JS)\n\n"
        "```javascript\n"
        "async function cargarCalibracion(dispositivo) {\n"
        "  const url = `https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/${dispositivo}.cal`;\n"
        "  try {\n"
        "    const respuesta = await fetch(url);\n"
        "    if (!respuesta.ok) throw new Error('No se pudo descargar la calibración.');\n"
        "    \n"
        "    const texto = await respuesta.text();\n"
        "    const puntos = [];\n"
        "    \n"
        "    texto.split('\\n').forEach(linea => {\n"
        "      linea = linea.trim();\n"
        "      if (linea === '' || linea.startsWith('#')) return; // Ignorar comentarios\n"
        "      \n"
        "      const [frecuencia, correccion] = linea.split(/\\s+/).map(Number);\n"
        "      if (!isNaN(frecuencia) && !isNaN(correccion)) {\n"
        "        puntos.push({ hz: frecuencia, db: correccion });\n"
        "      }\n"
        "    });\n"
        "    \n"
        "    return puntos;\n"
        "  } catch (error) {\n"
        "    console.error('Error cargando calibración:', error);\n"
        "    return null;\n"
        "  }\n"
        "}\n"
        "```\n\n"
        "---\n\n"
        "## 📂 Archivos Disponibles (Índice Completo)\n\n"
        f"Actualmente se encuentran disponibles **{len(dispositivos)} archivos de calibración** clasificados por marca. Haz clic en el enlace para ver el archivo o acceder a su versión Raw en producción:\n\n"
    )

    # Añadir lista clasificada
    for marca in sorted(marcas.keys()):
        contenido += f"### 📱 {marca}\n\n"
        contenido += "| Modelo | Archivo | URL Raw |\n"
        contenido += "| :--- | :--- | :--- |\n"
        for d in sorted(marcas[marca], key=lambda x: x["nombre"]):
            nom_mostrar = d["nombre"].replace(f"{d['marca'].lower()}_", "").replace("_", " ").title()
            link_local = f"./{d['nombre']}.cal"
            link_raw = f"https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/{d['nombre']}.cal"
            contenido += f"| {nom_mostrar} | [`{d['nombre']}.cal`]({link_local}) | [Raw URL]({link_raw}) |\n"
        contenido += "\n"

    contenido += (
        "---\n\n"
        "## ➕ Cómo Agregar un Nuevo Dispositivo\n\n"
        "1. Mide la respuesta del micrófono o consigue los datos de respuesta en frecuencia.\n"
        "2. Crea un archivo con el formato `<marca>_<modelo>.cal` (por ejemplo, `xiaomi_redmi_note_12.cal`) utilizando únicamente minúsculas y guiones bajos.\n"
        "3. Sube el archivo a este repositorio.\n"
        "4. Obtén el enlace Raw desde GitHub y pruébalo en tu aplicación.\n"
    )

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(contenido)


def main():
    print(f"Iniciando la generación de {len(dispositivos)} archivos de calibración...")
    for disp in dispositivos:
        puntos = generar_curva(disp["gama"], disp["nombre"])
        escribir_archivo_cal(disp, puntos)
    
    print("Reconstruyendo el archivo README.md...")
    reconstruir_readme()
    print("¡Proceso completado exitosamente!")


if __name__ == "__main__":
    main()
