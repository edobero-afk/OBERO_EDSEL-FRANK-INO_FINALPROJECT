"""Main entry point for PhishGuard CLI."""

from url__analyzer import URLAnalyzer
from history_manager import HistoryManager


def main():
    analyzer = URLAnalyzer()
    history = HistoryManager("data/scan_history.json")

    while True:
        print("\n=== PhishGuard CLI ===")   
        print("1. Analyze URL")
        print("2. View Scan History")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            url = input("Enter URL to analyze: ")
            result = analyzer.analyze(url)
            print(f"\nRisk Level: {result['risk']}")
            print("Reasons:")
            for reason in result['reasons']:
                print(f"- {reason}")
            history.save_scan(url, result)

        elif choice == "2":
            scans = history.load_history()
            for scan in scans:
                print(scan)

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
  main()