"""
나만의 프롬프트 관리 프로그램 (Prompt Manager)
Python 3.10 이상 지원
"""

# 미리 정의된 카테고리 목록
CATEGORIES = [
    "텍스트 생성",
    "이미지 생성",
    "영상 생성",
    "페르소나",
    "자동화",
    "기타"
]

# 기본 프롬프트 데이터 (회의록 요약 스크립트 기반 구성)
prompts = [
    {
        "title": "고객 포털 개편 프로젝트 킥오프 회의록 요약",
        "content": """다음은 2025년 하반기 고객 포털 개편 프로젝트 킥오프 회의 관련 데이터입니다.

# 회의 기본 정보
MEETING_INFO = {
    "title": "2025년 하반기 고객 포털 개편 프로젝트 킥오프",
    "date": "2025년 7월 3일 (목) 오후 2시~3시 40분",
    "attendees": [
        "기획팀장",
        "개발파트장",
        "디자인팀 담당자",
        "QA팀 담당자",
        "마케팅팀 담당자",
        "외부 벤더사 담당자"
    ]
}

# 결정사항
DECISIONS = [
    "주간 회의는 매주 화요일 오전 10시로 고정",
    "리스크 관리 담당자로 개발파트장 지정",
    "다음 주 월요일(7/7)까지 각 팀별 세부 일정 초안 제출"
]

# Action Items
ACTION_ITEMS = [
    {"owner": "각 팀", "task": "세부 일정 초안 제출", "due": "7월 7일 (월)"},
    {"owner": "외부 벤더사", "task": "내부 일정 확정 내용 전달", "due": "다음 주"},
    {"owner": "외부 벤더사", "task": "API 명세서 제공", "due": "8월 중순"},
    {"owner": "디자인팀", "task": "모바일 UX 와이어프레임 초안 작성", "due": "8월 말 목표"},
    {"owner": "마케팅팀", "task": "SNS 채널 준비 시작", "due": "9월 중"}
]

# 리스크 및 미결사항
RISKS_AND_OPEN_ISSUES = [
    "경영진 희망 런칭일(10월 말) 대비 개발팀/디자인팀/QA팀 일정 빡빡함",
    "외부 벤더사 내부 일정 미확정으로 인한 전체 API 연동 테스트 일정 불확실성",
    "프로젝트 관련 예산이 아직 경영진 승인 대기 중임"
]

# 후속 일정
SCHEDULES = [
    "다음 주 월요일 (7/7): 각 팀 세부 일정 초안 제출",
    "매주 화요일 오전 10시: 정기 주간 회의",
    "8월 첫째 주 전: 디자인팀 모바일 UX 리서치 착수 예정",
    "8월 중순: 외부 벤더사 API 명세서 제공 예정",
    "9월 중: 마케팅팀 SNS 채널 준비 시작 예정",
    "10월 말: 경영진 희망 프로젝트 런칭 목표일"
]

# 확인 필요 사항
NEEDS_CHECK = [
    "최종 런칭 목표일: 경영진 희망일(10월 말)과 각 팀(개발, 디자인, QA) 필요 일정 간 간극 조정 필요",
    "외부 벤더사 일정: 벤더사 내부 일정 확정 여부 및 연동 테스트 정확한 소요 기간 확인 필요",
    "프로젝트 예산: 경영진 승인 완료 여부 및 최종 예산 규모 확인 필요",
    "QA 및 마케팅 상세 일정: 개발 완료 시점 및 런칭 3주 전 베타 유저 모집 캠페인 확정 일정 확인 필요"
]

위 데이터를 바탕으로 팀 공유용 요약 보고서를 깔끔하게 정리해줘.""",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "개편 포털 모바일 UX 컨셉 이미지 생성",
        "content": "2025년형 고객 포털 모바일 UI/UX 스마트폰 화면, 모던한 블루 톤 브랜드 컬러, 직관적이고 미니멀한 레이아웃, 스튜디오 조명, 8k 고화질 앱 mock-up",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "IT 프로젝트 리스크 관리 전문가 페르소나",
        "content": "당신은 15년 경력의 전문 IT PM입니다. 레거시 코드 문제 및 벤더사 API 연동 지연으로 10월 말 런칭 일정이 불확실할 때, 개발팀과 벤더사 간 리스크를 관리하고 일정을 조정하는 명확한 대응 가이드를 작성해주세요.",
        "category": "페르소나",
        "favorite": True
    },
    {
        "title": "주간 회의록 파이썬 요약 스크립트 자동 생성",
        "content": "print_meeting_minutes() 함수처럼 MEETING_INFO, DECISIONS, ACTION_ITEMS 데이터를 입력받아 마크다운 표 및 불렛 포인트 형태로 출력을 자동화하는 파이썬 코드를 작성해줘.",
        "category": "자동화",
        "favorite": False
    },
    {
        "title": "경영진 승인 요청용 프로젝트 예산 보고서 작성",
        "content": "고객 포털 개편 프로젝트의 예산 승인이 아직 대기 중인 상태입니다. 경영진을 설득하기 위해 10월 런칭 시 얻을 수 있는 기대효과(로그인 전환율 15% 개선 등)를 포함한 예산 승인 요청서를 작성해줘.",
        "category": "기타",
        "favorite": False
    },
    {
        "title": "시네마틱 모바일 포털 런칭 홍보 티저 영상",
        "content": "스마트폰 화면 속 고객 포털 앱이 유연하게 동작하는 시네마틱 3D 모션 그래픽, 세련된 트랜지션, 4k 60fps 시각 효과",
        "category": "영상 생성",
        "favorite": True
    }
]


def show_menu() -> None:
    """메인 메뉴를 출력합니다."""
    print("\n========================================")
    print("        나만의 프롬프트 관리")
    print("========================================")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")
    print("========================================")


def print_category_menu() -> None:
    """카테고리 선택 메뉴를 출력합니다."""
    print("\n카테고리 선택")
    for idx, category in enumerate(CATEGORIES, start=1):
        print(f"{idx}. {category}")


def add_prompt() -> None:
    """새로운 프롬프트를 추가합니다."""
    print("\n=== 프롬프트 추가 ===")
    
    # 제목 입력 (빈 문자열 방지)
    while True:
        title = input("제목: ").strip()
        if title:
            break
        print("제목을 입력해야 합니다. 다시 입력해주세요.")
        
    # 내용 입력 (빈 문자열 방지)
    while True:
        content = input("내용: ").strip()
        if content:
            break
        print("내용을 입력해야 합니다. 다시 입력해주세요.")
        
    # 카테고리 선택
    print_category_menu()
    while True:
        try:
            choice = int(input("\n선택: "))
            if 1 <= choice <= len(CATEGORIES):
                category = CATEGORIES[choice - 1]
                break
            else:
                print("잘못된 카테고리 번호입니다. 다시 선택해주세요.")
        except ValueError:
            print("숫자만 입력 가능합니다. 다시 선택해주세요.")

    # 프롬프트 추가 (favorite 기본값은 False)
    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }
    prompts.append(new_prompt)
    print(f"\n'{title}' 프롬프트가 성공적으로 추가되었습니다!")


def show_list() -> None:
    """모든 프롬프트 목록을 출력합니다."""
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("\n등록된 프롬프트가 없습니다.")
        return

    print()
    for idx, p in enumerate(prompts, start=1):
        fav_star = " ⭐" if p["favorite"] else ""
        print(f"{idx}. [{p['category']}] {p['title']}{fav_star}")

    print(f"\n총 {len(prompts)}개의 프롬프트")


def show_by_category() -> None:
    """카테고리별로 프롬프트를 조회합니다."""
    print("\n=== 카테고리별 조회 ===")
    print_category_menu()
    
    while True:
        try:
            choice = int(input("\n선택: "))
            if 1 <= choice <= len(CATEGORIES):
                selected_category = CATEGORIES[choice - 1]
                break
            else:
                print("잘못된 카테고리 번호입니다. 다시 선택해주세요.")
        except ValueError:
            print("숫자만 입력 가능합니다. 다시 선택해주세요.")

    print(f"\n[{selected_category}] 카테고리 프롬프트\n")
    
    # 해당 카테고리에 속하는 프롬프트 필터링
    filtered = [p for p in prompts if p["category"] == selected_category]
    
    if not filtered:
        print("해당 카테고리에 등록된 프롬프트가 없습니다.")
        return

    for idx, p in enumerate(filtered, start=1):
        fav_star = " ⭐" if p["favorite"] else ""
        print(f"{idx}. {p['title']}{fav_star}")

    print(f"\n총 {len(filtered)}개의 프롬프트")


def search_prompt() -> None:
    """제목 또는 내용에 검색어가 포함된 프롬프트를 검색합니다."""
    print("\n=== 프롬프트 검색 ===")
    keyword = input("검색어: ").strip()
    
    if not keyword:
        print("검색어를 입력하지 않았습니다.")
        return

    results = []
    # 제목 또는 내용에 검색어(대소문자 구분 없이) 포함 여부 확인
    for p in prompts:
        if keyword.lower() in p["title"].lower() or keyword.lower() in p["content"].lower():
            results.append(p)

    print("\n검색 결과:\n")
    if not results:
        print("검색 결과가 없습니다.")
        return

    for idx, p in enumerate(results, start=1):
        fav_star = " ⭐" if p["favorite"] else ""
        print(f"{idx}. [{p['category']}] {p['title']}{fav_star}")

    print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")


def show_detail() -> None:
    """선택한 프롬프트의 상세 정보를 출력합니다."""
    print("\n=== 프롬프트 상세 보기 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    try:
        index = int(input("번호 입력: "))
        if 1 <= index <= len(prompts):
            p = prompts[index - 1]
            fav_star = "⭐" if p["favorite"] else "❌"
            
            print("\n----------------------------------------")
            print(f"제목: {p['title']}")
            print(f"카테고리: {p['category']}")
            print(f"즐겨찾기: {fav_star}")
            print("----------------------------------------")
            print("내용:\n")
            print(p['content'])
            print("----------------------------------------")
        else:
            print("존재하지 않는 프롬프트 번호입니다.")
    except ValueError:
        print("숫자만 입력 가능합니다.")


def toggle_favorite() -> None:
    """프롬프트의 즐겨찾기 상태를 토글합니다."""
    print("\n=== 즐겨찾기 관리 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    try:
        index = int(input("프롬프트 번호 입력: "))
        if 1 <= index <= len(prompts):
            p = prompts[index - 1]
            # 즐겨찾기 상태 반전 (True <-> False)
            p["favorite"] = not p["favorite"]
            
            if p["favorite"]:
                print(f"\n'{p['title']}' 프롬프트를 즐겨찾기에 추가했습니다!")
            else:
                print(f"\n'{p['title']}' 프롬프트를 즐겨찾기에서 해제했습니다.")
        else:
            print("존재하지 않는 프롬프트 번호입니다.")
    except ValueError:
        print("숫자만 입력 가능합니다.")


def show_favorites() -> None:
    """즐겨찾기로 지정된 프롬프트 목록만 출력합니다."""
    print("\n=== 즐겨찾기 목록 ===")
    fav_list = [p for p in prompts if p["favorite"]]

    if not fav_list:
        print("\n즐겨찾기에 등록된 프롬프트가 없습니다.")
        return

    print()
    for idx, p in enumerate(fav_list, start=1):
        print(f"{idx}. [{p['category']}] {p['title']} ⭐")

    print(f"\n총 {len(fav_list)}개의 즐겨찾기")


def main() -> None:
    """프로그램 메인 루프를 실행합니다."""
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            toggle_favorite()
        elif choice == "7":
            show_favorites()
        elif choice == "0":
            print("\n프로그램을 종료합니다. 이용해주셔서 감사합니다!")
            break
        else:
            print("\n잘못된 메뉴 번호입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()