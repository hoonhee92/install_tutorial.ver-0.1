COREMAXTECH. OpenStack 통합 가이드 페이지
================================================

COREMAXTECH OpenStack 솔루션은 현대 IT 환경의 요구를 충족시키기 위해 설계된 통합 클라우드 플랫폼입니다.  

Ceph 스토리지와 통합되어 컴퓨팅, 네트워킹, 스토리지, 모니터링 등 모든 클라우드 인프라를 안전하고 효율적으로 관리할 수 있습니다.  

OpenStack과 전문 플러그인을 통해 강력한 클라우드 환경을 구축하고 비즈니스 민첩성을 극대화할 수 있습니다.

.. note::
   이 문서는 현재 개발 중인 프로젝트에 대한 가이드입니다.


제품특징
--------

1. **고성능 인프라와 멀티노드 아키텍처**

- 멀티노드 구성: 컨트롤러, 컴퓨팅, 스토리지 노드로 분리된 구조로 안정성과 성능을 최적화
- Ceph 통합: Cinder와 Manila를 통한 블록 및 파일 스토리지 지원  
- Nova 최적화: 다양한 하이퍼바이저(KVM, VMware)와의 호환성 제공 


2. **통합 관리 및 자동화**

- Horizon 대시보드: 직관적인 UI로 OpenStack 서비스 통합 관리  
- Prometheus 및 Grafana 모니터링: 실시간 클러스터 및 네트워크 상태 모니터링
- 자동화 스케줄링: 자원 배치 및 네트워크 설정 자동화  


3. **보안 및 장애 복구** 

- Keystone 인증: 세분화된 접근 제어 제공  
- TLS 암호화: HAProxy와 Octavia 기반 보안 강화  
- Masakari 복구: 장애 발생 시 자동 복구로 서비스 연속성 보장


4. **유연한 확장성과 사용자 편의성**

- 스케일 아웃: 노드 추가를 통해 확장 용이  
- 한글화 지원: 사용자 접근성을 고려한 UI 제공  

도입효과
--------

1. **안정적이고 확장 가능한 인프라 구축**

- 멀티노드 아키텍처로 서비스 연속성과 성능 보장
- Ceph 스토리지로 데이터 안전성과 비용 절감

2. **운영 효율 극대화**

- Horizon 대시보드와 자동화된 자원 배치로 관리 간소화

3. **보안 및 장애 대응 강화**

- Keystone 인증 및 Masakari 자동 복구

4. **비용 절감**

- 오픈소스 기반으로 라이선스 비용 최소화

5. **유연한 확장과 미래 대비**

- Kubernetes 통합으로 클라우드 네이티브 워크로드 지원


목차
--------

.. toctree::
   :caption: COREMAX OPENSTACK
   :maxdepth: 2

   개요 <intro/intro>

--------

.. toctree::
   :caption: 설치 가이드
   :maxdepth: 2

   설치 <install/install-openstack>

--------

.. toctree::
   :caption: 운영 가이드
   :maxdepth: 2

   운영 <operation/operation-openstack>

--------

.. toctree::
   :caption: 릴리즈
   :maxdepth: 2

   ver 1.0.1 <release/1.0.1>



연락처
--------

**회사명**

- CoreMax Technology Co. Ltd.

**주소**

- 서울특별시 금천구 가산디지털1로 2, 207 (가산동, 우림라이온스밸리 2차)

**전화**

- 02-6672-4350

**이메일**

- hhpark@coremaxtech.com
