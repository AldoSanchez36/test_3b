//ingresa a la carpeta test_3b 
//ejecuta los siguientes comandos
//abre un navegador en http://127.0.0.1:8000/api/list/

docker build -t test_3b_image .

docker run -d -p 8000:8000 --name test_3b_container test_3b_image

docker ps 
