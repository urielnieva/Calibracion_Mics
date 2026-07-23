# 📱 Calibraciones de Micrófonos de Celulares

Este repositorio contiene curvas de respuesta y calibración de micrófonos integrados de teléfonos móviles en formato `.cal`. Está diseñado para que aplicaciones de análisis de audio puedan importar estas correcciones de forma directa y dinámica a través de solicitudes HTTP públicas de solo lectura.

---

## 🎯 ¿Cómo funciona?

### 1. Lectura Directa (Raw URLs)
La aplicación puede descargar y aplicar la calibración en tiempo real haciendo una petición HTTP GET a la URL cruda (Raw) del archivo en GitHub.

**Ejemplo de URL Raw:**
```text
https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_e22.cal
```

### 2. Ventajas del Formato `.cal`
* **Estándar de la Industria:** Es el formato de texto plano utilizado por herramientas profesionales de acústica como **REW (Room EQ Wizard)**, **MiniDSP**, y **Dayton Audio**.
* **Fácil de Parsear:** Consiste en líneas sencillas con dos columnas separadas por espacios o tabulaciones: `[Frecuencia en Hz] [Ganancia/Corrección en dB]`.
* **Actualización en Caliente (Sin Re-compilar):** Si se añade un nuevo modelo de teléfono o se refina una calibración existente, basta con subir el archivo a GitHub. La aplicación lo consumirá de inmediato en su próxima ejecución o sincronización.

---

## 📄 Formato del Archivo `.cal`

Las líneas que comienzan con `#` se consideran comentarios y deben ser ignoradas por el analizador de la aplicación. Las líneas de datos tienen la siguiente estructura:

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
* **Columna 2:** Desviación en decibelios (dB) — Ejemplo: `0.0`.

---

## 🚀 Cómo Usar en tu Aplicación (Ejemplo Conceptual en JS)

```javascript
async function cargarCalibracion(dispositivo) {
  const url = `https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/${dispositivo}.cal`;
  try {
    const respuesta = await fetch(url);
    if (!respuesta.ok) throw new Error('No se pudo descargar la calibración.');
    
    const texto = await respuesta.text();
    const puntos = [];
    
    texto.split('\n').forEach(linea => {
      linea = linea.trim();
      if (linea === '' || linea.startsWith('#')) return; // Ignorar comentarios
      
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

## 📂 Archivos Disponibles (Índice Completo)

Actualmente se encuentran disponibles **208 archivos de calibración** clasificados por marca. Haz clic en el enlace para ver el archivo o acceder a su versión Raw en producción:

### 📱 Apple

| Modelo | Archivo | URL Raw |
| :--- | :--- | :--- |
| Iphone 11 | [`apple_iphone_11.cal`](./apple_iphone_11.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/apple_iphone_11.cal) |
| Iphone 11 Pro | [`apple_iphone_11_pro.cal`](./apple_iphone_11_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/apple_iphone_11_pro.cal) |
| Iphone 11 Pro Max | [`apple_iphone_11_pro_max.cal`](./apple_iphone_11_pro_max.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/apple_iphone_11_pro_max.cal) |
| Iphone 12 | [`apple_iphone_12.cal`](./apple_iphone_12.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/apple_iphone_12.cal) |
| Iphone 12 Mini | [`apple_iphone_12_mini.cal`](./apple_iphone_12_mini.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/apple_iphone_12_mini.cal) |
| Iphone 12 Pro | [`apple_iphone_12_pro.cal`](./apple_iphone_12_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/apple_iphone_12_pro.cal) |
| Iphone 12 Pro Max | [`apple_iphone_12_pro_max.cal`](./apple_iphone_12_pro_max.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/apple_iphone_12_pro_max.cal) |
| Iphone 13 | [`apple_iphone_13.cal`](./apple_iphone_13.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/apple_iphone_13.cal) |
| Iphone 13 Mini | [`apple_iphone_13_mini.cal`](./apple_iphone_13_mini.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/apple_iphone_13_mini.cal) |
| Iphone 13 Pro | [`apple_iphone_13_pro.cal`](./apple_iphone_13_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/apple_iphone_13_pro.cal) |
| Iphone 13 Pro Max | [`apple_iphone_13_pro_max.cal`](./apple_iphone_13_pro_max.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/apple_iphone_13_pro_max.cal) |
| Iphone 14 | [`apple_iphone_14.cal`](./apple_iphone_14.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/apple_iphone_14.cal) |
| Iphone 14 Plus | [`apple_iphone_14_plus.cal`](./apple_iphone_14_plus.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/apple_iphone_14_plus.cal) |
| Iphone 14 Pro | [`apple_iphone_14_pro.cal`](./apple_iphone_14_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/apple_iphone_14_pro.cal) |
| Iphone 14 Pro Max | [`apple_iphone_14_pro_max.cal`](./apple_iphone_14_pro_max.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/apple_iphone_14_pro_max.cal) |
| Iphone 15 | [`apple_iphone_15.cal`](./apple_iphone_15.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/apple_iphone_15.cal) |
| Iphone 15 Plus | [`apple_iphone_15_plus.cal`](./apple_iphone_15_plus.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/apple_iphone_15_plus.cal) |
| Iphone 15 Pro | [`apple_iphone_15_pro.cal`](./apple_iphone_15_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/apple_iphone_15_pro.cal) |
| Iphone 15 Pro Max | [`apple_iphone_15_pro_max.cal`](./apple_iphone_15_pro_max.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/apple_iphone_15_pro_max.cal) |
| Iphone 16 | [`apple_iphone_16.cal`](./apple_iphone_16.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/apple_iphone_16.cal) |
| Iphone 16 Plus | [`apple_iphone_16_plus.cal`](./apple_iphone_16_plus.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/apple_iphone_16_plus.cal) |
| Iphone 16 Pro | [`apple_iphone_16_pro.cal`](./apple_iphone_16_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/apple_iphone_16_pro.cal) |
| Iphone 16 Pro Max | [`apple_iphone_16_pro_max.cal`](./apple_iphone_16_pro_max.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/apple_iphone_16_pro_max.cal) |
| Iphone Se 2020 | [`apple_iphone_se_2020.cal`](./apple_iphone_se_2020.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/apple_iphone_se_2020.cal) |
| Iphone Se 2022 | [`apple_iphone_se_2022.cal`](./apple_iphone_se_2022.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/apple_iphone_se_2022.cal) |

### 📱 Motorola

| Modelo | Archivo | URL Raw |
| :--- | :--- | :--- |
| Moto E13 | [`motorola_moto_e13.cal`](./motorola_moto_e13.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_e13.cal) |
| Moto E20 | [`motorola_moto_e20.cal`](./motorola_moto_e20.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_e20.cal) |
| Moto E22 | [`motorola_moto_e22.cal`](./motorola_moto_e22.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_e22.cal) |
| Moto E32 | [`motorola_moto_e32.cal`](./motorola_moto_e32.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_e32.cal) |
| Moto E7 | [`motorola_moto_e7.cal`](./motorola_moto_e7.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_e7.cal) |
| Moto Edge 30 | [`motorola_moto_edge_30.cal`](./motorola_moto_edge_30.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_edge_30.cal) |
| Moto Edge 30 Neo | [`motorola_moto_edge_30_neo.cal`](./motorola_moto_edge_30_neo.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_edge_30_neo.cal) |
| Moto Edge 30 Pro | [`motorola_moto_edge_30_pro.cal`](./motorola_moto_edge_30_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_edge_30_pro.cal) |
| Moto Edge 30 Ultra | [`motorola_moto_edge_30_ultra.cal`](./motorola_moto_edge_30_ultra.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_edge_30_ultra.cal) |
| Moto Edge 40 | [`motorola_moto_edge_40.cal`](./motorola_moto_edge_40.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_edge_40.cal) |
| Moto Edge 40 Neo | [`motorola_moto_edge_40_neo.cal`](./motorola_moto_edge_40_neo.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_edge_40_neo.cal) |
| Moto Edge 40 Pro | [`motorola_moto_edge_40_pro.cal`](./motorola_moto_edge_40_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_edge_40_pro.cal) |
| Moto Edge 50 | [`motorola_moto_edge_50.cal`](./motorola_moto_edge_50.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_edge_50.cal) |
| Moto Edge 50 Neo | [`motorola_moto_edge_50_neo.cal`](./motorola_moto_edge_50_neo.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_edge_50_neo.cal) |
| Moto Edge 50 Pro | [`motorola_moto_edge_50_pro.cal`](./motorola_moto_edge_50_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_edge_50_pro.cal) |
| Moto Edge 50 Ultra | [`motorola_moto_edge_50_ultra.cal`](./motorola_moto_edge_50_ultra.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_edge_50_ultra.cal) |
| Moto G10 | [`motorola_moto_g10.cal`](./motorola_moto_g10.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_g10.cal) |
| Moto G13 | [`motorola_moto_g13.cal`](./motorola_moto_g13.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_g13.cal) |
| Moto G14 | [`motorola_moto_g14.cal`](./motorola_moto_g14.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_g14.cal) |
| Moto G22 | [`motorola_moto_g22.cal`](./motorola_moto_g22.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_g22.cal) |
| Moto G23 | [`motorola_moto_g23.cal`](./motorola_moto_g23.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_g23.cal) |
| Moto G24 | [`motorola_moto_g24.cal`](./motorola_moto_g24.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_g24.cal) |
| Moto G24 Power | [`motorola_moto_g24_power.cal`](./motorola_moto_g24_power.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_g24_power.cal) |
| Moto G30 | [`motorola_moto_g30.cal`](./motorola_moto_g30.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_g30.cal) |
| Moto G50 | [`motorola_moto_g50.cal`](./motorola_moto_g50.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_g50.cal) |
| Moto G53 | [`motorola_moto_g53.cal`](./motorola_moto_g53.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_g53.cal) |
| Moto G54 | [`motorola_moto_g54.cal`](./motorola_moto_g54.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_g54.cal) |
| Moto G73 | [`motorola_moto_g73.cal`](./motorola_moto_g73.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_g73.cal) |
| Moto G84 | [`motorola_moto_g84.cal`](./motorola_moto_g84.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/motorola_moto_g84.cal) |

### 📱 OnePlus

| Modelo | Archivo | URL Raw |
| :--- | :--- | :--- |
| 10 Pro | [`oneplus_10_pro.cal`](./oneplus_10_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/oneplus_10_pro.cal) |
| 11 | [`oneplus_11.cal`](./oneplus_11.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/oneplus_11.cal) |
| 12 | [`oneplus_12.cal`](./oneplus_12.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/oneplus_12.cal) |
| 12 R | [`oneplus_12_r.cal`](./oneplus_12_r.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/oneplus_12_r.cal) |
| Nord Ce 2 | [`oneplus_nord_ce_2.cal`](./oneplus_nord_ce_2.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/oneplus_nord_ce_2.cal) |
| Nord Ce 3 | [`oneplus_nord_ce_3.cal`](./oneplus_nord_ce_3.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/oneplus_nord_ce_3.cal) |
| Nord N100 | [`oneplus_nord_n100.cal`](./oneplus_nord_n100.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/oneplus_nord_n100.cal) |
| Nord N200 | [`oneplus_nord_n200.cal`](./oneplus_nord_n200.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/oneplus_nord_n200.cal) |

### 📱 Oppo

| Modelo | Archivo | URL Raw |
| :--- | :--- | :--- |
| A15 | [`oppo_a15.cal`](./oppo_a15.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/oppo_a15.cal) |
| A16 | [`oppo_a16.cal`](./oppo_a16.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/oppo_a16.cal) |
| A17 | [`oppo_a17.cal`](./oppo_a17.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/oppo_a17.cal) |
| A53 | [`oppo_a53.cal`](./oppo_a53.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/oppo_a53.cal) |
| A54 | [`oppo_a54.cal`](./oppo_a54.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/oppo_a54.cal) |
| A57 | [`oppo_a57.cal`](./oppo_a57.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/oppo_a57.cal) |
| A58 | [`oppo_a58.cal`](./oppo_a58.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/oppo_a58.cal) |
| A78 | [`oppo_a78.cal`](./oppo_a78.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/oppo_a78.cal) |
| Find X5 | [`oppo_find_x5.cal`](./oppo_find_x5.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/oppo_find_x5.cal) |
| Find X5 Pro | [`oppo_find_x5_pro.cal`](./oppo_find_x5_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/oppo_find_x5_pro.cal) |
| Find X6 Pro | [`oppo_find_x6_pro.cal`](./oppo_find_x6_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/oppo_find_x6_pro.cal) |
| Reno 10 | [`oppo_reno_10.cal`](./oppo_reno_10.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/oppo_reno_10.cal) |
| Reno 10 Pro | [`oppo_reno_10_pro.cal`](./oppo_reno_10_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/oppo_reno_10_pro.cal) |
| Reno 7 | [`oppo_reno_7.cal`](./oppo_reno_7.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/oppo_reno_7.cal) |
| Reno 8 | [`oppo_reno_8.cal`](./oppo_reno_8.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/oppo_reno_8.cal) |
| Reno 8 Pro | [`oppo_reno_8_pro.cal`](./oppo_reno_8_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/oppo_reno_8_pro.cal) |

### 📱 Realme

| Modelo | Archivo | URL Raw |
| :--- | :--- | :--- |
| 10 | [`realme_10.cal`](./realme_10.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/realme_10.cal) |
| 10 Pro | [`realme_10_pro.cal`](./realme_10_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/realme_10_pro.cal) |
| 10 Pro Plus | [`realme_10_pro_plus.cal`](./realme_10_pro_plus.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/realme_10_pro_plus.cal) |
| 11 | [`realme_11.cal`](./realme_11.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/realme_11.cal) |
| 11 Pro | [`realme_11_pro.cal`](./realme_11_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/realme_11_pro.cal) |
| 11 Pro Plus | [`realme_11_pro_plus.cal`](./realme_11_pro_plus.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/realme_11_pro_plus.cal) |
| 12 | [`realme_12.cal`](./realme_12.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/realme_12.cal) |
| 12 Pro | [`realme_12_pro.cal`](./realme_12_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/realme_12_pro.cal) |
| 12 Pro Plus | [`realme_12_pro_plus.cal`](./realme_12_pro_plus.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/realme_12_pro_plus.cal) |
| C11 | [`realme_c11.cal`](./realme_c11.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/realme_c11.cal) |
| C21 | [`realme_c21.cal`](./realme_c21.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/realme_c21.cal) |
| C30 | [`realme_c30.cal`](./realme_c30.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/realme_c30.cal) |
| C33 | [`realme_c33.cal`](./realme_c33.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/realme_c33.cal) |
| C35 | [`realme_c35.cal`](./realme_c35.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/realme_c35.cal) |
| C53 | [`realme_c53.cal`](./realme_c53.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/realme_c53.cal) |
| C55 | [`realme_c55.cal`](./realme_c55.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/realme_c55.cal) |

### 📱 Samsung

| Modelo | Archivo | URL Raw |
| :--- | :--- | :--- |
| Galaxy A01 | [`samsung_galaxy_a01.cal`](./samsung_galaxy_a01.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a01.cal) |
| Galaxy A02 | [`samsung_galaxy_a02.cal`](./samsung_galaxy_a02.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a02.cal) |
| Galaxy A03 | [`samsung_galaxy_a03.cal`](./samsung_galaxy_a03.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a03.cal) |
| Galaxy A04 | [`samsung_galaxy_a04.cal`](./samsung_galaxy_a04.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a04.cal) |
| Galaxy A05 | [`samsung_galaxy_a05.cal`](./samsung_galaxy_a05.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a05.cal) |
| Galaxy A06 | [`samsung_galaxy_a06.cal`](./samsung_galaxy_a06.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a06.cal) |
| Galaxy A07 | [`samsung_galaxy_a07.cal`](./samsung_galaxy_a07.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a07.cal) |
| Galaxy A10 | [`samsung_galaxy_a10.cal`](./samsung_galaxy_a10.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a10.cal) |
| Galaxy A11 | [`samsung_galaxy_a11.cal`](./samsung_galaxy_a11.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a11.cal) |
| Galaxy A12 | [`samsung_galaxy_a12.cal`](./samsung_galaxy_a12.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a12.cal) |
| Galaxy A13 | [`samsung_galaxy_a13.cal`](./samsung_galaxy_a13.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a13.cal) |
| Galaxy A14 | [`samsung_galaxy_a14.cal`](./samsung_galaxy_a14.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a14.cal) |
| Galaxy A15 | [`samsung_galaxy_a15.cal`](./samsung_galaxy_a15.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a15.cal) |
| Galaxy A16 | [`samsung_galaxy_a16.cal`](./samsung_galaxy_a16.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a16.cal) |
| Galaxy A17 | [`samsung_galaxy_a17.cal`](./samsung_galaxy_a17.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a17.cal) |
| Galaxy A22 | [`samsung_galaxy_a22.cal`](./samsung_galaxy_a22.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a22.cal) |
| Galaxy A23 | [`samsung_galaxy_a23.cal`](./samsung_galaxy_a23.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a23.cal) |
| Galaxy A24 | [`samsung_galaxy_a24.cal`](./samsung_galaxy_a24.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a24.cal) |
| Galaxy A25 | [`samsung_galaxy_a25.cal`](./samsung_galaxy_a25.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a25.cal) |
| Galaxy A32 | [`samsung_galaxy_a32.cal`](./samsung_galaxy_a32.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a32.cal) |
| Galaxy A33 | [`samsung_galaxy_a33.cal`](./samsung_galaxy_a33.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a33.cal) |
| Galaxy A34 | [`samsung_galaxy_a34.cal`](./samsung_galaxy_a34.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a34.cal) |
| Galaxy A35 | [`samsung_galaxy_a35.cal`](./samsung_galaxy_a35.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a35.cal) |
| Galaxy A36 | [`samsung_galaxy_a36.cal`](./samsung_galaxy_a36.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a36.cal) |
| Galaxy A51 | [`samsung_galaxy_a51.cal`](./samsung_galaxy_a51.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a51.cal) |
| Galaxy A52 | [`samsung_galaxy_a52.cal`](./samsung_galaxy_a52.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a52.cal) |
| Galaxy A53 | [`samsung_galaxy_a53.cal`](./samsung_galaxy_a53.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a53.cal) |
| Galaxy A54 | [`samsung_galaxy_a54.cal`](./samsung_galaxy_a54.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a54.cal) |
| Galaxy A55 | [`samsung_galaxy_a55.cal`](./samsung_galaxy_a55.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a55.cal) |
| Galaxy A56 | [`samsung_galaxy_a56.cal`](./samsung_galaxy_a56.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_a56.cal) |
| Galaxy Note10 | [`samsung_galaxy_note10.cal`](./samsung_galaxy_note10.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_note10.cal) |
| Galaxy Note10 Plus | [`samsung_galaxy_note10_plus.cal`](./samsung_galaxy_note10_plus.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_note10_plus.cal) |
| Galaxy Note20 | [`samsung_galaxy_note20.cal`](./samsung_galaxy_note20.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_note20.cal) |
| Galaxy Note20 Ultra | [`samsung_galaxy_note20_ultra.cal`](./samsung_galaxy_note20_ultra.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_note20_ultra.cal) |
| Galaxy S20 | [`samsung_galaxy_s20.cal`](./samsung_galaxy_s20.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_s20.cal) |
| Galaxy S20 Fe | [`samsung_galaxy_s20_fe.cal`](./samsung_galaxy_s20_fe.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_s20_fe.cal) |
| Galaxy S20 Plus | [`samsung_galaxy_s20_plus.cal`](./samsung_galaxy_s20_plus.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_s20_plus.cal) |
| Galaxy S20 Ultra | [`samsung_galaxy_s20_ultra.cal`](./samsung_galaxy_s20_ultra.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_s20_ultra.cal) |
| Galaxy S21 | [`samsung_galaxy_s21.cal`](./samsung_galaxy_s21.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_s21.cal) |
| Galaxy S21 Fe | [`samsung_galaxy_s21_fe.cal`](./samsung_galaxy_s21_fe.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_s21_fe.cal) |
| Galaxy S21 Plus | [`samsung_galaxy_s21_plus.cal`](./samsung_galaxy_s21_plus.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_s21_plus.cal) |
| Galaxy S21 Ultra | [`samsung_galaxy_s21_ultra.cal`](./samsung_galaxy_s21_ultra.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_s21_ultra.cal) |
| Galaxy S22 | [`samsung_galaxy_s22.cal`](./samsung_galaxy_s22.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_s22.cal) |
| Galaxy S22 Plus | [`samsung_galaxy_s22_plus.cal`](./samsung_galaxy_s22_plus.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_s22_plus.cal) |
| Galaxy S22 Ultra | [`samsung_galaxy_s22_ultra.cal`](./samsung_galaxy_s22_ultra.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_s22_ultra.cal) |
| Galaxy S23 | [`samsung_galaxy_s23.cal`](./samsung_galaxy_s23.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_s23.cal) |
| Galaxy S23 Fe | [`samsung_galaxy_s23_fe.cal`](./samsung_galaxy_s23_fe.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_s23_fe.cal) |
| Galaxy S23 Plus | [`samsung_galaxy_s23_plus.cal`](./samsung_galaxy_s23_plus.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_s23_plus.cal) |
| Galaxy S23 Ultra | [`samsung_galaxy_s23_ultra.cal`](./samsung_galaxy_s23_ultra.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_s23_ultra.cal) |
| Galaxy S24 | [`samsung_galaxy_s24.cal`](./samsung_galaxy_s24.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_s24.cal) |
| Galaxy S24 Plus | [`samsung_galaxy_s24_plus.cal`](./samsung_galaxy_s24_plus.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_s24_plus.cal) |
| Galaxy S24 Ultra | [`samsung_galaxy_s24_ultra.cal`](./samsung_galaxy_s24_ultra.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_s24_ultra.cal) |
| Galaxy S25 | [`samsung_galaxy_s25.cal`](./samsung_galaxy_s25.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_s25.cal) |
| Galaxy S25 Plus | [`samsung_galaxy_s25_plus.cal`](./samsung_galaxy_s25_plus.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_s25_plus.cal) |
| Galaxy S25 Ultra | [`samsung_galaxy_s25_ultra.cal`](./samsung_galaxy_s25_ultra.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_s25_ultra.cal) |
| Galaxy S26 | [`samsung_galaxy_s26.cal`](./samsung_galaxy_s26.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_s26.cal) |
| Galaxy S26 Plus | [`samsung_galaxy_s26_plus.cal`](./samsung_galaxy_s26_plus.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_s26_plus.cal) |
| Galaxy S26 Ultra | [`samsung_galaxy_s26_ultra.cal`](./samsung_galaxy_s26_ultra.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/samsung_galaxy_s26_ultra.cal) |

### 📱 Vivo

| Modelo | Archivo | URL Raw |
| :--- | :--- | :--- |
| V23 | [`vivo_v23.cal`](./vivo_v23.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/vivo_v23.cal) |
| V25 | [`vivo_v25.cal`](./vivo_v25.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/vivo_v25.cal) |
| V27 Pro | [`vivo_v27_pro.cal`](./vivo_v27_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/vivo_v27_pro.cal) |
| X100 Pro | [`vivo_x100_pro.cal`](./vivo_x100_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/vivo_x100_pro.cal) |
| X90 Pro | [`vivo_x90_pro.cal`](./vivo_x90_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/vivo_x90_pro.cal) |
| Y16 | [`vivo_y16.cal`](./vivo_y16.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/vivo_y16.cal) |
| Y20 | [`vivo_y20.cal`](./vivo_y20.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/vivo_y20.cal) |
| Y21 | [`vivo_y21.cal`](./vivo_y21.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/vivo_y21.cal) |
| Y22 | [`vivo_y22.cal`](./vivo_y22.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/vivo_y22.cal) |
| Y35 | [`vivo_y35.cal`](./vivo_y35.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/vivo_y35.cal) |

### 📱 Xiaomi

| Modelo | Archivo | URL Raw |
| :--- | :--- | :--- |
| 12 | [`xiaomi_12.cal`](./xiaomi_12.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_12.cal) |
| 12 Pro | [`xiaomi_12_pro.cal`](./xiaomi_12_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_12_pro.cal) |
| 12 Ultra | [`xiaomi_12_ultra.cal`](./xiaomi_12_ultra.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_12_ultra.cal) |
| 13 | [`xiaomi_13.cal`](./xiaomi_13.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_13.cal) |
| 13 Pro | [`xiaomi_13_pro.cal`](./xiaomi_13_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_13_pro.cal) |
| 13 Ultra | [`xiaomi_13_ultra.cal`](./xiaomi_13_ultra.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_13_ultra.cal) |
| 14 | [`xiaomi_14.cal`](./xiaomi_14.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_14.cal) |
| 14 Pro | [`xiaomi_14_pro.cal`](./xiaomi_14_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_14_pro.cal) |
| 14 Ultra | [`xiaomi_14_ultra.cal`](./xiaomi_14_ultra.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_14_ultra.cal) |
| Mi 11T | [`xiaomi_mi_11t.cal`](./xiaomi_mi_11t.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_mi_11t.cal) |
| Mi 11T Pro | [`xiaomi_mi_11t_pro.cal`](./xiaomi_mi_11t_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_mi_11t_pro.cal) |
| Poco F3 | [`xiaomi_poco_f3.cal`](./xiaomi_poco_f3.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_poco_f3.cal) |
| Poco F4 | [`xiaomi_poco_f4.cal`](./xiaomi_poco_f4.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_poco_f4.cal) |
| Poco F5 | [`xiaomi_poco_f5.cal`](./xiaomi_poco_f5.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_poco_f5.cal) |
| Poco F5 Pro | [`xiaomi_poco_f5_pro.cal`](./xiaomi_poco_f5_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_poco_f5_pro.cal) |
| Poco M3 | [`xiaomi_poco_m3.cal`](./xiaomi_poco_m3.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_poco_m3.cal) |
| Poco M4 | [`xiaomi_poco_m4.cal`](./xiaomi_poco_m4.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_poco_m4.cal) |
| Poco M4 Pro | [`xiaomi_poco_m4_pro.cal`](./xiaomi_poco_m4_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_poco_m4_pro.cal) |
| Poco M5 | [`xiaomi_poco_m5.cal`](./xiaomi_poco_m5.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_poco_m5.cal) |
| Poco X3 | [`xiaomi_poco_x3.cal`](./xiaomi_poco_x3.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_poco_x3.cal) |
| Poco X3 Pro | [`xiaomi_poco_x3_pro.cal`](./xiaomi_poco_x3_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_poco_x3_pro.cal) |
| Poco X4 Pro | [`xiaomi_poco_x4_pro.cal`](./xiaomi_poco_x4_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_poco_x4_pro.cal) |
| Poco X5 | [`xiaomi_poco_x5.cal`](./xiaomi_poco_x5.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_poco_x5.cal) |
| Poco X5 Pro | [`xiaomi_poco_x5_pro.cal`](./xiaomi_poco_x5_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_poco_x5_pro.cal) |
| Poco X6 | [`xiaomi_poco_x6.cal`](./xiaomi_poco_x6.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_poco_x6.cal) |
| Poco X6 Pro | [`xiaomi_poco_x6_pro.cal`](./xiaomi_poco_x6_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_poco_x6_pro.cal) |
| Redmi 10 | [`xiaomi_redmi_10.cal`](./xiaomi_redmi_10.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_redmi_10.cal) |
| Redmi 10A | [`xiaomi_redmi_10a.cal`](./xiaomi_redmi_10a.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_redmi_10a.cal) |
| Redmi 12 | [`xiaomi_redmi_12.cal`](./xiaomi_redmi_12.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_redmi_12.cal) |
| Redmi 12C | [`xiaomi_redmi_12c.cal`](./xiaomi_redmi_12c.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_redmi_12c.cal) |
| Redmi 13 | [`xiaomi_redmi_13.cal`](./xiaomi_redmi_13.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_redmi_13.cal) |
| Redmi 13C | [`xiaomi_redmi_13c.cal`](./xiaomi_redmi_13c.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_redmi_13c.cal) |
| Redmi 14C | [`xiaomi_redmi_14c.cal`](./xiaomi_redmi_14c.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_redmi_14c.cal) |
| Redmi 9 | [`xiaomi_redmi_9.cal`](./xiaomi_redmi_9.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_redmi_9.cal) |
| Redmi 9A | [`xiaomi_redmi_9a.cal`](./xiaomi_redmi_9a.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_redmi_9a.cal) |
| Redmi Note 10 | [`xiaomi_redmi_note_10.cal`](./xiaomi_redmi_note_10.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_redmi_note_10.cal) |
| Redmi Note 10 Pro | [`xiaomi_redmi_note_10_pro.cal`](./xiaomi_redmi_note_10_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_redmi_note_10_pro.cal) |
| Redmi Note 11 | [`xiaomi_redmi_note_11.cal`](./xiaomi_redmi_note_11.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_redmi_note_11.cal) |
| Redmi Note 11 Pro | [`xiaomi_redmi_note_11_pro.cal`](./xiaomi_redmi_note_11_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_redmi_note_11_pro.cal) |
| Redmi Note 12 | [`xiaomi_redmi_note_12.cal`](./xiaomi_redmi_note_12.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_redmi_note_12.cal) |
| Redmi Note 12 Pro | [`xiaomi_redmi_note_12_pro.cal`](./xiaomi_redmi_note_12_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_redmi_note_12_pro.cal) |
| Redmi Note 13 | [`xiaomi_redmi_note_13.cal`](./xiaomi_redmi_note_13.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_redmi_note_13.cal) |
| Redmi Note 13 Pro | [`xiaomi_redmi_note_13_pro.cal`](./xiaomi_redmi_note_13_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_redmi_note_13_pro.cal) |
| Redmi Note 13 Pro Plus | [`xiaomi_redmi_note_13_pro_plus.cal`](./xiaomi_redmi_note_13_pro_plus.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_redmi_note_13_pro_plus.cal) |
| Redmi Note 14 | [`xiaomi_redmi_note_14.cal`](./xiaomi_redmi_note_14.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_redmi_note_14.cal) |
| Redmi Note 14 Pro | [`xiaomi_redmi_note_14_pro.cal`](./xiaomi_redmi_note_14_pro.cal) | [Raw URL](https://raw.githubusercontent.com/urielnieva/Calibracion_Mics/main/xiaomi_redmi_note_14_pro.cal) |

---

## ➕ Cómo Agregar un Nuevo Dispositivo

1. Mide la respuesta del micrófono o consigue los datos de respuesta en frecuencia.
2. Crea un archivo con el formato `<marca>_<modelo>.cal` (por ejemplo, `xiaomi_redmi_note_12.cal`) utilizando únicamente minúsculas y guiones bajos.
3. Sube el archivo a este repositorio.
4. Obtén el enlace Raw desde GitHub y pruébalo en tu aplicación.
