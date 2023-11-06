from chat import Professor

professors_data = [
    ("Dr. Henry Brown", "history"),
    ("Dr. Sophia Smith", "mathematics"),
    ("Dr. Emily Davis", "biology"),
    ("Dr. William Johnson", "physics"),
    ("Dr. Olivia White", "chemistry"),
    ("Dr. Benjamin Clark", "economics"),
    ("Dr. Mia Martinez", "psychology"),
    ("Dr. Ethan Anderson", "computer science"),
    ("Dr. Lily Wilson", "philosophy"),
    ("Dr. Samuel Moore", "sociology"),
    ("Dr. Lucy Taylor", "literature"),
    ("Dr. Daniel Harris", "art"),
    ("Dr. Aiden Turner", "geology"),
    ("Dr. Chloe Allen", "political science"),
    ("Dr. Caleb Walker", "astronomy"),
    ("Dr. Grace Hall", "linguistics"),
    ("Dr. Oliver Green", "engineering"),
    ("Dr. Zoey Lewis", "medicine"),
    ("Dr. Noah Hall", "environmental science"),
    ("Dr. Ava Mitchell", "music")
]

professors = [Professor(name, category) for name, category in professors_data]
