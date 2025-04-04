# Dies ist ein Programme welches eine Ausgewählte Frucht in einer Liste gezählt wird

fruits = ["Apple", "banana", "Banana", "orange", "Banana"]

# hier nutzen wir neue Methoden, .strip() und .lower()
to_count = input("Welche Frucht möchtest du zählen? ").strip().lower()

# hier 'sanatizen' wir unsere fruits (sorgen dafür dass alles klein geschrieben ist mit .lower())
fruits_sanitized = [fruit.lower() for fruit in fruits]

# hier zählen wir!
amount = fruits_sanitized.count(to_count)

# hier nutzen wir string interpolation!
print(f"Die Frucht '{to_count}' kommt {amount} Mal in der Liste vor.")