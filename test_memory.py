from memory import save_memory, get_related_memories

user_id = "12a34bc5-de67-8901-fg23-h4567890ijkl"  # Use your real Supabase UID

save_memory(user_id, "Company X launched a new AI product for the healthcare sector.")

results = get_related_memories("What did Company X launch?")
for doc in results:
    print("🧠 Retrieved:", doc.page_content)
