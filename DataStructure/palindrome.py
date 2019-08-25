# 회문 찾기 알고리즘
# lower()함수는 주어진 알파벳을 소문자로 바꾸는 기능을 합니다.

def palindrome(s):
    # 큐와 스택을 리스트로 정의
    qu = []
    st = []
    for x in s:
        if x.isalpha(): # 해당 문자가 알파벳이면(공백, 숫자, 특수문자가 아니면)
            # 큐와 스택에 각각 그 문자를 추가
            qu.append(x.lower())
            st.append(x.lower())
    while qu:
        if qu.pop(0) != st.pop():
            return False
    return True

print(palindrome("Wow"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I am Adam."))

def noquandstPalindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        print("s[i] :", s[i])
        print("s[j] :", s[j])
        print("---")
        if s[i].isalpha() == False:
            i += 1
        elif s[j].isalpha() == False:
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
    return True

print(noquandstPalindrome("Wow"))
print(noquandstPalindrome("Madam, I'm Adam."))
print(noquandstPalindrome("Madam, I am Adam."))