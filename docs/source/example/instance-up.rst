COREMAX OPENSTACK 인스턴스 생성 가이드
=====================================

이 문서는 OpenStack Horizon 대시보드를 활용하여 이미지를 생성하고, 네트워크를 구성하며, 키 페어를 생성한 뒤 인스턴스를 배포하고 플로팅 IP를 부여하는 전체 과정을 다룹니다.

가이드
------------
이 가이드는 OpenStack Horizon을 사용하여 간단하고 효율적으로 인스턴스를 생성하는 과정을 안내합니다.


이미지 생성
~~~~~~~~~~~~

   - 프로젝트 > 컴퓨트 > 이미지 메뉴로 이동하여 이미지 생성 버튼 클릭.

   - 이름, 소스, 포맷, 공유 유형을 입력한 뒤 생성 버튼 클릭.

   - 이미지 상태가 Active로 변경되면 성공적으로 업로드된 것입니다.

네트워크 구성
~~~~~~~~~~~~

   - 프로젝트 > 네트워크 > 네트워크 메뉴로 이동하여 네트워크 생성 버튼 클릭.

   - 네트워크 이름과 서브넷 정보를 입력한 뒤 생성.

   - 프로젝트 > 네트워크 > 라우터 메뉴로 이동하여 라우터 생성 버튼 클릭.

   - 라우터 이름을 입력하고 생성된 라우터에 서브넷 연결.

   - 게이트웨이를 설정하여 외부 네트워크와 연결.

키 페어 생성
~~~~~~~~~~~~

   - 프로젝트 > 컴퓨트 > 키 페어 메뉴로 이동.

   - 키 페어 생성 버튼 클릭 후 이름 입력.

   - SSH 키 생성 옵션 선택 후 .pem 파일 다운로드 또는 기존 공개 키 업로드.

인스턴스 생성
~~~~~~~~~~~~

   - 프로젝트 > 컴퓨트 > 인스턴스 메뉴로 이동하여 인스턴스 생성 버튼 클릭.

   - 세부 정보를 입력: 이름, 이미지, Flavor, 네트워크, 보안 그룹, 키 페어.

   - 정보를 확인한 뒤 인스턴스 생성 버튼 클릭.

   - 인스턴스 상태가 Active로 변경되면 완료.

플로팅 IP 부여
~~~~~~~~~~~~

   - 프로젝트 > 네트워크 > 플로팅 IP 메뉴로 이동하여 플로팅 IP 할당 버튼 클릭.

   - 외부 네트워크 선택 후 IP 할당.

   - 컴퓨트 > 인스턴스 메뉴에서 대상 인스턴스의 액션 버튼 클릭.

   - Associate Floating IP를 선택하고 할당된 IP 연결.


추가 참고 사항
~~~~~~~~~~~~
- **보안 그룹**: SSH, HTTP 등 필요한 포트를 열어야 합니다.
- **모니터링**: Horizon 대시보드에서 생성된 인스턴스의 상태와 로그 확인.

관련 링크
----------
- OpenStack 공식 문서: <https://docs.openstack.org>

결론
-----
이 가이드는 OpenStack Horizon 대시보드에서 인스턴스를 생성하고 네트워크를 설정하는 방법을 간단하고 체계적으로 설명합니다. OpenStack의 유연한 리소스를 활용하여 사용자 경험을 최적화할 수 있습니다.
