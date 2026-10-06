# 하나메일 바로가기 앱 아이콘 생성 스크립트 (간단한 봉투 아이콘)
from PIL import Image, ImageDraw

BG_COLOR = (0, 103, 71)      # 하나금융 그린 계열
ENVELOPE_COLOR = (255, 255, 255)
LINE_COLOR = (0, 103, 71)

def draw_icon(size):
    img = Image.new("RGB", (size, size), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # 봉투 사각형 영역 (아이콘 가운데, 여백 비율 적용)
    margin = size * 0.18
    left, top = margin, size * 0.28
    right, bottom = size - margin, size * 0.72
    draw.rectangle([left, top, right, bottom], fill=ENVELOPE_COLOR)

    # 봉투 접힘선 (삼각형 플랩)
    mid_x = size / 2
    draw.line([(left, top), (mid_x, size * 0.5)], fill=LINE_COLOR, width=max(2, size // 40))
    draw.line([(right, top), (mid_x, size * 0.5)], fill=LINE_COLOR, width=max(2, size // 40))

    return img

for size, name in [(192, "icon-192.png"), (512, "icon-512.png"), (180, "apple-touch-icon.png")]:
    icon = draw_icon(size)
    icon.save(f"icons/{name}")
    print(f"saved icons/{name}")
