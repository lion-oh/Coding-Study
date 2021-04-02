# Coding-Study Day 11
* Date: 2021.04.02 13:00 ~ 14:00
* Author: HR

## Type: hash(in python >>> dict type)
### Question1 ★★: 위장(x), 91.7/100 (test case #1 실패)  
- HR: 가능한 모든 조합을 구하여 count  
- 다르 풀이: 문제 접근을 다르게... 옷을 꼭 입어야 함 --> 옷이 없는 경우를 추가하여 조합을 구한다 --> 2^n - 1(모두 옷을 안 입고 있는 경우)  


### 
## 새롭게 알게된 사실
01. collections.Counter: 컨테이너에 동일한 값의 자료가 몇개인지를 파악. dict형태로 return해줌.  
- e.g. lst = ['a'. 'b', 'a'] --> Counter({'a': 2, 'b': 1})  
  
02. Default Dict: 인자로 주어진 객체의 기본값을 딕셔너리값의 초깃값으로 지정할 수 있음.  
- e.g. int_dict = defaultdict(int) --> int_dict['key1'] --> {'key': 0}  
- 처음 키를 지정할 때 값을 주지 않으면 해당 키에 대한 값을 디폴트 값으로 지정하겠다~~~  

03. eval: 매개변수로 받은 expression을 문자열로 받아서, 실행하는 함수임.  
- e.g. eval("1+2") --> 3  

04. np.prod: 배열 원소 간 곱 함수.  
- e.g. np.prod(array([1,2,3,4])) --> 1x2x3x4 --> 24  

### 
## 고민해볼것!
- 제시된 조건만 보려고 하지말고, 맥락은 같지만 다르게 해석하자 --> 문제 해결이 간단해질 수 있다...  

