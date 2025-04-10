import pandas as pd
import random
from datetime import datetime

locks = ["Bonneville", "The Dalles", "John Day", "McNary", "Ice Harbor", "Lower Monumental", "Little Goose", "Lower Granite"]
directions = ["Upstream", "Downstream"]

data = []

for lock in locks:
    for direction in directions:
        count = random.randint(0, 6)
        data.append({
            "Date": datetime.today().strftime("%Y-%m-%d"),
            "Lock Name": lock,
            "Direction": direction,
            "Barge Count": count
        })

df = pd.DataFrame(data)
df.to_csv("barge_data.csv", index=False)
print("✅ barge_data.csv updated with simulated data.")