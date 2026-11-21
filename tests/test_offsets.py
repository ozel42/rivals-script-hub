from src.shared.offsets import OFFSETS, VERSION


def test_version_string():
    assert VERSION.startswith("2026.")


def test_required_offsets():
    for key in ("players_chain", "local_humanoid_chain", "can_collide"):
        assert key in OFFSETS
        assert OFFSETS[key] is not None
</br>