# Rebanada 02: Radar Geopolítico Taiwán-China y Modelo Probabilístico de Fletes

## 1. Modelo Estocástico de Fletes con Saltos Geopolíticos
A diferencia del tipo de cambio, los fletes marítimos tienen dinámicas de asimetría positiva extrema (cuando hay una crisis en el Estrecho de Taiwán o en el Mar Rojo, los fletes no suben un 1%, sino que pueden saltar un 40% a 150% en semanas debido a la escasez de buques y seguros de guerra).

$$S_t = S_0 \exp\left( \left(\mu - \frac{1}{2}\sigma^2 - \lambda k \right)t + \sigma W_t \right) \prod_{i=1}^{N_t} (1 + J_i)$$

- $S_0$: Costo spot base actual ($4,450 USD / FEU para Shanghai/Kaohsiung a Manzanillo).
- $\mu$: Deriva de estacionalidad (post Golden Week china de octubre: leve tendencia de ajuste a la baja en noviembre).
- $\sigma$: Volatilidad semanal ordinaria del flete ($\approx 12\%$ anualizada).
- $\lambda$: Frecuencia de saltos por incidentes o maniobras militares chinas en el Estrecho de Taiwán ($\lambda \approx 0.15$).
- $\ln(1+J) \sim \mathcal{N}(\mu_J, \sigma_J^2)$: Magnitud de salto en caso de bloqueo o desvío de buques ($\mu_J = +0.25$ a $+0.40$, es decir, aumento de +$1,000 a +$2,000 USD por contenedor).

## 2. Los 4 Canales del Radar Cuantamental
1. 🇹🇼 **Canal Taiwán & Estrecho:** Ejercicios del PLA, incursiones en ADIZ, producción en TSMC, Kaohsiung port operations.
2. 🇨🇳 **Canal China Continental & Exportaciones:** Puertos de Shanghai, Ningbo, Shenzhen, subsidios navieros, demanda manufacturera.
3. 🇲🇽 **Canal México & Logística Portuaria:** Días de espera en Manzanillo y Lázaro Cárdenas, saturación de patios, ferrocarril Ferromex/CPKC.
4. 🚢 **Canal Líneas Navieras & Tarifas Spot:** Tarifas de Maersk, MSC, COSCO, Evergreen, Yang Ming, recargos BAF/PSS.
