

> [!faq] Kafka란?
> 대규모 이벤트/데이터 스트리밍 플랫폼이다.

![[Pasted image 20240222171245.png]]

먼저 카프카를 사용하기 위해 알아야하는 개념들로는

- Producer
- Consumer
- Topic
- Broker
- Partition
- Zookeeper
- Replication Factor
- In-sync Replica

등이 있다. Kafka를 최소한으로 활용하기위해서 최소한 이것들의 개념정도는 알아야한다.

## Producer

- Kafka Cluster 내 Topic이 포함된 Kafka Broker에 메세지를 `발행`하는 "주체"

## Consumer

- Kafka Cluster 내 Topic이 포함된 Kafka Broker에 메세지를 `소비`하는 "주체"
- Consumer Group : 메세지를 소비하는 "주체 집단"

## Zookeeper

- 분산 처리 시스템에서 분산 처리를 위한 코디네이터
	- 누가 리더인지, 어느 상황인지, 동기화 상태 등을 관리
- Kafka Cluster를 관리
- Kafka Broker의 상태를 관리하고 Cluster내에 포함된 Topic들을 관리하며 등록된 Consumer 정보를 관리하는 "주체"

즉, Kafka Cluster의 메타데이터를 관리하는 주체

## Topic

> [!quote] 고가용성, 고성능을 구현하는 핵심 개념

- 메시지를 발행하고 소비할 수 있는 "객체"

Kafka Topic에는 수많은 설정값들이 존재하고 이 설정값들에 따라서 성능, 가용성에 엄청난 차이를 불러 일으킨다.

### Partition

먼저, Topic는 1개 이상의 Partition으로 이루어진다.

Partition 이란, 하나의 토픽에 포함된 메세지들을 물리적으로 분리하여 저장하는 저장소

> [!fail] Not Sharding, Partitioning!!

위의 말대로 하나의 메세지를 분리해서 저장하는것이 아니라, 하나의 메세지가 하나의 파티션에 들어가는 형태

기본적으로 파티션이 많으면 성능이 향상, 성능에 직결되는 요소

- 하나의 파티션은 하나의 Broker에 소속되어있다.
- 하나의 카프카 브로커는 1개 이상의 파티션을 가지고있다.

파티션의 개수가 많다고해서 카프카 브로커의 갯구가 많은것을 의미하지는 않는다.
즉, 파티션의 갯수가 절대적인 성능의 결정 요소가 아님


### Replication Factor

Replication Factor은 가용성을 위한 개념

하나의 파티션은 카프카 클러스터 내에 1개 이상의 Replica를 가질 수 있고,
RF(Replication Factor) 는 이 복제본의 갯수를 의미해요.

즉, RF가 1이상의 수치를 가져야만 고가용성을 달성할 수 있다.
- 일반적으로 클수록, 가용성이 높다
- 하지만, 브로커의 갯수가 충분할  때 한정

하지만, 너무 클 경우 저장 공간을 낭비할 수 있고, 메세지를 발행할 때 지연시간이 길어질 수있다.

### In-sync Replica(ISR)

파티션의 복제본이 많아질수록, 즉 RF가 커질수록 메세지를 Produce할 때 지연시간이 길어진다.
하지만 그럼에도 지연시간을 짧게 유지하고싶다면?

그래서 나온게 ISR 그룹이다. 
ISR 그룹이란 하나의 파티션에 대한 Replica들이 동기화된 그룹을 의미한다.

이게 무슨 말이냐면, 프로듀서가 메세지를 발행할 때 파티션의 RF만큼 메세지를 복제하게 될텐데
이 메세지 복제의 정상적인 완료를 판단하는 기준이다.

- ISR그룹에 많은 파티션을 포함하면 신뢰성/가용성은 향상되지만, 지연시간 증가
- ISR그룹에 적은 파티션을 포함하면 신뢰성/가용성은 하락하지만, 지연시간 감소

적절하게 토픽에 Produce되었다 -> 토픽 내 파티션의 모든 ISR 그룹에 복제 되었다.


