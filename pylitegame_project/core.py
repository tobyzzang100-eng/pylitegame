import pygame


class Game:
    """
    pylitegame의 메인 클래스.
    pygame를 더 쉽게 쓰기 위한 가벼운 래퍼입니다.
    """

    def __init__(self):
        pygame.init()
        self.surface = None
        self.bg_color = (255, 255, 255)
        self.clock = pygame.time.Clock()
        self._running = False

    # ── 색깔 처리 ──────────────────────────────────────────────
    def _parse_color(self, color):
        """문자열('red'), RGB튜플(255,0,0), pygame.Color 모두 지원"""
        if isinstance(color, str):
            return pygame.Color(color)
        return color

    # ── 화면 생성 ──────────────────────────────────────────────
    def screen(self, size, color="white", title="pylitegame"):
        """
        size  : (가로, 세로)
        color : 배경색
        title : 창 제목
        """
        self.surface = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.bg_color = self._parse_color(color)
        self.surface.fill(self.bg_color)
        pygame.display.flip()
        self._running = True

    # ── 화면 업데이트 ───────────────────────────────────────────
    def update(self, fps=60, clear=True):
        """
        게임 루프 안에서 매번 호출하세요.
        clear=True  : 매 프레임 배경을 지움
        clear=False : 잔상 효과 가능
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

        if clear and self.surface:
            self.surface.fill(self.bg_color)

        self.clock.tick(fps)

    def flip(self):
        """그린 내용을 화면에 표시"""
        pygame.display.flip()

    def quit(self):
        """pygame 종료"""
        pygame.quit()

    @property
    def running(self):
        """루프 실행 여부"""
        return self._running

    # ── 도형 그리기 ────────────────────────────────────────────

    def circle(self, pos, radius, color, width=0):
        pygame.draw.circle(self.surface, self._parse_color(color), pos, radius, width)

    def rect(self, pos, size, color, width=0, border_radius=0):
        r = pygame.Rect(pos, size)
        pygame.draw.rect(
            self.surface,
            self._parse_color(color),
            r,
            width,
            border_radius=border_radius,
        )

    def line(self, start, end, color, width=1):
        pygame.draw.line(self.surface, self._parse_color(color), start, end, width)

    def lines(self, points, color, closed=False, width=1):
        pygame.draw.lines(self.surface, self._parse_color(color), closed, points, width)

    def polygon(self, points, color, width=0):
        pygame.draw.polygon(self.surface, self._parse_color(color), points, width)

    def ellipse(self, pos, size, color, width=0):
        r = pygame.Rect(pos, size)
        pygame.draw.ellipse(self.surface, self._parse_color(color), r, width)

    def arc(self, pos, size, color, start_angle, stop_angle, width=1):
        """
        start_angle, stop_angle : 도(degree) 단위
        """
        import math

        r = pygame.Rect(pos, size)
        pygame.draw.arc(
            self.surface,
            self._parse_color(color),
            r,
            math.radians(start_angle),
            math.radians(stop_angle),
            width,
        )

    def triangle(self, p1, p2, p3, color, width=0):
        self.polygon([p1, p2, p3], color, width)

    def text(self, msg, pos, color, size=24, font=None):
        f = pygame.font.Font(font, size)
        surf = f.render(str(msg), True, self._parse_color(color))
        self.surface.blit(surf, pos)