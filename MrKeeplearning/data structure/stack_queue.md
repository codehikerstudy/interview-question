+<figure align = "center">
<img src="https://user-images.githubusercontent.com/27791880/214284129-c552621d-93ee-4860-9334-dc3e3eb1ce3c.jpeg" width=400>
<figcaption><b>이미지 출처: twitter - Greg Kyte, CPA</b></figcaption>
</figure>

# 1. 개요

스택과 큐는 데이터 접근 방식을 설명하는 대표적인 자료구조이다. 데이터를 입력하고 출력하는 그 순서에 따라서 스택과 큐가 구분되고, 이러한 특징을 적재적소에 활용하여 많은 실제 시스템 또는 서비스 등에 적용하고 있다.

이번 글에서는 스택과 큐에 대한 개념과 실제 구현까지 다루어보려고 한다.

# 2. 스택

<figure align = "center">
<img src="https://user-images.githubusercontent.com/27791880/214289299-031b3bf5-b368-472b-a4c4-833991c56956.svg">
<figcaption><b>이미지 출처: Wikipedia - Stack</b></figcaption>
</figure>

스택을 설명하는 한 단어를 선택하라고 한다면 바로 **LIFO(Last In First Out)** 라고 할 수 있다.

스택은 같은 구조와 크기의 자료를 top이라고 정한 곳에서만 접근할 수 있는데, 스택에 자료가 삽입되면 이 자료는 스택의 마지막 자료이며 top은 이 마지막 자료를 가리킨다. 마찬가지로, 스택에서 자료를 삭제할 때는 top에서만 가능하기 때문에 top이 가리키는 스택의 마지막 자료만 삭제할 수 있다.

<figure align = "center">
<img src="https://user-images.githubusercontent.com/27791880/214294904-b6f584c2-31b2-4673-be5d-f6614e5b6e5d.svg" width=400>
<figcaption><b>이미지 출처: Wikipedia - Stack</b></figcaption>
</figure>

결과적으로 스택은 접근하는 순서에 따라서 데이터가 스택에 쌓이게 되고, 가장 마지막에 삽입된 데이터가 가장 먼저 삭제되는 후입선출(LIFO)의 구조를 갖는다.

스택에서 top으로 데이터를 삽입하는 연산을 **push**, top에서 데이터를 삭제하는 연산을 **pop**이라고 한다.

그리고, 개발자들이 가장 많이 사용하는 사이트의 이름으로도 존재하듯이 완전히 가득 찬 스택에 데이터를 추가로 삽입하려고 할 때는 **스택 오버플로우(stack overflow)** 가 발생한다.

## 2.1. 스택의 적용

### 역폴란드 표기법(RPN, reverse Polish notation)

후위 표기법이라고도 불리는 역폴란드 표기법은 연산자를 연산 대상의 뒤에 쓰는 연산 표기법이다. 예를 들어 `1 + 2`가 일반적인 중위 표기법이라면, RPN으로 작성했을 때 `1 2 + `가 된다.

RPN으로 수식을 작성한다면 앞에서부터 읽어나가면서 스택에 저장하면 되기 때문에 컴퓨터 친화적인 표기법이다. 예를 들어 `(3 + 5) * 4`를 RPN으로 표기한다면 `3 5 + 4 *`이 되는데 이것의 연산 과정은 다음과 같다.

1. 숫자 `3`이 스택에 담긴다.
2. 숫자 `5`가 스택에 담긴다.
3. `+`가 입력되면 스택에서 두 수를 꺼내고 더한 뒤 그 결과(`8`)를 스택에 담는다.
4. 숫자 `4`가 스택에 담긴다.
5. `8`과 `4`를 스택에서 꺼내어 곱한 뒤 그 결과(`32`)를 스택에 담는다.




# 3. 스택 구현

스택을 구현하는 방법으로 array와 linked list를 사용하는 방법 2가지를 생각할 수 있다.


<br/>
<br/>

# References

* [Greg Kyte, CPA - twitter](https://twitter.com/gregkyte/status/1012088894886572032)
* [Wikipedia - 스택](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))
* [Wikipedia - 큐](https://ko.wikipedia.org/wiki/%ED%81%90_(%EC%9E%90%EB%A3%8C_%EA%B5%AC%EC%A1%B0))
* [Wikipedia - 역폴란드 표기법](https://ko.wikipedia.org/wiki/%EC%97%AD%ED%8F%B4%EB%9E%80%EB%93%9C_%ED%91%9C%EA%B8%B0%EB%B2%95)
