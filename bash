mkdir habit-tracker
cd habit-tracker

# Инициализируем Git
git init

# Создаем README.md
echo "# Трекер привычек" > README.md
echo "Проект для изучения Git. Позволяет добавлять и отслеживать ежедневные привычки." >> README.md

# Создаем .gitignore
echo "__pycache__/" > .gitignore
echo "*.pyc" >> .gitignore
echo "data/" >> .gitignore  # Игнорируем папку с данными

# Первый коммит
git add README.md .gitignore
git commit -m "init: начальная структура проекта
git remote add origin https://github.com/ВАШ_ЛОГИН/habit-tracker.git
git branch -M main
git push -u origin main
