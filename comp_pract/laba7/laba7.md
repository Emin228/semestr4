#### 1. Изучение проекта

Проект представляет собой веб-приложение для учёта расходов, реализованное с использованием технологии WebAssembly.

Структура проекта:

- `main.c` — основная бизнес-логика приложения на языке C.
- `app.js` — взаимодействие между WebAssembly и пользовательским интерфейсом.
- `index.html` — графический интерфейс пользователя.

Принцип работы:

1. Пользователь вводит дату, категорию, сумму и описание расхода.
2. JavaScript получает данные из формы.
3. Данные передаются в WebAssembly-модуль через экспортированные функции Emscripten.
4. Код на C сохраняет запись о расходе.
5. После изменения данных WebAssembly вызывает JavaScript-функции обновления интерфейса.
6. Интерфейс отображает таблицу расходов, общую сумму и суммы по категориям.

---

#### 2. Установка Emscripten

Например:

```
git clone https://github.com/emscripten-core/emsdk.gitcd emsdkemsdk install latestemsdk activate latestemsdk_env.bat
```

Проверка:

```
emcc --version
```

---

#### 3. Компиляция проекта

```
emcc main.c -o index.js -s WASM=1 -O2 \-s EXPORTED_RUNTIME_METHODS='["stringToUTF8","UTF8ToString"]' \-s EXPORTED_FUNCTIONS='["_main","_jsAddExpense","_jsDeleteExpense","_jsClearAllExpenses","_jsGetTotalExpenses","_jsGetExpenseCount","_jsGetCategoryCount","_getExpenseJSON","_getCategoryTotalJSON","_freeMemory","_malloc","_free"]' \--shell-file index.html \-s ALLOW_MEMORY_GROWTH=1
```

Запуск:

```
python -m http.server 8000
```

Открыть:

```
http://localhost:8000
```

---

#### 4. Реализованное улучшение (Improvement)

Самый простой вариант:

### Добавлена функция поиска расходов по категории

В `app.js` был добавлен текстовый поиск.

HTML:

```
<input type="text" id="searchCategory" placeholder="Search category">
```

JavaScript:

```
const searchInput = document.getElementById('searchCategory');searchInput.addEventListener('input', function() {    const filter = this.value.toLowerCase();    const rows = expenseTableBody.getElementsByTagName('tr');    for (let row of rows) {        const categoryCell = row.children[1];        if (!categoryCell) continue;        const text = categoryCell.textContent.toLowerCase();        row.style.display =            text.includes(filter) ? '' : 'none';    }});
```

Результат:

- пользователь может быстро находить расходы нужной категории;
- повышено удобство работы с большим количеством записей.

---

#### 5. Вывод

В ходе работы был изучен процесс создания веб-приложений на основе WebAssembly. Был освоен инструмент Emscripten для компиляции C-кода в WebAssembly, выполнена сборка и запуск приложения Budget Planner. Также было реализовано улучшение в виде поиска расходов по категориям, что повысило удобство использования приложения. Получен практический опыт взаимодействия C, JavaScript и WebAssembly в рамках единого веб-приложения.