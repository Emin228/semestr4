## Часть 1
Скрипт Paycharm
```bash
#!/bin/bash

echo "Elizbaryan Emin Vanikovich 1-1"
sudo apt update
sudo apt install -y wget tar


VERSION="2025.1.1"


URL="https://download.jetbrains.com/python/pycharm-community-${VERSION}.tar.gz"


TMP_DIR="/tmp/pycharm_install"

INSTALL_DIR="/opt/pycharm"

# Создание временной папки
mkdir -p $TMP_DIR

echo "Скачивание PyCharm..."
wget -O $TMP_DIR/pycharm.tar.gz $URL

echo "Распаковка архива..."
tar -xzf $TMP_DIR/pycharm.tar.gz -C $TMP_DIR

echo "Установка PyCharm..."
sudo rm -rf $INSTALL_DIR
sudo mv $TMP_DIR/pycharm-community-* $INSTALL_DIR

echo "Создание символьной ссылки..."
sudo ln -sf $INSTALL_DIR/bin/pycharm.sh /usr/local/bin/pycharm

echo "Очистка временных файлов..."
rm -rf $TMP_DIR

echo "PyCharm успешно установлен!"
```
## Часть 2
Скрипт VsCode
```bash
#!/bin/bash

sudo apt update
sudo apt install -y wget gpg apt-transport-https


wget -qO- https://packages.microsoft.com/keys/microsoft.asc \
| gpg --dearmor \
| sudo tee /etc/apt/keyrings/packages.microsoft.gpg > /dev/null

# Добавление репозитория VS Code
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" \
| sudo tee /etc/apt/sources.list.d/vscode.list


sudo apt update


sudo apt install -y code

echo "Visual Studio Code успешно установлен!"
echo "Запуск: code"
```