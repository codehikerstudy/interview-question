# 동기화 (Synchronization)문제와 해결 방안

## 📌 동기화 (Synchronization)

동기화 (Synchronization): 다수의 프로세스 혹은 스레드를 동시에 실행해도 **공유 데이터의 일관성을 유지**하는 것

멀티 스레드는 하나의 프로세스에서의 공유된 자원을 사용하며 얻는 이점이 많다. 공유된 자원을 사용함으로써 메모리를 효율적으로 사용할 수 있고, 스레드 간 컨텍스트 스위칭이 가볍다는 장점이 있다. 하지만 이러한 이점과 동시에 동기화 작업을 해야 된다는 단점 또한 존재한다.
<br>
즉, **자원을 공유하며 공동으로 사용하기 때문에 공유 자원 접근 순서를 정하여 문제가 발생하지 않도록 해야 한다**는 것이다.
<br>

예를 들어 하나의 객체에 두 개의 스레드가 접근할 때, **스레드가 언제 컨텍스트 스위칭이 되었는지에 따라 결과가 달라질 수 있는 현상**이 발생할 수도 있는 것이다. 이를 **경쟁 조건(Race condition)** 이라고 한다. 우리는 동기화 해결 방안을 논하기 전에 먼저 경쟁 조건과 임계 영역에 대해 알아야 한다.

---

## 📌 경쟁 조건 (Race condition)과 임계 영역 (Critical section)

경쟁 조건 (Race condition): 여러 프로세스 혹은 스레드가 동시에 같은 데이터를 접근할 때 접근 순서에 따라 결과가 달라질 수 있는 상황
<br>

임계 영역(Critical section): 공유 데이터의 **일관성을 보장**하기 위해 하나의 프로세스 혹은 스레드만 진입해서 실행 가능한 영역. 즉, 두 개의 프로세스 혹은 스레드가 **동시에 진입해서는 안되는 영역**을 말한다.
<br>

임계 영역은 다음과 같이 이루어져 있다.

<center><img src="https://user-images.githubusercontent.com/84573261/223098308-dfca3203-9c9d-4d94-866a-ec912fdd36c3.png"></center>

<center><a href="https://velog.io/@tjswodud/%EA%B3%B5%EB%A3%A1%EC%B1%85-%EA%B0%95%EC%9D%98-%EB%82%B4%EC%9A%A9-%EC%A0%95%EB%A6%AC-6%EC%9E%A5.-Synchronization-Tools" title="critical section 출처">Critical section 사진 출처</a></center>
<br>

위의 사진을 보면 임계 영역을 지나기 전에 **entry section**이 보일 것이다. 이는 임계 영역에 진입하기 전에 임계 영역에 진입할 요건이 되는지를 확인하는 영역을 말한다. 그리고 임계 영역을 지난 뒤 **exit section**이 보이는데, 이는 임계 영역에서 작업이 끝난 뒤의 퇴출 구역이다. 마지막으로 **remainder section**은 나머지 구역들을 말한다.
<br>

임계 영역 문제는 **임계 구역으로 지정되어야 할 코드 영역이 임계 구역으로 지정되지 않았을 때 발생할 수 있는 문제**를 말한다. ([임계 영역 문제 정의 출처: 위키피디아](https://ko.wikipedia.org/wiki/%EC%9E%84%EA%B3%84_%EA%B5%AC%EC%97%AD_%EB%AC%B8%EC%A0%9C))
<br>
이러한 임계 영역 문제를 해결하기 위한 조건은 총 3가지로, 다음과 같이 상호 배제, 진행, 한정된 대기 조건을 **모두 충족**해야만 한다.

- 상호 배제 (mutual exclusion): **한 번에 하나의 프로세스 혹은 스레드만** 임계 영역에서 작업할 수 있다.

- 진행 (progress): **진행이 계속 될 수 있도록** 해야 한다. 즉, 어떤 프로세스 혹은 스레드가 임계 영역에 들어가길 원한다면 그 중 하나는 임계 영역에서 작업할 수 있도록 한다.

- 한정된 대기 (bounded waiting): 어떤 프로세스 혹은 스레드가 임계 영역을 들어가지 못하고 무한정 대기하고 있으면 안된다.
<br>

그렇다면, 어떻게 임계 영역 문제를 해결하기 위한 상호 배제 (mutual exclusion)를 보장할 수 있을까? 이는 바로 **락 (lcok)을 활용하는 것**이다!
<br>

<center><img src="https://user-images.githubusercontent.com/84573261/223101924-6f38cdf3-bf16-4233-bf35-44976dab833b.png"></center>

<center><a href="https://velog.io/@jxlhe46/OS-Ch6-2.-%EB%8F%99%EA%B8%B0%ED%99%94-%EB%8F%84%EA%B5%AC" title="lock 출처">Lock 사진 출처</a></center>
<br>

위의 사진을 보면 **acquire lock**이 보일 것이다.  프로세스 혹은 스레드는 acquire lock에서 lock을 획득하기 위해 경쟁을 하게 되고, 그 중에 성공한 프로세스 혹은 스레드만 임계 영역에 진입하여 실행하는 것이다.

이와 같이 lock을 얻기 위해 경합을 하는 방법으로 **스핀락 (Spinlock)과 뮤텍스 (Mutex)** 가 있다. 우선 스핀락에 대해 설명하고자 한다.

---

## 📌 스핀락 (Spinlock)

스핀락 (Spinlock): lock을 가질 수 있을 때까지 계속해서 반복하여 시도하는 방법
<br>

아래의 간단한 코드를 통해 스핀락의 동작 방식을 볼 수 있다.

```
volatile int lock = 0;  // global 변수

void critical() {
    while (test_and_set(&lock) == 1);
    ... critical section
    lock = 0;
}

int TestAndSet(int* lockPtr) {
    int oldLock = *lockPtr;
    *lockPtr = 1;
    return oldLock;
}
```
- test_and_set: 현재 lock이 획득 가능한 상태인지 확인하고, 가능한 경우 lock을 획득하는 함수


만약 thread 1과 thread 2가 있다고 가정하자. 우선 thread 1이 진입을 할 경우 현재 lock = 0이므로 while문에서 벗어날 것이다. **그리고 이와 함께 TestAndSet을 지나갔으므로 lock은 0에서 1로 변하게 될 것이다.**
<br>
그 다음 thread 1은 critical section에서 작업을 진행할 것이다. **그 다음 thread 2가 진입을 할 경우 이전에 lock = 1로 바뀌었으므로 while문에서 나오지 못하게 될 것이다**. 왜냐하면 thread 1이 critical section에서 작업을 마친 뒤에 lock = 0을 거쳐야 while문을 나올 수 있기 때문이다. **이렇게 lock을 가질 수 있을 때까지 계속해서 반복하여 시도하는 방법을 스핀락 (Spinlock)** 이라고 한다.
<br>

그러면 여기서 '멀티 코어 환경에서 thread 1과 thread 2가 **동시에** 진입하면 **동시에** 들어갈 수 있지 않을까?' 라고 생각할 수도 있다. 하지만 TestAndSet은 CPU atomic 명령어이기 때문에 동시에 들어갈 수가 없다. CPU atomic 명령어의 특징은 다음과 같다.

- 실행 중에 간섭받거나 중단되지 않는다.

    - 이 말은 thread 1이 TestAndSet을 진행하는 도중에 thread 2로 실행될 일이 없다는 뜻과 같다.

- 같은 메모리 영역에 대해 동시에 실행되지 않는다.

    - 결국 thread 1, thread2 둘 중 어떤 것이 먼저 실행될지는 모르지만, 동시에 실행될 일은 없다는 뜻이다.
<br>

결국 **CPU가 알아서 동기화 시켜준다**는 것이다. 하지만 스핀락의 치명적인 단점이 존재하는데, 이는 바로 다른 스레드가 작업을 진행함으로 인해 **lock을 얻기 위해 기다리는 동안 CPU를 낭비한다는 단점**이 있다. 쉽게 말해서 CPU의 효율이 좋지 않다는 것이다.
<br>

그래서 이를 해결하기 위해 나온 것이 뮤텍스 (Mutex)이다. 뮤텍스를 간단하게 말하자면 프로세스 혹은 스레드가 lock을 기다리는 동안 **계속해서 반복하여 시도하는 것이 아니라, lock을 얻기 전까지 멈춰 있는 것**을 말한다.

---

## 📌 뮤텍스 (Mutex)

뮤텍스 (Mutex): lock을 얻을 수 있을 때까지 기다리는 방법

아래의 간단한 코드를 통해 뮤텍스의 동작 방식을 볼 수 있다.

```
class Mutex {
    int value = 1;
    int guard = 0;
}

Mutex::lock() {
    while (test_and_set(&guard));
    if (value == 0) {
        ...현재 스레드를 큐에 넣음;
        guard = 0 & go to sleep
    }else {
        value = 0;
        guard = 0;
    }

Mutex::unlock() {
	while (test_and_set(&guard));
    if(큐에 하나라도 대기중인 경우) {
    	하나를 깨움
    } else {
    	value = 1;
    }
    guard = 0;
}

mutex -> lock();
..critical section
mutex -> unlock();
```

우선 class Mutex를 보자. 프로세스 혹은 스레드는 value를 취득해야 임계 영역에 진입이 가능하다. (value = 1) 그리고 guard는 value값을 안전하게 바꿔주기 위한 값이다. value는 여러 프로세스 혹은 스레드가 공유하는 데이터로, 여러 프로세스 혹은 스레드가 동시에 접근하면 race condition이 발생할 수도 있기 때문에 별도의 guard 변수가 필요하다. guard는 다음과 같이 작업이 진행된다.

1. value 값을 바꿔주는 작업을 하기 전에 guard를 얻기 위해 서로 다른 프로세스 혹은 스레드가 경합을 한다. 그리고 그 중 하나의 프로세스 혹은 스레드가 취득하게 되면 value 값을 바꿔주는 로직을 수행한다.

2. 작업이 끝난 뒤 guard = 0으로 바뀌게 된다.
<br>

그 다음 mutex -> lock()인 Mutex::lock()을 보자. 프로세스 혹은 스레드들은 mutex -> lock()에서 lcok을 갖기 위해 경쟁을 한다. 이 때 lock은 value 값에 의해 움직인다. 만약 value값을 누군가가 갖고 있다면 (if value == 0), 스레드는 자기 차례가 되기 전에 큐에 들어가서 기다린다. 만약 value값을 누군가가 갖고 있지 않다면 lock을 얻은 뒤 critical section에서 작업을 수행한다.
<br>

마지막으로 mutex -> unlock()과 Mutex::unlock()을 보자. 만약 큐에 대기중인 프로세스 혹은 스레드가 있을 경우 이를 변경해주고, 그것이 아니라면 value 값은 다시 1이 된다.
<br>

이렇게 lock을 가질 수 있을 때까지 대기하는 방법을 뮤텍스 (Mutex)라 하며, 뮤텍스의 핵심은 **큐에서 대기하기 때문에 CPU 낭비를 최소화 시킬 수 있다는 것**이다.
<br>

그렇다면 뮤텍스가 스핀락보다 무조건 좋을까? 이에 대한 답으로는 No이다.**멀티 코어 환경에서 임계 영역에서의 작업이 컨텍스트 스위칭보다 빨리 끝날 경우 스핀락이 뮤텍스보다 좋다.** 이유는 다음과 같다.
<br> 
우선 **뮤텍스의 경유 큐에서 대기하다가 임계 영역으로 진입하게 될 때 컨텍스트 스위칭이 발생**하게 된다. 하지만 스핀락의 경우 컨텍스트 스위칭 없이 lock을 가질 수 있을 때까지 계속 반복하기 때문에 스핀락이 더 좋다고 볼 수 있다.
<br>
그리고 '멀티 코어 환경에서'라는 전제가 붙은 이유는 **싱글 코어에서는 스핀락에서 컨텍스트 스위칭이 발생하기 때문**이다. (lock = 0인 상태의 프로세스가 lock을 얻게 된다면 다른 프로세스와 컨텍스트 스위칭이 발생하기 때문)

---

## 📌 세마포 (Semaphore)

세마포 (Semaphore): signal 메커니즘을 가진, 하나 이상의 프로세스 혹은 스레드가 임계 영역에 접근하도록 하는 장치

아래의 간단한 코드를 통해 세마포의 동작 방식을 볼 수 있다.

```
class Semaphore {
    int value = 1;  // value값이 0,1 뿐만 아니라 0,1,2..를 가질 수 있다.
    int guard = 0;
}

Semaphore::wait() {
    while (test_and_set(&guard));
    if (value == 0) {
        ...현재 스레드를 큐에 넣음;
        guard = 0 & go to sleep
    }else {
        value -= 1; // value 값 차감
        guard = 0;
    }

Semaphore::signal() {
	while (test_and_set(&guard));
    if(큐에 하나라도 대기중인 경우) {
    	하나를 깨움
    } else {
    	value += 1; // value 값 증감
    }
    guard = 0;
}

semaphore -> wait();
..critical section
semaphore -> signal();
```

위의 코드를 보면 뮤텍스와 확연하게 차이가 나는 부분이 있을 것이다. 이는 바로 value이다. 우선 class Semaphore를 보면 int value = 1이라고 되어 있는데, 이는 단순히 1 뿐만 아니라 0,1,2...값을 가질 수 있다. 이는 다음과 같이 분류된다.

- value = 1, 즉 0과 1로만 이루어진 세마포를 **이진 세마포**라고 한다.

- value가 1보다 더 많은 값을 갖는 세마포를 **카운팅 세마포**라고 한다.
<br>

그리고 뮤텍스와 다르게 value -= 1과 value += 1로 되어 있는 것을 볼 수 있을 것이다. 왜냐하면 세마포는 **프로세스 혹은 스레드가 하나 이상 들어갈 수 있도록 하기 위함**이다. 즉, 세마포는 뮤텍스와 같이 하나의 프로세스 혹은 스레드만 설정할 수 있고, **뮤텍스와 달리 여러 개의 프로세스 혹은 스레드를 설정**할 수 있다. 
<br>

세마포는 주로 순서를 정해줄 때 사용한다. 만약 멀티 코어 환경에서 thread 1과 thread 2가 있다고 가정해보자. 또한 코어 별 작업 순서는 다음과 같이 이루어져 있다고 가정해보자

- thread 1: task 1 작업을 수행한 뒤 semaphore -> signal();

- thread 2: task 2 작업을 수행한 뒤 semaphore -> wait();. 그 다음 task 3을 수행

이러한 경우, thread 1과 thread 2가 동시에 실행되든, thread 1이 먼저 수행되든, thread 2가 먼저 수행되든 thread 2의 task3은 thread 1의 taks 1 작업이 끝난 뒤에 진행될 수 있다. 즉, 순서가 보장된다는 것이다.
<br>

이전에 말했듯 세마포의 value가 단순히 1로 되어 있는 경우를 이진 세마포 (Binary semaphore)라 하였는데, 그렇다면 뮤텍스와 이진 세마포는 같다고 볼 수 있을까? 결과부터 말하자면, 뮤텍스와 이진 세마포는 같지 않다. 이유는 다음과 같다.

1. 뮤텍스는 lock을 가진 프로세스/스레드가 lock을 해제할수 있으며, 그렇기 때문에 **뮤텍스는 어떤 프로세스/스레드가 lock을 해제할지 예상**할 수 있다. 이와 달리 세마포는 wait()를 하는 프로세스/스레드가 signal()을 날리는 프로세스/스레드와 다를 수 있다.

2. **뮤텍스는 priority inheritance 속성을 갖지만**, 세마포는 갖고 있지 않다. 
<br>

priority inheritance는 다음과 같다. 만약 우선 순위가 높은 process 1과 우선 순위가 낮은 process 2가 있으며, process 2가 lock을 얻어 임계 영역에 진입하였다고 가정해보자.<br> 
여기서 process 1은 process 2보다 우선 순위가 높음에도 lock이 없기 때문에 작업을 할 수가 없다. 또한 process 2는 우선 순위가 낮기에 작업이 오래 걸릴 확률이 높다.
<br>
그래서 **CPU는 process 2의 우선 순위를 process 1만큼 높인다.** 그래서 스케줄러가 스케줄링을 할 때 process 2의 우선 순위가 process 1만큼 높다고 판단해 process 2를 먼저 실행시켜 임계 영역을 빨리 작업할 수 있도록 한다. 이를 priority inheritance라 한다. 이러한 priority inheritance 속성을 뮤텍스는 갖고 있으나, 세마포는 누가 signal을 날릴지 알 수 없기 때문에 priority inheritance 속성을 갖고 있지 않다.

---

### 👀 Reference
1. https://velog.io/@tjswodud/%EA%B3%B5%EB%A3%A1%EC%B1%85-%EA%B0%95%EC%9D%98-%EB%82%B4%EC%9A%A9-%EC%A0%95%EB%A6%AC-6%EC%9E%A5.-Synchronization-Tools

2. https://www.youtube.com/watch?v=gTkvX2Awj6g&ab_channel=%EC%89%AC%EC%9A%B4%EC%BD%94%EB%93%9C

3. https://velog.io/@ohju96/Multi-Process-Multi-Thread-%EB%8F%99%EA%B8%B0%ED%99%94-%ED%95%B4%EA%B2%B0

4. https://42place.innovationacademy.kr/archives/7120