Interprocess communication의 방법으로 살펴본 message passing system과 shared memory system은 프로세스 간 통신 뿐만 아니라 client-server system을 포함한 다른 시스템에서도 사용할 수가 있다.

한편, 이번 포스트를 통해서 살펴볼 방법들은 client-server system에서만 활용할 수 있는 프로세스 간 통신 방법이다.

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

# 2. Remote Procedure Calls(RPC)

<p align="center">
<img src="https://user-images.githubusercontent.com/27791880/229567310-934c9f2b-70dd-4c5e-9541-40132d5ed821.png">
</p>

RPC는 네트워크를 통해 연결된 다른 시스템에 상주하는 프로세스와 서로 통신하기를 원할 때 활용된다.

RPC는 네트워크에 연결되어 있는 시스템의 프로세스들 간에 [procedure calls](https://ko.wikipedia.org/wiki/%ED%95%A8%EC%88%98_(%EC%BB%B4%ED%93%A8%ED%84%B0_%EA%B3%BC%ED%95%99))을 추상화한 것으로 한 프로그램이 네트워크의 세부 사항을 이해하지 않고도 네트워크의 다른 컴퓨터에 있는 프로그램에서 서비스를 요청하는 데 사용할 수 있는 프로세스 간 통신 기술이다.

RPC는 IPC를 기반으로 구현되었기 때문에 IPC 메커니즘과 많은 면에서 유사하다. 그러나, 프로세스가 별도의 시스템에서 실행되는 환경을 다루고 있기 때문에 RPC의 원격 서비스를 제공할 때 **메시지 기반 통신 방식**을 사용해야 한다. 따라서 IPC의 통신 방식 중 Message passing system을 사용해야 한다.

RPC는 IPC의 Message passing system을 활용하게 되는데, IPC와 RPC는 무슨 차이가 있을까?

IPC와 달리 RPC 통신으로 교환되는 메시지는 잘 구성되어 있기(well structured) 때문에 더 이상 단순한 데이터 패킷이 아니다. 한편, IPC의 경우 메시지 전달 시스템으로 전달되는 메시지는 단지 데이터 패킷일 뿐이다.

# Reference.

* [tutorialspoint: Operating Systems Client/Server Communication](https://www.tutorialspoint.com/operating-systems-client-server-communication)
* [연세대학교 SWE3001 운영체제 강의자료](http://csys.yonsei.ac.kr/lect/os/o3-4.pdf)