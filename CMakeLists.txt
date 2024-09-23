cmake_minimum_required(VERSION 3.5)

project(RobotApp VERSION 0.1 LANGUAGES CXX)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Укажите версию Python
find_package(Python3 COMPONENTS Development REQUIRED)

# Укажите путь к Boost.Python
find_package(Boost REQUIRED COMPONENTS python311)

# Убедитесь, что CMake находит заголовки для Python
include_directories(${Python3_INCLUDE_DIRS})

# Также можно добавить пути к заголовкам Boost (опционально, если они не найдены автоматически)
include_directories(${Boost_INCLUDE_DIRS})

find_package(Qt6 REQUIRED COMPONENTS
    3DCore
    3DRender
    3DInput
    3DLogic
    3DExtras
    3DAnimation
    Widgets
)


set(PROJECT_SOURCES
        src/main.cpp
        src/mainwindow.cpp
        src/mainwindow.ui
        include/mainwindow.h
)
include_directories(include)

add_executable(RobotApp
    ${PROJECT_SOURCES}
)

target_link_libraries(RobotApp PRIVATE
    Qt6::Widgets
    Qt6::3DCore
    Qt6::3DRender
    Qt6::3DLogic
    Qt6::3DExtras
    Qt6::3DAnimation
    ${Python3_LIBRARIES}  # Добавляем библиотеки Python
    ${Boost_LIBRARIES}    # Добавляем библиотеки Boost.Python
)


