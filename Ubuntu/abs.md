Процесс- абстрактый термин. Под ним понимается набор ресурсов задачи во время её выполнения:
<ul>
<li>Память
<li>Открытые файловые дискрипторы
<li>Контекст выполнения
<li>pid
<li>Обработчики сигналов
<li>Как минимум, один поток
</ul>
Поток имеют:
<ul>
  <li>Общую виртуальную память
  <li>Каждый - сврй виртуальный процессор
</ul>

Stack - адреса возврата из подпрограмм (аргументы функций)<br>
mmap - разделяемая библиотека
heap - всякие локальные переменные и временные данные программы
data - инициализированные глобальные и статические переменные

Рекурсивная функция - функция, вызывающая сама себя

Виртуальная файловая система /proc - Не имеет существующих файлов, существует только в оперативной памяти. Содержит оперативную информаию о системе и процессах в ней. В файлы можно писать значения, изменяя этим параметры системы
