<p align="center"><img src="https://user-images.githubusercontent.com/27791880/212748133-a66bffd4-039b-4784-8686-fc525bfd6eb7.svg" width=500></p>

<br/>

# 1. 해시 테이블

해시테이블은 해시맵이라고도 불리며, Key와 Value라는 두 가지 값을 함께 맵핑하여 데이터를 저장하는 자료구조이다. 이미 각 언어들은 내부적으로 해시테이블의 기능을 제공하고 있고 대표적으로 Python에는 딕셔너리가, Java에는 Map 컬렉션을 통해서 해당 기능을 제공하고 있다.

해시 테이블은 Key를 임의의 해시 함수에 입력하여 출력된 해시 값을 데이터가 저장되는 배열의 인덱스로 활용한다. 따라서, 특정 value에 접근하려 할 때 key를 통해서 해당 value에 바로 접근하는 것이 가능하기 때문에 $O(1)$의 시간복잡도를 가진다.

보통 배열로 미리 hash table의 크기만큼 공간을 만들어두고 사용하지만, 해시 테이블에서는 충돌이라는 이벤트가 자주 발생한다. 이 충돌을 가장 간단하면서도 일반적으로 해결하는 방법은 공간을 늘리는 방법이고, 따라서 해시 테이블은 공간과 시간을 맞바꾸는 자료구조이다. 공간을 늘리게 될 경우 충돌이 일어날 확률은 줄어들지만, 공간 활용의 낭비가 발생한다. 앞서 말했듯 해시 테이블은 해시를 인덱스로 활용하고 있지만, 해시가 순서를 갖추어 생성되는 것이 아니기 때문에 데이터를 저장하는 과정에서 무수히 많은 빈공간이 생기게 된다.

해시 테이블에서는 각 배열의 원소를 **버킷(Bucket)** 이라고 칭한다. 그리고 이 버킷의 수는 최초 해시 테이블 생성 시 고정되어 있는데, 이 때문에 충돌이 발생하게 된다. 따라서 뒤에서 다룰 충돌에 대한 해결방법 중 하나인 **Chaining**에서는 **슬롯(Slot)** 을 버킷에 추가하여 공간을 추가로 확보하게 된다. **슬롯**은 하나의 데이터를 저장할 수 있는 공간이라고 할 수 있고, 하나의 버킷에는 다수의 슬롯이 추가될 수 있다.

# 2. 해시 함수

해시 함수는 입력으로 받은 key에 대해서 특정한 연산을 거쳐 고정된 길이로 변환된 해시(해시 테이블의 주소·인덱스의 역할을 한다)를 제공한다. 해시 함수에 들어가는 산술연산에는 다양한 방법이 있고, 이 중에서도 가장 간단한 방법으로는 나누기를 통한 나머지 값을 활용(모듈로 연산)하는 방법이 있다.

해시 함수를 거친다고 해서 고유한 해시값을 얻을 수 있는 것은 아니다. 서로 다른 key를 가지더라도 해시함수를 거쳤을 때 나오는 해시 값은 동일할 수 있다.

정말 간단하게 key를 5로 나눈 나머지를 해시로 사용하는 해시함수가 있다고 가정해보자. Key로 13과 18이 주어졌다면 둘 다 나머지로 3을 반환하기 때문에 동일한 해시를 가지게 된다.

# 3. 해시 함수에서의 충돌

[생일문제(Birthday problem)](https://ko.wikipedia.org/wiki/%EC%83%9D%EC%9D%BC_%EB%AC%B8%EC%A0%9C)에서도 알 수 있다시피 생각보다 충돌은 빈번하게 발생한다. 특히나 $O(1)$의 시간 복잡도를 기대하고 사용하는 해시 테이블에서 충돌이 자주 발생하게 되면 이것은 해시테이블의 존재를 무색하게 만든다.

그래서 해시테이블에서의 충돌을 해결할 수 있는 방법은 크게 Open hashing과 Closed hashing이 존재한다.

## 3.1. Open hashing (a.k.a. Seperate chaining)

<p align="center"><img src="https://user-images.githubusercontent.com/27791880/212811568-f071350e-69e7-4def-a0e6-ce4f9eb1ddf6.png" width=400></p>

| **이미지 출처**: Data Structure Lecture#22: Searching 3(Chapter 9) U Kang Seoul National University

Open hashing은 개별 체이닝(Seperate chaining)이라고 불리기도 하며, 이름처럼 해시 테이블에 기본 할당된 공간 바깥에서 충돌을 처리하는 기법이다. 충돌이 발생하면 링크드 리스트 자료구조를 활용해서 기존 동일한 해시에 저장되어 있던 데이터에 이어서 데이터를 추가로 저장한다.

기본 생성된 해시 테이블 외의 공간에 충돌이 발생하는 데이터를 저장하기 때문에 기존에 생성된 공간이 낭비되는 문제가 발생할 수도 있다.

## 3.2. Closed hashing (a.k.a. Open addressing)

Closed hashing은 Open addressing이라고 불리기도 하며, 이름처럼 해시 테이블 내부의 다른 슬롯에서 충돌을 처리하는 기법이다. 이 기법은 세부적으로 Bucket Hashing과 Linear Probing(선형탐사) 방식으로 나누어 볼 수 있다.

### Closed hashing - Bucket Hashing

<p align="center"><img src="https://user-images.githubusercontent.com/27791880/212812233-4b327198-7452-41dc-accd-628bc8e7569c.png" width=250></p>

| **이미지 출처**: Data Structure Lecture#22: Searching 3(Chapter 9) U Kang Seoul National University

버킷 해싱 또한 2가지 방식으로 나누어서 볼 수 있다.

먼저 위의 그림과 같은 경우 N개의 슬롯을 M개의 버킷으로 그룹화했다. 기본적으로 해시함수를 통해 나온 해시를 버킷의 첫 번째 슬롯에 할당한다. 만약 첫 번째 슬롯에 이미 값이 할당되어 있다면 같은 버킷 내에 존재하는 다음 슬롯을 확인한다. 만약 버킷 내에서 모든 슬롯에 값이 할당되어 있다면 Overflow 버킷에 값을 저장한다.

<p align="center"><img src="https://user-images.githubusercontent.com/27791880/212824878-38a36e7d-3ef1-44fe-b6f4-a2bfb210025d.png" width=250></p>

| **이미지 출처**: Data Structure Lecture#22: Searching 3(Chapter 9) U Kang Seoul National University

버킷 해싱의 두번째 방식은 첫 번째 방식과 달리 슬롯을 따로 버킷으로 그룹화하지 않는다. 만약 슬롯이 비어있다면 해당 위치에 데이터를 삽입하고, 비어있지 않다면 다음 슬롯으로 이동하며 빈 슬롯을 탐색한다. 마지막 슬롯까지 탐색을 했음에도 빈 슬롯이 없다면, Overflow 버킷에 삽입한다.

**그룹화가 되어 있지 않다면 슬롯을 순회하면서 빈 공간을 계속 탐색하면 굳이 Overflow 버킷까지 안가도 되지 않을까?**

Hashtable에서는 해시함수를 통해서 할당받은 해시를 시작점으로 해시테이블의 끝까지 이동하면서 빈 공간을 탐색한다. 따라서, 만약 위의 그림을 참고했을 때, 해시가 8인 슬롯이 채워진 상태이고 내 현재 해시가 6이라면 빈 슬롯을 못찾는 상황이 발생하고 Overflow 버킷에 데이터를 삽입하게 된다.

### Bucket Hashing과 Open hashing

버킷 해싱은 오픈 해싱보다 충돌이 더 잦기 때문에 특정 아이템을 탐색하기까지 더 많은 시간이 소요된다. 충돌이 잦다는 것은 그만큼 해시테이블에 빈슬롯이 적다는 것으로 해석할 수도 있다. 따라서, 버킷 해싱은 오픈 해싱에 비해서 적은 공간을 사용한다.

하지만, 첫 번째 버킷해싱처럼 슬롯이 그룹화가 된 경우, 특정 해시를 가지는 버킷이 가득 찬 상태이고 해당 해시에 대해서 계속해서 충돌이 일어난다면 다른 빈 슬롯이 많은 상태일지라도 계속해서 Overflow 버킷에 데이터를 삽입하기 때문에 공간 낭비가 있을 수 있다.

### Closed hashing - Linear Probing(선형 탐사)

<p align="center"><img src="https://user-images.githubusercontent.com/27791880/212832969-dda862ed-08e7-45ee-b081-36b196c47204.svg"></p>

| **이미지 출처**: Wikipedia - Linear probing

선형 탐사 방식은 버킷 해싱의 두번째 방식에서 Overflow 버킷을 사용하지 않는 방식이라고 생각해도 좋다.

역시나 Closed hashing 기법 중 하나이기 때문에 주어진 저장공간 내에서 충돌 문제를 해결한다. 특정 해시에서 충돌이 발생하면 다음 해시(주소)의 슬롯을 탐색하여 가장 먼저 등장하는 빈 슬롯에 데이터를 저장하는 기법이다.

위의 이미지에서는 John Smith와 Sandra Dee가 동일하게 873이라는 해시를 가지고 따라서 Sandra Dee를 비어있는 다음 해시인 874를 주소로 가지는 슬롯에 데이터를 저장해서 충돌을 해결했다.

이러한 선형 탐사 방식의 문제점은 특정 위치에 데이터들이 뭉치는 클러스터링 현상이 발생한다는 점이다. 데이터가 해시 테이블 전역에 고르게 분포하지 못하고 이러한 클러스터의 규모가 커질수록 Probing 속도는 저하되고 해싱 효율도 떨어진다.

<br/>
<br/>

**Ref.**
* [Wikipedia - Hash table](https://en.wikipedia.org/wiki/Hash_table)
* [Data Structure Lecture#22: Searching 3(Chapter 9) U Kang Seoul National University](https://ocw.snu.ac.kr/sites/default/files/NOTE/Data%20Structures%20(21).pdf)
* [파이썬 알고리즘 인터뷰](https://product.kyobobook.co.kr/detail/S000001932748)