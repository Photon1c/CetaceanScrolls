# log_scroll_entry.py
import json
from datetime import datetime

def log_entry(transcription, interpretation, output_path="cetacean_scrolls_log.json"):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "transcription": transcription,
        "interpretation": interpretation
    }
    if os.path.exists(output_path):
        with open(output_path, "r+") as f:
            data = json.load(f)
            data.append(entry)
            f.seek(0)
            json.dump(data, f, indent=2)
    else:
        with open(output_path, "w") as f:
            json.dump([entry], f, indent=2)
