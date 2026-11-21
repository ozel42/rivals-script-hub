from src.shared.config import HubConfig, load_config


def test_defaults_present():
    cfg = HubConfig()
    assert cfg.aimbot.enabled is True
    assert cfg.aimbot.fov_px > 0
    assert cfg.esp.head_dot is True


def test_load_missing_returns_defaults(tmp_path):
    cfg = load_config(tmp_path / "nope.toml")
    assert isinstance(cfg, HubConfig)
    assert cfg.triggerbot.fire_delay_ms > 0