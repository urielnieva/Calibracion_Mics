# 📱 Calibraciones de Micrófonos de Celulares

Este repositorio contiene curvas de respuesta y calibración de micrófonos integrados de teléfonos móviles en formato `.cal`. Está diseñado para que aplicaciones de análisis de audio puedan importar estas correcciones de forma directa y dinámica a través de solicitudes HTTP públicas de solo lectura.

---

## 🎯 ¿Cómo funciona?

### 1. Lectura Directa (Raw URLs)
La aplicación puede descargar y aplicar la calibración en tiempo real haciendo una petición HTTP GET a la URL cruda (Raw) del archivo en GitHub. 

**Ejemplo de URL Raw:**
```text
https://raw.githubusercontent.com/<TuUsuario>/<TuRepo>/main/motorola_e22.cal
```

### 2. Ventajas del Formato `.cal`
* **Estándar de la Industria:** Es el formato de texto plano utilizado por herramientas profesionales de acústica como **REW (Room EQ Wizard)**, **MiniDSP**, y **Dayton Audio**.
* **Fácil de Parsear:** Consiste en líneas sencillas con dos columnas separadas por espacios o tabulaciones: `[Frecuencia en Hz] [Ganancia/Corrección en dB]`.
* **Actualización en Caliente (Sin Re-compilar):** Si se añade un nuevo modelo de teléfono o se refina una calibración existente, basta con subir el archivo a GitHub. La aplicación lo consumirá de inmediato en su próxima ejecución o sincronización.

---

## 📄 Formato del Archivo `.cal`

Las líneas que comienzan con `#` se consideran comentarios y deben ser ignoradas por el analizador de la aplicación.
Las líneas de datos tienen la siguiente estructura:

```text
# Calibracion Micrófono Motorola Moto E22
20.0    -3.2
63.0    -1.5
125.0    0.8
1000.0   0.0
8000.0   1.4
20000.0 -3.1
```

* **Columna 1:** Frecuencia en Hertz (Hz) — Ejemplo: `1000.0`
* **Columna 2:** Desviación en decibelios (dB) — Ejemplo: `0.0`. *Un valor negativo significa que el micrófono atenúa esa frecuencia y la app debe sumarle esa cantidad para compensar; un valor positivo significa que el micrófono la acentúa y la app debe restarla.*

---

## 📂 Archivos Disponibles

Actualmente se encuentran disponibles los siguientes archivos de calibración:

| Archivo | Dispositivo | Estado |
| :--- | :--- | :--- |
| [motorola_e22.cal](./motorola_e22.cal) | Motorola Moto E22 | Activo / Calibrado |
| [samsung_s23.cal](./samsung_s23.cal) | Samsung Galaxy S23 | Activo / Estimado |
| [iphone_13.cal](./iphone_13.cal) | Apple iPhone 13 | Activo / Estimado |

---

## 🚀 Cómo Usar en tu Aplicación (Ejemplo Conceptual en JS)

```javascript
async function cargarCalibracion(dispositivo) {
  const url = `https://raw.githubusercontent.com/<TuUsuario>/<TuRepo>/main/${dispositivo}.cal`;
  try {
    const respuesta = await fetch(url);
    if (!respuesta.ok) throw new Error('No se pudo descargar la calibración.');
    
    const texto = await respuesta.text();
    const puntos = [];
    
    texto.split('\n').forEach(linea => {
      linea = linea.trim();
      if (linea === '' || linea.startsWith('#')) return; // Ignorar vacíos y comentarios
      
      const [frecuencia, correccion] = linea.split(/\s+/).map(Number);
      if (!isNaN(frecuencia) && !isNaN(correccion)) {
        puntos.push({ hz: frecuencia, db: correccion });
      }
    });
    
    return puntos;
  } catch (error) {
    console.error('Error cargando calibración:', error);
    return null;
  }
}
```

---

## ➕ Cómo Agregar un Nuevo Dispositivo

1. Mide la respuesta del micrófono o consigue los datos de respuesta en frecuencia.
2. Crea un archivo con el formato `<marca>_<modelo>.cal` (por ejemplo, `xiaomi_redmi_note_12.cal`) utilizando únicamente minúsculas y guiones bajos.
3. Sube el archivo a este repositorio.
4. Obtén el enlace Raw desde GitHub y pruébalo en tu aplicación.
