<p align="center">
<img src="https://user-images.githubusercontent.com/27791880/229112647-bd073f00-ccf0-4e5b-85c1-a8a7d3d4070d.png" width="600">
</p>

<br/>
<br/>

지난 포스트에서 다루었던 communication link의 논리적 구현 방법 중 하나인 direct/indirect communication에 이어서 이번 포스트에서는 남은 synchronous/asynchronous communication과 automatic/explicit buffering을 다룬다. 그리고 2가지의 논리적 구현 방법은 각각 동기화에 대한 이슈와 버퍼링에 대한 이슈가 있다.

# 1. Synchronization

Message Passing System에서 프로세스 간 통신은 커널에 `send()`와 `receive()` 동작에 대한 호출을 통해서 이루어진다. 그리고 프로세스가 이러한 동작을 하려고 할 때 그 동작이 차단(block)된다면 사용하려는 리소스에 접근할 수 있게 되거나 I/O 작업이 완료되는 것과 같은 상태를 기다리는 것으로 간주하면 된다. 

즉, 현재의 스케줄 상황에 따라서 프로세스가 메시지를 수신하거나 송신하는 작업은 block될 수도 block되지 않을 수도 있다.

이처럼 Message passing은 blocking 타입과 non-blocking 타입으로 나누어서 볼 수 있고, 각각 synchronous(동기식) 통신과 asynchronous(비동기식) 통신으로 불리기도 한다.

## 1.1. 동기식 통신(synchronous communication) - Blocking type

* **Blocking send** : 송신 프로세스는 수신 프로세스나 메일박스에서 메시지를 받을 때까지 block되어 있다.
* **Blocking receive** : 수신 프로세스는 수신 메시지가 있을 때까지 block되어 있다.

즉, Blocking type은 다음 메시지를 처리할 수 있는 상태가 되기 전까지 block상태를 유지하는 것이기 때문에 sender와 receiver가 동기화된 상태라고 볼 수 있다.

## 1.2. 비동기식 통신(asynchronous communication) - Non-blocking type

* **Non-blocking send** : 송신 프로세스는 수신측에 메시지를 보내고 바로 return한다. 수신측의 수신 여부와 상관 없이 계속 자신의 작업을 수행한다.
* **Non-blocking receive** : 수신 프로세스는 유효한 메시지를 받거나 null을 받고 바로 return한다. 마찬가지로 어떤 메시지를 받았던 상관 없이 자신의 작업을 계속 수행한다.

즉, 현재의 `send` 또는 `receive` 동작이 상대측 동작에 영향을 받지 않는 상태로 서로 동기화된 상태를 유지하지 않는다.

# 2. Buffering

앞서 다루었던 바와 같이 메시지 전달 시스템에서 프로세스들이 서로 통신하려면 프로세스들 사이에 communication link가 설정되어야 한다고 했다. 그리고 프로세스 간의 통신이 direct이든 indirect이든 프로세스 간에 교환되는 메시지는 이 링크에 연관된 message queue(버퍼)에 저장되어 전송된다.

그리고 이 버퍼는 다음과 같이 3가지 방법으로 구현될 수 있다.

## Zero Capacity(무용량)

Buffer queue를 무용량으로 구현할 경우 큐의 최대 길이는 0이다. 즉, 링크에 버퍼가 없는 상태이다. 따라서 링크에는 대기 중인 메시지가 있을 수 없고, sender는 receiver가 준비되어 메시지를 직접 수신할 수 있을 때까지 기다려야 한다.

이것은 앞서 다룬 **Blocking send**와 유사한 상태이다. 만약 첫 번째 메시지가 보내진 상태에서 sender process가 block된 상태가 아니라면 두 번째 메시지를 보낼 것이다. 그리고 receiver process가 아직 첫 번째 메시지를 수신하지 못한 상태일 경우 두 번째 메시지는 queue에서 기다려야 한다. 하지만 zero capacity로 구현된 버퍼에서는 어떠한 것도 대기할 수 없다. 따라서, zero capacity로 구현된 버퍼에서 sender는 receiver가 앞서 보낸 메시지를 수신하기 전까지 block되어야 한다.

이러한 특징들 때문에 zero capacity는 **no buffering** 또는 **automatic buffering** 이라고 불리기도 한다.

## Bounded Capacity(유한용량)

유한 용량으로 구현된 Buffer queue는 최대 n개의 메시지가 담겨 있을 수 있다. 새 메시지를 보낼 때 큐가 가득 찬 상태가 아니라면 메시지가 큐에 들어가고 sender process는 기다림 없이 작업을 이어갈 수 있다. 하지만 버퍼의 용량은 유한한 상태이기 때문에 만약 링크의 buffer queue가 가득 찼다면 sender process는 기다려야 한다(block).

## Unbounded Capacity(무한용량)

Unbounded Capacity의 buffer queue는 무한한 길이의 버퍼를 가지고 있기 때문에 sender process가 보낸 메시지는 얼마든지 buffer queue에서 대기할 수 있다. 따라서 sender process는 block될 일이 없다.

# Reference.

* [Neso Academy: Processes | Chapter-3 | Operating System](https://youtube.com/playlist?list=PLBlnK6fEyqRgKl0MbI6kbI5ffNt7BF8Fn)
* [Notes for msc: Message Passing System](https://notesformsc.org/message-passing-system/)
* [geeks for geeks: Inter Process Communication](https://www.geeksforgeeks.org/inter-process-communication-ipc/)