import csv
from datetime import datetime
import matplotlib.pyplot as plt

# 讀取審核過的乾淨資料
clean_file = "data/u2_campus_threat_daily_clean.csv"
rows = []
with open(clean_file, mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

# ----------------------------------------------------
# CHART 1: LINE CHART (PHISHING + FAILED LOGINS OVER TIME)
# ----------------------------------------------------
dates = [row["date"] for row in rows]
phishing = [int(row["phishing_reports"]) for row in rows]
failed_logins = [int(row["failed_logins"]) for row in rows]

plt.figure(figsize=(10, 5))
plt.plot(dates, phishing, label="Phishing Reports", color="#D9534F")
plt.plot(dates, failed_logins, label="Failed Logins", color="#0275D8")
plt.title("Phishing Reports and Failed Logins Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Incidents Count")
step = max(1, len(dates) // 10)
plt.xticks(range(0, len(dates), step), dates[::step], rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("chart1_threats_over_time.png")
plt.clf()

# ----------------------------------------------------
# CHART 2: WEEKDAY VS WEEKEND (PHISHING REPORTS)
# ----------------------------------------------------
def is_weekend(d):
    return datetime.strptime(d, "%Y-%m-%d").weekday() >= 5  # 5 = Sat, 6 = Sun

wd, we = [], []
for row in rows:
    (we if is_weekend(row["date"]) else wd).append(int(row["phishing_reports"]))

avg_wd = sum(wd) / len(wd)
avg_we = sum(we) / len(we)
print(f"weekday {avg_wd:.2f} ({len(wd)} days) | weekend {avg_we:.2f} ({len(we)} days)")

plt.figure(figsize=(6, 4))
plt.bar(["Weekday", "Weekend"], [avg_wd, avg_we], color=["#4A90E2", "#F5A623"])
plt.text(0, avg_wd, f"{avg_wd:.2f}", ha="center", va="bottom")
plt.text(1, avg_we, f"{avg_we:.2f}", ha="center", va="bottom")
plt.title("Phishing Attacks Drop Significantly on Weekends During School Term")
plt.xlabel("Day Type")
plt.ylabel("Average Phishing Reports")
plt.ylim(bottom=0)
plt.tight_layout()
plt.savefig("chart2_weekday_weekend.png")
plt.clf()

# ----------------------------------------------------
# CHART 3: LOGIN SUCCESS RATE HISTOGRAM
# ----------------------------------------------------
rates = [float(row["login_success_rate"]) for row in rows]

plt.figure(figsize=(7, 4))
plt.hist(rates, bins=15, edgecolor="white", color="#4A90E2")
plt.title("Most Days Sit Between 45% and 72% Login Success — One Day Collapses to 0%")
plt.xlabel("Login Success Rate")
plt.ylabel("Number of Days")
plt.tight_layout()
plt.savefig("chart3_success_rate.png")
plt.clf()