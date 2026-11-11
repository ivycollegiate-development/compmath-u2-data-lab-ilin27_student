### Chart 2: Weekday vs Weekend Phishing Activity

* **Findings for School IT Administrators:**
  Phishing reports are concentrated during the instructional workweek, averaging 7.98 reports per day across 44 weekdays compared to 2.88 reports per day across 16 weekend days (a decline of approximately 64%). This indicates threat actors align their campaigns with operational school hours.

* **Key Metric:**
  IT administrators should plan defensive monitoring around the baseline of 7.98 attacks per weekday.

* **Honest Limitation:**
  The dataset contains 44 weekday observations against only 16 weekend days; due to the smaller weekend sample size, the weekend average carries higher statistical variance.

---

### Chart 3: Distribution of Login Success Rates

* **Findings for School IT Administrators:**
  Authentication success does not hover near 100%; daily login success rates sit primarily between 45% and 72%, with a median of 0.56 (56%). Out of 60 days, only 4 days achieved success rates above 0.90. Crucially, on 2026-10-24, the rate plummeted to 0.0, forming a severe outlier.

* **Honest Limitation & Investigation Needed:**
  The heavy left tail is dictated entirely by that single 0% outlier day. Before concluding there was an active breach, administrators must verify if this collapse stemmed from scheduled system maintenance or authentication logging downtime.