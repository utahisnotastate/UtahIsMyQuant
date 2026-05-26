"""Launch Omni-Sieve Streamlit dashboard."""
from src.ui.omni_sieve_dashboard import run_dashboard


def run_dashboard_cli() -> None:
    import streamlit.web.cli as stcli
    import sys

    sys.argv = ["streamlit", "run", "src/ui/omni_sieve_dashboard.py", "--server.headless=true"]
    stcli.main()


if __name__ == "__main__":
    run_dashboard()
