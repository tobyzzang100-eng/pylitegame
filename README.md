# pylitegame
[![PyPI version](https://img.shields.io/pypi/v/pylitegame.svg)](https://pypi.org/project/pylitegame/)
[![Python](https://img.shields.io/pypi/pyversions/pylitegame.svg)](https://pypi.org/project/pylitegame/)

pylitegame는 pygame을 더 쉽게 사용할 수 있도록 설계된 가벼운 2D 게임 래퍼입니다.  
pylitegame is a lightweight 2D game wrapper designed to make pygame easier to use.

복잡한 초기 설정 없이 직관적인 방식으로 화면과 도형을 다룰 수 있습니다.  
It allows you to handle screens and shapes in an intuitive way without complex setup.

---

# 🎯 특징 Features

초보자도 쉽게 이해할 수 있는 간단한 API를 제공합니다.  
Provides a simple API that beginners can easily understand.

pygame의 반복적인 코드 작성을 줄여줍니다.  
Reduces repetitive pygame boilerplate code.

도형, 텍스트, 화면 관리 기능을 하나의 클래스로 통합했습니다.  
Integrates shapes, text, and screen management into a single class.

가볍고 학습용 프로젝트에 적합합니다.  
Lightweight and suitable for learning projects.

---

# ✅ 장점 Advantages

설정이 간단하여 빠르게 게임 제작을 시작할 수 있습니다.  
Simple setup allows quick start for game creation.

교육 환경과 입문자 수업에 적합합니다.  
Suitable for educational environments and beginner classes.

코드 가독성이 높고 구조가 명확합니다.  
Offers high readability and clear structure.

---

# ⚠ 단점 Limitations

pygame의 모든 고급 기능을 포함하지는 않습니다.  
Does not include all advanced features of pygame.

대규모 상업용 프로젝트에는 적합하지 않을 수 있습니다.  
May not be suitable for large-scale commercial projects.

고급 충돌 처리나 물리 엔진은 기본 제공되지 않습니다.  
Advanced collision handling or physics engines are not included.

---

# 📘 공식 문법 설명 Official Syntax Reference

---

## 1. Game 클래스  
## 1. Game Class  

Game 클래스는 pylitegame의 핵심 객체입니다.  
The Game class is the core object of pylitegame.

이 객체는 화면 생성과 도형 그리기 기능을 관리합니다.  
It manages screen creation and shape drawing.

---

## 2. screen(size, color, title)

게임 창을 생성하고 배경색과 제목을 설정합니다.  
Creates the game window and sets background color and title.

size는 (width, height) 형태입니다.  
size is in the form (width, height).

color는 문자열 또는 RGB 튜플을 사용할 수 있습니다.  
color can be a string or an RGB tuple.

---

## 3. update(fps=60, clear=True)

게임 루프에서 매 프레임 호출되어 화면을 갱신합니다.  
Called every frame in the game loop to update the screen.

fps는 초당 프레임 수를 의미합니다.  
fps means frames per second.

clear가 True이면 이전 화면을 지웁니다.  
If clear is True, the previous frame is cleared.

---

## 4. flip()

현재 프레임에 그린 내용을 화면에 표시합니다.  
Displays the current frame’s drawings on the screen.

---

## 5. running 속성

게임이 계속 실행 중인지 여부를 나타냅니다.  
Indicates whether the game is still running.

---

# 🎨 도형 그리기 Shape Drawing

## circle(pos, radius, color, width=0)

원을 그립니다.  
Draws a circle.

width가 0이면 채워진 원이 됩니다.  
If width is 0, the circle is filled.

---

## rect(pos, size, color, width=0, border_radius=0)

사각형을 그립니다.  
Draws a rectangle.

border_radius로 모서리를 둥글게 할 수 있습니다.  
border_radius makes rounded corners.

---

## line(start, end, color, width=1)

두 점을 연결하는 선을 그립니다.  
Draws a line between two points.

---

## lines(points, color, closed=False, width=1)

여러 점을 연결합니다.  
Connects multiple points.

closed가 True이면 닫힌 도형이 됩니다.  
If closed is True, it forms a closed shape.

---

## polygon(points, color, width=0)

다각형을 그립니다.  
Draws a polygon.

---

## triangle(p1, p2, p3, color, width=0)

삼각형을 그립니다.  
Draws a triangle.

---

## ellipse(pos, size, color, width=0)

타원을 그립니다.  
Draws an ellipse.

---

## arc(pos, size, color, start_angle, stop_angle, width=1)

원의 일부를 그립니다.  
Draws part of a circle.

각도는 도(degree)를 사용합니다.  
Angles use degrees.

---

# 🔤 텍스트 출력 Text Rendering

## text(msg, pos, color, size=24, font=None)

화면에 문자열을 출력합니다.  
Displays text on the screen.

size는 글자 크기입니다.  
size is the font size.

---

# 🛑 종료 Termination

## quit()

pygame을 안전하게 종료합니다.  
Safely shuts down pygame.

---

# 🔁 실행 구조 Execution Flow

Game 객체를 생성하고 screen으로 창을 만든 뒤 update와 flip을 반복 호출합니다.  
Create a Game object, open a window with screen, and repeatedly call update and flip.

이 과정에서 도형과 텍스트를 그려 게임 화면을 구성합니다.  
During this process, draw shapes and text to build the game screen.
