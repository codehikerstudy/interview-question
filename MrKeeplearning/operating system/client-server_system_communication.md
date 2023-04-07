Interprocess communication의 방법으로 살펴본 message passing system과 shared memory system은 프로세스 간 통신 뿐만 아니라 client-server system을 포함한 다른 시스템에서도 사용할 수가 있다.

한편, 이번 포스트를 통해서 살펴볼 방법들은 client-server system에서 주로 활용되는 프로세스 간 통신 방법이다.

클라이언트-서버 통신에는 클라이언트와 서버라는 두 구성요소가 포함되며 클라이언트는 서버에 요청을 보내고 서버는 클라이언트의 요청에 응답하는 형태를 띈다.

# 1. 소켓(Sockets)

<p align="center">
<img src="https://user-images.githubusercontent.com/27791880/229504965-37b839bb-7a7b-406a-8ab8-1ed8fc008b39.png">
</p>

소켓은 클라이언트-서버 시스템에서 통신을 위해서 사용되는 전략 중 하나로, 통신을 위한 endpoint로 정의된다. 따라서 네트워크를 통해서 통신하는 한 쌍의 프로세스나 시스템은 각각에 대해서 한 쌍의 소켓을 사용한다.

네트워크를 통해서 통신하는 것들이 오직 한 쌍의 프로세스만 있지는 않을 것이다. 따라서 특정 소켓을 찾아가 통신을 하기 위해서는 소켓을 구분할 수 있어야 하는데, 소켓은 포트번호와 연결된 IP주소를 통해서 식별이 가능하다.

소켓을 사용하는 프로세스들 간에 통신이 이루어질 때 서버 소켓은 특정 포트를 통해서 들어오는 클라이언트의 요청을 기다린다. 요청을 받으면 서버는 클라이언트 소켓에서 연결을 수락하여 연결을 완료한다.

그리고 서버는 well-known 포트로부터 오는 신호를 수신하기 위해서 telnet, ftp 그리고 http와 같은 프로토콜들이 내장되어 있다. 예를 들어 telnet 서버는 23번 포트를 사용하고, ftp 서버는 21번 포트를, 그리고 web 또는 http 서버는 80번 포트를 사용한다. 또한 1024번 이하의 모든 포트번호들은 well-known 포트로 취급된다. 따라서 이러한 포트들은 특정 서비스를 위해서 할당된 상태이기 때문에 클라이언트 프로세스나 또 다른 프로세스들에 할당될 수 없다.

## 1.1. 소켓을 이용한 통신 예시

<p align="center">
<img src="https://user-images.githubusercontent.com/27791880/229532999-34e12ac3-ed8c-42e1-9fa7-6a0d659d9a6e.png">
</p>

**host X**를 클라이언트로, **web server**를 서버로 생각해보자. 클라이언트는 서버 측에 무엇인가를 요청하고 싶고, 서버는 클라이언트가 요청한 정보를 전달해 줌으로써 해당 요청에 응답해야 한다. 둘 사이에 이러한 상호작용이 일어나려면 링크로 연결되어야 한다. 클라이언트와 서버 사이에 communication link를 설정하기 위해서 소켓의 개념을 사용한다.

클라이언트 프로세스가 연결 요청을 시작하면 호스트 컴퓨터(Host X)에서 포트를 할당한다. 위의 그림을 살펴보면 현재 host X의 ip주소는 `146.86.5.20`이고 뒤에 이어서 `1625`번의 포트가 따라오는 것을 확인할 수 있다.

마찬가지로 Web server도 IP 주소가 있고 소켓도 가지고 있다. 웹 서버 측의 소켓은 클라이언트 프로세스와 통신할 웹 서버의 프로세스에 속한다. 소켓의 IP 주소는 웹서버의 IP 주소와 동일하고 웹서버인 만큼 well-known 포트인 80번 포트를 사용하고 있다.

이렇게 클라이언트와 서버 측의 소켓이 준비된 상태에서 호스트 간에 이동하는 패킷은 목적지 포트 번호를 기반으로 적절한 프로세스에 전달된다.

만약 호스트 컴퓨터에서 또 다른 프로세스가 웹서버의 동일한 소켓의 80번 포트와 통신하고 싶다면 어떻게 해야할까? 해당 프로세스는 호스트 컴퓨터에서 또 다른 소켓을 할당받고 1024보다 큰 수 중 1625를 제외한 임의의 숫자를 포트넘버로 사용하게 된다. 그리고 해당 프로세스는 웹서버의 80번 포트에 연결된 소켓과 통신할 수 있게 된다.

# 2. 원격 프로시저 호출(Remote Procedure Calls, RPC)

<p align="center">
<img src="https://user-images.githubusercontent.com/27791880/230550840-cfe2a488-b122-4ea2-856f-14371c96ad6c.png" width="600">
</p>

원격 프로시저 호출(RPC)은 클라이언트-서버 기반의 분산 컴퓨팅 환경 프로그램을 구성할 때 도움이 되는 기술이다. RPC는 기존의 로컬 프로시저 호출을 확장한 것을 기반으로 하여, 호출된 프로시저가 호출하는 프로시저(caller)와 같은 주소 공간 안에 있을 필요가 없다. 즉, 쉽게 설명하자면 client process가 네트워크로 연결된 원격의 다른 프로세스에 접근해서 프로시저를 호출하여 사용하는 방법이라고 이해할 수 있다.

RPC를 통해서 통신하려는 2개의 프로세스가 있을 때 이 둘은 같은 시스템 내에 있을 수도, 혹은 네트워크로 연결된 서로 다른 시스템 내에 있을 수도 있다. 대표적인 예시로 최근 많이 사용되는 **MSA(Micro Service Architecture)** 를 생각해 볼 수 있다. MSA에서 각각의 서비스들은 서로 다른 환경을 가질 수 있고, RPC는 이들 사이에서 서비스에 사용되는 언어에 영향을 받지 않고 프로시저 호출을 가능하게 한다.

### 💡참고 사항

RPC는 제어 흐름([flow of control](https://ko.wikipedia.org/wiki/%EC%A0%9C%EC%96%B4_%ED%9D%90%EB%A6%84))이 caller와 callee 사이에 번갈아 발생하는 클라이언트-서버(e.g., 쿼리-응답) 상호 작용에서 특히 적합하다. 개념상으로 클라이언트와 서버는 동시에 실행되지 않지만, 실행 중인 스레드가 caller에서 callee로 점프한 뒤 되돌아온다.

## 2.1. RPC의 동작 방식

### 용어 정리1: Stub이란?

RPC의 동작 방식을 살펴보기 전에 먼저 Stub이 무엇인지 알아보자. 스텁은 클라이언트와 서버 간의 매개 변수와 같은 데이터를 각 머신에 맞게 변환해주는 코드 조각이다.

예를 들어, 스텁이 없는 상태에서 서버 측의 포인터가 클라이언트 측에서 전달 받은 매개 변수로 사용된다면 문제가 생길 것이다. 클라이언트와 서버는 서로 다른 메모리 공간을 점유하고 사용하고 있는 상태이기 때문에 클라이언트 측에서 사용된 포인터가 서버 측에서 사용된다면 같은 데이터를 가리키고 있지 않을 것이다.

또 다른 예시로, 클라이언트에서는 [리틀 엔디안 형식](http://www.tcpschool.com/c/c_refer_endian)을 사용하고 서버에서는 [빅 엔디안 형식](http://www.tcpschool.com/c/c_refer_endian)을 따른다고 했을 때, 전달 받은 데이터를 실행하는 과정에서 문제가 발생하게 된다.

이러한 문제들이 발생하는 것을 방지하기 위해서 클라이언트와 서버 측에서 전달되는 데이터들은 스텁을 거쳐 패킷(Packet) 형태로 상대측에 전달된다.

### 용어 정리2: RPC runtime이란?

아래에 나오는 이미지를 보면 하단에 **RPC runtime**이라고 적힌 박스를 확인할 수 있다. **RPC runtime**은 RPC 사용을 위해 네트워크 통신에 사용되는 함수와 루틴을 모아 놓은 라이브러리다. 주로 네트워크 간 주고 받은 패킷들을 관리하고 전송, 승인, 라우팅 및 암호화, 오류 처리 등 다양한 작업을 처리할 수 있다.

### RPC의 동작 과정

<p align="center">
<img src="https://user-images.githubusercontent.com/27791880/230564311-871b6a1f-f1c3-4cb1-8216-255c4ab6dcd9.png" width="600">
</p>

1. 클라이언트에서 클라이언트 스텁쪽으로 **client stub procedure**를 호출하기 위한 매개변수(parameter)를 전달한다. 이때, client stub은 클라이언트의 주소 공간 내에 있다.
2. 클라이언트 스텁에서 받은 매개변수들을 [marshalling](https://ko.wikipedia.org/wiki/%EB%A7%88%EC%83%AC%EB%A7%81_(%EC%BB%B4%ED%93%A8%ED%84%B0_%EA%B3%BC%ED%95%99))(pack)해서 서버 측에 전달하기 위한 패킷으로 변환한다.
3. 클라이언트 스텁에서 해당 패킷을 transport layer(RPC runtime)에 보내고, 여기서 다시 원격지의 서버(Server Machine)로 전달한다.
4. 서버 측 transport layer에서 패킷을 받고 서버 스텁에 전달해준다. 서버 스텁에서도 수신한 패킷에 대해 demarshalling(unpack) 작업을 수행해 서버에 맞게 패킷을 변환하고 서버 측에 클라이언트에서 요청한 프로시저 호출을 수행한다.
5. 서버 측의 프로시저가 모두 처리되면 처리 결과에 대한 반환값을 일반적인 프로시저 콜을 통해서 서버 스텁에 전달한다. 그리고 서버 스텁에서는 marshalling 작업업을 통해서 패킷으로 만들어 transport layer에 전달한다.
6. 서버 측 Transport layer(RPC runtime)에서 패킷을 클라이언트 측 transport layer에 전달하고 해당 패킷은 다시 클라이언트 스텁에 전달된다.
7. 클라이언트 스텁은 패킷에 대해서 demarshalling을 진행해서 파라미터 값과 실행 결과값을 추출하고 클라이언트는 해당 값들을 획득한다.

## 2.2. RPC의 장단점

1. RPC는 **추상화를 제공**한다. 즉, 네트워크 프로토콜과 같은 부분은 사용자에게 숨겨진다. 따라서 이러한 점은 개발자가 신경써야 되는 부분이 줄어들어 개발의 편의성을 높여줄 수 있다.
2. RPC는 종종 성능 향상을 위해서 많은 프로토콜 계층들을 생략하는데, 프로그램이 RPC를 자주 호출하는 경우 도움이 될 수 있다.
3. RPC를 사용하면 로컬 환경에서 뿐만 아니라 분산 환경에서도 응용 프로그램을 사용할 수 있다.

이외에도 RPC가 활용되는 MSA 환경에서도 쉽게 언어를 확장할 수 있고 코드를 재작성해야 하는 번거로움이 사라진다는 장점도 있다.

한편, 앞서 살펴본 client stub이나 server stub에서 처리가 불가능하거나 허용되지 않은 매개변수가 전달된 경우 RPC를 사용할 수 없는 상황이 생길 수 있다. 또한 네트워크를 통해 연결된 환경에서 네트워크가 갑자기 끊어졌을 때와 같이 네트워크 상황에 따라 프로시저 호출과 반환에 대한 시간이 보장되지 않는 단점도 있다.

# Reference.

* [tutorialspoint: Operating Systems Client/Server Communication](https://www.tutorialspoint.com/operating-systems-client-server-communication)
* [연세대학교 SWE3001 운영체제 강의자료](http://csys.yonsei.ac.kr/lect/os/o3-4.pdf)
* [geeks for geeks: RPC in Operating System](https://www.geeksforgeeks.org/remote-procedure-call-rpc-in-operating-system/)
* [Neso Academy: Processes | Chapter-3 | Operating](https://youtube.com/playlist?list=PLBlnK6fEyqRgKl0MbI6kbI5ffNt7BF8Fn)
* [Hackyboiz: RPC](https://hackyboiz.github.io/2021/10/22/poosic/rpc/)
* [위키백과: 메소드 스텁](https://ko.wikipedia.org/wiki/%EB%A9%94%EC%86%8C%EB%93%9C_%EC%8A%A4%ED%85%81)