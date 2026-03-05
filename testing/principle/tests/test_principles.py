#import sys
#sys.path.append("../src")
#TODO make it with `clearpip install -e .`
#in project root_dir after setup.py defined

# Ранее тестирование позволяет съэкономить время позднее
# Тесты показывают наличие ошибок, а не отсутвие 
# Тесты не должны дублировать логику тестируемого кода
# Тесты не должны использовать ВСЕ наборы входных параметров
# Тесты должны покрывать "кластеры" входных параметров
# Тесты должны обнаруживать новые ошибки (pescicide paradox)
# Тесты покрывают как успешные так и ошибочные кейсы

from math_demo import add

def test_addition():
    assert 2 + 2 == 4
    print("Test ADDITION PASSED")

if __name__ == "__main__":
    test_addition()