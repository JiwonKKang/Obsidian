
>[!faq] Immersion.gg
>Riot API를 활용한 전적검색 및 승률 분석 플랫폼

## 개발 배경 및 목적

<img width="500" alt="개발목적" src="https://github.com/JiwonKKang/Immersion.gg-Back/assets/128073698/7967ce14-093a-46b8-97be-ac91fd5c5c86">

## 개발 도구

- 프론트 : React
- 백엔드 : Spring, Redis, Kafka, Docker
- 클라우드 : Azure VM, Azure Database for MySQL
- CI/CD : Git Actions, Docker Compose
- 협업 도구 : Azure DevOps

## 인프라 구성

![인프라 구성도 2|500](https://github.com/JiwonKKang/Immersion.gg-Back/assets/128073698/d352e476-6c50-465b-aeb6-83a46f4c44ce)

- 리액트로 프론트 구성
- GPTAnalyzer 서비스와 Kafka를 이용한 비동기 통신
- Riot CDN 이미지 정보 Redis 캐싱
- 리버스 프록시 서버로 Nginx 구성


## 프로젝트 소개

> 메인화면
<img width="500" alt="메인 화면" src="https://github.com/JiwonKKang/Immersion.gg-Back/assets/128073698/cab47e7a-9ae8-42d7-9d5c-eb788c4bde84">

---

> 소환사 상세 화면
<img width="500" alt="소환사 상세화면" src="https://github.com/JiwonKKang/Immersion.gg-Back/assets/128073698/39f28688-b60f-49eb-8911-047b8392fafc">

---

> 게임 상세 정보 
<img width="500" alt="상세화면 상세" src="https://github.com/JiwonKKang/Immersion.gg-Back/assets/128073698/a2df2143-adbe-4451-b20a-d2f74a126448">

---

> 승률 분석 화면
<img width="500" alt="승률 분석 화면" src="https://github.com/JiwonKKang/Immersion.gg-Back/assets/128073698/63eef321-58f7-4659-90c4-7ab18b09935e">

---

> GPT 승률 통계 분석
<img width="500" alt="GPT 분석" src="https://github.com/JiwonKKang/Immersion.gg-Back/assets/128073698/a2ffeb5a-5ea7-44e5-a9ff-3aeab4b8f885">

---

> 인게임 정보 화면
<img width="500" alt="인게임 화면" src="https://github.com/JiwonKKang/Immersion.gg-Back/assets/128073698/4828f959-5b0b-4175-a88f-c689f573bedb">


## 프로젝트하면서 부딪힌 문제상황들

- 매치 정보 가져올때 참여자 10명정보를 쿼리를 한개씩 또 날리는 N + 1 문제 발생  
   => JPA Batch Size를 이용해 IN 쿼리로 한방 쿼리를 날려 성능 크게 향상
- RIOT API에서 가져온 소환사의 매치 정보들을 한개씩 insert 쿼리가 날라가서 50개 매치정보 가져오는데 30초 소요  
   => batch insert를 통해 한방 insert 쿼리를 날려 성능 향상 30초 -> 10초
- RIOT CDN의 이미지 정보를 매번 API를 통해 받아서 성능 이슈 발생  
   => 최초 한번만 API를 통해 가져오고 이후 Redis 캐싱을 통해 성능 향상
- 클라이언트가 Kafka 메세지 브로커를 찾지 못하는 이슈 발생  
   => 도커 브리지 네트워크를 만들어서 해결
- CI/CD 배포 파이프라인을 만들면서 Docker 로그인 과정에서 권한 이슈 발생  
   => sudo chmod 666 /var/run/docker.sock 을 통해 해결
- 배포완료 과정에서 서비스를 내렸다가 다시 올릴때 nginx가 다시 올라온 서비스를 못찾는 이슈 발생  
   => 배포 완료과정에 docker compose stop nginx 추가 및 nginx에 서비스 의존성 추가
- JPA에서 save를 할때 이미 Key값이 있는경우에는 persist가 아니라 merge를 하기때문에 쓸데없는 select 쿼리 발생  
   => Persistable 상속하여 isNew 오버라이딩


