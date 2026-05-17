"""Module for URL risk analysis."""

class URLAnalyzer:
    """Analyzes URLs for phishing indicators."""

    def analyze(self, url):
        reasons = []
        score = 0

        suspicious_keywords = ["login", "verify", "secure", "account", "update"]

        if len(url) > 50:
            score += 1
            reasons.append("URL is unusually long")

        if "http://" in url:
            score += 1
            reasons.append("Uses insecure HTTP protocol")

        if url.count("-") > 2:
            score += 1
            reasons.append("Too many hyphens detected")

        for word in suspicious_keywords:
            if word in url.lower():
                score += 1
                reasons.append(f"Contains suspicious keyword: {word}")

        if score >= 4:
            risk = "HIGH"
        elif score >= 2:
            risk = "MEDIUM"
        else:
            risk = "LOW"

        return {
            "risk": risk,
            "reasons": reasons if reasons else ["No suspicious indicators found"]
        }