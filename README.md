# AirBnB Clone Shell

[![N|Solid](https://www.elfinanciero.com.mx/uploads/2019/05/07/2b8eba3cb01557277748_standard_desktop_medium_retina.png)]()

Mediante este proyecto que consta de tres partes aprenderemos como hacer una aplicacion modular similar a la plataforma AIRBNB.


Esta es la primera parte, el shell. Desde el shell podremos controlar las funciones principales de una base de datos como crear, leer, actualizar y eliminar en todas las clases nombradas anteriormente.
# Command interpreter
El interprete de comandos facilita el manejo de los datos mediante los siguientes métodos:

| Command | Function |
| ------ | ------ |
| create | Crea una instancia nueva de una clase |
| show | Muestra la información de un elemento |
| update | Actualiza la información de un objeto |
| destroy | Elimina una instancia |
| all | Muestra todos los objetos de una instancia |

## How to use it

### Interactive mode
Para usar el modo interactivo solo debes ejecutar el comando ./console

    ./console
    (hbnb)

### Non interactive mode

Para usar el modo no interactivo debes usar el comando echo y dentro de comillas las instrucciones del interprete luego usa un pipe con el nombre del archivo (./console).

    echo "create BaseModel" | ./console
    (hbnb) b55d9817-62f5-4554-bdaf-24e7a83ad9a3
    (hbnb)
    
### Commands


* [create]() - Para usar este comando necesitas escribir "create" y después el nombre de la clase. Ten en cuenta que solo puedes crear un objeto de las clases nombradas en la parte inferior de este archivo.
```
    create BaseModel
    843497da-f9c5-4ffc-bdf3-1a6b68f74702
```    
* [show]() - Para usar este comando necesitas escribir "show", el nombre de la clase y el id. Debes escribir todos los datos previamente solicitados
```
show BaseModel 843497da-f9c5-4ffc-bdf3-1a6b68f74702
[BaseModel] (843497da-f9c5-4ffc-bdf3-1a6b68f74702) {'created_at': datetime.datetime(2019, 7, 2, 18, 34, 35, 37016), 'id': '843497da-f9c5-4ffc-bdf3-1a6b68f74702', 'updated_at': datetime.datetime(2019, 7, 2, 18, 34, 35, 37138)}
(hbnb) show
** class name missing **
(hbnb)
(hbnb) show BaseModel
** instance id missing **
(hbnb)
```

* [update]() - Para usar este comando necesitas escribir "update", el nombre de la clase, el id, el nombre del atributo y el valor. Debes escribir todos los datos previamente solicitados
```
(hbnb) update BaseModel b6f2ef1d-9673-47c5-ab4e-44eff3d05e9f user Nildiert
(hbnb) show BaseModel b6f2ef1d-9673-47c5-ab4e-44eff3d05e9f)
[BaseModel] (b6f2ef1d-9673-47c5-ab4e-44eff3d05e9f) {'updated_at': datetime.datetime(2019, 7, 2, 20, 35, 24, 853837), 'user': 'Nildiert', 'created_at': datetime.datetime(2019, 7, 2, 17, 2, 52, 520693), 'id': 'b6f2ef1d-9673-47c5-ab4e-44eff3d05e9f'}
(hbnb)
```
* [destroy]() - Para usar este comando necesitas escribir "destroy", el nombre de la clase y el id.
```
(hbnb) destroy BaseModel b6f2ef1d-9673-47c5-ab4e-44eff3d05e9f
(hbnb) show BaseModel b6f2ef1d-9673-47c5-ab4e-44eff3d05e9f
** no instance found **
(hbnb) 
```
* [all]() - Para usar este comando necesitas escribir "all", y el nombre de la clase.
```
[BaseModel] (843497da-f9c5-4ffc-bdf3-1a6b68f74702) {'created_at': datetime.datetime(2019, 7, 2, 18, 34, 35, 37016), 'id': '843497da-f9c5-4ffc-bdf3-1a6b68f74702', 'updated_at': datetime.datetime(2019, 7, 2, 18, 34, 35, 37145)}
[BaseModel] (843497da-f9c5-4ffc-bdf3-1a6b66f8475 {'created_at': datetime.datetime(2019, 7, 2, 18, 34, 35, 37016), 'id': '843497da-f9c5-4ffc-bdf3-1a6b66f84755', 'updated_at': datetime.datetime(2019, 7, 2, 18, 34, 35, 37145)}
```

## Classes

Manipularemos la información en diferentes clases:

  - User
  - State
  - Amenity
  - Place
  - Review
  
#### Holberton school cohort 8 - Bogotá

See [Holberton School](https://www.holbertonschool.com/)

### Collaborators

 - Nildiert Jimenez
 - Javier Bonilla
