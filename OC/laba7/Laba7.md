# Ход работы

Для выполнения практического задания была выбрана среда разработки **PyCharm Community**. В качестве исходного материала использовался официальный архив PyCharm для Linux, который был предварительно распакован в рабочем каталоге.

## 1. Подготовка рабочей среды и создание структуры пакета

На начальном этапе были заданы переменные, необходимые для сборки пакета:

```bash
PKGNAME=pycharm-community
VERSION=1.0
ARCH=amd64
BUILDDIR=~/Elizbaryan-EV/Lab7/build/${PKGNAME}_${VERSION}_${ARCH}
SRC_DIR=pycharm-2026.1
```

После этого была создана основная структура каталогов будущего `deb`-пакета:

```bash
mkdir -p "$BUILDDIR/DEBIAN"
mkdir -p "$BUILDDIR/opt/$PKGNAME"
mkdir -p "$BUILDDIR/usr/bin"
mkdir -p "$BUILDDIR/usr/share/applications"
```

Далее была выполнена проверка созданных директорий. Это позволило убедиться, что структура каталога сборки подготовлена правильно и содержит все необходимые разделы для размещения файлов пакета.

## 2. Копирование файлов IDE в каталог пакета

На следующем этапе файлы из распакованного архива PyCharm были скопированы в каталог, который после установки будет находиться в `/opt`:

```bash
cp -r "$SRC_DIR"/. "$BUILDDIR/opt/$PKGNAME/"
```

После копирования была проверена структура полученного каталога. В нём находились основные файлы среды разработки, включая исполняемые файлы, библиотеки, ресурсы и вспомогательные компоненты IDE.

## 3. Создание launcher для запуска программы

Для удобного запуска PyCharm из командной строки была создана символическая ссылка на основной исполняемый файл:

```bash
ln -s "/opt/$PKGNAME/bin/pycharm.sh" "$BUILDDIR/usr/bin/$PKGNAME"
```

После установки пакета пользователь сможет запускать программу с помощью команды:

```bash
pycharm-community
```

## 4. Создание управляющего файла control

Для корректной сборки пакета был создан управляющий файл `control` в каталоге `DEBIAN`:

```bash
cat > "$BUILDDIR/DEBIAN/control" <<EOF
Package: $PKGNAME
Version: $VERSION
Section: devel
Priority: optional
Architecture: $ARCH
Maintainer: Элизбарян Э.В, <emin@example.com>
Installed-Size: $(du -sk "$BUILDDIR/opt/$PKGNAME" | cut -f1)
Description: PyCharm Community packaged for Astra Linux
 PyCharm Community IDE installed into /opt with launcher and desktop entry.
EOF
```

В данном файле указана основная информация о пакете: название, версия, архитектура, категория, приоритет, сопровождающий, размер установленного приложения и краткое описание.

## 5. Создание ярлыка приложения в меню

Чтобы PyCharm отображался в графическом меню системы, был создан `.desktop`-файл:

```bash
cat > "$BUILDDIR/usr/share/applications/$PKGNAME.desktop" <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=PyCharm Community
Comment=Python IDE by JetBrains
Exec=/opt/$PKGNAME/bin/pycharm.sh %f
Icon=/opt/$PKGNAME/bin/pycharm.svg
Terminal=false
Categories=Development;IDE;
StartupNotify=true
StartupWMClass=jetbrains-pycharm-ce
EOF
```

Параметр:

```bash
Categories=Development;IDE;
```

указывает, что приложение должно отображаться в разделе, связанном с разработкой программного обеспечения.

## 6. Создание postinst-скрипта и настройка прав доступа

Для обновления базы desktop-файлов после установки был создан скрипт `postinst`:

```bash
cat > "$BUILDDIR/DEBIAN/postinst" <<'EOF'
#!/bin/sh
set -e

if command -v update-desktop-database >/dev/null 2>&1; then
    update-desktop-database /usr/share/applications >/dev/null 2>&1 || true
fi

exit 0
EOF
```

Затем были назначены необходимые права доступа к служебным файлам пакета:

```bash
chmod 755 "$BUILDDIR/DEBIAN/postinst"
chmod 644 "$BUILDDIR/DEBIAN/control"
chmod 644 "$BUILDDIR/usr/share/applications/$PKGNAME.desktop"
```

После этого была выполнена проверка прав доступа, чтобы убедиться, что файлы имеют корректные разрешения для последующей сборки и установки пакета.

## 7. Проверка структуры пакета перед сборкой

Перед началом сборки была проверена итоговая структура каталогов и файлов. В каталоге сборки должны присутствовать следующие элементы:

```text
DEBIAN/control
DEBIAN/postinst
/opt/pycharm-community
/usr/bin/pycharm-community
/usr/share/applications/pycharm-community.desktop
```

Наличие этих файлов и каталогов подтвердило, что структура пакета подготовлена корректно.

## 8. Сборка deb-пакета

Сборка пакета выполнялась командой:

```bash
fakeroot dpkg-deb --build "build/${PKGNAME}_${VERSION}_${ARCH}"
```

В процессе работы было установлено, что при преждевременном завершении сборки может формироваться повреждённый или неполный файл пакета. Дополнительная проверка показала, что каталог `/opt/pycharm-community` занимает несколько гигабайт, следовательно, файлы IDE были скопированы правильно.

На основании этого был сделан вывод, что проблема возникла не из-за ошибки в структуре пакета, а из-за недостаточного объёма свободного места на виртуальном диске.

## 9. Увеличение размера виртуального диска

Так как в виртуальной машине оказалось недостаточно свободного пространства, размер виртуального диска был увеличен в **VirtualBox**. После этого внутри Astra Linux была выполнена проверка диска и его разделов.

Было установлено, что размер виртуального диска увеличен до 50 ГБ. Затем основной раздел и файловая система были расширены, чтобы использовать добавленное пространство.

После выполнения этих действий в системе появилось достаточно свободного места для завершения сборки пакета.

# Результат работы

В ходе выполнения практической работы была подготовлена структура `deb`-пакета для установки **PyCharm Community** в Astra Linux.

Созданный пакет устанавливает IDE в каталог:

```bash
/opt/pycharm-community
```

Также создаётся команда запуска:

```bash
/usr/bin/pycharm-community
```

Дополнительно формируется ярлык приложения:

```bash
/usr/share/applications/pycharm-community.desktop
```

В ярлыке указана категория:

```bash
Categories=Development;IDE;
```

Благодаря этому PyCharm Community отображается в меню приложений в разделе «Разработка».

## Приложение

![](Pasted%20image%2020260616222635.png)
![](Pasted%20image%2020260616222735.png)
![](Pasted%20image%2020260616222824.png)

![](Pasted%20image%2020260616222934.png)

![](Pasted%20image%2020260616223335.png)


## ССылка
[pycharm-community_1.0_amd64.deb - Google Диск](https://drive.google.com/file/d/1t3SlyQs4x9_kCLkV1zADDWmAK8CTrWYZ/view)
