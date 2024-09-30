import pytest
from src.energy import Microgrid


def test_microgrid_initialization():
    g = Microgrid(1000, 500)
    assert g.production_capacity == 1000
    assert g.storage_capacity == 500
    assert g.current_storage == 0
    assert g.consumption == 0


def test_produce_energy():
    g = Microgrid(1000, 500)
    g.produce_energy(600)
    assert g.current_storage == 500
    g.produce_energy(200)
    assert g.current_storage == 500


def test_consume_energy():
    g = Microgrid(1000, 500)
    g.produce_energy(500)
    g.consume_energy(200)
    assert g.current_storage == 300
    assert g.consumption == 200
    g.consume_energy(400)
    assert g.current_storage == 0
    assert g.consumption == 500


def test_get_status():
    g = Microgrid(1000, 500)
    g.produce_energy(500)
    g.consume_energy(200)
    status = g.get_status()
    assert status == {
        'production_capacity': 1000,
        'storage_capacity': 500,
        'current_storage': 300,
        'consumption': 200
    }


def test_simulate():
    g = Microgrid(1000, 500)
    g.simulate([300, 400, 500], [100, 200, 300])
    assert g.current_storage == 200
    assert g.consumption == 600
