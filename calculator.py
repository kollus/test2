#!/usr/bin/env python3
"""
간단한 계산기 프로그램
사칙연산(+, -, *, /)을 지원합니다.
"""

def add(a, b):
    """두 수를 더합니다."""
    return a + b

def subtract(a, b):
    """두 수를 뺍니다."""
    return a - b

def multiply(a, b):
    """두 수를 곱합니다."""
    return a * b

def divide(a, b):
    """두 수를 나눕니다."""
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다!")
    return a / b

def calculator():
    """계산기 메인 함수"""
    print("=" * 40)
    print("Python 계산기에 오신 것을 환영합니다!")
    print("=" * 40)
    
    while True:
        print("\n사용 가능한 연산:")
        print("1. 덧셈 (+)")
        print("2. 뺄셈 (-)")
        print("3. 곱셈 (*)")
        print("4. 나눗셈 (/)")
        print("5. 종료 (q)")
        
        choice = input("\n연산을 선택하세요 (1-5 또는 +,-,*,/,q): ").strip()
        
        if choice in ['5', 'q', 'Q', '종료']:
            print("계산기를 종료합니다. 감사합니다!")
            break
        
        if choice not in ['1', '2', '3', '4', '+', '-', '*', '/']:
            print("잘못된 입력입니다. 다시 선택해주세요.")
            continue
        
        try:
            num1 = float(input("첫 번째 숫자를 입력하세요: "))
            num2 = float(input("두 번째 숫자를 입력하세요: "))
            
            if choice in ['1', '+']:
                result = add(num1, num2)
                operation = "+"
            elif choice in ['2', '-']:
                result = subtract(num1, num2)
                operation = "-"
            elif choice in ['3', '*']:
                result = multiply(num1, num2)
                operation = "*"
            elif choice in ['4', '/']:
                result = divide(num1, num2)
                operation = "/"
            
            print(f"\n결과: {num1} {operation} {num2} = {result}")
            
        except ValueError as e:
            if "could not convert" in str(e):
                print("오류: 유효한 숫자를 입력해주세요!")
            else:
                print(f"오류: {e}")
        except Exception as e:
            print(f"예상치 못한 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    calculator()
