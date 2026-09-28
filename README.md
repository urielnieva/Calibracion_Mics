# 📱 Calibraciones de Micrófonos de Celulares

Curvas de corrección para micrófonos de teléfonos, en formato `.cal` de texto plano, pensadas para
que una app de análisis de audio las descargue por HTTP y las aplique.

**Acá solo hay calibraciones medidas.** Si un modelo no está en la lista, no existe su curva y la
app debe medir en plano y avisar que no hay calibración. Una calibración inventada es peor que
ninguna: hace que la app diga "calibrado" mientras mide con error.

> Hasta septiembre de 2026 este repo tenía 211 archivos generados con números aleatorios por un
> script (`generate_calibrations.py`), marcados en su encabezado como "Gama de hardware simulada".
> No eran mediciones y se eliminaron. Quedan en el historial de git.

---

## Modelos disponibles

| Modelo | Archivo | Estado |
| :--- | :--- | :--- |
| Samsung Galaxy S23 (SM-S911) | [`samsung_galaxy_s23.cal`](./samsung_galaxy_s23.cal) | Medido — v2, 2026-09-28 |

URL directa:

```text
https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_s23.cal
```

---

## Formato

Líneas de dos columnas, `[Frecuencia en Hz] [Corrección en dB]`, separadas por espacios o
tabulaciones. Las líneas que empiezan con `#` son comentarios.

```text
# Frecuencia(Hz)	Corrección(dB)
1000.0  	18.2
8000.0  	-10.4
```

Dos cosas importantes sobre la convención:

* **El valor se SUMA al nivel medido.** Es la corrección a aplicar, no la respuesta del micrófono
  (o sea: el signo ya viene invertido respecto de una curva de respuesta).
* **Incluye el offset de sensibilidad**, es decir el desplazamiento parejo en dB que hace que el
  nivel absoluto en dB SPL coincida con un sonómetro calibrado. Por eso los valores no están
  centrados en 0.

---

## Cada curva vale para un camino de captura

Una calibración medida describe la cadena completa: cápsula, puerto acústico y el procesado que
aplica el sistema operativo. En Android eso depende de la fuente de audio que pide la app:

* `UNPROCESSED` — camino crudo, sin AGC ni supresión de ruido ni la ecualización de fábrica. **Es
  el único válido para medir**, y es el que corresponde a las curvas de este repo.
* `MIC`, `CAMCORDER`, `VOICE_RECOGNITION` — traen la ecualización del fabricante y procesado
  dinámico. La respuesta es otra, cambia con el nivel y con el contenido, y no se puede corregir
  con una curva fija.

En el Galaxy S23, la diferencia entre ambos caminos llega a **más de 30 dB en 10 kHz**. Aplicar una
curva de `UNPROCESSED` sobre una captura procesada deja la medición peor que sin calibrar.

---

## Cómo se mide una curva nueva

1. Poner la app en `UNPROCESSED`, mono, 48 kHz, con los efectos de plataforma desactivados.
2. Reproducir ruido rosa por un sistema cuya respuesta se conozca, medida con un micrófono de
   medición calibrado (por ejemplo con Smaart).
3. Grabar o medir con el celular **en el mismo punto** que el micrófono de referencia. Esto es lo
   que más importa: a distinta posición, la sala cambia la medición decenas de dB en graves.
4. Calcular, por tercios de octava, la diferencia entre lo que mide el celular y lo que mide la
   referencia. La corrección es esa diferencia con el signo invertido.
5. Anotar también el offset de nivel: cuántos dB de diferencia hay entre el SPL que muestra la app
   y el del sonómetro calibrado, con la misma ponderación y la misma integración.
6. No corregir los picos y pozos angostos de la sala. Si las mediciones en dos posiciones no
   coinciden en una zona, esa zona es sala y se deja sin tocar.
7. Guardar como `<marca>_<modelo>.cal` en minúsculas con guiones bajos, con un encabezado que diga
   cómo y cuándo se midió, y con qué camino de captura.
