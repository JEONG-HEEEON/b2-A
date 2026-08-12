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

# 기본 프롬프트 데이터 (최소 3개 이상, 서로 다른 카테고리)
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다.\n주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요.",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "제품 썸네일 이미지 생성",
        "content": "미니멀한 느낌의 IT 기기 3D 렌더링 스타일, 밝은 배경, 고화질 8k, 스튜디오 조명",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": "당신은 클라우드 및 AI 기술 전문 IT 컨설턴트입니다.\n비개발자도 이해하기 쉬운 용어로 기술 도입 전략을 설명해주세요.",
        "category": "페르소나",
        "favorite": False
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
            # 즐겨찾기 상태 반전
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