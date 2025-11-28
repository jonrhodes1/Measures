import json
import subprocess
import sys
from pathlib import Path


def run_cli(args):
    result = subprocess.run(
        [sys.executable, "-m", "measures.cli", *args],
        check=False,
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout, result.stderr


def test_cli_outputs_human_readable_summary(tmp_path: Path):
    data = "1 2 3 4"
    data_file = tmp_path / "values.txt"
    data_file.write_text(data, encoding="utf-8")

    code, stdout, stderr = run_cli(["-f", str(data_file)])
    assert code == 0
    assert stderr == ""
    assert "Mean:" in stdout
    assert "Median:" in stdout


def test_cli_json_output():
    code, stdout, stderr = run_cli(["1", "2", "2", "3", "--json"])
    assert code == 0
    assert stderr == ""
    payload = json.loads(stdout)
    assert payload["mode"] == [2.0]
    assert payload["count"] == 4


def test_cli_reports_invalid_number():
    code, stdout, stderr = run_cli(["not-a-number"])
    assert code != 0
    assert "Invalid number" in stderr
