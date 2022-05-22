from gpu import GPU
from generator import Generator


def test_gpu():
    g = GPU("Nvidia", 1660, "TU116", ["Ti", 6, 1500.0, "GTX"], "7680×4320")
    assert g.manufacture == "Nvidia"
    assert g.model == 1660
    assert g.chip == "TU116"
    assert g.mod == "Ti"
    assert g.memory == 6
    assert g.frequency == 1500.0
    assert g.prefix == "GTX"
    assert g.resolution == "7680×4320"


def test_gpu_get_info():
    g = GPU("Nvidia", 1660, "TU116", ["Ti", 6, 1500.0, "GTX"], "7680×4320")
    assert isinstance(g.get_info(), str)


def test_gen_single_type():
    g = Generator()
    p = g.generator()
    assert isinstance(p, GPU)
    assert isinstance(p.manufacture, str)
    assert isinstance(p.model, int)
    assert isinstance(p.chip, str)
    assert isinstance(p.mod, str)
    assert isinstance(p.memory, int)
    assert isinstance(p.frequency, float)
    assert isinstance(p.resolution, str)
    assert isinstance(p.prefix, str)


def test_gen_1000_type():
    g = Generator()
    p = g.generate_1000()
    assert isinstance(p, list)
    assert isinstance(p[0], GPU)
    assert len(p) == 1000


def test_gen_10000_type():
    g = Generator()
    p = g.generate_10000()
    assert isinstance(p, list)
    assert isinstance(p[0], GPU)
    assert len(p) == 10000
