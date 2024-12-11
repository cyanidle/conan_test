# conan_test

## Установить зависимости
conan install conan --build=missing
## Сгенерировать cmake
cmake --preset conan-release
## Собрать проект
cmake --build build/Release

# Создание пакета
conan create ./conan