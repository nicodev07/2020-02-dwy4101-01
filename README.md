# DWY4101
## Como levantar Ambiente Virtual
1. Ir a la carpeta **ambiente-virtual**
2. Crear un nuevo ambiente virtual con el comando
```sh
python3 -m venv dwy4101-duoc
```
3. Entrar al ambiente virtual utilizando **Git Bash** , depende del s.o estos comandos.

**En Windows**
```sh
source ./dwy4101-duoc/Scripts/activate
```

**En Mac o Linux**
```sh
source ./dwy4101-duoc/bin/activate
````

4. Luego que entras en el ambiente virtual, debes ejecutar el siguiente comando para **instalar los modulos de python**
```sh
pip install -r requirements.txt
```

**NOTA:** Debes estar sobre la carpeta de **ambiente-virtual**

5. Posicionarte sobre la carpeta a trabajar **(ej. 30/10)**
```sh
cd ..
cd 30/10
cd ejemplodjango
```

6. Ejecutar el **manage.py** del proyecto.
```sh
python manage.py runserver
```

## Como levantar Proyecto React
1. Debes ubicarte sobre la carpeta a trabajar (ej. ejemplo-api-frontend del día 30/10)
```sh
cd 30/10
cd ejemplo-api-frontend
```

2. Ejecutar el comando para **instalar** los modulos de **npm**
```sh
npm install
````
3. Ejecutar el script para **iniciar** el proyecto
```sh
npm start
```
4. Happy Coding!

## Observaciones generales
1. El comando para el ambiente virtual, deja tomada la **terminal** por ende, debes ejecutar el proceso para levantar el proyecto de react en otra terminal.
2. El comando para ejecutar **React** deja tomada la terminal, por ende, **debes** ejecutar otra terminal.
3. Si tienes problemas por que no se visualiza los cambios en **Django** o **ReactJS** debes cortar el proceso y volver a ejecutar el comando.

**Para ejecutar el proceso debes presionar control + c dentro de la terminal**
