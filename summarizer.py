
        suggestions.append("- Update deprecated dependencies or APIs.")
    if not suggestions:
        suggestions.append("✅ No obvious errors or warnings detected in the logs.")
    return "\n".join(suggestions)

def main():
    print("\n🔍 Discovering pod...")
    pod_name = find_demo_logger_pod()
    print(f"🔗 Found pod: {pod_name}")

    print(f"\n📥 Fetching last {LOG_LINES} lines from pod logs...")
    logs = fetch_logs(pod_name)
    print("--- Logs Fetched ---")
    print(logs)
    print("--------------------\n")

    summarizer = load_summarizer()
    prompt = (
        "Summarize the following logs by listing errors and warnings "
        "with counts and provide actionable suggestions:\n\n"
        + logs
    )
    print("🧠 Generating summary...")
    summary_result = summarizer(
        prompt,
        max_length=150,
        do_sample=False
    )
    summary_text = summary_result[0]["summary_text"]

    print("\n=== Summary ===\n")
    print(summary_text)

    print("\n=== Suggestions ===\n")
    print(suggest_actions(logs))

    print("\n🎉 Done.")

if __name__ == "__main__":
    main()

     
