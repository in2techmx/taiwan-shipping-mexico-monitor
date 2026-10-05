# Rebanada 01: Dominio de Fletes Marítimos Asia-México, Rutas y Contratos

## 1. Rutas Marítimas Transpacíficas Críticas
1. **Ruta China Continental ➔ México Pacífico:**
   - Puertos de Origen: Shanghai (SGSIN), Ningbo-Zhoushan (CNNGB), Shenzhen/Yantian (CNYAT).
   - Puertos de Destino: Manzanillo (MXZLO), Lázaro Cárdenas (MXLZC).
   - Tránsito normal: 18 - 24 días.
2. **Ruta Taiwán ➔ México Pacífico:**
   - Puertos de Origen: Kaohsiung (TWKHH), Keelung (TWKEL).
   - Puertos de Destino: Manzanillo (MXZLO), Lázaro Cárdenas (MXLZC).
   - Tránsito normal: 19 - 25 días.
   - Tráfico a través del **Estrecho de Taiwán (Formosa Strait)** y Mar de Filipinas.

## 2. Contratos de Datos Institucionales
### `FreightSpotQuote`
```json
{
  "routeId": "SHANGHAI_TO_MANZANILLO | KAOHSIUNG_TO_MANZANILLO",
  "originPort": "Kaohsiung, Taiwán",
  "destinationPort": "Manzanillo, Colima, México",
  "containerType": "40ft High Cube (FEU) | 20ft Standard (TEU)",
  "spotPriceUsd": 4480.0,
  "weeklyChangePct": 2.15,
  "transitDays": 22,
  "congestionDaysDestination": 4.5,
  "warRiskPremiumUsd": 350.0
}
```

### `TaiwanStraitTensionIndex`
```json
{
  "tensionLevel": "ELEVADA | MODERADA | NORMAL | CRÍTICA",
  "militaryExerciseZoneActive": true,
  "straitDeviationRequired": false,
  "transitDelayExpectedDays": 3.0,
  "bafSurchargeUsd": 120.0
}
```
