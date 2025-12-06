import re

def process_list(numbers):
    return sorted([num for num in numbers if num % 2 == 0], reverse=True) if numbers else []

def filter_long_words(words):
    return [word.lower() for word in words if len(word) > 5]

def extract_emails(text):
    return re.findall(r'\b\w+@\w+\.\w+\b', text)

def mask_phone_numbers(text):
    pattern = r'(\+\d+\s*\(\d{3}\)\s*\d{3}-\d{2}-\d{2}|8\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2})'
    return re.sub(pattern, '***-**-**', text)

def extract_failed_logins(logs):
    return [match.group(1) for log in logs if (match := re.search(r'^(\d+\.\d+\.\d+\.\d+).*?"\s+401\s+', log))]

if name == "__main__":
    # Тест 1
    print("Чётные числа по убыванию:", process_list([3, 6, 1, 8, 2, 9]))
    
    # Тест 2
    words_test = ["apple", "Banana", "Cherry", "date", "Elderberry"]
    print("Длинные слова в нижнем регистре:", filter_long_words(words_test))
    
    # Тест 3
    email_text = "Contact support@example.com or admin@test.org"
    print("Найденные email:", extract_emails(email_text))
    
    # Тест 4
    phone_text = "Call +7 (999) 123-45-67 or 8 999 123 45 67"
    print("Замаскированные номера:", mask_phone_numbers(phone_text))
    
    # Тест 5
    logs = [
        '192.168.1.1 - - [25/Nov/2025:10:00:01 +0300] "GET /index.html HTTP/1.1" 200 1234',
        '10.0.0.5 - - [25/Nov/2025:10:01:22 +0300] "POST /login HTTP/1.1" 401 567',
        '172.16.0.10 - - [26/Nov/2025:09:55:10 +0300] "GET /profile HTTP/1.1" 200 890'
    ]
    print("IP с неудачными входами:", extract_failed_logins(logs))
