import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def test_install_copy_and_run(tmp_path):
    env = {**os.environ, "HOME": str(tmp_path)}
    subprocess.run(["bash", str(ROOT / "install.sh")], check=True, env=env, capture_output=True)
    for d in (tmp_path / ".claude/skills/rt-chile", tmp_path / ".agents/skills/rt-chile"):
        assert (d / "SKILL.md").exists() and (d / "data/zonas_comunas.csv").exists()
        assert not (d / "tests").exists()
    out = subprocess.run([sys.executable, str(tmp_path / ".agents/skills/rt-chile/scripts/zona.py"), "Temuco"],
                         check=True, capture_output=True, text=True).stdout
    assert json.loads(out)["zona"] in "ABCDEFGHI"
    subprocess.run(["bash", str(ROOT / "install.sh"), "--uninstall"], check=True, env=env, capture_output=True)
    assert not (tmp_path / ".claude/skills/rt-chile").exists()
