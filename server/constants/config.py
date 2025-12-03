from pathlib import Path as path

base_dir = path(__file__).resolve().parent.parent  # server/
db_file = base_dir / "db" / "to_do_db.sqlite"

