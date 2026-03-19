#!/usr/bin/env python3
"""
Трекер привычек - учебный проект для Git
"""

def show_help():
    """Показать справку"""
    help_text = """
    Команды:
    add <название> - добавить новую привычку
    list           - показать все привычки
    done <номер>   - отметить привычку как выполненную
    help           - показать эту справку
    exit           - выход
    """
    print(help_text)

def main():
    print("=== Трекер привычек ===")
    show_help()
    
    while True:
        command = input("\n> ").strip().lower()
        
        if command == "help":
            show_help()
        elif command == "exit":
            print("До свидания!")
            break
        elif command == "":
            continue
        else:
            print(f"Неизвестная команда: {command}")

if __name__ == "__main__":
    main()
