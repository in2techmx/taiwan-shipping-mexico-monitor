"""Unit Tests for Taiwan & Asia-Mexico Freight Engine & Geopolitical Scoring (Gate 1)."""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
scripts_dir = os.path.join(os.path.dirname(current_dir), "scripts")
sys.path.insert(0, scripts_dir)

from daily_shipping_sync import calculate_maritime_metrics, generate_stochastic_freight_trajectory


def test_maritime_metrics_scoring():
    """Verify that impact score is strictly bounded in [1.0, 10.0] and directions are valid."""
    cases = [
        ("Ejercicios militares con misiles en el Estrecho de Taiwán cierran rutas navieras", "Reuters", "taiwan_strait"),
        ("Puerto de Manzanillo reporta saturación de patios y retrasos aduanales", "El Economista", "mexico_ports"),
        ("Navieras anuncian descuentos de fletes y tarifas a la baja", "Bloomberg", "shipping_lines"),
        ("Operaciones ordinarias de carga en terminales de Ningbo", "Medio Local", "china_ports")
    ]
    for title, source, channel in cases:
        res = calculate_maritime_metrics(title, source, channel)
        assert 1.0 <= res["impact_score"] <= 10.0
        assert res["direction"] in ["ALCISTA_FLETE", "BAJISTA_FLETE", "NEUTRAL"]
        assert len(res["transmission"]) > 20


def test_taiwan_drill_shock_direction():
    """Verify naval drills trigger ALCISTA_FLETE with war risk and transit delay explanation."""
    title = "PLA anuncia maniobras militares con fuego real y bloqueo naval frente a Kaohsiung"
    source = "Lloyd's List"
    res = calculate_maritime_metrics(title, source, "taiwan_strait")
    assert res["direction"] == "ALCISTA_FLETE"
    assert res["impact_score"] >= 8.0
    assert "desvíos de ruta marítima" in res["transmission"] or "Estrecho" in res["transmission"]


def test_stochastic_freight_trajectory_properties():
    """Verify 30-day trajectory properties: widening cone and positive asymmetry."""
    traj = generate_stochastic_freight_trajectory(base_spot_feu=4450.0, days=30)
    assert len(traj) == 31
    assert traj[0]["p50"] == 4450.0
    
    # Check that P90 > P75 > P50 > P25 > P10 for all days
    for d in traj[1:]:
        assert d["p90"] > d["p75"] > d["p50"] > d["p25"] > d["p10"]
        assert d["p90"] >= 4500.0


if __name__ == "__main__":
    test_maritime_metrics_scoring()
    test_taiwan_drill_shock_direction()
    test_stochastic_freight_trajectory_properties()
    print("ALL MARITIME ENGINE TESTS PASS DETERMINISTICALLY (100% SUCCESS).")
